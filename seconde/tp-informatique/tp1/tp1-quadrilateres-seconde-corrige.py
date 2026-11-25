# =============================================================================
#            TP 1 - PYTHON : QUELLE EST LA NATURE DE CE QUADRILATÈRE ?
#                       Seconde - Géométrie repérée
#                         >>> CORRIGÉ <<<
# =============================================================================
#
# OBJECTIF
#   Écrire, petit à petit, des fonctions qui reçoivent les coordonnées des
#   sommets d'un quadrilatère ABCD et qui permettent de dire s'il s'agit
#   d'un carré, d'un rectangle, d'un losange, d'un parallélogramme, ou d'un
#   quadrilatère quelconque.
#
# COMMENT EXÉCUTER UNE FONCTION AVEC SPYDER
#   Ce fichier est découpé en CELLULES : chaque cellule commence par une
#   ligne  # %%  et contient en général une fonction. On exécute une seule
#   cellule à la fois :
#
#   - Méthode 1 (conseillée) : cliquez n'importe où dans la cellule de la
#     fonction (elle est alors surlignée), puis appuyez sur  Ctrl + Entrée.
#     Seule cette cellule est exécutée.
#   - Méthode 2 : sélectionnez à la souris toutes les lignes de la fonction
#     (de la ligne  def  jusqu'à sa dernière ligne), puis appuyez sur  F9.
#
#   N'UTILISEZ PAS la touche F5 ni le triangle vert « Exécuter le fichier » :
#   ils exécutent TOUT le fichier, et la moindre erreur dans une fonction pas
#   encore terminée affiche un message d'erreur et arrête tout.
#
#   - Exécutez les cellules DANS L'ORDRE : une fonction n'existe pour Python
#     qu'après avoir exécuté sa cellule.
#   - Si vous modifiez une fonction, exécutez de nouveau sa cellule !
#
# COMMENT TESTER UNE FONCTION
#   Après avoir exécuté la cellule d'une fonction, tapez son nom avec des
#   valeurs dans la CONSOLE (en bas à droite), puis appuyez sur Entrée.
#   Exemple : tapez   reste(7)   puis Entrée.
#   Sous chaque fonction, vous trouverez des tests à taper, avec la réponse
#   que Python doit afficher. Si vous obtenez autre chose, corrigez !
#
# LÉGENDE
#   [EXEMPLE]       fonction déjà écrite : lisez-la, exécutez-la, testez-la.
#   [À COMPLÉTER]   remplacez les  ...  par ce qu'il faut.
#   [À ÉCRIRE]      écrivez la fonction entièrement, seul(e).
#   [QUESTION]      répondez dans le fichier, en commentaire (ligne avec #).
#
# Toutes les lignes qui commencent par # sont des COMMENTAIRES :
# Python les ignore, elles servent à expliquer le programme.
# =============================================================================


# %% [EXEMPLE 1] Le reste d'une division
#
# En Python, a % b donne le RESTE de la division de a par b.
# Par exemple 17 % 3 donne 2, car 17 = 3 × 5 + 2.

def reste(n):
    r = n % 3
    return(r)

# Tests à taper dans la console :
#   reste(17)                               réponse attendue : 2
#   reste(12)                               réponse attendue : 0
#
# [QUESTION 1] Que vaut le reste quand n est divisible par 3 ?
# Réponse : le reste vaut 0.


# %% [EXEMPLE 2] Une fonction qui renvoie un message
#
# Rappel :  if  veut dire « si »,  else  veut dire « sinon ».
#   ==   veut dire « est égal à »   (ne pas confondre avec = qui AFFECTE
#        une valeur à une variable)
# Un texte s'écrit entre guillemets.

def divisible_par_3(n):
    if n % 3 == 0:
        return("divisible par 3")
    else:
        return("pas divisible par 3")

# Tests à taper dans la console :
#   divisible_par_3(12)                     réponse attendue : 'divisible par 3'
#   divisible_par_3(17)                     réponse attendue : 'pas divisible par 3'


# %% [EXEMPLE 3] Une fonction avec plusieurs arguments
#
# Une fonction peut recevoir plusieurs nombres : on les sépare par des
# virgules. Cette fonction regarde si le nombre a divise le nombre b.

def divise(a, b):
    if b % a == 0:
        return("a divise b")
    else:
        return("a ne divise pas b")

