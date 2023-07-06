import psycopg2

class conn_bd():
    def conn(consulta):
        hostname = 'localhost'
        port = '5432'
        database = 'plataforma_estudei'
        username = 'postgres'
        password = '1234'
        conn_string = f"host='{hostname}' port='{port}' dbname='{database}' user='{username}' password='{password}'"

        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(f"{consulta}")
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return results