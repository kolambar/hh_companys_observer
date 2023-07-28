from filler_db import get_all_vacancies, get_all_employers, fill_with_data
from src.function import ask_for_adding_employer
from src.db_creater import create_db


db_name = 'vacancies_from_hh'
list_of_employers = [1740, 1455, 3529, 2324020, 3778, 32570, 4759060, 238161, 15478]


create_db(db_name)
ask_for_adding_employer(list_of_employers)

all_employers = get_all_employers(list_of_employers)
all_vacancies = get_all_vacancies(list_of_employers)

fill_with_data(all_employers, all_vacancies, db_name)
