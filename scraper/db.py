import psycopg2
from psycopg2 import Error



def insert(
    title,
    link,
    description,
    category,
    requirement,
    company_name,
    company_description,
    location,
    company_size,
    company_logo,
    salary,
    post_date,
    language
):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="jcuser",
                                    password="string",
                                    host="localhost",
                                    port="5432",
                                    database="jc")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        
        sql = """
            INSERT INTO "job"(
	            title,
	            link,
	            description,
	            category,
	            requirement,
	            company_name,
	            company_description,
	            location,
	            company_size,
	            company_logo,
	            salary,
	            post_date,
	            language
            )
	        VALUES (
                %s,
	            %s,
	            %s,
	            %s,
	            %s,
	            %s,
	            %s,
	            %s,
	            %s,
	            %s,
	            %s,
	            %s,
	            %s
            );
        """
        
        data = (
            title,
            link,
            description,
            category,
            requirement,
            company_name,
            company_description,
            location,
            company_size,
            company_logo,
            salary,
            post_date,
            language
        )
        
        cursor.execute(sql, data)
        connection.commit()
        
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
