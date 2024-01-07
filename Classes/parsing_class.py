import requests


class HeadHunter:
    """
    Класс для получения вакансий по айди работодателя
    с сайта HeadHunter по API.
    """
    url = f'https://api.hh.ru/vacancies'

    def get_vacancies_by_id_39305(self):
        """Метод для получения вакансий по айди 39305(Газпромнефть)."""
        employer_id = ['39305']
        headers = {'User-Agent': '2nd parser'}
        params = {'employer_id': employer_id, 'page': 0, 'per_page': 100}
        response = requests.get(self.url, params=params, headers=headers)
        vacancies = response.json()
        return vacancies

    def get_vacancies_by_id_907345(self):
        """Метод для получения вакансий по айди 907345(Лукойл)."""
        employer_id = ['907345']
        headers = {'User-Agent': '2nd parser'}
        params = {'employer_id': employer_id, 'page': 0, 'per_page': 100}
        response = requests.get(self.url, params=params, headers=headers)
        vacancies = response.json()
        return vacancies

    def get_vacancies_by_id_23427(self):
        """Метод для получения вакансий по айди 23427(РЖД)."""
        employer_id = ['23427']
        headers = {'User-Agent': '2nd parser'}
        params = {'employer_id': employer_id, 'page': 0, 'per_page': 100}
        response = requests.get(self.url, params=params, headers=headers)
        vacancies = response.json()
        return vacancies

    def get_vacancies_by_id_740(self):
        """Метод для получения вакансий по айди 740(Норникель)."""
        employer_id = ['740']
        headers = {'User-Agent': '2nd parser'}
        params = {'employer_id': employer_id, 'page': 0, 'per_page': 100}
        response = requests.get(self.url, params=params, headers=headers)
        vacancies = response.json()
        return vacancies

    def get_vacancies_by_id_1808(self):
        """Метод для получения вакансий по айди 1808(НОВАТЭК)."""
        employer_id = ['1808']
        headers = {'User-Agent': '2nd parser'}
        params = {'employer_id': employer_id, 'page': 0, 'per_page': 100}
        response = requests.get(self.url, params=params, headers=headers)
        vacancies = response.json()
        return vacancies

    def get_vacancies_by_id_575665(self):
        """Метод для получения вакансий по айди 575665(Татнефть)."""
        employer_id = ['575665']
        headers = {'User-Agent': '2nd parser'}
        params = {'employer_id': employer_id, 'page': 0, 'per_page': 100}
        response = requests.get(self.url, params=params, headers=headers)
        vacancies = response.json()
        return vacancies

    def get_vacancies_by_id_6041(self):
        """Метод для получения вакансий по айди 6041(Северсталь)."""
        employer_id = ['6041']
        headers = {'User-Agent': '2nd parser'}
        params = {'employer_id': employer_id, 'page': 0, 'per_page': 100}
        response = requests.get(self.url, params=params, headers=headers)
        vacancies = response.json()
        return vacancies

    def get_vacancies_by_id_59(self):
        """Метод для получения вакансий по айди 59(Рольф)."""
        employer_id = ['59']
        headers = {'User-Agent': '2nd parser'}
        params = {'employer_id': employer_id, 'page': 0, 'per_page': 100}
        response = requests.get(self.url, params=params, headers=headers)
        vacancies = response.json()
        return vacancies

    def get_vacancies_by_id_1373(self):
        """Метод для получения вакансий по айди 1373(Аэрофлот)."""
        employer_id = ['1373']
        headers = {'User-Agent': '2nd parser'}
        params = {'employer_id': employer_id, 'page': 0, 'per_page': 100}
        response = requests.get(self.url, params=params, headers=headers)
        vacancies = response.json()
        return vacancies

    def get_vacancies_by_id_7172(self):
        """Метод для получения вакансий по айди 7172(Лента)."""
        employer_id = ['7172']
        headers = {'User-Agent': '2nd parser'}
        params = {'employer_id': employer_id, 'page': 0, 'per_page': 100}
        response = requests.get(self.url, params=params, headers=headers)
        vacancies = response.json()
        return vacancies
