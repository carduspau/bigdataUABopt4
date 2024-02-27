"""
noms = ['John', 'Smith', 'Jana']
notes = [1, 7, 5]

dicc = {}

for i in range(len(noms)):
    dicc[noms[i]] = notes[i]

print(dicc)
"""

#EXPLICACIO DEL ZIP
noms = ['John', 'Smith', 'Jana']
notes = [1, 7, 5]

for noms,notes in zip(noms,notes):
    print(noms,notes)




