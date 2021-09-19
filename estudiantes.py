from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArhivos import Archivo
from entidadesUnemi import *
from datetime import date
import time

# Procesos de las Opciones del Menu Mantenimiento
def carreras():
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE CARRERAS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Descripcion Carrera: ")
   gotoxy(37,5)
   descarrera = input()
   archiCarrera = Archivo("./datos/carrera.txt",";")
   carreras = archiCarrera.leer()
   if carreras : idSig = int(carreras[-1][0])+1
   else: idSig=1
   carrera = Carrera(idSig,descarrera)
   datos = carrera.getCarrera()
   datos = ';'.join(datos)
   archiCarrera.escribir([datos],"a")

def materias():
    borrarPantalla()
    gotoxy(20, 2);
    print("MANTENIMIENTO DE MATERIAS")
    gotoxy(15, 4);
    print("Codigo: ")
    gotoxy(15, 5);
    print("Descripcion Materia: ")
    gotoxy(37, 5); desMateria = input()
    archiMateria = Archivo("./datos/materia.txt", ";")
    materias = archiMateria.leer()
    if materias:
        idSig = int(materias[-1][0]) + 1
    else:
        idSig = 1
    materia = Materia(idSig, desMateria)
    datos = materia.getMateria()
    datos = ';'.join(datos)
    archiMateria.escribir([datos], "a")

def periodos():
    borrarPantalla()
    validar = Valida()
    gotoxy(20, 2);
    print("MANTENIMIENTO DE PERIODOS")
    gotoxy(15, 4);
    print("Periodo:            [                       ]")
    gotoxy(15, 5);
    print("Descripcion Periodo: ")
    periodoPeriodo = validar.solo_numeros("Error: Solo numeros",37,4)
    gotoxy(37, 5);descripcionPeriodo = input()
    archiPeriodo = Archivo("./datos/periodo.txt", ";")
    periodos = archiPeriodo.leer()
    if periodos:
        idSig = int(periodos[-1][0]) + 1
    else:
        idSig = 1
    periodo = Periodo(periodoPeriodo, descripcionPeriodo)
    datos = periodo.getPeriodo()
    datos = ';'.join(datos)
    archiPeriodo.escribir([datos], "a")

