from filler_db import get_all_vacancies, get_all_employers, fill_with_data
from src.function import ask_for_adding_employer
from src.dbm_manager import DBMmanager
from src.function import check_answer
from src.db_creater import create_db


db_name = 'vacancies_from_hh'  # название бд
list_of_employers = [1740, 1455, 3529, 2324020, 3778, 32570, 4759060, 238161, 15478, 2696688]  # список id работодателей

# создает бд
create_db(db_name)
# спрашивает у пользователя, хочет ли тот добавить ещё id
ask_for_adding_employer(list_of_employers)

# получает список данных с работодателями
all_employers = get_all_employers(list_of_employers)
# получает список данных с вакансиями
all_vacancies = get_all_vacancies(list_of_employers)

# заполняет базу данных полученными данными
fill_with_data(all_employers, all_vacancies, db_name)

'''
Начала блока работы с базой данных.
Тут пользователю задаются уточняющие вопросы для вывода наиболее подходящих вопросов
'''
vac_searcher = DBMmanager('vacancies_from_hh')


answer = input('Вывести список копаний и количество их вакансий? Напишите либо "да", либо "нет".\n').strip().lower()

# здесь и далее используется функция проверяющая ответ.
if check_answer(answer):
    # здесь и далее используются функции, смысл который отражен в input выше.
    vac_searcher.get_companies_and_vacancies_count()


answer = input('Вывести список вакансий со всей нужной информацией? Напишите либо "да", либо "нет".\n').strip().lower()

if check_answer(answer):
    vac_searcher.get_all_vacancies()


answer = input('Вывести средние минимальную и максимальную зарплаты? Напишите либо "да", либо "нет".\n').strip().lower()

if check_answer(answer):
    vac_searcher.get_avg_salary()


answer = input('Вывести вакансии с зарплатой выше среднего? Напишите либо "да", либо "нет".\n').strip().lower()

if check_answer(answer):
    vac_searcher.get_vacancies_with_higher_salary()


answer = input('Хотите воспользоваться поиском по ключевому слову? Напишите либо "да", либо "нет".\n').strip().lower()

if check_answer(answer):
    key_word = input('\nВведите ключевое слово:\n')
    vac_searcher.get_vacancies_with_keyword(key_word)


# закрывает соединение
vac_searcher.close_conn()
