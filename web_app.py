import fastapi
from model import NoteResponse, CreateNoteResponse, UpdateNoteRequest
from typing import List
from datetime import datetime
import json
from fastapi import HTTPException

# Хранилище заметок
notes_db = {}

# Путь к файлу с токенами
TOKENS_FILE_PATH = "tokens.json"


api_router = fastapi.APIRouter()


def load_tokens():
    """Загружает токены из файла tokens.json."""
    try:
        with open("token.json", "r", encoding="utf-8") as file:
            tokens = json.load(file)
            return list(tokens.values())  # Возвращаем список токенов
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Tokens file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid tokens file format")


# Проверка токена
def verify_token(token: str):
    tokens_db = load_tokens()  # Загружаем токены
    if token not in tokens_db:
        raise HTTPException(status_code=401, detail="Invalid or missing token")


# Получение заметки по ID
@api_router.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, token: str):
    verify_token(token)  # Проверка токена
    note = notes_db.get(note_id)
    if not note:
        raise fastapi.HTTPException(status_code=404, detail="Note not found")
    return note


# Создание заметки
@api_router.post("/notes", response_model=CreateNoteResponse)
def create_note(token: str, text: str):
    verify_token(token)  # Проверка токена
    note_id = len(notes_db) + 1
    note = NoteResponse(id=note_id, text=text, created_at=datetime.now(), updated_at=datetime.now())
    notes_db[note_id] = note
    return CreateNoteResponse(id=note_id)


# Обновление заметки
@api_router.patch("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, token: str, request: UpdateNoteRequest):
    verify_token(token)  # Проверка токена
    note = notes_db.get(note_id)
    if not note:
        raise fastapi.HTTPException(status_code=404, detail="Note not found")
    note.text = request.text
    note.updated_at = datetime.now()
    notes_db[note_id] = note
    return note


# Удаление заметки
@api_router.delete("/notes/{note_id}", response_model=NoteResponse)
def delete_note(note_id: int, token: str):
    verify_token(token)  # Проверка токена
    note = notes_db.pop(note_id, None)
    if not note:
        raise fastapi.HTTPException(status_code=404, detail="Note not found")
    return note


# Получение списка всех заметок
@api_router.get("/notes", response_model=List[int])
def get_notes_list(token: str):
    verify_token(token)  # Проверка токена
    return list(notes_db.keys())

