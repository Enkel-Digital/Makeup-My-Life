import psycopg2

def connection() :
    try :
        connection_details = "dbname='makeupdb' user='icebear' host='localhost' port='5432'" 
        connection = psycopg2.connect(connection_details)
        connection.autocommit = True
        cursor = connection.cursor()
    except :
        print('connection unsuccessful')


if __name__ == '__main__' :
    connection()