import psycopg2


class DBMmanager:
    """Подключаться к БД Postgres"""
    pass


def get_companies_and_vacancies_count():
    """получает список всех компаний и количество вакансий у каждой компании"""
    pass


def get_all_vacancies():
    """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
    pass


def get_avg_salary():
    """Получает среднюю зарплату по вакансиям"""
    pass


def get_vacancies_with_higher_salary():
    """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
    pass


def get_vacancies_with_keyword():
    """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”."""
    pass
