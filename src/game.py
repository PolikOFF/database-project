from Classes.write_employers_class import WriteEmployers
from Classes.write_vacancies_class import WriteVacancies
from src.DB_creation import db_create, create_tables, refresh_tables
from Classes.data_received_from_the_user import UserDataSelection


def game_with_user():
    """Функция для взаимодействия с пользователем."""
    print('''Это программа для получения данных по вакансиям.
    
Вам предложится несколько вариантов для получения информации по компаниям,
а так же получения некоторой статистики.
''')

    # Reset DB
    try:
        db_create()
    except Exception():
        refresh_tables()
        create_tables()
    # Выбор пользователя, что он хочет получать по компании и статистике.
    UserDataSelection().selected_company()
    UserDataSelection().selected_statistic()
    # Запись полученных данных по API в БД
    WriteEmployers.write_employers()
    WriteVacancies.write_vacancies()
    # Запрос на продолжение работы
    answer = input('Желаете получить еще данных?\nДа/Нет')
    while answer.lower() != ['Да', 'Нет']:
        # Reset DB
        try:
            db_create()
        except Exception():
            refresh_tables()
            create_tables()
        if answer == 'да':
            answer = input('''Какие данные вы хотели бы увидеть?
        -----------------------------
        1 - Начать с выбора компаний.
        -----------------------------
        2 - Получить еще данные по статистике.
        -----------------------------\n''')
            if answer == '1':
                print('Получение данных...')
                UserDataSelection().selected_company()
                UserDataSelection().selected_statistic()
            elif answer == '2':
                print('Получение данных...')
                UserDataSelection().selected_statistic()
        elif answer == 'нет':
            print('Спасибо за использование нашего сервиса! Возвращайтесь снова!')
            quit()
        else:
            print('Выберите пожалуйста варианты ответа из списка')
