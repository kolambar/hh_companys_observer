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
            "page": 1,
            "employer_id": employer
        }
        return requests.get('https://api.hh.ru/vacancies/', params=params).json()

#
# vac = HhApiAsker.get_vacancy('15478')
# print(vac)

#  employer_id = {Яндекс: 1740, hh: 1455, Сбер: 3529, точка: 2324020, инфотекст: 3778, icl: 32570, HR Prime: 4759060,
#  Сима: 238161
