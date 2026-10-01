"""Тесты функций-парсеров и обработки команд из main.py."""

import pytest
from figures import Circle, Rectangle, Triangle, Container
from main import parse_circle, parse_rectangle, parse_triangle, handle_add, process_file


class TestParseCircle:
    """Тесты parse_circle."""

    def test_valid_circle(self):
        """Корректные данные создают Circle."""
        parts = ["ADD", "Circle", "0", "0", "5", "красный", "2024-01-01"]
        fig = parse_circle(parts)
        assert isinstance(fig, Circle)
        assert fig.r == 5
        assert fig.color == "красный"

    def test_bad_radius_raises(self):
        """Нечисловой радиус вызывает ValueError."""
        parts = ["ADD", "Circle", "0", "0", "abc", "красный", "2024-01-01"]
        with pytest.raises(ValueError):
            parse_circle(parts)


class TestParseRectangle:
    """Тесты parse_rectangle."""

    def test_valid_rectangle(self):
        """Корректные данные создают Rectangle."""
        parts = ["ADD", "Rectangle", "0", "4", "6", "0", "зеленый", "2024-02-01"]
        fig = parse_rectangle(parts)
        assert isinstance(fig, Rectangle)
        assert fig.x1 == 0.0
        assert fig.color == "зеленый"

    def test_bad_coordinate_raises(self):
        """Нечисловая координата вызывает ValueError."""
        parts = ["ADD", "Rectangle", "abc", "4", "6", "0", "зеленый", "2024-02-01"]
        with pytest.raises(ValueError):
            parse_rectangle(parts)


class TestParseTriangle:
    """Тесты parse_triangle."""

    def test_valid_triangle(self):
        """Корректные данные создают Triangle."""
        parts = ["ADD", "Triangle", "0", "0", "3", "0", "0", "4", "синий", "2024-03-01"]
        fig = parse_triangle(parts)
        assert isinstance(fig, Triangle)
        assert fig.color == "синий"

    def test_missing_params_raises(self):
        """Недостаточно параметров вызывает IndexError."""
        parts = ["ADD", "Triangle", "0", "0", "3"]
        with pytest.raises(IndexError):
            parse_triangle(parts)

    


class TestHandleAdd:
    """Тесты handle_add."""

    def test_add_circle(self):
        """handle_add добавляет круг в контейнер."""
        cont = Container()
        parts = ["ADD", "Circle", "0", "0", "5", "красный", "2024-01-01"]
        handle_add(parts, 1, cont)
        assert len(cont.items) == 1
        assert isinstance(cont.items[0], Circle)

    def test_add_rectangle(self):
        """handle_add добавляет прямоугольник."""
        cont = Container()
        parts = ["ADD", "Rectangle", "0", "4", "6", "0", "зеленый", "2024-02-01"]
        handle_add(parts, 1, cont)
        assert len(cont.items) == 1
        assert isinstance(cont.items[0], Rectangle)

    def test_add_triangle(self):
        """handle_add добавляет треугольник."""
        cont = Container()
        parts = ["ADD", "Triangle", "0", "0", "3", "0", "0", "4", "синий", "2024-03-01"]
        handle_add(parts, 1, cont)
        assert len(cont.items) == 1
        assert isinstance(cont.items[0], Triangle)

    def test_unknown_type_does_not_add(self):
        """Неизвестный тип фигуры — контейнер остаётся пустым."""
        cont = Container()
        parts = ["ADD", "Фигура", "0", "0"]
        handle_add(parts, 1, cont)
        assert len(cont.items) == 0

    def test_missing_params_does_not_add(self):
        """Неполные данные — контейнер остаётся пустым."""
        cont = Container()
        parts = ["ADD", "Circle", "0"]
        handle_add(parts, 1, cont)
        assert len(cont.items) == 0

    def test_negative_radius_does_not_add(self):
        """Отрицательный радиус — контейнер остаётся пустым."""
        cont = Container()
        parts = ["ADD", "Circle", "0", "0", "-5", "красный", "2024-01-01"]
        handle_add(parts, 1, cont)
        assert len(cont.items) == 0


class TestProcessFile:
    """Тесты process_file."""

    def test_file_not_found(self, capsys):
        """Несуществующий файл — программа не падает, выводит ошибку."""
        process_file("несуществующий_файл.txt")
        output = capsys.readouterr().out
        assert "не найден" in output

    def test_valid_file(self, tmp_path, capsys):
        """Корректный файл — фигуры обрабатываются без ошибок."""
        test_file = tmp_path / "test_input.txt"
        test_file.write_text(
            "ADD Circle 0 0 5 красный 2024-01-01\nPRINT\n",
            encoding="utf-8"
        )
        process_file(str(test_file))
        output = capsys.readouterr().out
        assert "[Круг]" in output