# Tests à taper dans la console :
#   divise(3, 12)                           réponse attendue : 'a divise b'
#   divise(5, 12)                           réponse attendue : 'a ne divise pas b'
#
# [QUESTION 2] Tapez  divise(12, 3)  : pourquoi la réponse change-t-elle ?
# Réponse : la réponse est 'a ne divise pas b' : maintenant a = 12 et b = 3,
# et 12 ne divise pas 3. L'ordre des arguments compte !


# %% [EXEMPLE 4] Afficher plusieurs résultats avec print
#
# print(...) AFFICHE dans la console. On peut afficher plusieurs choses
# à la suite, en les séparant par des virgules.
# a // b donne le QUOTIENT de la division de a par b (sans la virgule).

def division(a, b):
    q = a // b
    r = a % b
    print("quotient :", q, "  reste :", r)

# Tests à taper dans la console :
#   division(17, 3)                         réponse attendue : quotient : 5   reste : 2
#   division(20, 4)                         réponse attendue : quotient : 5   reste : 0


# %% [EXEMPLE 5] Un « si » dans un « si »
#
# Pour vérifier DEUX conditions, on peut placer un if à l'intérieur d'un
# autre if. Attention au décalage vers la droite (l'indentation) : c'est
# lui qui indique à Python ce qui est « à l'intérieur ».

def divisible_par_3_et_5(n):
    if n % 3 == 0:
        if n % 5 == 0:
            return("divisible par 3 et par 5")
        else:
            return("divisible par 3 mais pas par 5")
    else:
        return("pas divisible par 3")

# Tests à taper dans la console :
#   divisible_par_3_et_5(30)                réponse attendue : 'divisible par 3 et par 5'
#   divisible_par_3_et_5(9)                 réponse attendue : 'divisible par 3 mais pas par 5'
#   divisible_par_3_et_5(10)                réponse attendue : 'pas divisible par 3'
#
# [QUESTION 3] Modifiez la fonction pour que divisible_par_3_et_5(10)
# réponde "divisible par 5 mais pas par 3". (Il faut ajouter un if dans
# le else.)
# Corrigé :
#   def divisible_par_3_et_5(n):
#       if n % 3 == 0:
#           if n % 5 == 0:
#               return("divisible par 3 et par 5")
#           else:
#               return("divisible par 3 mais pas par 5")
#       else:
#           if n % 5 == 0:
#               return("divisible par 5 mais pas par 3")
#           else:
#               return("pas divisible par 3")


# =============================================================================
#                    PLACE À LA GÉOMÉTRIE !
# Dans toute la suite, on se place dans un repère orthonormé.
# Un point A(xA ; yA) est donné par DEUX variables : xA et yA.
# ATTENTION : en Python, la virgule décimale s'écrit avec un POINT :
# 2,5 s'écrit 2.5   (la virgule sert à séparer les nombres).
# =============================================================================


# %% PARTIE 1 - [À COMPLÉTER] Milieu d'un segment
#
# La fonction milieu reçoit les coordonnées de A et de B et AFFICHE les
# coordonnées du milieu du segment [AB].

def milieu(xA, yA, xB, yB):
    x = (xA + xB) / 2
    y = (yA + yB) / 2
    print("Le milieu a pour coordonnées :", x, ";", y)

# Tests à taper dans la console :
#   milieu(1, 2, 5, 4)                      réponse attendue : Le milieu a pour coordonnées : 3.0 ; 3.0
#   milieu(-2, 1, 3, 0)                     réponse attendue : Le milieu a pour coordonnées : 0.5 ; 0.5
#   milieu(4, -6, 4, 6)                     réponse attendue : Le milieu a pour coordonnées : 4.0 ; 0.0


# %% PARTIE 2 - [À COMPLÉTER] Distance entre deux points
#
# La fonction distance reçoit les coordonnées de A et de B et renvoie la
# distance AB.
# En Python :  x² s'écrit  x**2   et la racine carrée de x s'écrit  sqrt(x).
# La ligne  from math import sqrt  permet d'utiliser sqrt : ne l'effacez pas.

from math import sqrt

def distance(xA, yA, xB, yB):
    d = sqrt((xB - xA)**2 + (yB - yA)**2)
    return(d)

