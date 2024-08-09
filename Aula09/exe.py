doces = []

doces.append('Pudim')
doces.append('Brigadeiro')
doces.append('Pave')
doces.append('Quindim')
doces.append('Torta de limao')

print ('Imprimindo a Lista')
print (doces)

doces.insert(3, 'Cajuzin')
for doce in doces:
    print(doce)
