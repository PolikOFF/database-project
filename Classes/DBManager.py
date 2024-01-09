import os
import psycopg2


class DBManager:
    """Класс для получения информации из базы данных."""

    @staticmethod
    def get_companies_and_vacancies():
        """
        Получает список всех компаний
        и количество вакансий у каждой компании.
        """
        try:
            with psycopg2.connect(
                host='localhost',
                user='postgres',
                password=os.getenv('PSQL_KEY'),
                database='vacancies',
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute('''
                        select employer_name, count(*) from vacancies
                        group by employer_name
                        ''')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        finally:
            conn.close()

    @staticmethod
    def get_all_vacancies():
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """
        try:
            with psycopg2.connect(
                host='localhost',
                user='postgres',
                password=os.getenv('PSQL_KEY'),
                database='vacancies',
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute('select employer_name, vacancy_name, salary_to, vacancy_url from vacancies')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        finally:
            conn.close()

    @staticmethod
    def get_avg_salary():
        """Получает среднюю зарплату по вакансиям."""
        try:
            with psycopg2.connect(
                    host='localhost',
                    user='postgres',
                    password=os.getenv('PSQL_KEY'),
                    database='vacancies',
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute('select avg(salary_to) from vacancies')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        finally:
            conn.close()

    @staticmethod
    def get_vacancies_with_higher_salary():
        """
        Получает список всех вакансий,
        у которых зарплата выше средней по всем вакансиям.
        """
        try:
            with psycopg2.connect(
                    host='localhost',
                    user='postgres',
                    password=os.getenv('PSQL_KEY'),
                    database='vacancies',
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute('select vacancy_name from vacancies '
                                'where salary_to > (select avg(salary_to) from vacancies)')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        finally:
            conn.close()

    @staticmethod
    def get_vacancies_with_keyword(keyword):
        """
        Получает список всех вакансий,
        в названии которых содержатся переданные в метод слова,
        например python.
        """
        try:
            with psycopg2.connect(
                    host='localhost',
                    user='postgres',
                    password=os.getenv('PSQL_KEY'),
                    database='vacancies',
            ) as conn:
                with conn.cursor() as cur:
                    coincidences = []
                    cur.execute(f"select vacancy_name, salary_to, vacancy_url from vacancies "
                                f"where vacancy_name like '%{keyword}%'")
                    rows = cur.fetchall()
                    for row in rows:
                        coincidences.append(row)
        finally:
            conn.close()
        return coincidences
