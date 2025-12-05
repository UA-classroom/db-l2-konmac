import psycopg2

try:

    hostname = "localhost"
    database = "Labb 1"
    username = "postgres"
    pwd = "postgres"
    port_id = "5432"

    conn = psycopg2.connect(
        host=hostname, dbname=database, user=username, password=pwd, port=port_id
    )

    cur = conn.cursor()





except Exception as error:
    print(error)
finally:
    cur.close()
    conn.close()
    
