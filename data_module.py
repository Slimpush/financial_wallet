import json
from typing import Any, List


def save_data(data: List[Any], file_path: str) -> None:
    """Сохранение данных в файл"""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def load_data(file_path: str) -> List[Any]:
    """Выгрузка данных из файла"""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Файл не найден.")
        return []
