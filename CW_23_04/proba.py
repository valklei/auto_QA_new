import json


space_mission = {
"Название": "Artemis I",
"Год запуска": 2022,
"Страна": "США",
"Экипаж": None, # Беспилотная миссия
"Продолжительность (дней)": 25,
"Оборудование": ["Орион", "Сервисный модуль", "Манекены с датчиками"],
"Результаты": {
"Дальность полёта (км)": 432000,
"Тестирование систем": "Успешно",
"Возвращение на Землю": True,
"Данные о радиации": {
"Общая доза (мЗв)": 12.5,
"Максимум на орбите Луны (мЗв)": 8.2
}
}
}

company_json = """
{
    "id": 111,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Барбершоп 'Цирюльникъ'",
    "description": "Крутые стрижки для крутых шишек"
}
"""

import json

invalid_json = "{ 'id': 111, 'name': 'Test Company' }"# Неправильные одинарные кавычки

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"Ошибка при разборе JSON: {e}")