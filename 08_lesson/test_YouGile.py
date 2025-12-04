from YougileApi import YougileApi
from config import user
from config import password
from config import company_id
from config import user_role

api = YougileApi("https://ru.yougile.com")


def test_positive_get_companies():
    # Получить компании

    body = api.get_company_list(user, password)
    assert body is not None


def test_positive_get_token():
    # Получить токен
    token = api.get_token(user, password, company_id)
    assert token is not None


def test_positive_add_new_project():
    # Добавление проекта

    name_project = "Мои документы"
    add_project = api.create_project(name_project, user_role)
    assert add_project["id"] is not None


def test_positive_edit_project():
    # Изменить проект

    # Создаём проект
    name_project = "Годовая отчётность"
    new_project = api.create_project(name_project, user_role)
    id_project = str(new_project.get("id"))

    # изменить информацию о проекте
    new_title = "Корпоратив"
    api.edit_project(new_title, user_role, id_project)

    # Получить проект по id
    get_project = api.get_project_id(id_project)
    assert get_project["title"] == new_title


def test_positive_get_project_id():
    # Получить проект по id

    # Создать проект
    name_project = "Новый год"
    new_project = api.create_project(name_project, user_role)
    id_project = str(new_project.get("id"))
    get_project = api.get_project_id(id_project)
    assert get_project["id"] == id_project


def test_negativ_add_new_project():
    # Добавление проекта с пустыми данными

    name_project = None
    if name_project is None:
        assert AssertionError
    else:
        add_project = api.create_project(name_project, user_role)
        assert add_project.get("id") is not None


def test_negativ_edit_project():
    # Изменить проект c несуществующим id

    new_title = "Новое название проекта"
    id_project = "!!bf0098-07f5-4477-b32f-9e63e5c03f2c"
    edited = api.edit_project(new_title, user_role, id_project)
    assert edited['statusCode'] == 404


def test_negative_get_project_id():
    # Получить проект по id, когда отсутствует обязательный параметр id

    id_project = None
    get_project = api.get_project_id(id_project)

    if id_project is None:
        assert get_project["statusCode"] == 404
    else:
        assert get_project.get("id") == id_project


def test_positive_del_token():
    # Удалить токен
    del_token = api.del_token()
    assert del_token.status_code == 200
