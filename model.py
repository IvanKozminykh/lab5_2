from pydantic import BaseModel
from datetime import datetime

# Модель для представления заметки
class NoteResponse(BaseModel):
    id: int
    text: str
    created_at: datetime
    updated_at: datetime

# Модель для создания заметки
class CreateNoteResponse(BaseModel):
    id: int

# Модель для обновления заметки
class UpdateNoteRequest(BaseModel):
    text: str
