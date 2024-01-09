import requests


class HeadHunter:
    """
    Класс для получения вакансий по айди работодателя
    с сайта HeadHunter по API.
    """
    url = f'https://api.hh.ru/vacancies'

    def get_vacancies(self):
        """Метод для получения вакансий по айди 39305(Газпромнефть)."""
        employer_id = ['39305', '907345', '23427', '740', '1808', '575665', '6041', '59', '1373', '7172']
        headers = {'User-Agent': '2nd parser'}
        params = {'employer_id': employer_id, 'page': 0, 'per_page': 90}
        response = requests.get(self.url, params=params, headers=headers)
        vacancies = response.json()
        return vacancies
