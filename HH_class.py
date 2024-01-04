import requests


class HeadHunter:
    """
    Класс для получения вакансий по десяти айди работодателя
    с сайта HeadHunter по API.
    """
    # @staticmethod
    # def get_vacancies_by_id():
    #     employer_id = ['39305', '907345', '23427', '740', '1808', '575665', '6041', '2748', '1373', '7172']
    #     """Метод для получения вакансий."""
    #     url = f'https://api.hh.ru/vacancies'
    #     headers = {'User-Agent': '2nd parser'}
    #     params = {'employer_id': employer_id, 'page': 0, 'per_page': 100}
    #     response = requests.get(url, params=params, headers=headers)
    #     vacancies = response.json()
    #     return vacancies

    @staticmethod
    def get_vacancies_by_id_39305():
        employer_id = ['39305']
        """Метод для получения вакансий по айди 39305(Газпромнефть)."""
        url = f'https://api.hh.ru/vacancies'
        all_vacancies = []
        for i in range(5):
            headers = {'User-Agent': '2nd parser'}
            params = {'employer_id': employer_id, 'page': i, 'per_page': 100}
            response = requests.get(url, params=params, headers=headers)
            vacancies_39305 = response.json()
            all_vacancies.append(vacancies_39305)
        return all_vacancies

    @staticmethod
    def get_vacancies_by_id_907345():
        employer_id = ['907345']
        """Метод для получения вакансий по айди 907345(Лукойл)."""
        url = f'https://api.hh.ru/vacancies'
        all_vacancies = []
        for i in range(5):
            headers = {'User-Agent': '2nd parser'}
            params = {'employer_id': employer_id, 'page': i, 'per_page': 100}
            response = requests.get(url, params=params, headers=headers)
            vacancies_39305 = response.json()
            all_vacancies.append(vacancies_39305)
        return all_vacancies

    @staticmethod
    def get_vacancies_by_id_23427():
        employer_id = ['23427']
        """Метод для получения вакансий по айди 23427(РЖД)."""
        url = f'https://api.hh.ru/vacancies'
        all_vacancies = []
        for i in range(5):
            headers = {'User-Agent': '2nd parser'}
            params = {'employer_id': employer_id, 'page': i, 'per_page': 100}
            response = requests.get(url, params=params, headers=headers)
            vacancies_39305 = response.json()
            all_vacancies.append(vacancies_39305)
        return all_vacancies

    @staticmethod
    def get_vacancies_by_id_740():
        employer_id = ['740']
        """Метод для получения вакансий по айди 740(Норникель)."""
        url = f'https://api.hh.ru/vacancies'
        all_vacancies = []
        for i in range(5):
            headers = {'User-Agent': '2nd parser'}
            params = {'employer_id': employer_id, 'page': i, 'per_page': 100}
            response = requests.get(url, params=params, headers=headers)
            vacancies_39305 = response.json()
            all_vacancies.append(vacancies_39305)
        return all_vacancies

    @staticmethod
    def get_vacancies_by_id_1808():
        employer_id = ['1808']
        """Метод для получения вакансий по айди 1808(НОВАТЭК)."""
        url = f'https://api.hh.ru/vacancies'
        all_vacancies = []
        for i in range(5):
            headers = {'User-Agent': '2nd parser'}
            params = {'employer_id': employer_id, 'page': i, 'per_page': 100}
            response = requests.get(url, params=params, headers=headers)
            vacancies_39305 = response.json()
            all_vacancies.append(vacancies_39305)
        return all_vacancies

    @staticmethod
    def get_vacancies_by_id_575665():
        employer_id = ['575665']
        """Метод для получения вакансий по айди 575665(Татнефть)."""
        url = f'https://api.hh.ru/vacancies'
        all_vacancies = []
        for i in range(5):
            headers = {'User-Agent': '2nd parser'}
            params = {'employer_id': employer_id, 'page': i, 'per_page': 100}
            response = requests.get(url, params=params, headers=headers)
            vacancies_39305 = response.json()
            all_vacancies.append(vacancies_39305)
        return all_vacancies

    @staticmethod
    def get_vacancies_by_id_6041():
        employer_id = ['6041']
        """Метод для получения вакансий по айди 6041(Северсталь)."""
        url = f'https://api.hh.ru/vacancies'
        all_vacancies = []
        for i in range(5):
            headers = {'User-Agent': '2nd parser'}
            params = {'employer_id': employer_id, 'page': i, 'per_page': 100}
            response = requests.get(url, params=params, headers=headers)
            vacancies_39305 = response.json()
            all_vacancies.append(vacancies_39305)
        return all_vacancies

    @staticmethod
    def get_vacancies_by_id_59():
        employer_id = ['59']
        """Метод для получения вакансий по айди 59(Рольф)."""
        url = f'https://api.hh.ru/vacancies'
        all_vacancies = []
        for i in range(5):
            headers = {'User-Agent': '2nd parser'}
            params = {'employer_id': employer_id, 'page': i, 'per_page': 100}
            response = requests.get(url, params=params, headers=headers)
            vacancies_39305 = response.json()
            all_vacancies.append(vacancies_39305)
        return all_vacancies

    @staticmethod
    def get_vacancies_by_id_1373():
        employer_id = ['1373']
        """Метод для получения вакансий по айди 1373(Аэрофлот)."""
        url = f'https://api.hh.ru/vacancies'
        all_vacancies = []
        for i in range(5):
            headers = {'User-Agent': '2nd parser'}
            params = {'employer_id': employer_id, 'page': i, 'per_page': 100}
            response = requests.get(url, params=params, headers=headers)
            vacancies_39305 = response.json()
            all_vacancies.append(vacancies_39305)
        return all_vacancies

    @staticmethod
    def get_vacancies_by_id_7172():
        employer_id = ['7172']
        """Метод для получения вакансий по айди 7172(Лента)."""
        url = f'https://api.hh.ru/vacancies'
        all_vacancies = []
        for i in range(5):
            headers = {'User-Agent': '2nd parser'}
            params = {'employer_id': employer_id, 'page': i, 'per_page': 100}
            response = requests.get(url, params=params, headers=headers)
            vacancies_39305 = response.json()
            all_vacancies.append(vacancies_39305)
        return all_vacancies
