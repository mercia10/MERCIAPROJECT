prenom= input("entrer votre prenom")
nom= input("entrer votre nom")
age=int(input("entrer votre age"))
print(f"bonjour{prenom} {nom} {age}")
if age<18: 
    print(f"bonjour{prenom} {nom} {age}ans, tu es mineur")
else:
    print(f"bonjour{prenom} {nom} {age} ans tu es majeur")
elif age>= 18 and age < 50:
    print(f"bonjour{prenom} {nom} {age} ans vous etes jeune")  
elif age <18 and age >= 10:
     print(f"bonjour{prenom} {nom} {age}ans, tu es mineur")
elif age < 10 and age >0:
     print(f"bonjour{prenom} {nom} {age}ans, tu es enfant")
else:
print(f"bonjour{prenom} {nom} {age} vous n'avait pas d'age")    