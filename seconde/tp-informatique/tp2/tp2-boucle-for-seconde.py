# =============================================================================
#                 TP 2 - PYTHON : RÉPÉTER AVEC LA BOUCLE FOR
#            Seconde - Arithmétique, pourcentages, fonctions
# =============================================================================
#
# OBJECTIF
#   Apprendre à faire RÉPÉTER des instructions à Python avec la boucle for,
#   et s'en servir pour :
#     - chercher les diviseurs d'un nombre et les nombres premiers ;
#     - calculer des évolutions successives en pourcentage ;
#     - faire le tableau de valeurs et tracer la courbe d'une fonction.
#   On réutilise tout ce qui a été vu au TP 1 : fonctions, return, print,
#   if / else, %, **, et l'arrêt d'une fonction au premier return.
#
# COMMENT EXÉCUTER UNE FONCTION AVEC SPYDER (comme au TP 1)
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


# %% [EXEMPLE 1] Une première boucle for
#
# La boucle for fait RÉPÉTER des instructions.
#   for i in range(5):
#       ...
# veut dire : « pour i allant de 0 à 4, faire ... ».
#
# ATTENTION : range(5) donne les nombres 0, 1, 2, 3, 4 : on commence à 0
# et on s'arrête JUSTE AVANT 5. Cela fait bien 5 nombres.
#
# Comme pour if, ce qui est répété est DÉCALÉ vers la droite (indenté),
# et la ligne du for se termine par deux-points  :

def compter():
    for i in range(5):
        print(i)

# Test à taper dans la console :
#   compter()                               réponse attendue : 0 1 2 3 4
#                                           (un nombre par ligne)


# %% [EXEMPLE 2] Choisir le début et la fin
#
# range(a, b) donne les entiers de a jusqu'à b, b NON COMPRIS.
# Par exemple range(1, 11) donne 1, 2, 3, ..., 10.
# La variable de la boucle peut porter n'importe quel nom : ici k.

def table(n):
    for k in range(1, 11):
        print(n, "x", k, "=", n * k)

# Tests à taper dans la console :
#   table(7)                                réponse attendue : 7 x 1 = 7
#                                                              7 x 2 = 14
#                                                              ...
#                                                              7 x 10 = 70
#
# [QUESTION 1] Que faut-il écrire dans le range pour que la table aille
# jusqu'à  7 x 20 ?
# Réponse :


# %% [EXEMPLE 3] Faire une somme avec une boucle : l'ACCUMULATEUR
#
# Pour calculer 1 + 2 + 3 + ... + n, on part d'une variable s qui vaut 0,
# puis on lui AJOUTE chaque nombre, un par un :
#   s = s + k   veut dire : « la nouvelle valeur de s est l'ancienne
#                             valeur de s, plus k ».
# Le return est APRÈS la boucle (il n'est pas décalé sous le for) : on
# renvoie s une seule fois, quand la boucle est terminée.

def somme(n):
    s = 0
    for k in range(1, n + 1):
        s = s + k
    return(s)

# Tests à taper dans la console :
#   somme(4)                                réponse attendue : 10   (1+2+3+4)
#   somme(10)                               réponse attendue : 55
#
# [QUESTION 2] Pourquoi a-t-on écrit  range(1, n + 1)  et pas  range(1, n) ?
# Réponse :
#
# [QUESTION 3] Que vaut 1 + 2 + 3 + ... + 100 ?
# Réponse :


# =============================================================================
#                 PARTIE 1 : ARITHMÉTIQUE
# Rappel du TP 1 :  n % d  donne le reste de la division de n par d.
# d est un DIVISEUR de n quand ce reste vaut 0.
# =============================================================================


# %% PARTIE 1 - [À COMPLÉTER] Afficher les diviseurs d'un nombre
#
# Un diviseur de n est compris entre 1 et n. On les essaie donc TOUS, un
# par un, avec une boucle, et on affiche ceux qui divisent n.
# C'est un « if » à l'intérieur d'un « for ».

def diviseurs(n):
    # d prend les valeurs 1, 2, 3, ..., n
    for d in range(1, ...):
        # on teste si d divise n
        if ... :
            print(d)

# Tests à taper dans la console :
#   diviseurs(12)                           réponse attendue : 1 2 3 4 6 12
#   diviseurs(13)                           réponse attendue : 1 13
#                                           (un nombre par ligne)


# %% PARTIE 1 - [À COMPLÉTER] Compter les diviseurs : le COMPTEUR
#
# Au lieu d'afficher les diviseurs, on veut les COMPTER. On utilise une
# variable compteur qui part de 0 et qui augmente de 1 à chaque diviseur
# trouvé (c'est le même principe que l'accumulateur de l'exemple 3).

def nombre_diviseurs(n):
    compteur = ...
    for d in range(1, n + 1):
        if n % d == 0:
            compteur = ...
    return(compteur)