# Tests à taper dans la console :
#   distance(1, 1, 4, 5)                    réponse attendue : 5.0
#   distance(-3, 2, 5, 2)                   réponse attendue : 8.0
#   distance(0, 0, 1, 1)                    réponse attendue : 1.4142135623730951
#
# [QUESTION 4] Quelle est la valeur exacte de la distance entre les points
# (0 ; 0) et (1 ; 1) ? Python donne-t-il cette valeur exacte ?
# Réponse : la valeur exacte est racine de 2, un nombre irrationnel.
# Python n'en donne qu'une valeur approchée.


# %% PARTIE 2 - [EXEMPLE 6] Attention aux nombres à virgule !
#
# Un ordinateur garde un nombre LIMITÉ de chiffres après la virgule : il ne
# connaît qu'une VALEUR APPROCHÉE de racine de 2. Tapez dans la console :
#   sqrt(2) ** 2                            on attend 2... que répond Python ?
#   0.1 + 0.2                               on attend 0.3... que répond Python ?
#
# CONCLUSION : si on compare deux distances avec ==, Python peut se tromper.
# L'astuce : une longueur est positive, donc  AB = CD  revient à  AB² = CD².
# Et AB² se calcule SANS racine carrée : avec des coordonnées entières,
# Python le calcule de façon EXACTE.


# %% PARTIE 2 - [À COMPLÉTER] Carré de la distance
#
# La fonction distance_carre renvoie AB² (le carré de la distance AB),
# sans utiliser de racine carrée.

def distance_carre(xA, yA, xB, yB):
    d2 = (xB - xA)**2 + (yB - yA)**2
    return(d2)

# Tests à taper dans la console :
#   distance_carre(1, 1, 4, 5)              réponse attendue : 25
#   distance_carre(0, 0, 1, 1)              réponse attendue : 2
#   distance_carre(2, -1, -1, 3)            réponse attendue : 25
#
# RÈGLE POUR LA SUITE DU TP : pour savoir si deux longueurs sont égales,
# on compare TOUJOURS leurs carrés.


# %% LES FIGURES DE TEST
#
# Dans toute la suite, ABCD est un quadrilatère dont les sommets sont donnés
# DANS L'ORDRE (on tourne autour de la figure).
# Les fonctions recevront 8 nombres, toujours dans cet ordre :
#        xA, yA, xB, yB, xC, yC, xD, yD
#
#   Figure 1 : A(0 ; 0)   B(4 ; 1)   C(5 ; 3)    D(1 ; 2)
#   Figure 2 : A(1 ; 1)   B(5 ; 1)   C(5 ; 3)    D(1 ; 3)
#   Figure 3 : A(0 ; 0)   B(2 ; 2)   C(-1 ; 5)   D(-3 ; 3)
#   Figure 4 : A(0 ; 0)   B(3 ; 1)   C(4 ; 4)    D(1 ; 3)
#   Figure 5 : A(0 ; 0)   B(2 ; 0)   C(2 ; 2)    D(0 ; 2)
#   Figure 6 : A(1 ; 0)   B(4 ; 1)   C(3 ; 4)    D(0 ; 3)
#   Figure 7 : A(0 ; 0)   B(5 ; 0)   C(4 ; 3)    D(1 ; 2)
#   Figure 8 : A(0 ; 0)   B(4 ; 1)   C(1 ; 2)    D(5 ; 3)


# %% PARTIE 3 - [À COMPLÉTER] Parallélogramme
#
# La fonction renvoie un message qui dit si ABCD est un parallélogramme.
# (Revoyez l'exemple 5 : un « si » dans un « si ».)

# PROPRIÉTÉ UTILISÉE : ABCD est un parallélogramme si et seulement si ses
# diagonales [AC] et [BD] ont le MÊME MILIEU.
# Deux points sont égaux quand ils ont la même abscisse ET la même ordonnée :
# il faut donc vérifier DEUX conditions, d'où le « si » dans un « si ».

def parallelogramme(xA, yA, xB, yB, xC, yC, xD, yD):
    # ÉTAPE 1 : coordonnées (x1 ; y1) du milieu de la diagonale [AC]
    x1 = (xA + xC) / 2
    y1 = (yA + yC) / 2
    # ÉTAPE 2 : coordonnées (x2 ; y2) du milieu de la diagonale [BD]
    x2 = (xB + xD) / 2
    y2 = (yB + yD) / 2
    # ÉTAPE 3 : on compare les deux milieux
    if x1 == x2:
        # Ici, les deux milieux ont la même abscisse.
        # Il reste à vérifier les ordonnées.
        if y1 == y2:
            # Même abscisse ET même ordonnée : c'est le même point.
            # Les diagonales ont le même milieu.
            return("ABCD est un parallélogramme")
        else:
            # Même abscisse, mais ordonnées différentes :
            # les milieux sont deux points différents.
            return("ABCD n'est pas un parallélogramme")
    else:
        # Les abscisses sont déjà différentes : les milieux sont
        # différents, inutile de regarder les ordonnées.
        return("ABCD n'est pas un parallélogramme")

