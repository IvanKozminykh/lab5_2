from model import NoteResponse, CreateNoteResponse, UpdateNoteRequest
from datetime import datetime

if __name__ == '__main__':
    # Тестируем сериализацию модели NoteResponse
    note_response = NoteResponse(
        id=123,
        text="Пример текста заметки",
        created_at=datetime(2023, 12, 25, 10, 15, 30),
        updated_at=datetime(2023, 12, 26, 18, 45, 15)
    )
    print("NoteResponse JSON:")
    print(note_response.json())

    # Тестируем сериализацию модели CreateNoteResponse
    create_note_response = CreateNoteResponse(
        id=124
    )
    print("\nCreateNoteResponse JSON:")
    print(create_note_response.json())

    # Тестируем сериализацию модели UpdateNoteRequest
    update_note_request = UpdateNoteRequest(
        text="Обновленный текст заметки"
    )
    print("\nUpdateNoteRequest JSON:")
    print(update_note_request.json())

