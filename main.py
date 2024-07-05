from db import connection, matriculas
import os

SERVER = 'DESKTOP-4K2KRR5\SQLSERVER'
DATABASE = 'Escuela'
TABLE = 'Matriculas'

def main():
    conexion = connection.conectar(SERVER, DATABASE)

    while True:
        os.system('cls')
        print('=====MATRICULAS=====')
        print(f'BASE DE DATOS: {DATABASE} | TABLA: {TABLE}')
        print('1 - Añadir Matricula\n2 - Buscar Matricula\n3 - Actualizar Matricula\n4 - Eliminar Matricula\n5 - Leer Matriculas \n6 - Salir\n')
        c = int(input('Ingrese una opción: ')) 
        match c:
            case 1:
                os.system('cls')
                matriculaID = input('Ingrese ID matricula: ')
                estudianteID = input('Ingrese ID del estudiante: ')
                cursoID = input('Ingrese ID del curso: ')
                FechaMatricula = input('Ingrese la fecha (DD/MM/AAAA): ')
                matr = {
                    'ID matricula':matriculaID,
                    'ID estudiante':estudianteID,
                    'ID cursos':cursoID,
                    'Fecha Matriculas': FechaMatricula
                    
                }
                result = matriculas.añadir(matr, conexion)
                if(result):
                    print('Matricula añadida exitosamente')
                    input("presione ENTER para continuar...")

            case 2:
                os.system('cls')
                matriculaID = input('Ingrese ID de la Matricula: ')
                resultado = matriculas.buscar(matriculaID, conexion)
                if resultado:
                    print('===MATRICULA===')
                    print(f"ID: {matriculaID}\nEstudiante: {resultado[1]}\nCurso: {resultado[2]}\nFecha: {resultado[3]}")
                    input('Presione ENTER para continuar...')
                else:
                    print('Matricula no encontrada')
                    input('Presione Enter para continuar...')
            case 3:
                 os.system('cls')
                 id = input('Ingrese ID de la Matricula: ')
                 resultado = matriculas.actualizar(id, conexion)
                 if(resultado):
                    print('Matricula actualizada exitosamente.')

            case 4:
                os.system('cls')
                matriculaID= input('Ingrese ID del Matricula: ')
                resultado = matriculas.eliminar(matriculaID, conexion)
                if(resultado):
                    print('Matricula eliminada exitosamente.')

            case 5:
                os.system('cls')
                matriculas.leer(conexion)
                c = None

            case 6:
                exit()


if __name__ == '__main__':
    main()
       