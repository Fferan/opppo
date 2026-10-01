"""Тесты классов геометрических фигур."""

import math
import pytest
from figures import Figure, Circle, Rectangle, Triangle


class TestFigureBase:
    """Тесты базового класса Figure."""

    def test_base_area_returns_zero(self):
        """Базовый класс возвращает площадь 0."""
        fig = Figure("красный", "2024-01-01")
        assert fig.area() == 0.0

    def test_base_perimeter_returns_zero(self):
        """Базовый класс возвращает периметр 0."""
        fig = Figure("красный", "2024-01-01")
        assert fig.perimeter() == 0.0

    def test_base_str_contains_figure(self):
        """Строковое представление базового класса содержит [Фигура]."""
        fig = Figure("красный", "2024-01-01")
        assert "[Фигура]" in str(fig)

    def test_base_stores_color_and_date(self):
        """Базовый класс сохраняет цвет и дату."""
        fig = Figure("зеленый", "2024-05-10")
        assert fig.color == "зеленый"
        assert fig.date == "2024-05-10"


class TestCircle:
    """Тесты класса Circle."""

    def test_area(self):
        """Площадь круга с радиусом 5."""
        c = Circle(0, 0, 5, "красный", "2024-01-01")
        assert math.isclose(c.area(), math.pi * 25)

    def test_area_unit_radius(self):
        """Площадь единичного круга (r=1)."""
        c = Circle(0, 0, 1, "синий", "2024-01-01")
        assert math.isclose(c.area(), math.pi)

    def test_perimeter(self):
        """Периметр круга с радиусом 5."""
        c = Circle(0, 0, 5, "красный", "2024-01-01")
        assert math.isclose(c.perimeter(), 2 * math.pi * 5)

    def test_str_contains_circle(self):
        """Строковое представление содержит [Круг]."""
        c = Circle(1, 2, 3, "синий", "2024-01-01")
        result = str(c)
        assert "[Круг]" in result
        assert "Радиус: 3" in result

    def test_zero_radius_raises(self):
        """Нулевой радиус вызывает ValueError."""
        with pytest.raises(ValueError):
            Circle(0, 0, 0, "красный", "2024-01-01")

    def test_negative_radius_raises(self):
        """Отрицательный радиус вызывает ValueError."""
        with pytest.raises(ValueError):
            Circle(0, 0, -5, "красный", "2024-01-01")


class TestRectangle:
    """Тесты класса Rectangle."""

    def test_area(self):
        """Площадь прямоугольника 6x4 = 24."""
        r = Rectangle(0, 4, 6, 0, "зеленый", "2024-02-01")
        assert math.isclose(r.area(), 24.0)

    def test_perimeter(self):
        """Периметр прямоугольника 2*(6+4) = 20."""
        r = Rectangle(0, 4, 6, 0, "зеленый", "2024-02-01")
        assert math.isclose(r.perimeter(), 20.0)

    def test_reversed_coords(self):
        """Прямоугольник с 'перевёрнутыми' координатами (x2 < x1)."""
        r = Rectangle(6, 0, 0, 4, "синий", "2024-02-01")
        assert math.isclose(r.area(), 24.0)

    def test_str_contains_rectangle(self):
        """Строковое представление содержит [Прямоугольник]."""
        r = Rectangle(0, 4, 6, 0, "зеленый", "2024-02-01")
        assert "[Прямоугольник]" in str(r)

    def test_degenerate_zero_width_raises(self):
        """Вырожденный прямоугольник (нулевая ширина) вызывает ValueError."""
        with pytest.raises(ValueError):
            Rectangle(0, 0, 0, 5, "красный", "2024-01-01")

    def test_degenerate_zero_height_raises(self):
        """Вырожденный прямоугольник (нулевая высота) вызывает ValueError."""
        with pytest.raises(ValueError):
            Rectangle(0, 0, 5, 0, "красный", "2024-01-01")


class TestTriangle:
    """Тесты класса Triangle."""

    def test_area(self):
        """Площадь прямоугольного треугольника 3-4-5 = 6."""
        t = Triangle(0, 0, 3, 0, 0, 4, "синий", "2024-03-01")
        assert math.isclose(t.area(), 6.0)

    def test_perimeter(self):
        """Периметр прямоугольного треугольника 3+4+5 = 12."""
        t = Triangle(0, 0, 3, 0, 0, 4, "синий", "2024-03-01")
        assert math.isclose(t.perimeter(), 12.0)

    def test_str_contains_triangle(self):
        """Строковое представление содержит [Треугольник]."""
        t = Triangle(0, 0, 3, 0, 0, 4, "синий", "2024-03-01")
        assert "[Треугольник]" in str(t)

    def test_collinear_points_raises(self):
        """Три точки на одной прямой вызывают ValueError."""
        with pytest.raises(ValueError):
            Triangle(0, 0, 1, 1, 2, 2, "красный", "2024-01-01")

    def test_equilateral_area(self):
        """Площадь равностороннего треугольника со стороной 2."""
        # Равносторонний треугольник: (0,0), (2,0), (1, sqrt(3))
        h = math.sqrt(3)
        t = Triangle(0, 0, 2, 0, 1, h, "белый", "2024-01-01")
        expected = (math.sqrt(3) / 4) * 4  # формула: (sqrt(3)/4) * a^2
        assert math.isclose(t.area(), expected, rel_tol=1e-9)
