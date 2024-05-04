from data_module import save_data
from typing import List, Dict, Any


def main_menu() -> None:
    """Вывод главного меню."""
    print("\nГлавное меню:")
    print("1. Показать баланс")
    print("2. Добавить запись")
    print("3. Редактировать запись")
    print("4. Поиск по записям")
    print("5. Выйти")


def print_record(record: Dict[str, Any]) -> None:
    """Вывод информации о записи."""
    print(f"Дата: {record['Дата']}")
    print(f"Категория: {record['Категория']}")
    print(f"Сумма: {record['Сумма']} руб.")
    print(f"Описание: {record['Описание']}")


def format_date(date_str: str) -> str:
    """Преобразование даты"""
    separators = ['.', ' ', '/']

    for sep in separators:
        if sep in date_str:
            date_str = date_str.replace(sep, '-')
            break

    return date_str


def get_choice() -> int:
    """Выбор команды"""
    while True:
        choice = input("\nВыберите операцию (1-5): ")
        if choice in ['1', '2', '3', '4', '5']:
            return int(choice)
        else:
            print("Выберите операцию в диапазоне от 1 до 5.")


def show_balance(data: List[Dict[str, Any]]) -> None:
    """Показать текущий баланс"""
    incomes = sum(record["Сумма"]
                  for record in data
                  if record["Категория"] == "Доходы"
                  )
    expenses = sum(record["Сумма"]
                   for record in data
                   if record["Категория"] == "Расходы"
                   )
    balance = incomes - expenses

    print("\nТекущий баланс:")
    print(f"Доходы: {incomes} руб.")
    print(f"Расходы: {expenses} руб.")
    print(f"Баланс: {balance} руб.")


def add_record(data: List[Dict[str, Any]]) -> None:
    """Добавить новую запись"""
    print("\nДобавление новой записи:")

    date = format_date(input("Введите дату (ДД-ММ-ГГГГ): "))
    category = input("Введите категорию (Доходы/Расходы): ").capitalize()
    amount = float(input("Введите сумму: "))
    description = input("Введите описание: ")

    record = {
        "Дата": date,
        "Категория": category,
        "Сумма": amount,
        "Описание": description
    }

    data.append(record)
    print("Запись успешно добавлена.")


def update_record(data: List[Dict[str, Any]]) -> None:
    """Редактировать существующую запись"""
    print("\nРедактирование записи:")

    date_to_update = input(
        "Введите дату записи для редактирования (ДД-ММ-ГГГГ): ")

    for record in data:
        if record["Дата"] == date_to_update:
            print("Найдена запись:")
            print_record(record)

            print("Введите новые значения:")
            record["Дата"] = format_date(input("Новая дата (ДД-ММ-ГГГГ): "))
            record["Категория"] = input(
                "Новая категория (Доходы/Расходы): ").capitalize()
            record["Сумма"] = float(input("Новая сумма: "))
            record["Описание"] = input("Новое описание: ")

            print("Запись успешно обновлена.")
            return

    print("Запись за эту дату не найдена.")


def search_records(data: List[Dict[str, Any]]) -> None:
    """Поиск записей по фильтрам"""
    print("\nПоиск записей:")

    criteria = input(
        "Введите критерий поиска (дата, категория, сумма): ").capitalize()

    if criteria == "Дата":
        search_value = format_date(
            input("Введите дату для поиска (ДД-ММ-ГГГГ): "))
        results = [record for record in data if record["Дата"] == search_value]
    elif criteria == "Категория":
        search_value = input(
            "Введите категорию для поиска (Доходы/Расходы): ").capitalize()
        results = [record for record in data
                   if record["Категория"] == search_value]
    elif criteria == "Сумма":
        search_value = float(input("Введите сумму для поиска: "))
        results = [record for record in data
                   if record["Сумма"] == search_value]
    else:
        print("Некорректный критерий поиска.")
        return

    if results:
        print("Результаты поиска:")
        for result in results:
            print_record(result)
    else:
        print("Записи по указанным критериям не найдены.")


def exit_program(data: List[Dict[str, Any]], file_path: str) -> None:
    """Выход из программы."""
    save_data(data, file_path)
    print("Данные сохранены. Программа завершена.")
    exit()
