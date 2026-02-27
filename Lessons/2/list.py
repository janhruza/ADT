# Seznamy (list)
# Teorie z 2. cviceni

if __name__ == "__main__":
    a = []
    b = list()
    a.append(5)
    a.append("Ahoj")
    a.append(3.14)
    a.append(True)
    print(a)
    print(type(a[0]))
    print(type(a[1]))
    print(type(a[2]))
    print(type(a[3]))

    # pop
    prvek = a.pop(1)
    print(prvek)
    print(a)

    # insert (inverzni pop)
    a.insert(2, prvek)
    print(a)

    # seradi kopii seznamu a a ulozi ji do b
    # spadne, nelze radit seznam ruznych typu
    b = sorted(a)
    print(b)

    # seradi seznam a
    a.sort()
    print(a)