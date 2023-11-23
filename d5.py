# Question 1

print(" ")
print("Question 1")
print(" ")
# Question 1

def triangle(x):
    # int -> str
    """ Fonction récursive qui prend un entier et retourne un dessin composé d'étoiles sous forme de triangle """
    
    if x <= 0:
        return ""
    
    else:
        pyramide = triangle(x - 1) + '*' * x + '\n'
        
        return pyramide

# Exemple question 1
print(triangle(5))

print(" ")
print("Question 2")
print(" ")

# Question 2

def etoiles(x):
    # int -> str
    """ Fonction récursif qui prend un entier et retourne une piramide inversé aligné a gauche et ensuite une piramide inversé a gauche
        d'une longeur dépendante du nombre donné et utilise le symbole * pour le faire """
    
    if x <= 0:
        return ""
    
    else:
        pyramide = '*' * x + '\n'

        dessin_f = pyramide + etoiles(x - 1) + pyramide
        
        return dessin_f
      

# Exemple question 2
print(etoiles(4))

print(" ")
print("Question 3")
print(" ")

# Question 3

def prodListePos_rec(liste, long):
    # List, len -> int
    """ Fonction qui prend une liste un la longueur de la liste et qui retourne le produit de tout les nombre >0 dans la liste """
    
    if long == 0:
        return 1
    
    elif liste[long - 1] > 0:
        p1 = liste[long - 1] * prodListePos_rec(liste, long - 1)
        
        return p1
    
    else:
        p2 = prodListePos_rec(liste, long - 1)
        
        return p2

def prodLRec1(liste):
    
    if len(liste) == 0:
        return 1
    
    elif liste[0] > 0:
        p1 = liste[0] * prodLRec1(liste[1:])
        
        return p1
    
    else :
        p2 = prodLRec1(liste[1:])
        
        return p2

# Exemples prodListePos_rec
l = [1, -2, 5, 0, 6, -5]
print(prodListePos_rec(l, len(l)))  
print(prodLRec1(l))                 

# Exemple prodListePos_rec
l = [1, -2, 5, 0, 6, -5]
print(prodListePos_rec(l, len(l)))  
print(prodLRec1(l))                 
