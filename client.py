import requests

BASE_URL = "http://localhost:8080"


def get_notes_list(token):
    """Получение списка всех заметок."""
    response = requests.get(f"{BASE_URL}/notes", params={"token": token})
    if response.status_code == 200:
        return response.json()
    print(f"Ошибка: {response.status_code}, {response.text}")
    return None


def create_note(token, text):
    """Создание новой заметки."""
    response = requests.post(f"{BASE_URL}/notes", params={"token": token, "text": text})
    if response.status_code == 200:
        return response.json()
    print(f"Ошибка: {response.status_code}, {response.text}")
    return None


def get_note(token, note_id):
    """Получение заметки по ID."""
    response = requests.get(f"{BASE_URL}/notes/{note_id}", params={"token": token})
    if response.status_code == 200:
        return response.json()
    print(f"Ошибка: {response.status_code}, {response.text}")
    return None


def update_note(token, note_id, text):
    """Обновление заметки."""
    response = requests.patch(f"{BASE_URL}/notes/{note_id}", params={"token": token}, json={"text": text})
    if response.status_code == 200:
        return response.json()
    print(f"Ошибка: {response.status_code}, {response.text}")
    return None


def delete_note(token, note_id):
    """Удаление заметки."""
    response = requests.delete(f"{BASE_URL}/notes/{note_id}", params={"token": token})
    if response.status_code == 200:
        return response.json()
    print(f"Ошибка: {response.status_code}, {response.text}")
    return None


def main():
    while True:
        print("Выберите действие:")
        print("1. Список заметок")
        print("2. Создать заметку")
        print("3. Просмотр заметки")
        print("4. Обновить заметку")
        print("5. Удалить заметку")
        print("6. Выход")
        action = input("Введите номер действия: ")

        if action == "1":
            token = input("Введите токен: ")
            notes = get_notes_list(token)
            if notes is not None:
                print("Список заметок:", notes)

        elif action == "2":
            token = input("Введите токен: ")
            text = input("Введите текст заметки: ")
            result = create_note(token, text)
            if result is not None:
                print("Заметка создана, ID:", result["id"])

        elif action == "3":
            token = input("Введите токен: ")
            note_id = int(input("Введите ID заметки: "))
            note = get_note(token, note_id)
            if note is not None:
                print("Заметка:", note)

        elif action == "4":
            token = input("Введите токен: ")
            note_id = int(input("Введите ID заметки: "))
            new_text = input("Введите новый текст заметки: ")
            result = update_note(token, note_id, new_text)
            if result is not None:
                print("Заметка обновлена:", result)

        elif action == "5":
            token = input("Введите токен: ")
            note_id = int(input("Введите ID заметки: "))
            result = delete_note(token, note_id)
            if result is not None:
                print("Заметка удалена:", result)

        elif action == "6":
            print("Выход")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()


