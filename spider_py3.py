#!/usr/bin/env python

import urllib.parse as urlparse
import requests
import re


# Address Metasploitable
target_url = "http://10.0.2.20/mutillidae/"
target_links = []


def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))


def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)
        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            crawl(link)
            print(link)


crawl(target_url)