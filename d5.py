# Question 1

print(" ")
print("Question 1")
print(" ")

def triangle(x):
    # int -> str 
    """ Fonction récursif qui prend un entier et retourne une piramide aligné à gauche d'une longueur dépendente du nombre donné et
        utilise le symbole * pour le faire """
    
    if x <= 0:
         return None
    else:
        triangle(x - 1)  
        print('*' * x)
        
# Exemple
triangle(5)

# Question 2

print(" ")
print("Question 2")
print(" ")

def etoiles(n):
    # int -> str
    """ Fonction récursif qui prend un entier et retourne une piramide inversé aligné a gauche et ensuite une piramide inversé a gauche
        d'une longeur dépendante du nombre donné et utilise le symbole * pour le faire """
    
    if n <= 0:
        return None
    else:
       
        print('*' * n)

        etoiles(n - 1)

        print('*' * n)

# Exemple
etoiles(4)
