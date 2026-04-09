try:
    acl = int(input("Ingrese el numero de ACL: "))
    if (1 <= acl <= 99) or (1300 <= acl <= 1999):
        print("Es ACL Estándar.")
    elif (100 <= acl <= 199) or (2000 <= acl <= 2699):
        print("Es ACL Extendida.")
    else:
        print("Ese numero no es  ninguna ACL.")
except ValueError:
    print("Tienes que ingresar un número, no letras.")
