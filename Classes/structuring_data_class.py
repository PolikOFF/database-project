
class DataStructiring:
    """Класс для работы с данными запроса по API"""
    def __init__(self, data):
        self.data = data

    def structuring_data(self):
        """Метод для отбора вакансий с указанной зарплатой и зарплатой в рублях"""
        vacancy_with_salary = []
        vacancy_dicts = []
        for vacancy in range(len(self.data)):
            if (self.data['items'][vacancy]['salary'] is not None and
                    self.data['items'][vacancy]['salary']['currency'] == 'RUR'):
                vacancy_with_salary.append([
                    self.data['items'][vacancy]['name'],
                    self.data['items'][vacancy]['employer']['id'],
                    self.data['items'][vacancy]['employer']['name'],
                    self.data['items'][vacancy]['salary']['from'],
                    self.data['items'][vacancy]['salary']['to'],
                    self.data['items'][vacancy]['alternate_url']
                ])
                for i in vacancy_with_salary:
                    dict_vacancy = {
                        'name_vacancy': i[0],
                        'employer_id': i[1],
                        'employer_name': i[2],
                        'salary_from': i[3],
                        'salary_to': i[4],
                        'url': i[5]
                    }
                    if dict_vacancy['salary_from'] is None:
                        dict_vacancy['salary_from'] = 0
                    elif dict_vacancy['salary_to'] is None:
                        dict_vacancy['salary_to'] = dict_vacancy['salary_from']
                    vacancy_dicts.append(dict_vacancy)
        return vacancy_dicts
