"""Тесты контейнера и функции _evaluate_condition."""

import pytest
from figures import Circle, Rectangle, Triangle, Container, _evaluate_condition


class TestContainerAdd:
    """Тесты добавления фигур в контейнер."""

    def test_add_single(self):
        """Добавление одной фигуры увеличивает длину на 1."""
        cont = Container()
        c = Circle(0, 0, 5, "красный", "2024-01-01")
        cont.add(c)
        assert len(cont.items) == 1

    def test_add_multiple(self):
        """Добавление трёх фигур разного типа."""
        cont = Container()
        cont.add(Circle(0, 0, 5, "красный", "2024-01-01"))
        cont.add(Rectangle(0, 4, 6, 0, "зеленый", "2024-02-01"))
        cont.add(Triangle(0, 0, 3, 0, 0, 4, "синий", "2024-03-01"))
        assert len(cont.items) == 3

    def test_added_figure_is_same_object(self):
        """Добавленная фигура — тот же объект, что передали."""
        cont = Container()
        c = Circle(0, 0, 5, "красный", "2024-01-01")
        cont.add(c)
        assert cont.items[0] is c


class TestContainerRemove:
    """Тесты удаления фигур по условию."""

    def _make_container(self):
        """Вспомогательный метод: контейнер с тремя фигурами."""
        cont = Container()
        cont.add(Circle(0, 0, 5, "красный", "2024-01-01"))       # S ~ 78.54
        cont.add(Circle(0, 0, 2, "желтый", "2024-01-02"))        # S ~ 12.57
        cont.add(Rectangle(0, 2, 2, 0, "синий", "2024-01-03"))   # S = 4.0
        return cont

    def test_remove_by_area(self):
        """Удаление фигур с площадью > 50."""
        cont = self._make_container()
        cont.remove_by_condition("area > 50")
        assert len(cont.items) == 2

    def test_remove_by_color(self):
        """Удаление фигур жёлтого цвета."""
        cont = self._make_container()
        cont.remove_by_condition("color == 'желтый'")
        assert len(cont.items) == 2

    def test_remove_nothing_when_no_match(self):
        """Условие не подходит ни одной фигуре — ничего не удаляется."""
        cont = self._make_container()
        cont.remove_by_condition("area > 1000")
        assert len(cont.items) == 3

    def test_remove_all_by_broad_condition(self):
        """Условие подходит всем — контейнер пуст."""
        cont = self._make_container()
        cont.remove_by_condition("area > 0")
        assert len(cont.items) == 0

    def test_remove_invalid_condition_keeps_all(self):
        """Некорректное условие — фигуры не удаляются."""
        cont = self._make_container()
        cont.remove_by_condition("abracadabra")
        assert len(cont.items) == 3


class TestContainerPrint:
    """Тесты вывода контейнера."""

    def test_print_empty(self, capsys):
        """Пустой контейнер выводит 'Контейнер пуст.'"""
        cont = Container()
        cont.print_all()
        output = capsys.readouterr().out
        assert "Контейнер пуст." in output

    def test_print_notempty(self, capsys):
        """Непустой контейнер выводит информацию о фигурах."""
        cont = Container()
        cont.add(Circle(0, 0, 5, "красный", "2024-01-01"))
        cont.print_all()
        output = capsys.readouterr().out
        assert "[Круг]" in output
        assert "всего: 1" in output


class TestEvaluateCondition:
    """Тесты функции _evaluate_condition."""

    def _make_context(self):
        """Контекст для тестов: круг с радиусом 5."""
        c = Circle(0, 0, 5, "красный", "2024-01-01")
        return {
            "area": c.area(),
            "perimeter": c.perimeter(),
            "color": c.color,
            "date": c.date,
            "type": "Circle",
            "r": c.r,
            "width": 0,
            "height": 0,
        }

    def test_equals_string_true(self):
        """Оператор == для строки (совпадение)."""
        ctx = self._make_context()
        assert _evaluate_condition("color == 'красный'", ctx) is True

    def test_equals_string_false(self):
        """Оператор == для строки (несовпадение)."""
        ctx = self._make_context()
        assert _evaluate_condition("color == 'синий'", ctx) is False

    def test_not_equals(self):
        """Оператор !=."""
        ctx = self._make_context()
        assert _evaluate_condition("color != 'синий'", ctx) is True

    def test_greater_true(self):
        """Оператор > (площадь ~78.5 > 50)."""
        ctx = self._make_context()
        assert _evaluate_condition("area > 50", ctx) is True

    def test_greater_false(self):
        """Оператор > (площадь ~78.5 > 100)."""
        ctx = self._make_context()
        assert _evaluate_condition("area > 100", ctx) is False

    def test_less(self):
        """Оператор <."""
        ctx = self._make_context()
        assert _evaluate_condition("area < 100", ctx) is True

    def test_greater_equal(self):
        """Оператор >=."""
        ctx = self._make_context()
        assert _evaluate_condition("r >= 5", ctx) is True

    def test_less_equal(self):
        """Оператор <=."""
        ctx = self._make_context()
        assert _evaluate_condition("r <= 5", ctx) is True

    def test_unknown_field_raises_key_error(self):
        """Неизвестное поле вызывает KeyError."""
        ctx = self._make_context()
        with pytest.raises(KeyError):
            _evaluate_condition("xyz > 10", ctx)

    def test_no_operator_raises_value_error(self):
        """Строка без оператора вызывает ValueError."""
        ctx = self._make_context()
        with pytest.raises(ValueError):
            _evaluate_condition("abracadabra", ctx)

    def test_equals_number(self):
        """Оператор == для числа."""
        ctx = self._make_context()
        assert _evaluate_condition("r == 5", ctx) is True