# Tests à taper dans la console :
#   parallelogramme(0, 0, 4, 1, 5, 3, 1, 2)     réponse attendue : 'ABCD est un parallélogramme'
#   parallelogramme(0, 0, 2, 2, -1, 5, -3, 3)   réponse attendue : 'ABCD est un parallélogramme'
#   parallelogramme(0, 0, 5, 0, 4, 3, 1, 2)     réponse attendue : "ABCD n'est pas un parallélogramme"
#   parallelogramme(0, 0, 4, 1, 1, 2, 5, 3)     réponse attendue : "ABCD n'est pas un parallélogramme"
#
# [QUESTION 5] Les figures 1 et 8 ont les mêmes points. Pourquoi la figure 8
# n'est-elle pas un parallélogramme ? (Tracez-la !)
# Réponse : les sommets ne sont pas reliés dans le même ordre : ABCD est un
# quadrilatère « croisé ». [AC] et [BD] sont ici deux côtés de la figure 1,
# qui n'ont pas le même milieu. L'ordre des sommets compte !


# %% PARTIE 4 - [À ÉCRIRE] Losange
#
# Écrivez la fonction  losange(xA, yA, xB, yB, xC, yC, xD, yD)  qui renvoie
# "ABCD est un losange" ou "ABCD n'est pas un losange".
# Aide : partez de votre fonction parallelogramme et ajoutez ce qu'il faut.
# Pour comparer deux longueurs, calculez leurs carrés.

# PROPRIÉTÉ UTILISÉE : un losange est un parallélogramme qui a deux côtés
# CONSÉCUTIFS de même longueur, par exemple AB = BC.
# Le programme se fait donc en deux temps :
#   1) on vérifie que ABCD est un parallélogramme (comme dans la partie 3) ;
#   2) SEULEMENT si c'est le cas, on compare AB et BC.
# Comme AB et BC sont des longueurs (positives), AB = BC revient à
# AB² = BC² : on compare les carrés (règle de la partie 2).

def losange(xA, yA, xB, yB, xC, yC, xD, yD):
    # ÉTAPE 1 : milieu (x1 ; y1) de [AC] et milieu (x2 ; y2) de [BD],
    # exactement comme dans la fonction parallelogramme
    x1 = (xA + xC) / 2
    y1 = (yA + yC) / 2
    x2 = (xB + xD) / 2
    y2 = (yB + yD) / 2
    # ÉTAPE 2 : carrés des longueurs de deux côtés consécutifs,
    # calculés comme dans la fonction distance_carre
    AB2 = (xB - xA)**2 + (yB - yA)**2      # AB²
    BC2 = (xC - xB)**2 + (yC - yB)**2      # BC²
    # ÉTAPE 3 : les tests, du plus général au plus précis
    if x1 == x2:
        if y1 == y2:
            # Ici, les diagonales ont le même milieu :
            # on SAIT que ABCD est un parallélogramme.
            # Il reste à tester les deux côtés consécutifs.
            if AB2 == BC2:
                # Parallélogramme ET AB = BC : c'est un losange.
                return("ABCD est un losange")
            else:
                # Parallélogramme, mais AB et BC sont différents :
                # ce n'est pas un losange.
                return("ABCD n'est pas un losange")
        else:
            # Les milieux sont différents (ordonnées différentes) :
            # pas un parallélogramme, donc pas un losange.
            return("ABCD n'est pas un losange")
    else:
        # Les milieux sont différents (abscisses différentes) :
        # pas un parallélogramme, donc pas un losange.
        return("ABCD n'est pas un losange")

# REMARQUE : il ne suffit PAS de tester AB = BC. Par exemple, pour
# A(0 ; 0), B(4 ; 0), C(4 ; 4), D(1 ; 2), on a AB² = BC² = 16, mais
# [AC] et [BD] n'ont pas le même milieu : ce n'est pas un losange.
# Sans l'étape « parallélogramme », on conclurait à tort. Il faut les DEUX
# conditions.

