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