def profesores():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE PROFESORES")
   gotoxy(15,4);print("Nombre  : ")
   gotoxy(15,5);print("Cedula: : ")
   gotoxy(15,6);print("Titulo: : ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(15,8);print("Carrera ID[    ]: ")
   gotoxy(25,4);nom = input()
   gotoxy(25,5);ced = input()
   gotoxy(25,6);tit = input()
   tel=validar.solo_numeros("Error: Solo numeros",25,7)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,8);id = input().upper()
      archiCarrera = Archivo("./datos/carrera.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
          gotoxy(33,8);print(entCarrera.descripcion)
      else: 
         gotoxy(33,8);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiProfesor = Archivo("./datos/profesor.txt")
        lisProfesores = archiProfesor.leer()
        if lisProfesores : idSig = int(lisProfesores[-1][0])+1
        else: idSig=1
        entProfesor = Profesor(idSig,nom,ced,entCarrera,tit,tel)
        datos = entProfesor.getProfesor()
        datos = ';'.join(datos)
        archiProfesor.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")     
     
# Menu Principal

def estudiantes():
   borrarPantalla()
   validar = Valida()
   gotoxy(20,2);print("MANTENIMIENTO DE ESTUDIANTES")
   gotoxy(15,5);print("Nombre Estudiante: ")
   gotoxy(15,6);print("Cedula Estudiante: ")
   gotoxy(15,7);print("Direccion Estudiante: ")
   gotoxy(15,8);print("Telefono Estudiante: ")
   gotoxy(37,5); nombreEstudiante = input()
   cedulaEstudiante = validar.solo_numeros("Error: Solo numeros", 37, 6)
   gotoxy(37,7); direccionEstudiante = input()
   telefonoEstudiante = validar.solo_numeros("Error: Solo numeros", 37, 8)
   archiEstudiante = Archivo("./datos/estudiante.txt",";")
   estudiantes = archiEstudiante.leer()
   if estudiantes : idSig = int(estudiantes[-1][0])+1
   else: idSig=1
   carrera = Estudiante(idSig,nombreEstudiante, cedulaEstudiante, direccionEstudiante, telefonoEstudiante)
   datos = carrera.getEstudiante()
   datos = ';'.join(datos)
   archiEstudiante.escribir([datos],"a")

def matriculas():
    borrarPantalla()
    validar = Valida()
    gotoxy(20, 2);
    print("INGRESO DE MATRICULA")
    gotoxy(15, 4);
    print("Estudiante    ID[           ]: ")
    gotoxy(15, 5);
    print("Carrera       ID[           ]: ")
    gotoxy(15, 6);
    print("Periodo       ID[           ]: ")
    gotoxy(15, 7);
    print("Valor: ")
    
    

    lisEstudiante, entEstudiante = [], None
    while not lisEstudiante:
        gotoxy(34, 4);
        id = input().upper()
        archiEstudiante = Archivo("./datos/estudiante.txt")
        lisEstudiante = archiEstudiante.buscar(id)
        if lisEstudiante:
            entEstudiante = Estudiante(lisEstudiante[0], lisEstudiante[1], lisEstudiante[2], lisEstudiante[3], lisEstudiante[4])
            gotoxy(34, 4);
            print(entEstudiante.nombre)
        else:
            gotoxy(34, 4);
            print("No existe Estudiante con ese codigo[{}]:".format(id))
            time.sleep(1);
            gotoxy(34, 4);
            print(" " * 40)

    lisCarrera, entCarrera = [], None
    while not lisCarrera:
        gotoxy(34, 5);
        id = input().upper()
        archiCarrera = Archivo("./datos/carrera.txt")
        lisCarrera = archiCarrera.buscar(id)
        if lisCarrera:
            entCarrera = Carrera(lisCarrera[0], lisCarrera[1])
            gotoxy(34, 5);
            print(entCarrera.descripcion)
        else:
            gotoxy(34, 5);
            print("No existe Carrera con ese codigo[{}]:".format(id))
            time.sleep(1);
            gotoxy(34, 5);
            print(" " * 40)

    lisPeriodo, entPeriodo = [], None
    while not lisPeriodo:
        gotoxy(34, 6);
        id = input().upper()
        archiPeriodo = Archivo("./datos/periodo.txt")
        lisPeriodo = archiPeriodo.buscar(id)
        if lisPeriodo:
            entPeriodo = Periodo(lisPeriodo[0], lisPeriodo[1])
            gotoxy(34, 6);
            print(entPeriodo.periodo)
        else:
            gotoxy(34, 6);
            print("No existe Periodo con ese codigo[{}]:".format(id))
            time.sleep(1);
            gotoxy(34, 6);
            print(" " * 40)
    
    valor = validar.solo_decimales("Ingrese valor","Error: Solo numeros" )
    gotoxy(15, 10);
    print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54, 10);
    grabar = input().lower()
    if grabar == "s":
        archiMatricula = Archivo("./datos/matricula.txt")
        lisMatricula = archiMatricula.leer()
        if lisMatricula:
            idSig = int(lisMatricula[-1][0]) + 1
        else:
            idSig = 1
        entMatricula = Matricula(idSig, entEstudiante, entCarrera, entPeriodo, valor)
        datos = entMatricula.getMatricula()
        datos = ';'.join(datos)
        archiMatricula.escribir([datos], "a")
        gotoxy(15, 11);
        input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(15, 11);
        input("Registro No fue Grabado\n presione una tecla para continuar...")

