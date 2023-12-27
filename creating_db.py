from sqlalchemy import create_engine, exc, text

DATABASE_NAME = 'university'
USERNAME = 'postgres'
PASSWORD = 'pass123'
HOST = 'localhost'
PORT = '5432'
OWNER_USER = 'postgres'
DATABASE_URL = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}'

def create_database():
    try:
        engine = create_engine(f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/postgres', isolation_level="AUTOCOMMIT")
        connection = engine.connect()
        
        connection.execute(text(f"CREATE DATABASE {DATABASE_NAME} WITH OWNER {OWNER_USER}"))

        connection.close()

        print(f"Database '{DATABASE_NAME}' was created successfully.")

        engine = create_engine(DATABASE_URL)

    except exc.SQLAlchemyError as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    create_database()