import requests
from diplom_2.data import Data
from diplom_2.base import BaseTest

class TestNewCreateUser(BaseTest):
    def test_new_create_user(self):
        headers = {
        'authorization': self.token
        }
        respons = requests.get(Data.name_5,headers=headers)
        assert respons.status_code==200

    def test_new_create_user_no_reg(self):
        respons = requests.get(Data.name_5)
        assert respons.status_code==200