"""
cli.py
------
Модуль содержит класс CLIInterface — отвечает за весь визуальный слой
приложения на базе библиотеки rich (таблицы, панели, меню) и за
обработку пользовательского ввода. Не содержит бизнес-логики хранения
данных — вся работа с задачами делегируется в TaskManager.
"""

from __future__ import annotations

import shutil
from datetime import date, datetime
from typing import Optional

from rich.align import Align
from rich.console import Console, Group
from rich.panel import Panel
from rich.prompt import Confirm, IntPrompt, Prompt
from rich.table import Table
from rich.text import Text

from models import Quadrant, Task
from task_manager import TaskManager

# Ниже этой ширины терминала квадранты выводятся в один столбец,
# а не сеткой 2x2 — иначе панели "схлопываются" и обрезаются
# (характерная проблема консоли PyCharm при неполном экране).
NARROW_TERMINAL_THRESHOLD = 100

# Ширина, которую приложение использует, если терминал вообще не смог
# сообщить свой реальный размер (например, специфичная псевдоконсоль IDE).
FALLBACK_WIDTH = 120


class CLIInterface:
    """Отвечает за отрисовку интерфейса и взаимодействие с пользователем."""

    def __init__(self, manager: TaskManager) -> None:
        self.manager = manager
        # width=None заставляет rich определять ширину терминала заново
        # перед КАЖДОЙ отрисовкой, а не один раз при старте. Это устраняет
        # рассинхрон при разворачивании/сворачивании окна PyCharm.
        self.console = Console(width=None, soft_wrap=False)

    def _current_width(self) -> int:
        """Достоверно определяет текущую ширину терминала.

        rich иногда получает от PyCharm устаревшее или дефолтное (80)
        значение ширины. Дополнительно сверяемся с shutil.get_terminal_size,
        которая чаще опрашивает ОС напрямую, и берём более надёжное значение.
        """
        rich_width = self.console.size.width
        os_width = shutil.get_terminal_size(fallback=(FALLBACK_WIDTH, 40)).columns
        # Если оба источника согласны — доверяем им. Если сильно расходятся
        # или одно из значений похоже на "дефолтную заглушку" (80),
        # берём большее как более вероятно корректное для широких окон.
        width = max(rich_width, os_width)
        return width if width > 0 else FALLBACK_WIDTH

    # ------------------------------------------------------------------ #
    # Главный цикл приложения
    # ------------------------------------------------------------------ #
    def run(self) -> None:
        """Запускает основной цикл приложения."""
        self._print_welcome()
        while True:
            self.show_matrix()
            self._print_menu()
            choice = Prompt.ask(
                "[bold cyan]Выберите действие[/bold cyan]",
                choices=["1", "2", "3", "4", "5", "6", "0"],
                show_choices=False,
            )
            self.console.clear()

            if choice == "1":
                self.add_task_flow()
            elif choice == "2":
                self.toggle_task_flow()
            elif choice == "3":
                self.move_task_flow()
            elif choice == "4":
                self.edit_task_flow()
            elif choice == "5":
                self.delete_task_flow()
            elif choice == "6":
                self.show_quadrant_detail_flow()
            elif choice == "0":
                self._print_goodbye()
                break

    # ------------------------------------------------------------------ #
    # Отрисовка матрицы и меню
    # ------------------------------------------------------------------ #
    def _print_welcome(self) -> None:
        self.console.clear()
        width = self._current_width()
        title = Text("МАТРИЦА ЭЙЗЕНХАУЭРА", style="bold white on dark_blue", justify="center")
        subtitle = Text("Управляй приоритетами, а не делами", style="italic grey70", justify="center")
        self.console.print(Panel(Group(title, subtitle), border_style="blue", padding=(1, 4)), width=width)

    def _print_goodbye(self) -> None:
        self.console.print(
            Panel(
                "[bold green]Все данные сохранены. До встречи![/bold green]",
                border_style="green",
                padding=(1, 4),
            )
        )

    def show_matrix(self) -> None:
        """Отображает все 4 квадранта в виде сетки 2x2 (или столбцом на узких экранах)."""
        width = self._current_width()
        matrix = self.manager.get_matrix()
        stats = self.manager.get_statistics()

        panels = {q: self._build_quadrant_panel(q, matrix[q]) for q in Quadrant}

        if width < NARROW_TERMINAL_THRESHOLD:
            # Узкий терминал (PyCharm на пол-экрана и т.п.) — выводим
            # квадранты друг под другом, чтобы ничего не обрезалось.
            grid = Table.grid(expand=True, padding=(0, 0, 1, 0))
            grid.add_column(ratio=1)
            for q in Quadrant:
                grid.add_row(panels[q])
        else:
            # Широкий терминал — классическая сетка 2x2, отрисованная
            # ОДНИМ объектом за ОДИН print, чтобы не возникало
            # рассинхрона ширины между верхней и нижней строками.
            grid = Table.grid(expand=True, padding=(0, 0, 1, 0))
            grid.add_column(ratio=1)
            grid.add_column(ratio=1)
            grid.add_row(panels[Quadrant.URGENT_IMPORTANT], panels[Quadrant.IMPORTANT_NOT_URGENT])
            grid.add_row(panels[Quadrant.URGENT_NOT_IMPORTANT], panels[Quadrant.NOT_IMPORTANT_NOT_URGENT])

        self.console.print(grid, width=width)

        stats_text = Text.from_markup(
            f"[bold]Всего задач:[/bold] {stats['total']}   "
            f"[bold green]Выполнено:[/bold green] {stats['done']}   "
            f"[bold yellow]В работе:[/bold yellow] {stats['pending']}"
        )
        stats_panel = Panel(Align.center(stats_text), border_style="grey50", padding=(0, 1))
        self.console.print(stats_panel, width=width)

    def _build_quadrant_panel(self, quadrant: Quadrant, tasks: list[Task]) -> Panel:
        """Строит панель rich с таблицей задач для одного квадранта."""
        table = Table(
            show_header=True,
            header_style=f"bold {quadrant.color}",
            box=None,
            expand=True,
            padding=(0, 1),
        )
        table.add_column("ID", width=4, justify="center")
        table.add_column("Задача", overflow="fold")
        table.add_column("Статус", width=14)
        table.add_column("Дедлайн", width=18)

        if not tasks:
            table.add_row("", "[dim]Задач пока нет[/dim]", "", "")
        else:
            for task in sorted(tasks, key=lambda t: t.done):
                title_text = task.title if not task.done else f"[strike dim]{task.title}[/strike dim]"
                table.add_row(str(task.id), title_text, task.status_label, task.deadline_label)

        header = f"[bold {quadrant.color}]{quadrant.title}[/bold {quadrant.color}] [dim]({quadrant.subtitle})[/dim]"
        return Panel(table, title=header, border_style=quadrant.color, padding=(1, 1))

    def _print_menu(self) -> None:
        width = self._current_width()
        menu = Table.grid(expand=True, padding=(0, 2))
        menu.add_column(ratio=1)
        menu.add_column(ratio=1)
        menu.add_column(ratio=1)
        menu.add_row(
            "[bold]1[/bold] Добавить задачу",
            "[bold]2[/bold] Отметить выполнение",
            "[bold]3[/bold] Переместить задачу",
        )
        menu.add_row(
            "[bold]4[/bold] Редактировать",
            "[bold]5[/bold] Удалить задачу",
            "[bold]6[/bold] Детали квадранта",
        )
        menu.add_row("[bold]0[/bold] Выход", "", "")
        self.console.print(Panel(menu, title="Меню", border_style="cyan", padding=(1, 2)), width=width)

    # ------------------------------------------------------------------ #
    # Вспомогательные методы ввода
    # ------------------------------------------------------------------ #
    def _ask_quadrant(self, prompt_text: str = "Выберите квадрант") -> Quadrant:
        table = Table(box=None, show_header=False, padding=(0, 1))
        table.add_column()
        table.add_column()
        for i in range(1, 5):
            q = Quadrant.from_index(i)
            table.add_row(f"[bold {q.color}]{i}[/bold {q.color}]", f"[{q.color}]{q.title}[/{q.color}]")
        self.console.print(Panel(table, title=prompt_text, border_style="cyan"))
        index = IntPrompt.ask("Номер квадранта", choices=["1", "2", "3", "4"], show_choices=False)
        return Quadrant.from_index(int(index))

    def _ask_deadline(self) -> Optional[date]:
        raw = Prompt.ask(
            "Дедлайн в формате [bold]ДД.ММ.ГГГГ[/bold] (Enter — пропустить)",
            default="",
            show_default=False,
        )
        if not raw.strip():
            return None
        try:
            return datetime.strptime(raw.strip(), "%d.%m.%Y").date()
        except ValueError:
            self.console.print("[bold red]Неверный формат даты, дедлайн не установлен.[/bold red]")
            return None

    def _ask_task_id(self, prompt_text: str) -> Optional[Task]:
        if self.manager.is_empty():
            self.console.print(Panel("[yellow]Список задач пуст.[/yellow]", border_style="yellow"))
            return None
        task_id = IntPrompt.ask(prompt_text)
        task = self.manager.get_task(int(task_id))
        if task is None:
            self.console.print(Panel(f"[bold red]Задача с ID {task_id} не найдена.[/bold red]", border_style="red"))
        return task

    def _pause(self) -> None:
        Prompt.ask("\n[dim]Нажмите Enter, чтобы продолжить[/dim]", default="", show_default=False)

    # ------------------------------------------------------------------ #
    # Сценарии действий пользователя
    # ------------------------------------------------------------------ #
    def add_task_flow(self) -> None:
        """Сценарий добавления новой задачи."""
        self.console.print(Panel("[bold]Добавление новой задачи[/bold]", border_style="green"))
        title = Prompt.ask("Название задачи")
        while not title.strip():
            self.console.print("[red]Название не может быть пустым.[/red]")
            title = Prompt.ask("Название задачи")
        description = Prompt.ask("Описание (необязательно)", default="", show_default=False)
        quadrant = self._ask_quadrant("В какой квадрант поместить задачу?")
        deadline = self._ask_deadline()

        task = self.manager.add_task(title=title, quadrant=quadrant, description=description, deadline=deadline)
        self.console.print(
            Panel(
                f"[bold green]Задача '{task.title}' (ID {task.id}) успешно добавлена в квадрант "
                f"'{quadrant.title}'![/bold green]",
                border_style="green",
            )
        )
        self._pause()

    def toggle_task_flow(self) -> None:
        """Сценарий переключения статуса выполнения задачи."""
        self.console.print(Panel("[bold]Отметить выполнение задачи[/bold]", border_style="green"))
        task = self._ask_task_id("Введите ID задачи")
        if task is None:
            self._pause()
            return
        updated = self.manager.toggle_task_status(task.id)
        status = "выполненной" if updated.done else "невыполненной"
        self.console.print(Panel(f"[bold green]Задача '{updated.title}' отмечена как {status}.[/bold green]", border_style="green"))
        self._pause()

    def move_task_flow(self) -> None:
        """Сценарий перемещения задачи между квадрантами."""
        self.console.print(Panel("[bold]Перемещение задачи между квадрантами[/bold]", border_style="green"))
        task = self._ask_task_id("Введите ID задачи для перемещения")
        if task is None:
            self._pause()
            return
        self.console.print(f"Текущий квадрант: [bold {task.quadrant.color}]{task.quadrant.title}[/bold {task.quadrant.color}]")
        new_quadrant = self._ask_quadrant("Выберите новый квадрант")
        self.manager.move_task(task.id, new_quadrant)
        self.console.print(
            Panel(f"[bold green]Задача '{task.title}' перемещена в '{new_quadrant.title}'.[/bold green]", border_style="green")
        )
        self._pause()

    def edit_task_flow(self) -> None:
        """Сценарий редактирования названия, описания и дедлайна задачи."""
        self.console.print(Panel("[bold]Редактирование задачи[/bold]", border_style="green"))
        task = self._ask_task_id("Введите ID задачи для редактирования")
        if task is None:
            self._pause()
            return

        self.console.print(f"Текущее название: [italic]{task.title}[/italic]")
        new_title = Prompt.ask("Новое название (Enter — оставить без изменений)", default="", show_default=False)

        self.console.print(f"Текущее описание: [italic]{task.description or '—'}[/italic]")
        new_description = Prompt.ask("Новое описание (Enter — оставить без изменений)", default=None, show_default=False)

        change_deadline = Confirm.ask("Изменить дедлайн?", default=False)
        new_deadline = task.deadline
        deadline_changed = False
        if change_deadline:
            new_deadline = self._ask_deadline()
            deadline_changed = True

        self.manager.edit_task(
            task.id,
            title=new_title if new_title.strip() else None,
            description=new_description,
            deadline=new_deadline,
            deadline_changed=deadline_changed,
        )
        self.console.print(Panel("[bold green]Задача обновлена.[/bold green]", border_style="green"))
        self._pause()

    def delete_task_flow(self) -> None:
        """Сценарий удаления задачи с подтверждением."""
        self.console.print(Panel("[bold]Удаление задачи[/bold]", border_style="red"))
        task = self._ask_task_id("Введите ID задачи для удаления")
        if task is None:
            self._pause()
            return
        confirmed = Confirm.ask(f"Удалить задачу '{task.title}'?", default=False)
        if confirmed:
            self.manager.delete_task(task.id)
            self.console.print(Panel("[bold green]Задача удалена.[/bold green]", border_style="green"))
        else:
            self.console.print(Panel("[yellow]Удаление отменено.[/yellow]", border_style="yellow"))
        self._pause()

    def show_quadrant_detail_flow(self) -> None:
        """Сценарий детального просмотра одного квадранта с описаниями задач."""
        quadrant = self._ask_quadrant("Какой квадрант показать подробно?")
        tasks = self.manager.get_tasks_by_quadrant(quadrant)

        if not tasks:
            self.console.print(Panel("[yellow]В этом квадранте пока нет задач.[/yellow]", border_style="yellow"))
            self._pause()
            return

        table = Table(title=quadrant.title, header_style=f"bold {quadrant.color}", border_style=quadrant.color, expand=True)
        table.add_column("ID", width=4, justify="center")
        table.add_column("Задача")
        table.add_column("Описание")
        table.add_column("Статус")
        table.add_column("Дедлайн")

        for task in tasks:
            table.add_row(
                str(task.id),
                task.title,
                task.description or "—",
                task.status_label,
                task.deadline_label,
            )

        self.console.print(table)
        self._pause()

"Если возникнут проблемы с интерфейсом просто выйдите из Меню (0) и зайдите обратно"
"Что-бы обратно зайти в меню в терминале напишите: python main.py"