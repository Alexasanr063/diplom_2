import requests
from diplom_2.data import Data
from diplom_2.base import BaseTest

class TestNewCreateUser(BaseTest):
    def test_new_create_user(self):

        headers = {
        'authorization': self.token
        }
        order_data = {
        "ingredients": Data.ingridients_1
        }
        respons = requests.post(Data.name_4,headers=headers,json=order_data)
        assert respons.status_code == 200

    def test_new_create_user_no_registration(self):

        order_data = {
        "ingredients": Data.ingridients_1
        }
        respons = requests.post(Data.name_4,json=order_data)
        assert respons.status_code == 200

    def test_new_create_user_no_ingridient(self):
        order_data = {
        "ingredients": []
        }
        headers = {
        'authorization': self.token
        }
        respons = requests.post(Data.name_4,headers=headers,json=order_data)
        assert respons.status_code == 400

    def test_new_create_user_no_correct_ingridient(self):
        order_data = {
        "ingredients": ['123','321']
        }
        headers = {
        'authorization': self.token
        }
        respons = requests.post(Data.name_4,headers=headers,json=order_data)
        assert respons.status_code == 500