from src.hh_api_asker import HhApiAsker
from src.function import ask_for_adding_employer


list_of_employers = [1740, 1455, 3529, 2324020, 3778, 32570, 4759060, 238161]

ask_for_adding_employer(list_of_employers)

for employer in list_of_employers:
    employers_data = HhApiAsker.get_vacancy(employer)
