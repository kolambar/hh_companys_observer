import requests


class HhApiAsker:
    """
    Подключается к HeadHunter
    """

    @staticmethod
    def get_vacancy(employer: list) -> list:
        """
        Подключается к HeadHunter и получает вакансии нужных работодателей
        """
        params = {
            "per_page=": 100,
            "page": 0,
            "employer_id": employer
        }

        # количество выдаваемых вакансий (count * 100)
        count = 5
        all_vacancies = []

        # цикл для запроса информации с разных страниц
        while params["page"] < count:
            vacancies = requests.get('https://api.hh.ru/vacancies/', params=params).json()["items"]
            all_vacancies.extend(vacancies)
            params["page"] += 1

        return all_vacancies

    @staticmethod
    def get_employers(employer: list):
        """
        Подключается к HeadHunter и получает информацию о работодателях
        """
        return requests.get(f'https://api.hh.ru/employers/{employer}').json()
