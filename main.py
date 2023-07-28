from filler_db import get_all_vacancies, get_all_employers, fill_with_data
from src.function import ask_for_adding_employer
from src.db_creater import create_db


db_name = 'vacancies_from_hh'  # название бд
list_of_employers = [1740, 1455, 3529, 2324020, 3778, 32570, 4759060, 238161, 15478]  # список id работодателей

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
