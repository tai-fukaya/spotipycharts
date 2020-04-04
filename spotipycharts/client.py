import requests
from bs4 import BeautifulSoup

def _get_item_list(url, data_type):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    selector = soup.find('div', attrs={'class': 'responsive-select', 'data-type': data_type})
    if selector is None:
        return []
    item_list = selector.find_all('li')
    return [{'name': x.text, 'code': x.get('data-value')} for x in item_list]

def get_country_list():
    url = 'https://spotifycharts.com/regional'
    data_type = 'country'
    return _get_item_list(url, data_type)

def get_duration_list(chart='regional', country='', freq='daily'):
    url = f"https://spotifycharts.com/{chart}/{country}/{freq}/latest"
    data_type = 'date'
    return _get_item_list(url, data_type)

def download_csv(chart='regional', country='', freq='daily', duration='latest'):
    url = f"https://spotifycharts.com/{chart}/{country}/{freq}/{duration}/download"
    return requests.get(url).text
