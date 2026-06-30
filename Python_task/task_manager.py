"""
task_manager.py
----------------
Модуль содержит класс TaskManager — "мозг" приложения, отвечающий за
хранение коллекции задач, их добавление/удаление/изменение, фильтрацию
по квадрантам матрицы Эйзенхауэра, а также за сохранение и загрузку
данных в/из JSON-файла.

Класс полностью независим от способа отображения данных (CLI, GUI, web)
и не содержит никакой логики ввода-вывода, кроме работы с файлом.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

from Python_task.models import Quadrant, Task


class TaskManager:
    """Управляет коллекцией задач и их персистентностью.

    Атрибуты:
        storage_path: Путь к JSON-файлу, в котором хранятся данные.
        tasks: Список всех задач в памяти.
    """

    def __init__(self, storage_path: str = "tasks.json") -> None:
        self.storage_path = Path(storage_path)
        self.tasks: List[Task] = []
        self._next_id: int = 1
        self.load()

    # ------------------------------------------------------------------ #
    # Персистентность
    # ------------------------------------------------------------------ #
    def load(self) -> None:
        """Загружает задачи из JSON-файла, если он существует.

        Если файл отсутствует или повреждён, приложение стартует
        с пустым списком задач (без падения с исключением).
        """
        if not self.storage_path.exists():
            self.tasks = []
            self._next_id = 1
            return

        try:
            raw_text = self.storage_path.read_text(encoding="utf-8")
            raw_data = json.loads(raw_text) if raw_text.strip() else []
            self.tasks = [Task.from_dict(item) for item in raw_data]
        except (json.JSONDecodeError, KeyError, ValueError):
            # Файл повреждён — не роняем приложение, начинаем с чистого листа.
            self.tasks = []

        self._next_id = (max((task.id for task in self.tasks), default=0) + 1)

    def save(self) -> None:
        """Сохраняет текущее состояние коллекции задач в JSON-файл."""
        data = [task.to_dict() for task in self.tasks]
        self.storage_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    # ------------------------------------------------------------------ #
    # CRUD-операции
    # ------------------------------------------------------------------ #
    def add_task(
        self,
        title: str,
        quadrant: Quadrant,
        description: str = "",
        deadline=None,
    ) -> Task:
        """Создаёт новую задачу, добавляет её в коллекцию и сохраняет файл."""
        task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description.strip(),
            quadrant=quadrant,
            deadline=deadline,
        )
        self.tasks.append(task)
        self._next_id += 1
        self.save()
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Возвращает задачу по её id или None, если не найдена."""
        return next((task for task in self.tasks if task.id == task_id), None)

    def delete_task(self, task_id: int) -> bool:
        """Удаляет задачу по id. Возвращает True при успехе."""
        task = self.get_task(task_id)
        if task is None:
            return False
        self.tasks.remove(task)
        self.save()
        return True

    def toggle_task_status(self, task_id: int) -> Optional[Task]:
        """Переключает статус выполнения задачи и сохраняет изменения."""
        task = self.get_task(task_id)
        if task is None:
            return None
        task.toggle_done()
        self.save()
        return task

    def move_task(self, task_id: int, new_quadrant: Quadrant) -> Optional[Task]:
        """Перемещает задачу в другой квадрант и сохраняет изменения."""
        task = self.get_task(task_id)
        if task is None:
            return None
        task.quadrant = new_quadrant
        self.save()
        return task

    def edit_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        deadline=None,
        deadline_changed: bool = False,
    ) -> Optional[Task]:
        """Редактирует поля задачи. Изменяются только переданные поля."""
        task = self.get_task(task_id)
        if task is None:
            return None
        if title:
            task.title = title.strip()
        if description is not None:
            task.description = description.strip()
        if deadline_changed:
            task.deadline = deadline
        self.save()
        return task

    # ------------------------------------------------------------------ #
    # Фильтрация и статистика
    # ------------------------------------------------------------------ #
    def get_tasks_by_quadrant(self, quadrant: Quadrant) -> List[Task]:
        """Возвращает список задач, относящихся к указанному квадранту."""
        return [task for task in self.tasks if task.quadrant == quadrant]

    def get_matrix(self) -> Dict[Quadrant, List[Task]]:
        """Возвращает словарь {квадрант: список задач} для всех 4 квадрантов."""
        return {quadrant: self.get_tasks_by_quadrant(quadrant) for quadrant in Quadrant}

    def get_statistics(self) -> Dict[str, int]:
        """Возвращает агрегированную статистику по всем задачам."""
        total = len(self.tasks)
        done = sum(1 for task in self.tasks if task.done)
        return {
            "total": total,
            "done": done,
            "pending": total - done,
        }

    def is_empty(self) -> bool:
        """Проверяет, есть ли вообще задачи в системе."""
        return len(self.tasks) == 0

"Если возникнут проблемы с интерфейсом просто выйдите из Меню (0) и зайдите обратно"
"Что-бы обратно зайти в меню в терминале напишите: python main.py"