from Classes.write_for_DB_class import WriteClass
from Classes.parsing_class import HeadHunter
from Classes.structuring_data_class import DataStructiring


class WriteVacancies:
    """Метод для записи данных о вакансиях в БД таблицы vacancies"""
    @staticmethod
    def write_vacancies():
        vac_responce_1 = HeadHunter().get_vacancies_by_id_39305()
        vac_responce_2 = HeadHunter().get_vacancies_by_id_907345()
        vac_responce_3 = HeadHunter().get_vacancies_by_id_23427()
        vac_responce_4 = HeadHunter().get_vacancies_by_id_740()
        vac_responce_5 = HeadHunter().get_vacancies_by_id_1808()
        vac_responce_6 = HeadHunter().get_vacancies_by_id_575665()
        vac_responce_7 = HeadHunter().get_vacancies_by_id_6041()
        vac_responce_8 = HeadHunter().get_vacancies_by_id_59()
        vac_responce_9 = HeadHunter().get_vacancies_by_id_1373()
        vac_responce_10 = HeadHunter().get_vacancies_by_id_7172()
        vac_data_1 = DataStructiring(vac_responce_1).structuring_data()
        vac_data_2 = DataStructiring(vac_responce_2).structuring_data()
        vac_data_3 = DataStructiring(vac_responce_3).structuring_data()
        vac_data_4 = DataStructiring(vac_responce_4).structuring_data()
        vac_data_5 = DataStructiring(vac_responce_5).structuring_data()
        vac_data_6 = DataStructiring(vac_responce_6).structuring_data()
        vac_data_7 = DataStructiring(vac_responce_7).structuring_data()
        vac_data_8 = DataStructiring(vac_responce_8).structuring_data()
        vac_data_9 = DataStructiring(vac_responce_9).structuring_data()
        vac_data_10 = DataStructiring(vac_responce_10).structuring_data()
        WriteClass(vac_data_1).write_data_for_vacancies()
        WriteClass(vac_data_2).write_data_for_vacancies()
        WriteClass(vac_data_3).write_data_for_vacancies()
        WriteClass(vac_data_4).write_data_for_vacancies()
        WriteClass(vac_data_5).write_data_for_vacancies()
        WriteClass(vac_data_6).write_data_for_vacancies()
        WriteClass(vac_data_7).write_data_for_vacancies()
        WriteClass(vac_data_8).write_data_for_vacancies()
        WriteClass(vac_data_9).write_data_for_vacancies()
        WriteClass(vac_data_10).write_data_for_vacancies()
