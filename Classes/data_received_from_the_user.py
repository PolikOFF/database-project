from Classes.DBManager import DBManager


class UserDataSelection:
    """Класс для получения от пользователя запросов компаниям."""
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

        if selected_statistics == '1':
            DBManager().get_companies_and_vacancies()
        elif selected_statistics == '2':
            DBManager().get_all_vacancies()
        elif selected_statistics == '3':
            DBManager().get_avg_salary()
        elif selected_statistics == '4':
            DBManager().get_vacancies_with_higher_salary()
        elif selected_statistics == '5':
            keyword = input('Введите слово или часть слова, входящего в название вакансии.')
            data = DBManager().get_vacancies_with_keyword(keyword)
            if data == []:
                print('Совпадейний не найдено.')
            else:
                for i in data:
                    print(i)
        elif selected_statistics == '6':
            print('''Спасибо за использование нашего сервиса.
Всего хорошего''')
            quit()
        else:
            print('Выбор должен быть целым, не отрицательным числом.')