def notas():
    borrarPantalla()
    validar = Valida()
    gotoxy(20, 2);
    print("INGRESO DE MATRICULA")
    gotoxy(15, 4);
    print("Nota 1: ")
    gotoxy(15, 5);
    print("Nota 2: ")
    gotoxy(15, 6);
    print("Periodo    ID[              ]: ")
    gotoxy(15, 7);
    print("Estudiante ID[              ]: ")
    gotoxy(15, 8);
    print("Materia    ID[              ]: ")
    gotoxy(15, 9);
    print("Profesor   ID[              ]: ")
    nota1 = validar.solo_numeros("Ingrese nota1",34,4 )
    nota2 = validar.solo_numeros("Ingrese nota2",34,5)


    lisPeriodo, entPeriodo = [], None
    while not lisPeriodo:
        gotoxy(34, 6);
        id = input().upper()
        archiPeriodo = Archivo("./datos/periodo.txt")
        lisPeriodo = archiPeriodo.buscar(id)
        if lisPeriodo:
            entPeriodo = Periodo(lisPeriodo[0], lisPeriodo[1])
            gotoxy(34, 6);
            print(entPeriodo.periodo)
        else:
            gotoxy(34, 6);
            print("No existe Periodo con ese codigo[{}]:".format(id))
            time.sleep(1);
            gotoxy(34, 6);
            print(" " * 40)

    lisEstudiante, entEstudiante = [], None
    while not lisEstudiante:
        gotoxy(34, 7);
        id = input().upper()
        archiEstudiante = Archivo("./datos/estudiante.txt")
        lisEstudiante = archiEstudiante.buscar(id)
        if lisEstudiante:
            entEstudiante = Estudiante(lisEstudiante[0], lisEstudiante[1], lisEstudiante[2], lisEstudiante[3], lisEstudiante[4])
            gotoxy(34, 7);
            print(entEstudiante.nombre)
        else:
            gotoxy(34, 7);
            print("No existe Estudiante con ese codigo[{}]:".format(id))
            time.sleep(1);
            gotoxy(34, 7);
            print(" " * 40)

    lisMateria, entMateria = [], None
    while not lisMateria:
        gotoxy(34, 8);
        id = input().upper()
        archiMateria = Archivo("./datos/materia.txt")
        lisMateria = archiMateria.buscar(id)
        if lisMateria:
            entMateria = Materia(lisMateria[0], lisMateria[1])
            gotoxy(34, 8);
            print(entMateria.descripcion)
        else:
            gotoxy(34, 8);
            print("No existe Materia con ese codigo[{}]:".format(id))
            time.sleep(1);
            gotoxy(34, 8);
            print(" " * 40)

    lisProfesor, entProfesor = [], None
    while not lisProfesor:
        gotoxy(34, 9);
        id = input().upper()
        archiProfesor = Archivo("./datos/profesor.txt")
        lisProfesor = archiProfesor.buscar(id)
        if lisProfesor:
            entProfesor = Profesor(lisProfesor[0], lisProfesor[1], lisProfesor[2], lisProfesor[2], lisProfesor[3], lisProfesor[4])
            gotoxy(34, 9);
            print(entProfesor.nombre)
        else:
            gotoxy(34, 9);
            print("No existe Profesor con ese codigo[{}]:".format(id))
            time.sleep(1);
            gotoxy(34, 9);
            print(" " * 40)

    gotoxy(15, 10);
    print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54, 10);
    grabar = input().lower()

    if grabar == "s":
        archiNota = Archivo("./datos/nota.txt")
        lisNota = archiNota.leer()
        if lisNota:
            idSig = int(lisNota[-1][0]) + 1
        else:
            idSig = 1
        entNota = Notas(idSig, entPeriodo, entEstudiante, entMateria, entProfesor, nota1, nota2)
        datos = entNota.getNotas()
        datos = ';'.join(datos)
        archiNota.escribir([datos], "a")
        gotoxy(15, 11);
        input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(15, 11);
        input("Registro No fue Grabado\n presione una tecla para continuar...")

opc=''
while opc !='5':  
    borrarPantalla()      
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Matriculacion","3) Notas","4) Consultas","5) Salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='6':
            borrarPantalla()    
            menu1 = Menu("Menu Mantenimiento",["1) Carrera","2) Materias","3) Periodos","4) Profesores","5) Estudiantes","6) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                carreras()
            elif opc1 == "2":
                materias()
            elif opc1 == "3":
                periodos()
            elif opc1 == "4":
                profesores()
            elif opc1 == "5":
                estudiantes()
                        
    elif opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Matriculacion",["1) Matricula","2) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                matriculas()
            elif opc2 == "2":
                pass
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Notas",["1) Notas","2) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                notas()
            
    elif opc == "4":
            borrarPantalla()
            menu4 = Menu("Menu Consultas",["1) Carreras","2) Materias","3) Periodos","4) Profesores","5) Estudiantes","6) Notas","7) Matricula","7) Salir"],20,10)
            opc4 = menu4.menu()
            if opc4 == "1":
                borrarPantalla()
                print("Listado de Profesor")
                print("id      Nombre   dpto")
                # leer el archivo carrera y retornar las carrera 
                lista = [["1","Daniel   ",2],["2","Ana",1]]
                archiDepartamento = Archivo("./datos/departamento.txt")
                lisDepartamento = archiDepartamento.buscar(id)
                if lisDepartamento:
                    print(1,"Daniel" ,lisDepartamento[1])
                    print(2,"Ana",2)
                input("      Presione una tecla para continuar...")
    elif opc == "5":
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()

