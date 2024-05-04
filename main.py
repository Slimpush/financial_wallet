from data_module import load_data, save_data
from CLI_module import (main_menu, get_choice, show_balance,
                        add_record, update_record, search_records)


def main():
    file_path = "data.json"
    data = load_data(file_path)

    while True:
        main_menu()
        choice = get_choice()

        if choice == 1:
            show_balance(data)
        elif choice == 2:
            add_record(data)
        elif choice == 3:
            update_record(data)
        elif choice == 4:
            search_records(data)
        elif choice == 5:
            try:
                save_data(data, file_path)
                print("Данные сохранены. Программа завершена.")
            except Exception as e:
                print(f"Ошибка при сохранении данных: {e}")
            break


if __name__ == "__main__":
    main()
