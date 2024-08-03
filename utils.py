import json
from json_db_lite import JSONDatabase


def dict_list_to_json(dict_list, filename):
    """
    Преобразует список словарей в JSON-строку и сохраняет её в файл.

    :param dict_list: Список словарей
    :param filename: Имя файла для сохранения JSON-строки
    :return: JSON-строка или None в случае ошибки
    """
    try:
        json_str = json.dumps(dict_list, ensure_ascii=False)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_str)
        return json_str
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при преобразовании списка словарей в JSON или записи в файл: {e}")
        return None


small_db = JSONDatabase(file_path='students.json')

# получаем все записи
def json_to_dict_list():
    return small_db.get_all_records()


# добавляем студента
def add_student(student: dict):
    student['date_of_birth'] = student['date_of_birth'].strftime('%Y-%m-%d')
    small_db.add_records(student)
    return True


# обновляем данные по студенту
def upd_student(upd_filter: dict, new_data: dict):
    small_db.update_record_by_key(upd_filter, new_data)
    return True


# удаляем студента
def dell_student(key: str, value: str):
    small_db.delete_record_by_key(key, value)
    return True
