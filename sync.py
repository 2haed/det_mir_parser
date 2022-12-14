import json
import logging
import sys
import aiohttp
import asyncio
import warnings
import time
import requests
from bs4 import BeautifulSoup
from constants import HOSTURL, HEADERS, URL
from fp.fp import FreeProxy

warnings.filterwarnings("ignore", category=DeprecationWarning)
logging.basicConfig(filename='errors.log', format='%(asctime)s| %(message)s', datefmt='%m-%d-%Y %I:%M:%S',
                    level=logging.INFO)


def make_proxies(n: int) -> dict:
    dict_of_proxies = dict()
    for i in range(n):
        proxy = FreeProxy(rand=True).get()
        dict_of_proxies[''.join(proxy.split(':')[0])] = proxy
    return dict_of_proxies


def get_free_proxies(n) -> list[str]:
    proxies = []
    url = "https://free-proxy-list.net/"
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for row in soup.find("table", class_="table table-striped table-bordered").find_all("tr")[1:n + 1]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies


def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        formatted = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(formatted, objects), sep=sep, end=end, file=file)


def get_page_data():
    with session.get(link, headers=HEADERS) as response:


def get_product_data():
    pass


async def main():
    pass


if __name__ == '__main__':
    start = time.time()

    print(time.time() - start)