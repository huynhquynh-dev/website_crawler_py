#!/usr/bin/env python
import urlparse
import requests
import re

# def request(url):
#     try:
#         return requests.get("http://" + url)
#     except requests.exceptions.ConnectionError:
#         pass


# target_url = "google.com"
# with open("subdomains-wordlist.txt", "r") as word_list:
#     for line in word_list:
#         word = line.strip()
#         test_url = word + "." + target_url
#         response = request(test_url)
#         if response:
#             print("[+] Discovered subdomain ---> " + test_url)


# Address Metasploitable
# target_url = "http://10.0.2.20/mutillidae/"
# with open("common.txt", "r") as word_list:
#     for line in word_list:
#         word = line.strip()
#         test_url = target_url + "/" + word
#         response = request(test_url)
#         if response:
#             print("[+] Discovered URL ---> " + test_url)

# Address Metasploitable
target_url = "http://10.0.2.20/mutillidae/"
target_links = []


def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)


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
