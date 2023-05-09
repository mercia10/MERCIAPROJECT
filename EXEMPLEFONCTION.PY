def password_function():
    password = "1234"
    while password !=True :
        password_enter  = input ("entrer le mot de pass")
        if password == password_enter:
            print ("bienvenue")
        
            break
##password_function()

def somme_nbr():
    return 5+5
##a =  somme_nbr()
###print(a)


def calcul_nbr (nbr1, nbr2):
        return nbr1*nbr2
        produit = calcul_nbr(4,5)
        print(produit)




