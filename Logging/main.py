import requests as rq
import logging

formatter = logging.Formatter('%(levelname)s: %(message)s')

# Создаём 3 логгера
handler = logging.FileHandler('success_responses.log', mode='w')
handler.setFormatter(formatter)
logger_success = logging.getLogger('RequestsLogger_success')
logger_success.setLevel('INFO')
logger_success.addHandler(handler)

handler = logging.FileHandler('bad_responses.log', mode='w')
handler.setFormatter(formatter)
logger_bad = logging.getLogger('RequestsLogger_bad')
logger_bad.setLevel('WARNING')
logger_bad.addHandler(handler)

handler = logging.FileHandler('blocked_responses.log', mode='w')
handler.setFormatter(formatter)
logger_blocked = logging.getLogger('RequestsLogger_blocked')
logger_blocked.setLevel('ERROR')
logger_blocked.addHandler(handler)

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        code = response.status_code
        print(response)
        if code == 200:
            logger_success.info(f'\'{site}\', response - {code}')
        else:
            logger_bad.warning(f'\'{site}\', response - {code}')

    except (rq.exceptions.ConnectionError, rq.exceptions.Timeout):
        print('error')
        logger_blocked.error(f'\'{site}\', NO CONNECTION')