# Tests à taper dans la console :
#   losange(0, 0, 3, 1, 4, 4, 1, 3)             réponse attendue : 'ABCD est un losange'
#   losange(1, 0, 4, 1, 3, 4, 0, 3)             réponse attendue : 'ABCD est un losange'
#   losange(0, 0, 4, 1, 5, 3, 1, 2)             réponse attendue : "ABCD n'est pas un losange"
#   losange(1, 1, 5, 1, 5, 3, 1, 3)             réponse attendue : "ABCD n'est pas un losange"


# %% PARTIE 5 - [À ÉCRIRE] Rectangle
#
# Écrivez la fonction  rectangle(xA, yA, xB, yB, xC, yC, xD, yD)  qui
# renvoie "ABCD est un rectangle" ou "ABCD n'est pas un rectangle".

# PROPRIÉTÉ UTILISÉE : un rectangle est un parallélogramme dont les
# DIAGONALES ont la même longueur : AC = BD.
# Même méthode que pour le losange :
#   1) on vérifie que ABCD est un parallélogramme ;
#   2) seulement si c'est le cas, on compare AC² et BD².
# Seule différence avec le losange : on compare les DIAGONALES [AC] et
# [BD], et non plus deux côtés.

def rectangle(xA, yA, xB, yB, xC, yC, xD, yD):
    # ÉTAPE 1 : milieu (x1 ; y1) de [AC] et milieu (x2 ; y2) de [BD]
    x1 = (xA + xC) / 2
    y1 = (yA + yC) / 2
    x2 = (xB + xD) / 2
    y2 = (yB + yD) / 2
    # ÉTAPE 2 : carrés des longueurs des deux diagonales
    AC2 = (xC - xA)**2 + (yC - yA)**2      # AC²
    BD2 = (xD - xB)**2 + (yD - yB)**2      # BD²
    # ÉTAPE 3 : les tests
    if x1 == x2:
        if y1 == y2:
            # Ici, ABCD est un parallélogramme (même milieu).
            # Il reste à comparer les diagonales.
            if AC2 == BD2:
                # Parallélogramme ET diagonales de même longueur :
                # c'est un rectangle.
                return("ABCD est un rectangle")
            else:
                # Parallélogramme, mais diagonales de longueurs
                # différentes : ce n'est pas un rectangle.
                return("ABCD n'est pas un rectangle")
        else:
            # Pas un parallélogramme (ordonnées des milieux différentes),
            # donc pas un rectangle.
            return("ABCD n'est pas un rectangle")
    else:
        # Pas un parallélogramme (abscisses des milieux différentes),
        # donc pas un rectangle.
        return("ABCD n'est pas un rectangle")

# Tests à taper dans la console :
#   rectangle(1, 1, 5, 1, 5, 3, 1, 3)           réponse attendue : 'ABCD est un rectangle'
#   rectangle(0, 0, 2, 2, -1, 5, -3, 3)         réponse attendue : 'ABCD est un rectangle'
#   rectangle(0, 0, 4, 1, 5, 3, 1, 2)           réponse attendue : "ABCD n'est pas un rectangle"
#   rectangle(0, 0, 3, 1, 4, 4, 1, 3)           réponse attendue : "ABCD n'est pas un rectangle"
#
# [QUESTION 6] Dans la figure 3, calculez à la main la longueur exacte des
# diagonales. Pourquoi a-t-on eu raison de comparer les carrés ?
# Réponse : AC² = (-1 - 0)² + (5 - 0)² = 26 et BD² = (-3 - 2)² + (3 - 2)² = 26,
# donc AC = BD = racine de 26, irrationnel. En comparant les carrés, Python
# compare les entiers 26 et 26 : la comparaison est exacte.


# %% PARTIE 6 - [À ÉCRIRE] Carré
#
# Écrivez la fonction  carre(xA, yA, xB, yB, xC, yC, xD, yD)  (sans accent
# dans le nom !) qui renvoie "ABCD est un carré" ou "ABCD n'est pas un carré".

# PROPRIÉTÉ UTILISÉE : un carré est à la fois un losange ET un rectangle.
# Il faut donc réunir les trois conditions vues jusqu'ici :
#   1) [AC] et [BD] ont le même milieu    -> parallélogramme ;
#   2) AB = BC                            -> c'est même un losange ;
#   3) AC = BD                            -> c'est aussi un rectangle.
# On empile les tests : chaque « if » n'est examiné que si le précédent
# est vrai.

