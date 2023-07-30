def ask_for_adding_employer(list_of_employers: list) -> None:
    """Спрашивает нужно ли добавить id и добавляет их в список"""
    answer = input(
        'Вы хотите добавить id компании к списку для отслеживания? Напишите либо id, либо нет.\n').strip().lower()

    while answer != "нет":
        try:
            list_of_employers.append(int(answer))
        except ValueError:
            print('Введите либо "нет", либо id компании')

        answer = input('Хотите добавить ещё один id?\n').strip().lower()


def check_answer(answer):
    while True:
        if answer == 'да':
            return True
        elif answer == 'нет':
            return False
        else:
            answer = input('Ответом может быть только "да" или "нет".\n')

