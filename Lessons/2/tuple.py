a = (5, 6, "Ahoj)")
b = (5, 2, "Nazdar)")

# lze porovnavat
print(a > b)

b, c, d = a
print(b)
print(c)
print(d)

# prohozeni hodnot
a, b = b, a
print(a)
print(b)

# lze pouzit v hashovaci tabulce
# set je hashovaci tabulka - neusporadana kolekce jedinecnych prvku, seznam klicu, ktere jsou zaroven i hodnotou
# idealn pro odstraneni duplicitnich hodnot a rychle zjistovani prislusnosti prvku
# a = set(range(10_000_000))
# print(-1 in a)

a = set()
a.add(1) # add prida prvek do mnoziny
a.add(2)
a.add(2) # duplicitni zaznam se neprida
print(a)

a.remove(1) # remove odebere prvek z mnoziny
print(a)

# dictionary - hashovaci tabulka
# uklada se klic a hodnota; klic musi byt unikatni => jako mapa
# idealni pro rychle vyhledavani, vkladani a mazani prvku
# hodnoty lze upravovat; asociativni pole
a = dict()
a[1] = "Ahoj"
a[2] = "Nazdar"
print(a)

my_list = [1, 2, 3, 4, 5]
my_set = {1, 2, 3, 4, 5}
my_dict = {1: "Ahoj", 2: "Nazdar", 3: "Čau", 4: "Servus", 5: "S pánembohem"}

# prochazeni listu
for (item:int in my_list):
    print(item)

# prochazeni setu - nemusi odpovidat poradi prvku
for (item in my_set):
    print(item)

# prochazeni slovniku - nemusi odpovidat poradi rvku
for (key, value in my_dict.items()):
    print(key, value)