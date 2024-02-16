##En proceso
import json

open_j=open("data/users.json")
clientes=json.load(open_j)

booo=True

while booo:
    menu_ad=int(input("\n---Menu Administracion---\n  1. Gestion de usuarios \n  2. Gestion de servicios \n  3. Reportes \n"))

    if menu_ad==1:


        while booo:
            menu_users=int(input("\n\n---Gestion de usuarios---\n  1. Listado \n  2. Servicios contratados \n  3. Bonificaciones \n"))

            if menu_users==1:
                for i in range(len(clientes)):
                    print(clientes[i]) ##CHECK

            if menu_users==2:
                servivi="data/services.json"
                with open(servivi, "r") as hihi:
                    services=json.loads(hihi)
                for i in range(len(clientes)):
                    print(clientes[i])
                    if clientes[i]["id"]==services[i]["id"]:
                        print(services[i]["name"])

            desvivir=str(input("\nVolver a gestion de usuarios? y/n\n"))
            if desvivir=="N" or desvivir=="n":
                break


    elif menu_ad==2:
        ##HABLAR DE SERVICIOS +LISTADO
        ##- Operaciones CRUD para cada tipo de servicio ofrecido, como Internet de Fibra Óptica, planes pospago, prepago, etc.
        ##- Capacidad para agregar, modificar y eliminar servicios según sea necesario.
        ##- Registro de información detallada sobre cada servicio, incluyendo características, precios, entre otros.
        
        while booo:
            menu_serv=int(input("\n\n---Gestion de usuarios---\n  1. Listado \n  2. Servicios contratados \n  3. Bonificaciones \n"))
            
            
            
            desvivir=str(input("\nVolver a gestion de usuarios? y/n\n"))
            if desvivir=="N" or desvivir=="n":
                break

    elif menu_ad==3:
        ##SERVICIOS OFRECIDOS POR LA EMPRESA
        while booo:
            main_rep=int("---Menu de Reportes---\n  1. Productos Disponibles \n  2. Servicios Disponibles \n  3. Servicios/Productos mas populares\n  4. Usuarios segun servicio\n")

    desvivir=str(input("\nFinalizar programa? y/n\n"))
    if desvivir=="y" or desvivir=="Y":
        break
