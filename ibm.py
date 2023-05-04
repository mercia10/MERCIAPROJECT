########calcul la factorielle d'un nombre
def fac(n): 
    return 1 if (n==1 or n==0) else n * fac(n - 1);  
 
num = 5; 
###affiche le resulta de la factorielle
print("LA FOCTORIEL",num,"est", fac(num))


