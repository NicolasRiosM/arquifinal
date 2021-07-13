import socket
import bcrypt
import time
import datetime
import hashlib

from conect import *
import threading
global email
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
print('connecting to {} port {}'.format(*server_address))
s.connect(server_address)

s.sendall(bytes('00005getsv','utf-8'))
recibido=s.recv(4096)
print(recibido)
def limpiar(var):
    var = str(var)
    var = var.replace("[","")
    var = var.replace("(","")
    var = var.replace("]","")
    var = var.replace(")","")
    var = var.replace(",","")
    return var

        
     
        
       
#-------------------------interfaz--------------------------------------#

while True:


    opcion = input("""Que servicio desea: 
	1.- Login
	2.- Register

        0.- salir



        En caso de algun inconveniente contactarse al mail admin@mail.udp.cl\n""")
    if opcion == "0":
        s.sendall(bytes('quit','utf-8'))
        time.sleep(5)
        break
    
    if(opcion == '1'):
        print("Ha seleccionado la opcion de inicio de sesión\n")
        #mandar a codigo maca
        
        
        #ingreso de dato
        
        email = input("Ingrese su email \n")
        password = input("Ingrese su contraseña\n")


        #enviar mensaje
        datos = email + " " + password 
        aux = llenado(len(datos+'log20'))
        mensaje = aux + 'log20' + datos
        print(mensaje)
        s.send(bytes(mensaje,'utf-8'))
        
       
        
        
        recibido=s.recv(4096)
        
        
        
        recibido = recibido[12:].decode()
        if recibido == "no_existe_usuario":
                print("No se pudo acceder")
                continue
        else:
                
                break
        

    if(opcion == '2'):
        
        print("Para crear su cuenta de usuario, ingrese sus datos a continuación.")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        rut = input("RUT: ")
        psw = input("Contraseña: ")
        contacto = input("Numero de contacto: ")
        region = input("Región de residencia: ")
        email = input("E-mail: ")
        #--------------HASH----------------
        pswAux=hashlib.md5(psw.encode())
        pswAux2=pswAux.hexdigest()
        #----------------------------------
        #envio de datos
        datos = nombre + " " + apellido + " " + rut + " " + pswAux2 + " " + contacto + " " + region + " " + email
        temp = llenado(len(datos+'regi7'))
        mensaje = temp + 'regi7' + datos
        s.sendall(bytes(mensaje,'utf-8'))
        
        recibido = s.recv(4096)
        print(recibido[10:])
        
        
