from src.hh_api_asker import HhApiAsker
from src.function import ask_for_adding_employer


list_of_employers = [1740, 1455, 3529, 2324020, 3778, 32570, 4759060, 238161, 15478]

ask_for_adding_employer(list_of_employers)

for employer in list_of_employers:
    employers_data = HhApiAsker.get_vacancy(employer)

    # количество вакансий у работодателя
    num_of_vac = employers_data['found']
    # список с вакансиями
    vacancies = employers_data['items']
    # название работодателя
    name_of_employer = vacancies[0]['employer']['name']

    print(f'название работодателя {name_of_employer}\n, количество вакансий у работодателя {num_of_vac}\n')

    for vac in vacancies:
        # имя вакансии
        vac_name = vac['name']
        # ссылка
        vac_url = vac['alternate_url']
        # зарплата
        if not vac['salary']:
            vac_salary = 'Не указана'
        elif not vac['salary']['from']:
            vac_salary = f"До {vac['salary']['to']}"
        else:
            vac_salary = f"От {vac['salary']['from']}"

        print(f'название вакансии {vac_name}, \nзп {vac_salary}, \nссылка {vac_url}\n')


