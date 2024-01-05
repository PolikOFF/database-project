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
                    cur.execute('insert into employers (employer_name, vacancy_count) values (%s, %s)',
                                (self.data['items'][0]['employer']['name'], len(self.data['items'])))
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
                    for i in range(len(self.data)):
                        cur.execute(
                            'insert into vacancies (vacancy_name, employer_id, employer_name, salary_from, salary_to, vacancy_url)'
                            'values (%s, %s, %s, %s, %s, %s)',
                            (self.data[i]['name_vacancy'],
                             self.data[i]['employer_id'],
                             self.data[i]['employer_name'],
                             self.data[i]['salary_from'],
                             self.data[i]['salary_to'],
                             self.data[i]['url'])
                        )
        finally:
            conn.close()
