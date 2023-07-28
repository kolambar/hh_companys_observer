import requests


class HhApiAsker:
    """
    Подключается к HeadHunter
    """

    @staticmethod
    def get_vacancy(employer):
        """
        Подключается к HeadHunter и получает вакансии нужных работодателей
        """
        params = {
            "per_page=": 100,
            "page": 0,
            "employer_id": employer
        }
        all_vacancies = []
        count = 5
        while params["page"] < count:
            vacancies = requests.get('https://api.hh.ru/vacancies/', params=params).json()["items"]
            all_vacancies.extend(vacancies)
            params["page"] += 1
        return all_vacancies

    @staticmethod
    def get_employers(employer):
        """
        Подключается к HeadHunter и получает вакансии нужных работодателей
        """
        return requests.get(f'https://api.hh.ru/employers/{employer}').json()

# vac = HhApiAsker.get_vacancy('5967884')
# print(vac)

#  employer_id = {Яндекс: 1740, hh: 1455, Сбер: 3529, точка: 2324020, инфотекст: 3778, icl: 32570, HR Prime: 4759060,
#  Сима: 238161
