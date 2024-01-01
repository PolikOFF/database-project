from HH_class import HeadHunter


def main():
    vac_responce = HeadHunter().get_vacancies_by_id()
    print(vac_responce)


if __name__ == '__main__':
    main()
