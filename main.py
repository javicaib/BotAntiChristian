import os

import requests
from dotenv import load_dotenv
import urllib3
from utils import getToday, verifyIP
urllib3.disable_warnings()

load_dotenv()


class SRNI:

    def __init__(self, url: str = os.getenv('BASE_URL'),
                 username: str = os.getenv('UCI_USER'),
                 password: str = os.getenv('UCI_PASSWORD')):
        self.url = url
        self.username = username
        self.password = password
        self.sesion = requests.Session()

    def getConectionCookie(self) -> dict:

        postData = {
            'username': self.username,
            'password': self.password,
        }
        authUrl = self.url+'auth/signin'
        try:
            response = self.sesion.post(authUrl, verify=False, params=postData)
            data = response.json()
        except Exception as error:
            print("Ocurrió un error:", error)

        return data

    def getIPs(self) -> list:
        self.getConectionCookie()
        url = self.url + f'api/{self.username}/ips'

        response = self.sesion.post(url, verify=False, json=getToday())
        data = response.json()
        ips = data["result"]
        return ips

    def isChristian(self) -> list:
        ips = self.getIPs()
        christian = False
        data = []
        for ip in ips:
            christian = verifyIP(ip["ip"])
            if christian:
                data.append(ip["ip"])
        return data

    def getLasChristianConnection(self) -> any:
        ips = self.isChristian()
        if not (ips):
            return print("Hoy no se ha conectado")
        url = self.url + f"api/{self.username}/{ips[0]}/urls"
        response = self.sesion.post(url, verify=False, json=getToday())
        data = response.json()
        return data["result"][-1]["date"]
