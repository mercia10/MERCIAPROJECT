list_name =[
    "franck", "mercia", "hermann"
    "joydy", "moise", "germain"
]
list_note =[34, 46, 20]
list_note.append(20)
###list_note.clear
list_note.count()
### liste inbrique  qui nous envoie au tableau
list_etudiant = [list_name,list_note]
###slicing
name =list_name[:-1]
print(name)
###l'indexing
print(f"nom et note{list_etudiant[0][0]} {list_etudiant [1][2]} ")
print(f"nom et note{list_etudiant[0][1::2]} {list_etudiant [1][1:]} ")

###structure itterative
for index in list_etudiant:
    print(index[0])
    list_name =[
    "franck", "mercia", "hermann"
    "joydy", "moise", "germain"
]
list_note =[34, 46, 20]
list_note.append(20)
###list_note.clear
list_note.count()
### liste inbrique  qui nous envoie au tableau
list_etudiant = [list_name,list_note]
##structure itterative
for index in enumerate (list_etudiant):
    for nomote in index :
        print(f"nom {nomote}")