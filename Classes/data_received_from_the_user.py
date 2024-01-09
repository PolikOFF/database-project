from Classes.DBManager import DBManager
from Classes.parsing_class import HeadHunter


class UserDataSelection:
    """Класс для получения от пользователя запросов компаниям."""
    @staticmethod
    def selected_company():
        """Метод для выбора вакансий пользователем."""
        answer = int(input("""Вам предлагается выбрать вакансии из 10 компаний.
1 - 'Газпромнефть' * 2 - 'Лукойл' * 3 - 'Российские Железные Дороги'
4 - 'Норникель' * 5 - 'НОВАТЭК' * 6 - 'Татнефть'
7 - 'Северсталь' * 8 - 'Рольф' * 9 - 'Аэрофлот' * 10 - 'Лента'
0 - Выбрать все компании 
11 - закончить работу

"""))

        while answer != ['1', "2", '3', '4', '5', '6', '7', '8', '9', '10', '11', '0']:
            if answer == '1':
                HeadHunter().get_vacancies_by_id_39305()
            elif answer == '2':
                HeadHunter().get_vacancies_by_id_907345()
            elif answer == '3':
                HeadHunter().get_vacancies_by_id_23427()
            elif answer == '4':
                HeadHunter().get_vacancies_by_id_740()
            elif answer == '5':
                HeadHunter().get_vacancies_by_id_1808()
            elif answer == '6':
                HeadHunter().get_vacancies_by_id_575665()
            elif answer == '7':
                HeadHunter().get_vacancies_by_id_6041()
            elif answer == '8':
                HeadHunter().get_vacancies_by_id_59()
            elif answer == '9':
                HeadHunter().get_vacancies_by_id_1373()
            elif answer == '10':
                HeadHunter().get_vacancies_by_id_7172()
            elif answer == '0':
                HeadHunter().get_vacancies_by_id_59()
                HeadHunter().get_vacancies_by_id_7172()
                HeadHunter().get_vacancies_by_id_1373()
                HeadHunter().get_vacancies_by_id_575665()
                HeadHunter().get_vacancies_by_id_1808()
                HeadHunter().get_vacancies_by_id_6041()
                HeadHunter().get_vacancies_by_id_907345()
                HeadHunter().get_vacancies_by_id_740()
                HeadHunter().get_vacancies_by_id_39305()
                HeadHunter().get_vacancies_by_id_23427()
            elif answer == '11':
                print('Возвращайтесь снова!')
                quit()
            else:
                print('Ответ на вопрос должен быть целым, не отрицательным числом.\n')
                break

    @staticmethod
    def selected_statistic():
        """Метод для получения от пользователя желаемых данных по статистике."""
        selected_statistics = input('''Выберите статистику, которую вы хотите получить.
        1 - Получение списка компаний или компании и количества вакансий у каждой.
        2 - Получение список всех вакансий с указанием названия компании,
            названия вакансии и зарплаты и ссылки на вакансию.
        3 - Получение средней зарплаты по вакансиям.
        4 - Получение списка всех вакансий,
            у которых зарплата выше средней по всем вакансиям.
        5 - Получает список всех вакансий,
            в названии которых содержатся переданное слово.
        6 - Выйти из программы.''')

        while selected_statistics != ['1', '2', '3', '4', '5', '6']:
            if selected_statistics == '1':
                data = DBManager().get_companies_and_vacancies()
                print(data)
            elif selected_statistics == '2':
                data = DBManager().get_all_vacancies()
                print(data)
            elif selected_statistics == '3':
                data = DBManager().get_avg_salary()
                print(data)
            elif selected_statistics == '4':
                data = DBManager().get_vacancies_with_higher_salary()
                print(data)
            elif selected_statistics == '5':
                keyword = input('Введите слово или часть слова, входящего в название вакансии.')
                data = DBManager().get_vacancies_with_keyword(keyword)
                if data is None:
                    print('Совпадейний не найдено.')
                else:
                    print(data)
                break
            elif selected_statistics == '6':
                print('''Спасибо за использование нашего сервиса.
                Всего хорошего''')
                quit()
            else:
                print('Выбор должен быть целым, не отрицательным числом.')
                continue
