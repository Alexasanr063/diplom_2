import requests
from diplom_2.data import Data
from diplom_2.base import BaseTest

class TestUserChanging(BaseTest):
    def test_user_changing(self):
        headers = {
        'authorization': self.token
        }
        response = requests.get(Data.name_3, headers=headers)
        assert response.status_code==200
        assert response.json()['user']['name'] == self.name

        response = requests.patch(Data.name_3, headers=headers, json=Data.DATAUSER2)
        assert response.status_code == 200
        assert response.json()['user']['name'] == 'САНЕК'

    def test_user_changing_no_registration(self):
        response = requests.patch(Data.name_3, json=Data.DATAUSER2)
        assert response.status_code == 401
        assert response.json()['message'] == 'You should be authorised'
