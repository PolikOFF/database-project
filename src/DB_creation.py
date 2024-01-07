import psycopg2
import os


def db_refresh():
    """
    Функция для пересоздания БД.
    Если база данных существует, она удаляется
    и создается новая
    """
    conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password=os.getenv('PSQL_KEY'),
            database='postgres',
    )
    cur = conn.cursor()
    conn.autocommit = True

    cur.execute('drop database if exists vacancies')
    cur.execute('create database vacancies')

    cur.close()
    conn.close()


def create_tables():
    try:
        with psycopg2.connect(
                host='localhost',
                user='postgres',
                password=os.getenv('PSQL_KEY'),
                database='vacancies',
        ) as conn:
            with conn.cursor() as cur:
                cur.execute('''
                create table vacancies
                (
                    vacancy_id serial primary key,
                    vacancy_name varchar not null,
                    employer_id int,
                    employer_name varchar(50),
                    salary_from int,
                    salary_to int,
                    vacancy_url varchar(30)
                );
                
                create table employers
                (
                    employer_id serial primary key,
                    employer_name varchar(50),
                    vacancy_count int
                );
                ''')
    finally:
        conn.close()
