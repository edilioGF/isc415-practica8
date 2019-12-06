from suds.client import Client

SOAP_URL = 'http://localhost:7777/ws/AcademicoWebService'
WSDL_URL = 'http://localhost:7777/ws/AcademicoWebService?wsdl'

client = Client(url=WSDL_URL, location=SOAP_URL)

while True:
    key = int(input('''\nPresione el numero de la opcion correspondiente

    (1) Listar estudiantes
    (2) Consultar una asignatura
    (3) Consultar un profesor
    (4) Salir
    
    :'''))
    
    if (key == 1):

        student_list = client.service.getAllEstudiante()

        for student in student_list:
            print("Matricula: {0}, Nombre: {1}".format(student['matricula'], student['nombre']))

    elif (key == 2):

        id = input("\nInserte el codigo de la asignatura: ")
        print(client.service.getAsignatura(id))

    elif (key == 3):
        
        id = input("\nInserte el codigo del profesor: ")
        print(client.service.getProfesor(id))

    elif (key == 4):
        break

    input("\nPresione ENTER para continuar...")
