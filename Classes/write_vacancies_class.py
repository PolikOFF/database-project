from Classes.write_for_DB_class import WriteClass
from Classes.parsing_class import HeadHunter
from Classes.structuring_data_class import DataStructiring


class WriteVacancies:
    """Метод для записи данных о вакансиях в БД таблицы vacancies"""
    @staticmethod
    def write_vacancies():
        vac_responce = HeadHunter().get_vacancies()
        vac_data = DataStructiring(vac_responce).structuring_data()
        WriteClass(vac_data).write_data_for_vacancies()

