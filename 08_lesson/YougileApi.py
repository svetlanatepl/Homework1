import requests


class YougileApi:

    def __init__(self, url):
        self.url = url
        self.token = None

    def get_company_list(self, user, password):
        # Список компаний

        payload = {
            "login": user,
            "password": password,
            "name": "SkyPro"
        }

        headers = {"Content-Type": "application/json"}
        response = requests.request(
            "POST", self.url + '/api-v2/auth/companies',
            json=payload, headers=headers
        )
        return response.json()["content"]

    def get_token(self, user, password, company_id):
        # Ключ авторизации

        payload = {
            "login": user,
            "password": password,
            "companyId": company_id
        }

        headers = {"Content-Type": "application/json"}
        response = requests.request(
            "POST", self.url + '/api-v2/auth/keys',
            json=payload, headers=headers
        )

        self.token = response.json()["key"]
        return self.token

    def get_project_list(self):
        # Список проектов

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.request(
            "GET", self.url + '/api-v2/projects', headers=headers
        )
        return response.json()

    def create_project(self, name_project, user_role):
        # Создать проект

        payload = {
            "title": name_project,
            "users": user_role
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.request(
            "POST", self.url + '/api-v2/projects',
            json=payload, headers=headers
        )
        return response.json()

    def edit_project(self, new_title, user_role, id_project):
        # Изменить проект

        payload = {
            "deleted": False,
            "title": new_title,
            "users": user_role
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        url_with_id_project = f"{self.url}/api-v2/projects/{id_project}"
        response = requests.request(
            "PUT", url_with_id_project, json=payload, headers=headers
        )
        return response.json()

    def get_project_id(self, id_project):
        # Получить проект по id

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

        url_with_id_project = f"{self.url}/api-v2/projects/{id_project}"
        response = requests.request(
            "GET", url_with_id_project, headers=headers
        )
        return response.json()

    def del_token(self):
        # Удалить токен

        headers = {"Content-Type": "application/json"}
        url_with_token = f"{self.url}//api-v2/auth/keys/{self.token}"
        response = requests.request("DELETE", url_with_token, headers=headers)
        return response
