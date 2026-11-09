/* Service worker du site : permet d'ouvrir le site SANS RÉSEAU (iPad, icône de l'écran d'accueil).
   Règle : le réseau d'abord (le site reste à jour), mais si le réseau ne répond pas en 3 s, ou pas du tout,
   on sert la copie gardée sur l'appareil. Chaque réponse reçue du réseau met la copie à jour.
   La copie complète est faite par le bouton « Préparer le hors ligne » du mode tableau (liste : hors-ligne.json).
   Firebase (googleapis) n'est JAMAIS intercepté : la synchro garde sa propre logique. */
const CACHE = "site-hors-ligne";
const EXTERNES = /^https:\/\/cdn\.jsdelivr\.net\/(npm\/katex@|pyodide\/)/;

self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", e => e.waitUntil(self.clients.claim()));

const portee = () => new URL(self.registration.scope).pathname;
function cle(url) {                                                   // une seule copie par fichier : sans « ?… » ni « #… », « …/ » = « …/index.html »
  const u = new URL(url); let p = u.pathname; if (p.endsWith("/")) p += "index.html";
  return u.origin + p;
}

self.addEventListener("fetch", e => {
  const r = e.request; if (r.method !== "GET" || r.headers.has("range")) return;
  const u = new URL(r.url);
  const local = u.origin === self.location.origin && u.pathname.startsWith(portee()) && !u.pathname.endsWith("/sw.js");
  if (!local && !EXTERNES.test(r.url)) return;
  e.respondWith(repondre(r));
});

async function repondre(r) {
  const c = await caches.open(CACHE), k = cle(r.url);
  const copie = await c.match(k);
  const reseau = fetch(r).then(res => {
    if (res && (res.status === 200 || res.type === "opaque")) c.put(k, res.clone()).catch(() => {});
    return res;
  });
  if (!copie) return reseau.catch(() => new Response(
    "<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width'><body style='font:18px system-ui;padding:24px'>" +
    "<h2>Pas de réseau</h2><p>Cette page n'a pas encore été gardée sur l'appareil.</p>" +
    "<p>Avec du réseau, ouvrez une page de cours, puis dans la barre du bas : <b>Préparer le hors ligne</b>.</p>",
    { status: 503, headers: { "Content-Type": "text/html; charset=utf-8" } }));
  return Promise.race([reseau.then(res => res.ok || res.type === "opaque" ? res : copie, () => copie),
                       new Promise(ok => setTimeout(() => ok(copie), 3000))]);
}
