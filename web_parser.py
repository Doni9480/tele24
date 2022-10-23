import random
import time

import requests
from bs4 import BeautifulSoup as Bs4
from fake_useragent import UserAgent

from write_read import WriteRead


# print(datetime.datetime.now())


class AlaToo24:

    def __init__(self, work: bool = False, url: str = None, attempt=5):
        if not url:
            self.url = "https://24.kg/"
        else:
            self.url = url
        if work:

            try:
                self.useragent = UserAgent().chrome
                self.headers = {
                    "accept": "application/json, text/plain, */*",
                    "user-agent": f"{self.useragent}",
                }
                if attempt == 5:
                    print(f'[INFO] start parsing -> {url} ... ', end='')
                    time.sleep(random.randrange(1, 3))

                elif attempt != 5:
                    print(f'[INFO] Attempt {attempt}: start parsing  -> {url} ... ', end='')
                    time.sleep(random.randrange(10, 12))

                self.set_response = requests.get(self.url, headers=self.headers)
                if self.set_response:
                    print('done!')
                else:
                    print('Not done!')
                    raise
            except Exception as _ex:
                if attempt != 1:
                    AlaToo24(url=url, attempt=attempt - 1)
                else:
                    self.set_response = None
            self.set_response = WriteRead().read_write_text_file(file="data.html", mod='w', encoding='utf-8',
                                                                 data_for_write=self.set_response.text)
        elif not work:
            try:
                self.set_response = WriteRead().read_write_text_file(file="data.html")
            except Exception as es:
                print(es)

    def get_html(self):
        return self.set_response

    def news_lents(self, html: str = None):
        if not html:
            html = self.set_response
        date_g = ''
        soup = Bs4(html, 'lxml')
        find_list_data = soup.find('div', {"id": "newslist"}).find_all(class_="col-xs-12")[1].find_all('div')
        dic = {}
        for ix, block in enumerate(find_list_data):
            class_div = str(block.get('class'))
            if "one" in class_div:
                try:
                    time_post = f"{block.find(class_='time').text}".strip()
                    title = block.find(class_='title')
                    link = f"https://24.kg{title.find('a').get('href')}".strip()
                    title = f"{title.text.strip()}".replace('\xa0', ' ')
                    subdic = dict([('time', time_post), ('title', title), ('link', link)])
                    dic[f'{date_g.strip()}'].append(subdic)
                except AttributeError as _ex:
                    continue
            elif "lineDate" in class_div:
                date_g = block.text
                dic[f'{date_g.strip()}'] = []
        return dic

    def get_more_info(self, html: str = None):
        if not html:
            html = self.set_response
        try:
            soup = Bs4(html, 'lxml')
            title = soup.find(class_='newsTitle').text
            text_content = soup.find('div', {"class": "cont", "itemprop": "articleBody"})
            return {'title': f"{title}", "content_text": f"{text_content}"}
        except AttributeError:
            return None

    def news_sections(self, html: str = None):
        if not html:
            html = self.set_response
        dic = {}
        try:
            soup = Bs4(html, 'lxml')
            other_block = soup.find('ul', {'class': 'nav navbar-nav'})
            links_block = other_block.find_all('a')
            for l in links_block:
                link = l.get('href')
                name = l.text.strip()
                dic[f'{name}'] = f"{self.url}{link[1::]}"
            return dic
        except Exception as ex:
            print(ex)
            return None


def main():
    url = "https://24.kg/"
    data = AlaToo24().news_sections()
    print(data)
    # get_page_data(url=url)
    # news_sections(data.text)
    # # dic = news_lents(data.text)
    # # rez = write_read_json(dic,mod='w')
    # # print(rez)
    # r = get_more_info(data.text)
    # print(r)


if __name__ == '__main__':
    main()
#
