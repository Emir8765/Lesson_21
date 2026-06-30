"""
main.py
-------
Точка входа в приложение "Список дел на основе матрицы Эйзенхауэра".

Запуск:
    python main.py
"""

from Python_task.cli import CLIInterface
from task_manager import TaskManager


def main() -> None:
    """Создаёт менеджер задач и интерфейс, запускает приложение."""
    manager = TaskManager(storage_path="tasks.json")
    app = CLIInterface(manager)
    app.run()


if __name__ == "__main__":
    main()


"Если возникнут проблемы с интерфейсом просто выйдите из Меню (0) и зайдите обратно"
"Что-бы обратно зайти в меню в терминале напишите: python main.py"