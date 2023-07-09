import psycopg2

class StringConection():
    def __init__(self):
        host = 'localhost'
        port = '5432'
        database = 'plataforma_estudei'
        username = 'postgres'
        password = '1234'
        self.conn_string = f"host={host} port={port} dbname={database} user={username} password={password}"

    def getConection(self):
        return self.conn_string
    
class ConectionDB():

    def connConsulta(self, consulta):
        objString = StringConection()
        conn = psycopg2.connect(objString.getConection())
        cursor = conn.cursor()
        cursor.execute(consulta)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results

    def connAlter(self, form):
        objString = StringConection()
        conn = psycopg2.connect(objString.getConection())
        cursor = conn.cursor()
        cursor.execute(form)
        conn.commit()
        cursor.close()
        conn.close()
        return True