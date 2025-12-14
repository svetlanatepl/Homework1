from sqlalchemy import create_engine, text


class EducationTable:

    __scripts = {
        "select": text("SELECT * FROM subject"),
        "insert_new": text(
            'INSERT INTO subject("subject_title", "subject_id") '
            'values (:new_name, :sub_id)'
        ),
        "get_max_id": text('SELECT MAX("subject_id") FROM subject'),
        "update_subject": text(
            "UPDATE subject SET (subject_title = :new_name)"
            " WHERE (subject_id = :sub_id)"
        ),
        "delete_by_id": text(
            "DELETE FROM subject WHERE subject_id = :id_to_delete"
        ),
        "get_subject_title": text(
            "SELECT subject_title FROM subject WHERE subject_id = :sub_id"
        ),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subjects(self):
        # Получить все предметы
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def get_max_id(self):
        # Получить максимальный Id в таблице subject

        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_max_id"])
        max_id = result.scalar()
        conn.close()
        return max_id

    def get_subject_title_by_subject_id(self, subject_id):
        # Получить наименование предмета по id

        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_subject_title"],
                              {"sub_id": subject_id})
        subject_title = result.scalar()
        conn.close()
        return subject_title

    def create_subject(self, name, subject_id):
        # Создание нового предмета

        conn = self.__db.connect()
        conn.execute(self.__scripts["insert_new"],
                     {"new_name": name, "sub_id": subject_id})
        conn.commit()
        conn.close()

    def update_subject(self, name, subject_id):
        # Изменение предмета

        conn = self.__db.connect()
        conn.execute(self.__scripts["update_subject"],
                     {"new_name": name, "sub_id": subject_id})
        conn.commit()
        conn.close()

    def delete(self, id):
        # Удаление предмета
        conn = self.__db.connect()
        conn.execute(self.__scripts["delete_by_id"], {"id_to_delete": id})
        conn.commit()
        conn.close()
