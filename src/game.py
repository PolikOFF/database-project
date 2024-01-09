from Classes.write_vacancies_class import WriteVacancies
from src.DB_creation import db_create, create_tables, refresh_tables
from Classes.data_received_from_the_user import UserDataSelection
import psycopg2


def game_with_user():
    """Функция для взаимодействия с пользователем."""
    print('''Это программа для получения данных по вакансиям.
    
Вам предложится несколько вариантов для получения информации по компаниям,
а так же получения некоторой статистики.

Заполняю таблицу данными по вакансиям компаний...\n''')
    answer = 'да'
    # Reset DB
    try:
        db_create()
        create_tables()
    except psycopg2.DatabaseError:
        refresh_tables()
    # Запись полученных данных по API в БД
    WriteVacancies.write_vacancies()
    # Выбор пользователя, что он хочет получать по статистике.
    UserDataSelection().selected_statistic()
    while answer != 'нет':
        # Запрос на продолжение работы
        answer = input('Желаете продолжить?\nДа/Нет')
        while answer.lower() != ['Да', 'Нет']:
            if answer == 'да':
                UserDataSelection().selected_statistic()
                break
            elif answer == 'нет':
                print('Спасибо за использование нашего сервиса! Возвращайтесь снова!')
                quit()
            else:
                print('Выберите пожалуйста варианты ответа из списка')
                break
