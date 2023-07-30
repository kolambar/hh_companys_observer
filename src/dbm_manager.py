from src.db_creater import config
import psycopg2


class DBMmanager:
    """Подключаться к БД Postgres"""

    def __init__(self, db_name):

        # определяет параметры для подключения
        params = config()
        params.update({'dbname': db_name})

        # подключается к дб
        self.conn = psycopg2.connect(**params)

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        with self.conn.cursor() as cur:
            cur.execute('''SELECT employers_name, COUNT(*) 
            FROM employers INNER JOIN vacancies USING (employers_id)
            GROUP BY employers_name
            ORDER BY COUNT(*) DESC''')
            print(*cur.fetchall())

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия вакансии, зарплаты, ссылки на нее"""
        with self.conn.cursor() as cur:
            cur.execute('''SELECT employers_name, vacancy_name, vacancy_salary_min, vacancy_salary_max, vacancy_url
            FROM employers INNER JOIN vacancies USING (employers_id)
            ORDER BY (vacancy_salary_min + vacancy_salary_max)''')
            print(*cur.fetchall())

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        with self.conn.cursor() as cur:
            cur.execute('''SELECT ROUND(AVG(vacancy_salary_min)), ROUND(AVG(vacancy_salary_max))
            FROM vacancies ''')
            print(*cur.fetchall())

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        with self.conn.cursor() as cur:
            cur.execute('''SELECT vacancy_name, vacancy_salary_min FROM vacancies
            WHERE vacancy_salary_min > (SELECT AVG(vacancy_salary_min) FROM vacancies)
            ORDER BY vacancy_salary_min''')
            print(*cur.fetchall())

    def get_vacancies_with_keyword(self, key_word):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова."""
        with self.conn.cursor() as cur:
            cur.execute("""SELECT vacancy_name, vacancy_salary_min, vacancy_salary_max, vacancy_url FROM vacancies
            WHERE vacancy_name LIKE  %s""",  ('%' + key_word + '%',))
            print(*cur.fetchall())

    def close_conn(self):
        """Закрывает соединение"""
        self.conn.close()
