import requests
from googletrans.gtoken import TokenAcquirer
import random
from googletrans import urls, utils
def build_params(query, src, dest, token):
    params = {
        'client': 't',
        'sl': src,
        'tl': dest,
        'hl': dest,
        'dt': ['at', 'bd', 'ex', 'ld', 'md', 'qca', 'rw', 'rm', 'ss', 't'],
        'ie': 'UTF-8',
        'oe': 'UTF-8',
        'otf': 1,
        'ssel': 0,
        'tsel': 0,
        'tk': token,
        'q': query,
    }
    return params


session = requests.Session()
service_urls = 'translate.google.com'
token_acquirer = TokenAcquirer(session=session, host=service_urls)
def _pick_service_url():
    return service_urls
    # if len(service_urls) == 1:
    #     return service_urls[0]
    # return random.choice(self.service_urls)

def _translate(text, dest, src):
        token = token_acquirer.do(text)
        params = build_params(query=text, src=src, dest=dest,
                                    token=token)
        url = 'https://{host}/translate_a/single'.format(host=_pick_service_url())
        r = session.get(url, params=params)
        print(url)
        data = utils.format_json(r.text)
        return r
print(_translate('hello how are you','hi','en').headers)
