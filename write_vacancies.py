from write_class import WriteClass
from HH_class import HeadHunter


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
        WriteClass(vac_responce_1).write_data_for_vacancies()
        WriteClass(vac_responce_2).write_data_for_vacancies()
        WriteClass(vac_responce_3).write_data_for_vacancies()
        WriteClass(vac_responce_4).write_data_for_vacancies()
        WriteClass(vac_responce_5).write_data_for_vacancies()
        WriteClass(vac_responce_6).write_data_for_vacancies()
        WriteClass(vac_responce_7).write_data_for_vacancies()
        WriteClass(vac_responce_8).write_data_for_vacancies()
        WriteClass(vac_responce_9).write_data_for_vacancies()
        WriteClass(vac_responce_10).write_data_for_vacancies()