def carre(xA, yA, xB, yB, xC, yC, xD, yD):
    # ÉTAPE 1 : les deux milieux (comme pour le parallélogramme)
    x1 = (xA + xC) / 2
    y1 = (yA + yC) / 2
    x2 = (xB + xD) / 2
    y2 = (yB + yD) / 2
    # ÉTAPE 2 : deux côtés consécutifs (comme pour le losange)
    AB2 = (xB - xA)**2 + (yB - yA)**2      # AB²
    BC2 = (xC - xB)**2 + (yC - yB)**2      # BC²
    # ÉTAPE 3 : les deux diagonales (comme pour le rectangle)
    AC2 = (xC - xA)**2 + (yC - yA)**2      # AC²
    BD2 = (xD - xB)**2 + (yD - yB)**2      # BD²
    # ÉTAPE 4 : les tests, dans l'ordre
    if x1 == x2:
        if y1 == y2:
            # Ici, ABCD est un parallélogramme.
            if AB2 == BC2:
                # Ici, ABCD est un losange (parallélogramme + AB = BC).
                if AC2 == BD2:
                    # Losange ET diagonales égales : c'est un carré.
                    return("ABCD est un carré")
                else:
                    # Losange, mais diagonales différentes :
                    # ce n'est pas un carré.
                    return("ABCD n'est pas un carré")
            else:
                # Parallélogramme, mais AB et BC différents :
                # pas un losange, donc pas un carré.
                return("ABCD n'est pas un carré")
        else:
            # Pas un parallélogramme, donc pas un carré.
            return("ABCD n'est pas un carré")
    else:
        # Pas un parallélogramme, donc pas un carré.
        return("ABCD n'est pas un carré")

# Tests à taper dans la console :
#   carre(0, 0, 2, 0, 2, 2, 0, 2)               réponse attendue : 'ABCD est un carré'
#   carre(1, 0, 4, 1, 3, 4, 0, 3)               réponse attendue : 'ABCD est un carré'
#   carre(1, 1, 5, 1, 5, 3, 1, 3)               réponse attendue : "ABCD n'est pas un carré"
#   carre(0, 0, 3, 1, 4, 4, 1, 3)               réponse attendue : "ABCD n'est pas un carré"


# %% PARTIE 7 - [À ÉCRIRE] Nature exacte du quadrilatère
#
# Écrivez la fonction  nature(xA, yA, xB, yB, xC, yC, xD, yD)  qui renvoie
# la nature la plus précise de ABCD :
#   "ABCD est un carré", "ABCD est un rectangle", "ABCD est un losange",
#   "ABCD est un parallélogramme" ou "ABCD est un quadrilatère quelconque".

# MÉTHODE : on reprend les calculs de la fonction carre, mais au lieu de
# répondre seulement « oui » ou « non », on donne un nom à CHAQUE cas.
# On pose les questions dans l'ordre, comme un arbre :
#
#   Même milieu ?  -- non -->  quadrilatère quelconque
#        |
#       oui  (parallélogramme)
#        |
#   AB = BC ?  -- oui -->  AC = BD ?  -- oui -->  carré
#        |                     |
#        |                    non  -->  losange
#       non
#        |
#   AC = BD ?  -- oui -->  rectangle
#        |
#       non  -->  parallélogramme (rien de plus)

def nature(xA, yA, xB, yB, xC, yC, xD, yD):
    # ÉTAPE 1 : les deux milieux
    x1 = (xA + xC) / 2
    y1 = (yA + yC) / 2
    x2 = (xB + xD) / 2
    y2 = (yB + yD) / 2
    # ÉTAPE 2 : deux côtés consécutifs
    AB2 = (xB - xA)**2 + (yB - yA)**2      # AB²
    BC2 = (xC - xB)**2 + (yC - yB)**2      # BC²
    # ÉTAPE 3 : les deux diagonales
    AC2 = (xC - xA)**2 + (yC - yA)**2      # AC²
    BD2 = (xD - xB)**2 + (yD - yB)**2      # BD²
    # ÉTAPE 4 : on suit l'arbre ci-dessus
    if x1 == x2:
        if y1 == y2:
            # Ici, ABCD est un parallélogramme : on cherche plus précis.
            if AB2 == BC2:
                # Ici, ABCD est un losange. Est-ce même un carré ?
                if AC2 == BD2:
                    # Losange ET diagonales égales : carré.
                    return("ABCD est un carré")
                else:
                    # Losange, diagonales différentes : losange seulement.
                    return("ABCD est un losange")
            else:
                # Parallélogramme, mais pas un losange.
                # Est-ce un rectangle ?
                if AC2 == BD2:
                    # Diagonales égales : rectangle.
                    return("ABCD est un rectangle")
                else:
                    # Ni losange, ni rectangle : parallélogramme seulement.
                    return("ABCD est un parallélogramme")
        else:
            # Les milieux sont différents : pas un parallélogramme.
            return("ABCD est un quadrilatère quelconque")
    else:
        # Les milieux sont différents : pas un parallélogramme.
        return("ABCD est un quadrilatère quelconque")

