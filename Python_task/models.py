"""
models.py
---------
Модуль содержит модель данных приложения — класс Task.

Task инкапсулирует всю информацию об отдельной задаче: идентификатор,
название, описание, квадрант матрицы Эйзенхауэра, статус выполнения
и дедлайн. Класс умеет сериализоваться в словарь (для JSON) и
восстанавливаться из словаря.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from typing import Optional


class Quadrant(str, Enum):
    """Перечисление четырёх квадрантов матрицы Эйзенхауэра."""

    URGENT_IMPORTANT = "important_urgent"
    IMPORTANT_NOT_URGENT = "important_not_urgent"
    URGENT_NOT_IMPORTANT = "not_important_urgent"
    NOT_IMPORTANT_NOT_URGENT = "not_important_not_urgent"

    @property
    def title(self) -> str:
        """Человекочитаемое название квадранта на русском языке."""
        titles = {
            Quadrant.URGENT_IMPORTANT: "Важно и Срочно",
            Quadrant.IMPORTANT_NOT_URGENT: "Важно, но Не срочно",
            Quadrant.URGENT_NOT_IMPORTANT: "Не важно, но Срочно",
            Quadrant.NOT_IMPORTANT_NOT_URGENT: "Не важно и Не срочно",
        }
        return titles[self]

    @property
    def subtitle(self) -> str:
        """Краткая рекомендация по работе с задачами этого квадранта."""
        subtitles = {
            Quadrant.URGENT_IMPORTANT: "Делать немедленно",
            Quadrant.IMPORTANT_NOT_URGENT: "Планировать",
            Quadrant.URGENT_NOT_IMPORTANT: "Делегировать",
            Quadrant.NOT_IMPORTANT_NOT_URGENT: "Удалить / Отложить",
        }
        return subtitles[self]

    @property
    def color(self) -> str:
        """Цвет для оформления квадранта в библиотеке rich."""
        colors = {
            Quadrant.URGENT_IMPORTANT: "red",
            Quadrant.IMPORTANT_NOT_URGENT: "green",
            Quadrant.URGENT_NOT_IMPORTANT: "yellow",
            Quadrant.NOT_IMPORTANT_NOT_URGENT: "grey58",
        }
        return colors[self]

    @classmethod
    def from_index(cls, index: int) -> "Quadrant":
        """Возвращает квадрант по его порядковому номеру (1-4) в меню."""
        mapping = {
            1: cls.URGENT_IMPORTANT,
            2: cls.IMPORTANT_NOT_URGENT,
            3: cls.URGENT_NOT_IMPORTANT,
            4: cls.NOT_IMPORTANT_NOT_URGENT,
        }
        if index not in mapping:
            raise ValueError(f"Недопустимый номер квадранта: {index}")
        return mapping[index]


@dataclass
class Task:
    """Модель отдельной задачи списка дел.

    Атрибуты:
        id: Уникальный числовой идентификатор задачи.
        title: Краткое название задачи.
        description: Развёрнутое описание задачи (может быть пустым).
        quadrant: Квадрант матрицы Эйзенхауэра, к которому отнесена задача.
        done: Флаг завершённости задачи.
        deadline: Необязательная дата дедлайна.
        created_at: Дата и время создания задачи (для информации/сортировки).
    """

    id: int
    title: str
    quadrant: Quadrant
    description: str = ""
    done: bool = False
    deadline: Optional[date] = None
    created_at: datetime = field(default_factory=datetime.now)

    def toggle_done(self) -> None:
        """Переключает статус выполнения задачи на противоположный."""
        self.done = not self.done

    @property
    def status_label(self) -> str:
        """Текстовая метка статуса с rich-разметкой."""
        return "[bold green]✔ Выполнено[/bold green]" if self.done else "[bold red]✘ В работе[/bold red]"

    @property
    def deadline_label(self) -> str:
        """Текстовое представление дедлайна для отображения в таблице."""
        if self.deadline is None:
            return "—"
        label = self.deadline.strftime("%d.%m.%Y")
        if not self.done and self.deadline < date.today():
            return f"[bold red]{label} (просрочено)[/bold red]"
        return label

    def to_dict(self) -> dict:
        """Сериализует задачу в словарь, пригодный для сохранения в JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "quadrant": self.quadrant.value,
            "done": self.done,
            "deadline": self.deadline.isoformat() if self.deadline else None,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Создаёт экземпляр Task из словаря, ранее полученного из JSON."""
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            quadrant=Quadrant(data["quadrant"]),
            done=data.get("done", False),
            deadline=date.fromisoformat(data["deadline"]) if data.get("deadline") else None,
            created_at=datetime.fromisoformat(data["created_at"]) if data.get("created_at") else datetime.now(),
        )

"Если возникнут проблемы с интерфейсом просто выйдите из Меню (0) и зайдите обратно"
"Что-бы обратно зайти в меню в терминале напишите: python main.py"