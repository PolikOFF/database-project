import psycopg2
import os


class WriteClass:
    """Класс для записи данных в БД."""
    def __init__(self, data):
        self.data = data

    def write_data_for_employers(self):
        """Метод для записи данных в БД таблицы employers"""
        try:
            with psycopg2.connect(
                    host='localhost',
                    database='vacancies',
                    user='postgres',
                    password=os.getenv('PSQL_KEY')
            ) as conn:
                with conn.cursor() as cur:
                    a = len(self.data[0]['items'])
                    b = len(self.data[1]['items'])
                    c = a + b
                    cur.execute('insert into employeers (employyer_name, vacancy_count) values (%s, %s)',
                                (self.data[0]['items'][0]['employer']['name'], c))
        finally:
            conn.close()

    def write_data_for_vacancies(self):
        """Метод для записи данных в БД таблицы vacancies"""
        try:
            with psycopg2.connect(
                    host='localhost',
                    database='vacancies',
                    user='postgres',
                    password=os.getenv('PSQL_KEY')
            ) as conn:
                with conn.cursor() as cur:
                    for vacancy in range(len(self.data)):
                        # Требуется доработка salary, т.к. нужно сделать исключение добавления вакансии без зарплаты.
                        if self.data[0]['items'][vacancy]['salary'] is None:
                            self.data[0]['items'][vacancy]['salary'] = 0
                        elif self.data[0]['items'][vacancy]['salary']['to'] is None:
                            self.data[0]['items'][vacancy]['salary']['to'] = self.data[0]['items'][vacancy]['salary']['from']
                        elif self.data[0]['items'][vacancy]['salary']['from'] is None:
                            self.data[0]['items'][vacancy]['salary']['from'] = self.data[0]['items'][vacancy]['salary']['to']
                        cur.execute('insert into vacancies (vacancy_name, salary, vacancy_url) values (%s, %s, %s)',
                                    (self.data[0]['items'][vacancy]['name'],
                                     self.data[0]['items'][vacancy]['salary'],
                                     self.data[0]['items'][vacancy]['alternate_url']))
                    for vacancy in range(len(self.data)):
                        if self.data[1]['items'][vacancy]['salary'] is None:
                            self.data[1]['items'][vacancy]['salary'] = 0
                        elif self.data[1]['items'][vacancy]['salary']['to'] is None:
                            self.data[1]['items'][vacancy]['salary']['to'] = self.data[1]['items'][vacancy]['salary'][
                                'from']
                        elif self.data[1]['items'][vacancy]['salary']['from'] is None:
                            self.data[1]['items'][vacancy]['salary']['from'] = self.data[1]['items'][vacancy]['salary'][
                                'to']
                        cur.execute('insert into vacancies (vacancy_name, salary, vacancy_url) values (%s, %s, %s)',
                                    (self.data[1]['items'][vacancy]['name'],
                                     self.data[1]['items'][vacancy]['salary'],
                                     self.data[1]['items'][vacancy]['alternate_url']))
        finally:
            conn.close()
