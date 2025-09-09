from symtable import Class
import requests
from diplom_2.data import Data
from diplom_2.base import BaseTest

class TestNewCreateUser(BaseTest):

    def test_successful_registration(self):
        assert self.token != ""


    def test_create_user(self):
        register_data = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }
        response = requests.post(Data.name_1, data=register_data)
        assert response.status_code == 403
        assert response.json()["message"] == 'User already exists'

    def test_not_all_feld(self):
        register_data = {
            "email": self.email,
            "name": self.name
        }
        response = requests.post(Data.name_1, data=register_data)
        assert response.status_code == 403
        assert response.json()["message"] == 'Email, password and name are required fields'