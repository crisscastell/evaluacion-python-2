import pyodbc

def añadir(Matriculas, conexion):
    try:
        cursor = conexion.cursor()
        query = 'INSERT INTO Matriculas VALUES(?, ?, ?, ?)'
        cursor.execute(query, Matriculas['ID matricula'], Matriculas['ID estudiante'], Matriculas['ID cursos'], Matriculas['Fecha Matriculas'])
        cursor.commit()
        cursor.close()
        return True
    except pyodbc.Error as error:
        print(f'Error al insertar. Error: {error}')
        cursor.close()
        input('Presione ENTER para continuar...')
        return None
    
def buscar(MatriculaID, conexion):
    try:
        cursor = conexion.cursor()
        query = 'SELECT * FROM Matriculas WHERE MatriculaID = ?'
        cursor.execute(query, MatriculaID)
        resultado = cursor.fetchone()
        return resultado
    except pyodbc.Error as error:
        print(f'Error al buscar. Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None
    
def actualizar(MatriculaID, conexion):
    try:
        resultado = buscar(MatriculaID, conexion)
        if not resultado:
            print('Matricula no encontrada') 
            input('Presione ENTER para continuar...')
            return None
        print('===MATRICULA===')
        print(f"ID: {MatriculaID}\nEstudiante: {resultado[1]}\nCurso: {resultado[2]}\nFecha: {resultado[3]}")
        print("=================")
        print('Escoja campo a actualizar:\n1 - Estudiante \n2 - Curso \n3 - Fecha \n4 - Cancelar')
        c = int(input())
        cursor = conexion.cursor()
        match c:
            case 1:
                EstudianteID = input('Ingrese el ID del nuevo estudiante: ')
                query = 'UPDATE Matriculas SET EstudianteID = ? WHERE MatriculaID = ?'
                cursor.execute(query, EstudianteID, MatriculaID)
                print("estudiante actualizado")
                input('Presione ENTER para continuar...')
            case 2:
                CursoID = input('Ingrese el ID del nuevo curso: ')
                query = 'UPDATE Matriculas SET CursoID = ? WHERE MatriculaID = ?'
                cursor.execute(query, CursoID, MatriculaID)
                print("curso actualizado")
                input('Presione ENTER para continuar...')
            case 3:
                FechaMatricula = input('Ingrese la nueva fecha (DD/MM/AAAA): ')
                query = 'UPDATE Matriculas SET FechaMatricula = ? WHERE MatriculaID = ?'
                cursor.execute(query, FechaMatricula, MatriculaID)
                print("fecha actualizada")
                input('Presione ENTER para continuar...')
            case 4:
                return
        cursor.commit()
        cursor.close()
        return True
    except pyodbc.Error as error:
        print(f'Error al actualizar. Error: {error}')
        cursor.close()
        input('Presione ENTER para continuar...')
        return None

def eliminar(MatriculaID, conexion):
    try:
        resultado = buscar(MatriculaID, conexion)
        if not resultado:
            print('Matricula no encontrada...')
            input('Presione Enter para continuar...')
            return None
        print('===MATRICULA===')
        print(f"ID: {MatriculaID}\nEstudiante: {resultado[1]}\nCurso: {resultado[2]}\nFecha: {resultado[3]}")
        print('Desea eliminarlo?:\n1 - Si\n2 - No')
        c = int(input())
        match c:
            case 1:
                cursor = conexion.cursor()
                cursor.execute('DELETE FROM Matriculas WHERE MatriculaID = ?', MatriculaID)
                cursor.commit()
                cursor.close()
                return True
            case 2:
                return False
    except pyodbc.Error as error:
        print(f'Error al eliminar. Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None
    
def leer(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute('SELECT MatriculaID, EstudianteID, CursoID FROM Matriculas')
        matriculas = cursor.fetchall()
        for i in matriculas:
            print(f'ID: {i[0]} - Estudiante ID: {i[1]} - Curso ID: {i[2]}')
        input('Presione ENTER para continuar...')
    except pyodbc.Error as err:
        print(f'Error: {err}')
        cursor.close()
        input('Presione ENTER para continuar...')

