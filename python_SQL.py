import json

def load_data():
    try:
        with open('phone_directory.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def save_data(data):
    with open('phone_directory.json', 'w') as file:
        json.dump(data, file)

def view_contacts(data):
    if data:
        print("Телефонный справочник:")
        for name, number in data.items():
            print(f"{name}: {number}")
    else:
        print("Телефонный справочник пустой.")

def add_contact(data):
    name = input("Введите имя контакта: ")
    number = input("Введите контактный номер: ")
    data[name] = number
    save_data(data)
    print("Контакт успешно добавлен.")

def import_contacts(data):
    file_name = input("Введите имя файла для импорта контактов из(в JSON формат): ")
    try:
        with open(file_name, 'r') as file:
            imported_data = json.load(file)
        data.update(imported_data)
        save_data(data)
        print("Контакты успешно импортированы.")
    except FileNotFoundError:
        print("Файл не найден.")

def search_contact(data):
    name = input("Введите имя контакта для поиска: ")
    if name in data:
        print(f"{name}: {data[name]}")
    else:
        print("Контакт не найден.")

def delete_contact(data):
    name = input("Введите имя контакта для удаления: ")
    if name in data:
        del data[name]
        save_data(data)
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")

def modify_contact(data):
    name = input("Введите имя контакта для изменения: ")
    if name in data:
        number = input("Введите новый контактный номер: ")
        data[name] = number
        save_data(data)
        print("Контакт успешно изменен.")
    else:
        print("Контакт не найден.")

def main():
    data = load_data()
    while True:
        print("\nPhone Directory - Main Menu:")
        print("1. Просмотр контактов")
        print("2.Добавить контакт")
        print("3. Импорт контактов")
        print("4. Поиск контакта")
        print("5. Удалить контакт")
        print("6. Изменить контакт")
        print("7. Выход")

        choice = input("Введите свой выбор(1-7): ")
        if choice == '1':
            view_contacts(data)
        elif choice == '2':
            add_contact(data)
        elif choice == '3':
            import_contacts(data)
        elif choice == '4':
            search_contact(data)
        elif choice == '5':
            delete_contact(data)
        elif choice == '6':
            modify_contact(data)
        elif choice == '7':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
