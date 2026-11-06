/* Exécute le Python de l'élève hors de la page (Pyodide) : une boucle infinie ne bloque jamais l'écran.
   Stop = la page supprime ce worker et en relance un autre. */
const VERSION = "0.27.7", BASE = `https://cdn.jsdelivr.net/pyodide/v${VERSION}/full/`;
self.envoyer = s => postMessage(JSON.parse(s));
let py = null;
const HARNAIS = String.raw`
import sys, ast, json, random, traceback, base64, io, os, builtins
os.environ["MPLBACKEND"] = "AGG"
import js
NS = {"__name__": "__main__"}
LIMITE = 100000
class BesoinInput(BaseException): pass
class TropLong(BaseException): pass
class Ctx: pass
ctx = Ctx()
def poster(**m): js.envoyer(json.dumps(m))
class Sortie:
    encoding = "utf-8"
    def __init__(self, genre): self.genre = genre
    def write(self, s):
        s = str(s); n = len(s); deja = ctx.ecrit; ctx.ecrit += n
        if ctx.ecrit > LIMITE + ctx.sauter: raise TropLong()
        if deja + n > ctx.sauter:
            poster(type="texte", genre=self.genre, texte=s[max(0, ctx.sauter - deja):])
        return n
    def flush(self): pass
    def isatty(self): return False
def lire(invite=""):
    if ctx.k < len(ctx.reponses):
        r = ctx.reponses[ctx.k]; ctx.k += 1
        sys.stdout.write(str(invite) + r + "\n")
        return r
    sys.stdout.write(str(invite))
    raise BesoinInput()
builtins.input = lire
def envoyer_figures():
    m = sys.modules.get("matplotlib.pyplot")
    if not m: return
    for num in m.get_fignums():
        ctx.figures += 1
        if ctx.figures > ctx.figures_vues:
            b = io.BytesIO(); m.figure(num).savefig(b, format="png", dpi=130, bbox_inches="tight")
            poster(type="figure", png=base64.b64encode(b.getvalue()).decode())
    m.close("all")
def preparer_courbes():
    import matplotlib; matplotlib.use("AGG")
    import matplotlib.pyplot as plt
    plt.show = lambda *a, **k: envoyer_figures()
    import pylab; pylab.show = plt.show
def signaler(e, nom):
    ligne = None
    if isinstance(e, SyntaxError) and e.filename == nom: ligne = e.lineno
    else:
        for f in traceback.extract_tb(e.__traceback__):
            if f.filename == nom: ligne = f.lineno
    poster(type="erreur", ligne=ligne, nom=type(e).__name__, message=str(e.msg if isinstance(e, SyntaxError) else e), console=nom == "<console>")
def lancer(code, decalage, mode, reponses, graine, sauter, figures_vues):
    ctx.ecrit = 0; ctx.sauter = sauter; ctx.k = 0; ctx.reponses = json.loads(reponses); ctx.figures = 0; ctx.figures_vues = figures_vues
    if mode == "tout" and not ctx.reponses: NS.clear(); NS["__name__"] = "__main__"
    photo = dict(NS); nom = "<console>" if mode == "console" else "<programme>"
    random.seed(graine)
    sys.stdout = Sortie("sortie"); sys.stderr = Sortie("sortie")
    try:
        arbre = compile("\n" * decalage + code, nom, "exec", ast.PyCF_ONLY_AST)
        dernier = None
        if mode == "console" and arbre.body and isinstance(arbre.body[-1], ast.Expr):
            dernier = ast.Expression(arbre.body.pop().value)
        exec(compile(arbre, nom, "exec"), NS)
        if dernier is not None:
            v = eval(compile(dernier, nom, "eval"), NS)
            if v is not None: sys.stdout.write(repr(v) + "\n")
        envoyer_figures()
        poster(type="fin")
    except BesoinInput:
        NS.clear(); NS.update(photo)
        poster(type="input", sauter=ctx.ecrit, figures=ctx.figures)
    except TropLong:
        poster(type="troplong")
    except SystemExit:
        envoyer_figures(); poster(type="fin")
    except BaseException as e:
        try: envoyer_figures()
        except BaseException: pass
        signaler(e, nom)
    finally:
        sys.stdout = sys.__stdout__; sys.stderr = sys.__stderr__
`;
async function demarrer() {
  try {
    importScripts(BASE + "pyodide.js");
    py = await loadPyodide({ indexURL: BASE });
    py.runPython(HARNAIS);
    postMessage({ type: "pret" });
  } catch (e) { postMessage({ type: "echec", message: String(e && e.message || e) }); }
}
const pret = demarrer();
onmessage = async ({ data: m }) => {
  await pret; if (!py) return;
  try {
    const courbes = /\b(matplotlib|pylab)\b/.test(m.code), lourd = courbes || /\bnumpy\b/.test(m.code);
    if (lourd) {
      postMessage({ type: "etat", texte: courbes ? "Chargement de matplotlib (la première fois, quelques instants)…" : "Chargement de numpy…" });
      await py.loadPackage(courbes ? ["matplotlib", "numpy"] : ["numpy"], { messageCallback: () => {}, errorCallback: () => {} });
      if (courbes) py.runPython("preparer_courbes()");
    }
    postMessage({ type: "debut" });
    py.globals.get("lancer")(m.code, m.decalage || 0, m.mode, JSON.stringify(m.reponses || []), m.graine, m.sauter || 0, m.figuresVues || 0);
  } catch (e) { postMessage({ type: "echec", message: String(e && e.message || e), enCours: true }); }
};
