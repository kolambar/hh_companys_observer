from configparser import ConfigParser
import psycopg2


def create_db(db_name):
    params = config()
    conn = None

    create_database(params, db_name)
    params.update({'dbname': db_name})
    try:
        conn = psycopg2.connect(**params)
        conn.autocommit = True
        with conn.cursor() as cur:

            create_employers_table(cur)
            create_vacancies_table(cur)

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def config(filename="database.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db


def create_database(params, db_name) -> None:
    """Создает новую базу данных."""
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
        cur.execute(f'CREATE DATABASE {db_name}')

    conn.close()


def create_employers_table(cur) -> None:
    """Создает таблицу employers."""
    cur.execute("""
                CREATE TABLE IF NOT EXISTS employers (
                employers_id INT PRIMARY KEY,
                employers_name VARCHAR
                )
                """)


def create_vacancies_table(cur) -> None:
    """Создает таблицу vacancies."""
    cur.execute("""
                CREATE TABLE IF NOT EXISTS vacancies (
                vacancy_id int GENERATED ALWAYS AS IDENTITY NOT NULL,
                vacancy_name VARCHAR,
                vacancy_salary_min INT,
                vacancy_salary_max INT,
                vacancy_url VARCHAR,
                employers_id INT REFERENCES employers(employers_id)                
                )
                """)
