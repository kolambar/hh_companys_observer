from src.hh_api_asker import HhApiAsker
from src.db_creater import config
import psycopg2


def get_all_employers(list_of_employers: list) -> list:
    """Выбирает нужные данные после запроса с hh"""
    # список с работодателей
    all_employers = []

    for employer in list_of_employers:
        employers_data = HhApiAsker.get_employers(employer)
        name = employers_data["name"]
        all_employers.append({"employers_id": employer, "name": name})

    return all_employers


def get_all_vacancies(list_of_employers: list) -> list:
    """Выбирает нужные данные после запроса с hh"""
    # список с вакансиями
    all_vacancies = []

    for employer in list_of_employers:
        vacancies_data = HhApiAsker.get_vacancy(employer)

        for vac in vacancies_data:
            # имя вакансии
            vac_name = vac['name']
            # ссылка на вакансию
            vac_url = vac['alternate_url']

            salary_min = None
            salary_max = None
            # получает зарплату вакансии
            if vac['salary']:
                salary_min = vac["salary"]["from"]
                salary_max = vac["salary"]["to"]

            # добавляет словарь с данными этой вакансии в список вакансий
            all_vacancies.append({"name": vac_name,
                                  "url": vac_url,
                                  "salary_min": salary_min,
                                  "salary_max": salary_max,
                                  "employer": employer})

    return all_vacancies


def fill_with_employers(cur, all_employers: list) -> None:
    """Заполняет таблицу employers данными из списка с работодателями"""
    for employer in all_employers:
        cur.execute("""INSERT INTO employers (employers_id, employers_name) VALUES (%s, %s)""",
                    (employer["employers_id"], employer["name"]))


def fill_with_vacancies(cur, all_vacancies: list) -> None:
    """Заполняет таблицу vacancies данными из списка с вакансиями"""
    for vacancy in all_vacancies:
        cur.execute("""INSERT INTO vacancies 
        (vacancy_name, vacancy_salary_min, vacancy_salary_max, vacancy_url, employers_id) VALUES (%s, %s, %s, %s, %s)""",
                    (vacancy["name"], vacancy["salary_min"], vacancy["salary_max"],
                     vacancy["url"], vacancy["employer"],))


def fill_with_data(all_employers: list, all_vacancies: list, db_name: str) -> None:
    """
    Подключается к бд и объединяет в себе функции fill_with_employers и fill_with_vacancies.
    Делает коммит, закрывает подключение
    """
    params = config()
    conn = None

    # указывает название бд, к которой нужно подключится
    params.update({'dbname': db_name})

    try:
        # подключается к бд
        conn = psycopg2.connect(**params)
        conn.autocommit = True
        with conn.cursor() as cur:

            # заполняет таблицы employers и vacancies
            fill_with_employers(cur, all_employers)
            fill_with_vacancies(cur, all_vacancies)

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
