import requests
from bs4 import BeautifulSoup

html2='https://quote.rbc.ru/ticker/59111'
html='https://www.rbc.ru/crypto/currency/btcusd'

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def get_btc(html):
    r = get_html('https://www.rbc.ru/crypto/currency/btcusd')
    if r:
        with open('test.html', 'w', encoding='utf8') as output_file:
            output_file.write(r)
    else:
        pass

def get_usd(html2):
    r = get_html('https://quote.rbc.ru/ticker/59111')

    if r:
        with open('test_usd.html', 'w', encoding='utf8') as output_file:
            output_file.write(r)
    else:
        pass

def get_btc_rate():
    html = get_html('https://www.rbc.ru/crypto/currency/btcusd')
    soup = BeautifulSoup(html, 'html.parser')
    btc_list = soup.find('div', class_="chart__info")

    title = btc_list.find('div').text.replace('\n','')
    btc_list.span.decompose()
    price = soup.find('div', class_="chart__subtitle js-chart-value").text.replace(' ','').replace('\n','').replace(',','.')
    result_btc = price
    return result_btc

def get_usd_rate():
    html2 = get_html('https://quote.rbc.ru/ticker/59111')
    soup = BeautifulSoup(html2, 'html.parser')
    usd_list = soup.find('div', class_="chart__info__row js-ticker")

    title = usd_list.find('span', class_="chart__info__sum").text.replace(' ','').replace('\n','').replace('₽','').replace(',',".")
    # price = soup.find('span', class_="item__company__sum js-reload-ticker-sum").text.replace(' ','').replace('₽','').replace('\n','').replace(',','.')
    # result =  price
    return title






if __name__ == "__main__":

    if html:
        get_btc(html)
        print(get_btc_rate())
    if html2:
        get_usd(html2)
        print(get_usd_rate())