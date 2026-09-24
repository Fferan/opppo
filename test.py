"""Тесты для проверки классов геометрических фигур и контейнера."""

import math
import pytest
from figures import Circle, Container, Rectangle, Triangle


class TestCircle:
    """Тесты для класса Circle."""

    def test_area(self):
        """Проверяет площадь круга."""
        c = Circle(0, 0, 5, "красный", "2024-01-01")
        assert c.area() == pytest.approx(math.pi * 25)

    def test_perimeter(self):
        """Проверяет периметр (длину окружности)."""
        c = Circle(0, 0, 5, "красный", "2024-01-01")
        assert c.perimeter() == pytest.approx(2 * math.pi * 5)

    def test_negative_radius_raises(self):
        """Проверяет, что отрицательный радиус вызывает ValueError."""
        with pytest.raises(ValueError):
            Circle(0, 0, -1, "красный", "2024-01-01")

    def test_zero_radius_raises(self):
        """Проверяет, что нулевой радиус вызывает ValueError."""
        with pytest.raises(ValueError):
            Circle(0, 0, 0, "красный", "2024-01-01")


class TestRectangle:
    """Тесты для класса Rectangle."""

    def test_area(self):
        """Проверяет площадь прямоугольника."""
        r = Rectangle(0, 4, 6, 0, "зеленый", "2024-02-01")
        assert r.area() == pytest.approx(24.0)

    def test_perimeter(self):
        """Проверяет периметр прямоугольника."""
        r = Rectangle(0, 4, 6, 0, "зеленый", "2024-02-01")
        assert r.perimeter() == pytest.approx(20.0)

    def test_degenerate_raises(self):
        """Проверяет, что вырожденный прямоугольник (нулевая сторона) вызывает ValueError."""
        with pytest.raises(ValueError):
            Rectangle(0, 0, 5, 0, "синий", "2024-01-01")


class TestTriangle:
    """Тесты для класса Triangle."""

    def test_area(self):
        """Проверяет площадь треугольника."""
        t = Triangle(0, 0, 3, 0, 0, 4, "синий", "2024-03-01")
        assert t.area() == pytest.approx(6.0)

    def test_perimeter(self):
        """Проверяет периметр треугольника."""
        t = Triangle(0, 0, 3, 0, 0, 4, "синий", "2024-03-01")
        assert t.perimeter() == pytest.approx(12.0)

    def test_collinear_raises(self):
        """Проверяет, что вырожденный треугольник (точки на одной прямой) вызывает ValueError."""
        with pytest.raises(ValueError):
            Triangle(0, 0, 1, 0, 2, 0, "синий", "2024-01-01")


class TestContainer:
    """Тесты для класса Container."""

    def test_add(self):
        """Проверяет добавление фигур в контейнер."""
        cont = Container()
        c = Circle(0, 0, 5, "красный", "2024-01-01")
        cont.add(c)
        assert len(cont.items) == 1

    def test_remove_by_area(self):
        """Проверяет удаление по условию на площадь."""
        cont = Container()
        c1 = Circle(0, 0, 5, "красный", "2024-01-01")   # S ~ 78.54
        c2 = Circle(0, 0, 2, "желтый", "2024-01-02")    # S ~ 12.57
        r = Rectangle(0, 2, 2, 0, "синий", "2024-01-03")  # S = 4.0

        cont.add(c1)
        cont.add(c2)
        cont.add(r)
        assert len(cont.items) == 3

        cont.remove_by_condition("area > 50")
        assert len(cont.items) == 2

    def test_remove_by_color(self):
        """Проверяет удаление по условию на цвет."""
        cont = Container()
        c2 = Circle(0, 0, 2, "желтый", "2024-01-02")
        r = Rectangle(0, 2, 2, 0, "синий", "2024-01-03")
        cont.add(c2)
        cont.add(r)

        cont.remove_by_condition("color == 'желтый'")
        assert len(cont.items) == 1
        assert cont.items[0] == r