# Tests à taper dans la console :
#   nombre_diviseurs(12)                    réponse attendue : 6
#   nombre_diviseurs(13)                    réponse attendue : 2
#   nombre_diviseurs(1)                     réponse attendue : 1


# %% PARTIE 1 - [À ÉCRIRE] Nombre premier
#
# Rappel : un nombre PREMIER est un entier qui a EXACTEMENT deux
# diviseurs : 1 et lui-même.
# Écrivez la fonction  premier(n)  qui renvoie "n est premier" ou
# "n n'est pas premier", en utilisant la fonction nombre_diviseurs.

# Écrivez votre fonction ici :




# Tests à taper dans la console :
#   premier(13)                             réponse attendue : 'n est premier'
#   premier(91)                             réponse attendue : "n n'est pas premier"
#   premier(97)                             réponse attendue : 'n est premier'
#
# [QUESTION 4] 1 est-il un nombre premier ? Pourquoi ?
# Réponse :
#
# [QUESTION 5] Pourquoi premier(91) répond-il que 91 n'est pas premier ?
# Réponse :


# %% PARTIE 1 - [À ÉCRIRE] Afficher les nombres premiers
#
# Écrivez la fonction  afficher_premiers(n)  qui AFFICHE tous les nombres
# premiers compris entre 2 et n.
# Aide : une boucle qui essaie tous les entiers k de 2 à n, et un if qui
# utilise nombre_diviseurs(k).

# Écrivez votre fonction ici :




# Tests à taper dans la console :
#   afficher_premiers(30)                   réponse attendue : 2 3 5 7 11 13 17 19 23 29
#                                           (un nombre par ligne)
#
# [QUESTION 6] Combien y a-t-il de nombres premiers inférieurs à 100 ?
# Réponse :


# =============================================================================
#                 PARTIE 2 : POURCENTAGES ET ÉVOLUTIONS
# Rappel du cours : augmenter de t %, c'est multiplier par  1 + t/100.
#                   diminuer  de t %, c'est multiplier par  1 - t/100.
# Une baisse de t % est donc une évolution de -t % : le même calcul
# 1 + t/100 marche si on donne à t une valeur négative.
# =============================================================================


# %% PARTIE 2 - [À COMPLÉTER] Évolutions successives
#
# Une valeur évolue de t % chaque année, pendant n années.
# La fonction evolution renvoie la valeur obtenue au bout de n années.
# Chaque tour de boucle = une année = une multiplication par 1 + t/100.

def evolution(valeur, t, n):
    # coefficient multiplicateur
    cm = ...
    # on répète n fois : une fois par année
    for annee in range(...):
        valeur = ...
    return(valeur)

# Tests à taper dans la console :
#   evolution(1000, 5, 1)                   réponse attendue : 1050.0
#   evolution(1000, 5, 2)                   réponse attendue : 1102.5
#   evolution(200, -10, 2)                  réponse attendue : 162.0
#
# [QUESTION 7] Un article à 100 € augmente de 10 %, puis baisse de 10 %.
# Calculez son prix avec  evolution(evolution(100, 10, 1), -10, 1).
# Revient-on à 100 € ? Pourquoi ?
# Réponse :


# %% PARTIE 2 - [À ÉCRIRE] Tableau d'évolution
#
# Une ville compte 20 000 habitants. Sa population baisse de 3 % par an.
# Écrivez la fonction  tableau_evolution(valeur, t, n)  qui AFFICHE, pour
# chaque année de 1 à n, le numéro de l'année et la valeur.
# Pour arrondir à l'unité, utilisez  round(valeur) .

# Écrivez votre fonction ici :




# Tests à taper dans la console :
#   tableau_evolution(20000, -3, 4)         réponse attendue : année 1 : 19400
#                                                              année 2 : 18818
#                                                              année 3 : 18253
#                                                              année 4 : 17706


# %% PARTIE 2 - [À COMPLÉTER] Au bout de combien d'années la valeur double ?
#
# On place 1000 € à 5 % par an. On cherche la PREMIÈRE année où le capital
# atteint le double (2000 €).
# Idée : on fait avancer les années une par une (boucle for), et dès que
# le capital dépasse le double, on renvoie le numéro de l'année.
# Rappel du TP 1 (question 7) : un return ARRÊTE la fonction... et donc
# aussi la boucle !

def doublement(valeur, t):
    cm = 1 + t / 100
    # le double de la valeur de départ
    cible = ...
    for annee in range(1, 101):
        valeur = ...
        if ... :
            return(annee)

# Tests à taper dans la console :
#   doublement(1000, 5)                     réponse attendue : 15
#   doublement(1000, 10)                    réponse attendue : 8
#
# [QUESTION 8] Le résultat dépend-il de la somme placée au départ ?
# Testez doublement(50, 5) et doublement(1000000, 5).
# Réponse :


