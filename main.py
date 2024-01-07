from Classes.write_employers_class import WriteEmployers
from Classes.write_vacancies_class import WriteVacancies
from Classes.DBManager import DBManager
from src.DB_creation import db_refresh, create_tables


def main():
    db_refresh()
    create_tables()
    # Запись данных в таблицы
    WriteEmployers.write_employers()
    WriteVacancies.write_vacancies()
    # Вызов методов класса
    DBManager().get_companies_and_vacancies()
    DBManager().get_all_vacancies()
    DBManager().get_avg_salary()
    DBManager().get_vacancies_with_higher_salary()
    DBManager().get_vacancies_with_keyword('бот')


if __name__ == '__main__':
    main()
