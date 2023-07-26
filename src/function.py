def ask_for_adding_employer(list_of_employers):
    """Спрашивает нужно ли добавить id и добавляет их в список"""
    answer = input(
        'Вы хотите добавить id компании к списку для отслеживания? Напишите либо нет, либо id.').strip().lower()

    while answer != "нет":
        list_of_employers.append(int(answer))
        answer = input('Хотите добавить ещё один id?').strip().lower()
