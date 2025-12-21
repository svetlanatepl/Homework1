from EducationTable import EducationTable
import pytest

db = EducationTable("postgresql://postgres:903@localhost:5432/postgres")


def test_add_subject():
    # Добавить новый предмет

    # Получить список предметов из БД
    db_before = db.get_subjects()

    # Получим максимальный id в таблице subject
    max_subject_id = db.get_max_id()

    # Добавляем новый предмет
    name = "Chinese"
    subject_id = max_subject_id + 1
    db.create_subject(name, subject_id)

    # Получить список предметов из БД
    db_after = db.get_subjects()

    # Удаление предмета
    db.delete(subject_id)

    # Проверка
    assert len(db_after) - len(db_before) == 1

def test_edit_subject():
    # Изменение информации о предмете

    # Получим максимальный id в таблице subject
    max_subject_id = db.get_max_id()

    # Добавляем новый предмет
    name = "Geometry"
    subject_id = max_subject_id + 1
    db.create_subject(name, subject_id)

    # Изменяем название предмета
    new_name = "Italian"
    db.update_subject(new_name, subject_id)

    # Получить название предмета по id
    subject_title = db.get_subject_title_by_subject_id(subject_id)

    # Удаление предмета
    db.delete(subject_id)

    # Проверка
    assert subject_title == new_name


def test_delete_subject():
    # Удаление предмета

    # Получить список предметов из БД
    db_before = db.get_subjects()

    # Получим максимальный id в таблице subject
    max_subject_id = db.get_max_id()

    # Добавляем новый предмет
    name = "Astronomy"
    subject_id = max_subject_id + 1
    db.create_subject(name, subject_id)

    # Удаление предмета
    db.delete(subject_id)

    # Получить список предметов из БД
    db_after = db.get_subjects()

    # Проверка
    assert len(db_after) - len(db_before) == 0
