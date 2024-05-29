import requests as rq
import logging

logger = logging.getLogger('RequestsLogger')

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    # ДОПОЛНИТЬ КОД ЗДЕСЬ
    try:
        logging.basicConfig(level=logging.INFO, filename="success_responses.log", filemode="w")
        response = rq.get(site, timeout=3)
        print(response)
        logging.info(f'\'{site}\', response - {response.status_code}')

    except rq.exceptions.RequestsWarning:
        logging.basicConfig(level=logging.WARNING, filename="bad_responses.log", filemode="w")
        logging.warning(f'\'{site}\', response - {response.status_code}')

    except (rq.exceptions.ConnectionError, rq.exceptions.Timeout):
        logging.basicConfig(level=logging.ERROR, filename="blocked_responses.log", filemode="w")
        logging.error(f'\'{site}\', NO CONNECTION')