# Tests à taper dans la console :
#   nature(0, 0, 4, 1, 5, 3, 1, 2)              réponse attendue : 'ABCD est un parallélogramme'
#   nature(1, 1, 5, 1, 5, 3, 1, 3)              réponse attendue : 'ABCD est un rectangle'
#   nature(0, 0, 2, 2, -1, 5, -3, 3)            réponse attendue : 'ABCD est un rectangle'
#   nature(0, 0, 3, 1, 4, 4, 1, 3)              réponse attendue : 'ABCD est un losange'
#   nature(0, 0, 2, 0, 2, 2, 0, 2)              réponse attendue : 'ABCD est un carré'
#   nature(1, 0, 4, 1, 3, 4, 0, 3)              réponse attendue : 'ABCD est un carré'
#   nature(0, 0, 5, 0, 4, 3, 1, 2)              réponse attendue : 'ABCD est un quadrilatère quelconque'
#   nature(0, 0, 4, 1, 1, 2, 5, 3)              réponse attendue : 'ABCD est un quadrilatère quelconque'
#
# [QUESTION 7] La figure 6 est aussi un losange et un rectangle. Pourquoi
# votre fonction nature répond-elle seulement « carré » ?
# Réponse : la fonction s'arrête au premier return rencontré. Pour un carré,
# on passe par AB2 == BC2 puis AC2 == BD2 : on arrive sur « carré », la
# réponse la plus précise, et la fonction s'arrête.


# %% DÉFI - À vous de jouer !
#
# 1) On considère les points E(-2 ; 1), F(1 ; -1), G(3 ; 2) et H(0 ; 4).
#    Quelle est la nature du quadrilatère EFGH ? Répondez avec votre
#    programme, puis justifiez sur papier.
#    Réponse : nature(-2, 1, 1, -1, 3, 2, 0, 4) renvoie 'ABCD est un carré'.
#    [EG] et [FH] ont le même milieu (0,5 ; 1,5) : parallélogramme ;
#    EF² = 13 = FG² : losange ;  EG² = 26 = FH² : rectangle. Donc carré.
#
# 2) Inventez un losange qui n'est pas un carré, et vérifiez-le avec nature.
#    Réponse : par exemple A(0 ; 0), B(2 ; 1), C(4 ; 0), D(2 ; -1) :
#    nature(0, 0, 2, 1, 4, 0, 2, -1) renvoie 'ABCD est un losange'.


# %% POUR ALLER PLUS LOIN
#
# Écrivez une fonction  perimetre(xA, yA, xB, yB, xC, yC, xD, yD)  qui
# renvoie le périmètre du quadrilatère ABCD.
# Tests : figure 2 -> 12.0     figure 5 -> 8.0

# MÉTHODE : le périmètre est la somme des longueurs des 4 côtés :
#   AB + BC + CD + DA.
# Cette fois, on a besoin des VRAIES longueurs (pas de leurs carrés), donc
# on utilise sqrt, comme dans la fonction distance de la partie 2.
# Pas de comparaison avec == ici : les valeurs approchées ne posent pas
# de problème.

def perimetre(xA, yA, xB, yB, xC, yC, xD, yD):
    # Longueur de chacun des 4 côtés, en tournant autour de la figure
    AB = sqrt((xB - xA)**2 + (yB - yA)**2)
    BC = sqrt((xC - xB)**2 + (yC - yB)**2)
    CD = sqrt((xD - xC)**2 + (yD - yC)**2)
    DA = sqrt((xA - xD)**2 + (yA - yD)**2)
    # On additionne les 4 longueurs
    p = AB + BC + CD + DA
    return(p)
