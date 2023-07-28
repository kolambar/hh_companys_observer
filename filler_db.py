from src.hh_api_asker import HhApiAsker


def get_all_vacancies(list_of_employers):
    all_vacancies = []
    for employer in list_of_employers:
        employers_data = HhApiAsker.get_vacancy(employer)
        # # список с вакансиями
        # print(employers_data)
        # vacancies = employers_data['items']

        for vac in employers_data:
            # имя вакансии
            vac_name = vac['name']
            # ссылка
            vac_url = vac['alternate_url']
            # зарплата
            salary_min = None
            salary_max = None
            if vac['salary']:
                salary_min = vac["salary"]["from"]
                salary_max = vac["salary"]["to"]
            all_vacancies.append({"name": vac_name,
                                  "url": vac_url,
                                  "salary_min": salary_min,
                                  "salary_max": salary_max,
                                  "employer": employer})
    return all_vacancies


def get_all_companies(list_of_employers):
    all_companies = []
    for employer in list_of_employers:
        employers_data = HhApiAsker.get_company(employer)
        name = employers_data["name"]
        all_companies.append({"id_company": employer, "name": name})
    return all_companies

# data = get_all_companies()
# for company in data:
#     cur.execute("""INSERT INTO company (id, name) VALUES (%s, %s)""", (company["id"], company["name"]))
