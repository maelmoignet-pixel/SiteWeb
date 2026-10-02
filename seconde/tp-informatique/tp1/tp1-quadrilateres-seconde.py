# =============================================================================
#            TP 1 - PYTHON : QUELLE EST LA NATURE DE CE QUADRILATÈRE ?
#                       Seconde - Géométrie repérée
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
# Réponse :


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
# Réponse :


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
    x = ...
    y = ...
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
    d = ...
    return(d)

# Tests à taper dans la console :
#   distance(1, 1, 4, 5)                    réponse attendue : 5.0
#   distance(-3, 2, 5, 2)                   réponse attendue : 8.0
#   distance(0, 0, 1, 1)                    réponse attendue : 1.4142135623730951
#
# [QUESTION 4] Quelle est la valeur exacte de la distance entre les points
# (0 ; 0) et (1 ; 1) ? Python donne-t-il cette valeur exacte ?
# Réponse :


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
    d2 = ...
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

def parallelogramme(xA, yA, xB, yB, xC, yC, xD, yD):
    # coordonnées du milieu de [AC]
    x1 = (xA + xC) / 2
    y1 = ...
    # coordonnées du milieu de [BD]
    x2 = ...
    y2 = ...
    if x1 == x2:
        if ... :
            return("ABCD est un parallélogramme")
        else:
            return("ABCD n'est pas un parallélogramme")
    else:
        return(...)

# Tests à taper dans la console :
#   parallelogramme(0, 0, 4, 1, 5, 3, 1, 2)     réponse attendue : 'ABCD est un parallélogramme'
#   parallelogramme(0, 0, 2, 2, -1, 5, -3, 3)   réponse attendue : 'ABCD est un parallélogramme'
#   parallelogramme(0, 0, 5, 0, 4, 3, 1, 2)     réponse attendue : "ABCD n'est pas un parallélogramme"
#   parallelogramme(0, 0, 4, 1, 1, 2, 5, 3)     réponse attendue : "ABCD n'est pas un parallélogramme"
#
# [QUESTION 5] Les figures 1 et 8 ont les mêmes points. Pourquoi la figure 8
# n'est-elle pas un parallélogramme ? (Tracez-la !)
# Réponse :


# %% PARTIE 4 - [À ÉCRIRE] Losange
#
# Écrivez la fonction  losange(xA, yA, xB, yB, xC, yC, xD, yD)  qui renvoie
# "ABCD est un losange" ou "ABCD n'est pas un losange".
# Aide : partez de votre fonction parallelogramme et ajoutez ce qu'il faut.
# Pour comparer deux longueurs, calculez leurs carrés.

# Écrivez votre fonction ici :



# Tests à taper dans la console :
#   losange(0, 0, 3, 1, 4, 4, 1, 3)             réponse attendue : 'ABCD est un losange'
#   losange(1, 0, 4, 1, 3, 4, 0, 3)             réponse attendue : 'ABCD est un losange'
#   losange(0, 0, 4, 1, 5, 3, 1, 2)             réponse attendue : "ABCD n'est pas un losange"
#   losange(1, 1, 5, 1, 5, 3, 1, 3)             réponse attendue : "ABCD n'est pas un losange"


# %% PARTIE 5 - [À ÉCRIRE] Rectangle
#
# Écrivez la fonction  rectangle(xA, yA, xB, yB, xC, yC, xD, yD)  qui
# renvoie "ABCD est un rectangle" ou "ABCD n'est pas un rectangle".

# Écrivez votre fonction ici :



# Tests à taper dans la console :
#   rectangle(1, 1, 5, 1, 5, 3, 1, 3)           réponse attendue : 'ABCD est un rectangle'
#   rectangle(0, 0, 2, 2, -1, 5, -3, 3)         réponse attendue : 'ABCD est un rectangle'
#   rectangle(0, 0, 4, 1, 5, 3, 1, 2)           réponse attendue : "ABCD n'est pas un rectangle"
#   rectangle(0, 0, 3, 1, 4, 4, 1, 3)           réponse attendue : "ABCD n'est pas un rectangle"
#
# [QUESTION 6] Dans la figure 3, calculez à la main la longueur exacte des
# diagonales. Pourquoi a-t-on eu raison de comparer les carrés ?
# Réponse :


# %% PARTIE 6 - [À ÉCRIRE] Carré
#
# Écrivez la fonction  carre(xA, yA, xB, yB, xC, yC, xD, yD)  (sans accent
# dans le nom !) qui renvoie "ABCD est un carré" ou "ABCD n'est pas un carré".

# Écrivez votre fonction ici :



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

# Écrivez votre fonction ici :



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
# Réponse :


# %% DÉFI - À vous de jouer !
#
# 1) On considère les points E(-2 ; 1), F(1 ; -1), G(3 ; 2) et H(0 ; 4).
#    Quelle est la nature du quadrilatère EFGH ? Répondez avec votre
#    programme, puis justifiez sur papier.
#    Réponse :
#
# 2) Inventez un losange qui n'est pas un carré, et vérifiez-le avec nature.
#    Réponse :


# %% POUR ALLER PLUS LOIN
#
# Écrivez une fonction  perimetre(xA, yA, xB, yB, xC, yC, xD, yD)  qui
# renvoie le périmètre du quadrilatère ABCD.
# Tests : figure 2 -> 12.0     figure 5 -> 8.0
