from collections import namedtuple
###le tuple contenant les nutriment d'un aliment*
tuple_fruit = ('banane', 1, 22 0,3)
print(tuple_fruit[0])
##definition d'un namedtuple
Fruit =namedtuple('Fruit', ['name', 'prot', 'carb', 'fat'])
fruit = namedtuple('Fruit', 'name prot carb fait')
##definition avec valeur par defaut
Fruit =namedtuple('Fruit', ['name', 'prot', 'carb', 'fait'], defaults=(0,0,0))
##instanciation d'un namedtuple
banane = Fruit ('banane', 1, 22 0,3)
print(banane)
orange = Fruit('orange', carb=12, prot=1)
print(orange)
###acces au champ par le nom ou  par indice
print(f' {banane,name} contient {banane[1]} de prot et {banane,carb} grs de glucides' )

###creation d'un namedtuple a partir d'un autre
abricot =orange._replace(name='abricot' ,carb=10)
print (abricot)
###creer un dictionnaire a partir d'un namedtuple
fruit_dict  =banane._asdict()
print(fruit _dict, type(fruit_dict))
###creerun namedtuple a partir d'un dictionnaire
banane2 = Fruit(**fruit_dict)
print(banane2)