while True:
    opcion = input("""Que servicio desea: 
	    1.- Agregar mascota
	    2.- Editar mascota
            3.- Eliminar mascota
            4.- Ver mascotas
            5.- Editar usuario 
            6.- Eliminar usuario
            0.- salir



            En caso de algun inconveniente contactarse al mail admin@mail.udp.cl\n""")

    if opcion=="1":
        
        email1 = email
        email2 = email1 + " "
        temp2= llenado(len(email2+'cr34d'))
        mesj= temp2+ 'cr34d' + email2
        s.sendall(bytes(mesj, 'utf-8'))

                
                

                #ID USUARIO:
        consulta0= f"SELECT idusuario FROM usuario WHERE email='{email1}';"
        idusuario1 = consultar(consulta0)
        idusuario1 = limpiar(idusuario1)
                

                #RELACION USUARIO PERRO
        consulta1= f"SELECT idmascota FROM usuariomascota where idusuario = '{idusuario1}';"
        idmascota1 = consultar(consulta1)
                
                
                #PERROS DISPONIBLES
        print("Sus perros ingresados: ")
        for gg in idmascota1:
            gg = limpiar(gg)
                        
            a = consultar(f"SELECT nombre, edad, raza, descripcion, idmascota FROM mascota where idmascota = '{gg}';")
            print(a)

                #ingreso de datos
        print("ingrese los siguientes datos del perrito")
        nombre = input("Escribir nombre: ")
        edad = input("Escribir edad en meses: ")
        raza = input("Escribir raza o callejero: ")
        descripcion = input("Escribir descripción corta: ")

                #envio de datos
        datos = nombre + " " + edad + " " + raza + " " + descripcion
        temp = llenado(len(datos+'cr34d'))
        mensaje = temp + 'cr34d' + datos
        s.sendall(bytes(mensaje,'utf-8'))
               

        
        recibido = s.recv(4096)
        print(recibido[10:])
        
        
    
    if opcion=="2":
        s.sendall(bytes('00010getsveditd','utf-8'))
        email1 = email

          

                #ID USUARIO:
        consulta0= f"SELECT idusuario FROM usuario WHERE email='{email1}';"
        idusuario1 = consultar(consulta0)
        idusuario1 = limpiar(idusuario1)

                #RELACION USUARIO PERRO
        consulta1= f"SELECT idmascota FROM usuariomascota where idusuario = '{idusuario1}';"
        idmascota1 = consultar(consulta1)

                #PERROS DISPONIBLES
        print("Sus perros ingresados: ")
        for gg in idmascota1:
            
            gg = limpiar(gg)
                        
            a = consultar(f"SELECT nombre, edad, raza, descripcion, idmascota FROM mascota where idmascota = '{gg}';")
            print(a)

                #ingreso de ide
        print("AVISO: En el arreglo del perro el ULTIMO NUMERO es el ID del animal")
        ide = input("Ingrese id de animal a editar: ")

                #ingreso nuevo de datos
        nombre = input("Escribir nombre: ")
        edad = input("Escribir edad: ")
        raza = input("Escribir raza: ")
        descripcion = input("Escribir descripcion: ")

                #envio de datos nuevos
        datos = nombre + " " + edad + " " + raza + " " + descripcion + " " + ide
        temp = llenado(len(datos+'editd'))
        mensaje = temp + 'editd' + datos
        s.sendall(bytes(mensaje,'utf-8'))
        
        recibido = s.recv(4096)
        print(recibido[10:])
      
           


        
    if opcion=="3":
        s.sendall(bytes('00010getsvelimd','utf-8'))
        email1 = email

             

                #ID USUARIO:
        consulta0= f"SELECT idusuario FROM usuario WHERE email='{email1}';"
        idusuario1 = consultar(consulta0)
        idusuario1 = limpiar(idusuario1)

                #RELACION USUARIO PERRO
        consulta1= f"SELECT idmascota FROM usuariomascota where idusuario = '{idusuario1}';"
        idmascota1 = consultar(consulta1)

                #PERROS DISPONIBLES
        print("Sus perros ingresados: ")
        for gg in idmascota1:
                gg = limpiar(gg)
                        
                a = consultar(f"SELECT nombre, edad, raza, descripcion, idmascota FROM mascota where idmascota = '{gg}';")
                print(a)

                #ingreso de ide
        print("AVISO: En el arreglo del perro el ULTIMO NUMERO es el ID del animal")
        ide = input("Ingrese id de animal a eliminar: ")

                #envio de datos viejos
        datos = ide + " " + "jaja"
        temp = llenado(len(datos+'elimd'))
        mensaje = temp + 'elimd' + datos
        s.sendall(bytes(mensaje,'utf-8'))
        
        recibido = s.recv(4096)
        print(recibido[10:])

            
        
    if opcion== "4":
        
        consulta = f"SELECT mascota.nombre, mascota.edad, mascota.raza, mascota.descripcion, usuario.nombre, usuario.apellido, usuario.contacto, usuario.email, usuario.region FROM mascota, usuario, usuariomascota WHERE mascota.idmascota = usuariomascota.idmascota AND usuario.idusuario = usuariomascota.idusuario;"
        respuesta = consultar(consulta)
               
        for i in respuesta:
            nombreM = i[0]
            edad = i[1]
            raza = i[2]
            desc = i[3]
            nombreU = i[4]
            apellido = i[5]
            contacto = i[6]
            email = i[7]
            region = i[8]
            print("Nombre mascota: ",nombreM,"\nEdad (meses): ",edad,"\nRaza: ",raza,"\nDescripcion: ",desc,"\nNombre dueñx: ",nombreU," ",apellido,"\nContacto: ",contacto,"\nEmail: ",email,"\nRegion: ",region)
            print("-----------------------------")
        temp = llenado(len('viewd'))
        mensaje = temp + 'viewd'
        s.sendall(bytes(mensaje,'utf-8'))
        recibido = s.recv(4096)
        print(recibido[10:])
      


            
    if opcion== "5":
        
        email1 = email # aqui pasas el atributo de mail
        print("Sus datos de usuario: ")
        consulta = f"SELECT nombre, apellido, rut, email, pass, contacto, region, tipodeusuario, idusuario FROM usuario WHERE email='{email1}';"
        datosU = consultar(consulta)
        n = datosU[0][0]
        a = datosU[0][1]
        r = datosU[0][2]
        e = datosU[0][3]
        p = datosU[0][4]
        c = datosU[0][5]
        re = datosU[0][6]
        t = datosU[0][7]
        id = datosU[0][8]
        if t == True:
            t = "Administrador"
        if t == False:
            t = "Usuario normal"
        print("Nombre completo: ",n,a,"\nRut: ",r,"\nEmail: ",e,"\nContraseña: ",p,"\nContacto: ",c,"\nRegion: ",re,"\nTipo de cuenta: ",t,"\nID usuario: ",id)
        print("-----------------------------")
        print("Editar datos: ")
        nombre = input("Escribir nombre: ")
        apellido = input("Escribir apellido: ")
        rut = input("Escribir rut: ")
        contraseña = input("Escribir contraseña: ")
        contacto = input("Escribir numero telefonico:")
        region = input("Escribir region:")

        
                
        pswAux=hashlib.md5(contraseña.encode())
        pswAux2=pswAux.hexdigest()

                #envio de datos
        datos = nombre + " " + apellido + " " + rut +  " " + pswAux2 + " " + contacto + " " + region + " " + email
        temp = llenado(len(datos+'editu'))
        mensaje = temp + 'editu' + datos
        s.sendall(bytes(mensaje,'utf-8'))
               

        recibido = s.recv(4096)
        
        print(recibido[10:])
    if opcion=="6":
       
        email = email
                # seleccionar tipo de usuario del usuario loggeado
        consulta0 = f"SELECT tipodeusuario FROM usuario where email='{email}';"
        tipousuario = consultar(consulta0)
        tipousuario = limpiar(tipousuario)
        print(tipousuario)
        print(type(tipousuario))
        if tipousuario != "1":
            print("No tiene permiso para realizar esta accion")
            email_borrar = "-"
        if tipousuario == "1":
            email_borrar = input("Escribir email para borrar su usuario: ")
                #envio de datos
        datos = email + " " + email_borrar
        temp = llenado(len(datos+'deltu'))
        mensaje = temp + 'deltu' + datos
        s.sendall(bytes(mensaje,'utf-8'))


        recibido = s.recv(4096)
        print(recibido[10:])


        
    if(opcion == "0"):
        s.sendall(bytes('quit','utf-8'))
        time.sleep(1)
        print("fin cliente")
        break

print("ha cerrado terminal")