# =============================================================================
#                 PARTIE 3 : FONCTIONS, TABLEAU DE VALEURS, COURBE
# =============================================================================


# %% PARTIE 3 - [EXEMPLE 4] Une fonction mathématique
#
# La fonction mathématique  f(x) = x² - 4x + 3  s'écrit en Python :

def f(x):
    return(x**2 - 4*x + 3)

# Tests à taper dans la console :
#   f(0)                                    réponse attendue : 3
#   f(2)                                    réponse attendue : -1
#   f(2.5)                                  réponse attendue : -0.75


# %% PARTIE 3 - [À COMPLÉTER] Tableau de valeurs
#
# La fonction tableau_valeurs affiche les valeurs de f(x) pour tous les
# entiers x de a à b (b compris).

def tableau_valeurs(a, b):
    for x in range(..., ...):
        print("x =", x, "   f(x) =", ...)

# Test à taper dans la console :
#   tableau_valeurs(-1, 5)                  réponse attendue : x = -1    f(x) = 8
#                                                              x = 0    f(x) = 3
#                                                              ...
#                                                              x = 5    f(x) = 8
#
# [QUESTION 9] D'après le tableau, quels sont les antécédents de 0 par f ?
# Quelle semble être la plus petite valeur prise par f ?
# Réponse :


# %% PARTIE 3 - [EXEMPLE 5] Placer des points dans un repère
#
# La ligne  import matplotlib.pyplot as plt  permet de dessiner : ne
# l'effacez pas.
#   plt.plot(x, y, "o")    place le point de coordonnées (x ; y)
#                          ("o" veut dire : dessiner un petit rond)
#   plt.grid()             ajoute un quadrillage
#   plt.show()             AFFICHE le dessin, une fois tous les points placés
# Le dessin apparaît dans l'onglet « Graphiques » (Plots), en haut à droite
# de Spyder.

import matplotlib.pyplot as plt

def trois_points():
    plt.plot(1, 2, "o")
    plt.plot(3, -1, "o")
    plt.plot(4, 4, "o")
    plt.grid()
    plt.show()

# Test à taper dans la console :
#   trois_points()                          trois points : (1 ; 2), (3 ; -1), (4 ; 4)


# %% PARTIE 3 - [À COMPLÉTER] Tracer la courbe de f
#
# On veut tracer la courbe de f entre a et b. On découpe [a ; b] en n
# morceaux de même longueur  pas = (b - a) / n , et on place les n + 1
# points de la courbe d'abscisses  x = a, a + pas, a + 2 x pas, ..., b.
# Avec beaucoup de points très proches, on « voit » la courbe.

def courbe(a, b, n):
    pas = ...
    for k in range(...):
        x = ...
        # on place le point de la courbe d'abscisse x
        plt.plot(x, ..., "o")
    plt.grid()
    plt.show()

# Tests à taper dans la console :
#   courbe(-1, 5, 60)                       une belle parabole « en U »
#   courbe(-1, 5, 3)                        ... seulement 4 points !
#
# [QUESTION 10] Pourquoi ne reconnaît-on pas la courbe avec n = 3 ?
# Réponse :


# %% PARTIE 3 - [À ÉCRIRE] Chercher le minimum
#
# Écrivez la fonction  minimum(a, b, n)  qui calcule f(x) pour les mêmes
# n + 1 valeurs de x que la fonction courbe, et renvoie la PLUS PETITE
# valeur de f(x) trouvée.
# Aide : une variable mini qui vaut f(a) au départ ; à chaque tour, si
# f(x) est plus petit que mini, mini prend la valeur f(x).

# Écrivez votre fonction ici :




# Tests à taper dans la console :
#   minimum(-1, 5, 60)                      réponse attendue : -1.0
#   minimum(3, 5, 20)                       réponse attendue : 0
#
# [QUESTION 11] Avec minimum(3, 5, 20), pourquoi trouve-t-on 0 et pas -1 ?
# Réponse :


# %% DÉFI - Les nombres parfaits
#
# Un nombre est PARFAIT s'il est égal à la somme de ses diviseurs, sans
# compter lui-même. Par exemple, 6 est parfait : 1 + 2 + 3 = 6.
# 1) Écrivez une fonction  somme_diviseurs(n)  qui renvoie la somme des
#    diviseurs de n, sans compter n.
# 2) Écrivez une fonction  parfaits(n)  qui affiche tous les nombres
#    parfaits entre 2 et n.
# Combien y en a-t-il jusqu'à 1000 ?

# Écrivez vos deux fonctions ici :




# Tests à taper dans la console :
#   somme_diviseurs(6)                      réponse attendue : 6
#   somme_diviseurs(12)                     réponse attendue : 16
#   parfaits(1000)                          réponse attendue : 6 28 496
#
# Réponse :
