import pytest
import requests
import random
from diplom_2.data import Data

class BaseTest:
    def setup_method(self):
        self.email = f"test{random.randint(10000,999999)}@yandex.ru"
        self.password = "password"
        self.name = "TestUser"

        register_data = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }
        response = requests.post(Data.name_1,data=register_data)
        self.token = response.json().get('accessToken', '')

    def teardown_method(self):
        if hasattr(self, 'token') and self.token:
            # Удаляем пользователя
            headers = {'authorization': f'Bearer {self.token}'}
            requests.delete(Data.name_3, headers=headers)