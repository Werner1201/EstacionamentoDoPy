def menu():
    esc = True
    while esc == True:
        print(f"{30*'-='}")
        print(f"{10*'-='}EstacionamentoDoPy{11*'-='}")
        print(f"{30*'-='}")
        res = int(input("Deseja continuar ?<S:1/N:0>"))
        if res == 1:
            esc = True
        else:
            esc = False


#Pequeno teste
menu()
