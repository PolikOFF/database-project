import requests


class HeadHunter:
    """Класс для работы с сайтом HeadHunter по API."""
    @staticmethod
    def get_vacancies_by_id():
        employer_id = ['газпромнефть']
        """Метод для получения вакансий."""
        url = f'https://api.hh.ru/employers'
        headers = {'User-Agent': '2nd parser'}
        params = {'text': employer_id, 'page': 0, 'per_page': 100}
        response = requests.get(url, params=params, headers=headers)
        vacancies = response.json()
        return vacancies

