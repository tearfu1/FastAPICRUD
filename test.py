import requests


def get_all_students_with_param_request(course: int):
    url = "http://127.0.0.1:8000/students"
    response = requests.get(url, params={"course": course})
    return response.json()


def get_all_students():
    url = "http://127.0.0.1:8000/students"
    response = requests.get(url)
    return response.json()


def get_all_students_with_param_path(course: int):
    url = f"http://127.0.0.1:8000/students/{course}"
    response = requests.get(url)
    return response.json()


def get_all_students_with_param_mix(course: int, major: str, enrollment_year: int):
    url = f"http://127.0.0.1:8000/students/{course}"
    response = requests.get(url, params={"major": major, "enrollment_year": enrollment_year})
    return response.json()


students = get_all_students_with_param_mix(2, major=None, enrollment_year=2018)
for i in students:
    print(i)