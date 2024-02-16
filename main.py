import json

open_j=open("data/users.json")
clientes=json.load(open_j)

booo=True

while booo:
    menu_ad=int(input("\n---Menu Administracion---\n  1. Gestion de usuarios \n  2. Gestion de servicios \n  3. Reportes \n"))

    if menu_ad==1:

        while booo:
            menu_users=int(input("\n\n---Gestion de usuarios---\n  1. Listado \n  2. Servicios contratados \n  3. Bonificaciones \n  4. Registrar nuevo usuario \n  5. Modificar usuario \n"))


            if menu_users==1: ##============================CHECK=====================================
                print("\n\n---Listado de usuarios---\n")
                for i in range(len(clientes)):
                    print(clientes[i])
                    print("\n")
            if menu_users==2:##============================CHECK=====================================
                servivi="data/services.json"
                with open(servivi, "r") as hihi:
                    services=json.load(hihi)
                print("\n\n---Servicios/Productos contratados por los usuarios---\n")
                for i in range(len(clientes)):
                    print(clientes[i])
                    print("\nServicios/Productos: ")
                    for j in range(len(services)):
                        for item in clientes[i]["services"]:
                            if item==services[j]["id_ser"]:
                                print(services[j]["name"])
                    print("\n")
            if menu_users==3: ##============================CHECK=====================================
                bonbon=int(input("\n\n---Bonificaciones---\n  1. Usuarios con bonificacion \n  2. Usuarios sin bonificacion \n"))
                while booo:
                    if bonbon==1:
                        print("\n\n---Listado de usuarios con bonificacion---\n")
                        for i in range(len(clientes)):
                            if clientes[i]["lealtad"]>=10:
                                print(clientes[i]) ##Miercoles ;_;
                                print("Este usuario tiene bonificacion de lealtad por ser cliente durante ",clientes[i]["lealtad"]," años\n")
                                with open("data/asesor.json","r") as estres:
                                    soy_unalis=json.loads(estres)
                                    holiwis=[clientes[i]]
                                    soy_unalis.append(holiwis)
                                with open("data/asesor.json","w"):
                                    json.dumps(soy_unalis)
                    if bonbon==2:
                        print("\n\n---Listado cuanto le falta al usuario para obtener bonificacion---\n")
                        for i in range(len(clientes)):
                            if clientes[i]["lealtad"]<10:
                                print(clientes[i])
                                print("Este usuario no tiene bonificacion de lealtad.Podra obtenerlo en ",10-clientes[i]["lealtad"]," años.\n")
                    desvivir=str(input("\nVolver a menu de bonificacioner? y/n\n"))
                    if desvivir=="N" or desvivir=="n":
                        break

            if menu_users==4: ##Borra jsons :(
                while booo:
                    new_id=int(input("\n>Ingrese el # de identificacion: "))
                    new_name=str(input("\n>Ingrese el primer nombre: "))
                    new_sec_name=str(input("\n>Ingrese el primer apellido: "))
                    new_num=int(input("\n>Ingrese el numero de telefono: "))
                    new_loc=str(input("\n>Ingrese la direccion: "))
                    
                    with open("data/users.json","r") as AAA:
                        clicli=json.loads(AAA)
                    new_user=clicli
                    
                    new_user={
                            "id":new_id,
                            "name":new_name,
                            "sec_name":new_sec_name,
                            "num_cel":new_num,
                            "direccion":new_loc,
                            "services":[],
                            "lealtad":0
                            }
                    
                    with open("data/users.json","w") as AAA:
                        clicli=json.dumps(new_user)
                    
                    desvivir=str(input("\nRegistrar otro usuario? y/n\n"))
                    if desvivir=="N" or desvivir=="n":
                        break
            if menu_users==5:
                print("\n---Lista Clientes---\n")
                for i in range(len(clientes)):
                    print(clientes[i])
                    print("\n")
                user_es=int(input("Que usuario va a editar segun su ID?"))
                for item in clientes:
                    if item["id"]==user_es:
                        
                    
            
            desvivir=str(input("\nVolver a gestion de usuarios? y/n\n"))
            if desvivir=="N" or desvivir=="n":
                break

    elif menu_ad==2:
        ##HABLAR DE SERVICIOS +LISTADO
        ##- Operaciones CRUD para cada tipo de servicio ofrecido, como Internet de Fibra Óptica, planes pospago, prepago, etc.
        ##- Capacidad para agregar, modificar y eliminar servicios según sea necesario.
        ##- Registro de información detallada sobre cada servicio, incluyendo características, precios, entre otros.
        
        while booo:
            menu_serv=int(input("\n\n---Gestion de servicios y productos---\n  1. Listado \n  2. listado con descripcion \n  3. Buscar servicio especifico\n"))
            servicios=open("data/services.json")
            serrevivi=json.load(servicios)
            if menu_serv==1:
                print("\n\n---Listado de servicios y productos---\n")
                for i in range(len(serrevivi)):
                    a=serrevivi[i]["id_ser"]
                    b=serrevivi[i]["name"]
                    print(f"{i}|| ID: {a}\nNombre: {b}\n||")
            desvivir=str(input("\nVolver a gestion de servicios? y/n\n"))
            if desvivir=="N" or desvivir=="n":
                break

    elif menu_ad==3:
        ##SERVICIOS OFRECIDOS POR LA EMPRESA
        while booo:
            main_rep=int("---Reportes---\n  1. Productos Disponibles \n  2. Servicios Disponibles \n  3. Servicios/Productos mas populares\n  4. Usuarios segun servicio\n")
            if main_rep==1:
                servicios=open("data/services.json")
                serrevivi=json.loads(servicios)
                if menu_serv==1:
                    print("\n\n---Listado de servicios y productos---\n")
                    for i in range(len(serrevivi)):
                        a=serrevivi[i]["id"]
                        b=serrevivi[i]["name"]
                        print(f"ID: {a} Nombre: {b}\n")
            
            desvivir=str(input("\nVolver al menu de reportes? y/n\n"))
            if desvivir=="N" or desvivir=="n":
                break
    desvivir=str(input("\nFinalizar programa? y/n\n"))
    if desvivir=="y" or desvivir=="Y":
        break
