import math


class Figure:
    """Базовый класс геометрической фигуры."""

    def __init__(self, color, date):
        self.color = str(color)
        self.date = str(date)

    def area(self):
        """Метод вычисления площади (переопределяется в наследниках)."""
        return 0.0

    def perimeter(self):
        """Метод вычисления периметра (переопределяется в наследниках)."""
        return 0.0


class Circle(Figure):
    """Класс Круг: целочисленный центр (x, y) и целочисленный радиус r."""

    def __init__(self, x, y, r, color, date):
        super().__init__(color, date)
        self.x = int(x)
        self.y = int(y)
        self.r = int(r)
        if self.r <= 0:
            raise ValueError("Радиус круга должен быть положительным")

    def area(self):
        return math.pi * (self.r ** 2)

    def perimeter(self):
        return 2 * math.pi * self.r

    def __str__(self):
        return (
            f"[Круг] Центр: ({self.x}, {self.y}), Радиус: {self.r} | "
            f"Цвет: {self.color} | Дата: {self.date} | "
            f"Площадь: {self.area():.2f} | Периметр: {self.perimeter():.2f}"
        )


class Rectangle(Figure):
    """Класс Прямоугольник: дробные координаты левого верхнего и правого нижнего углов."""

    def __init__(self, x1, y1, x2, y2, color, date):
        super().__init__(color, date)
        self.x1 = float(x1)
        self.y1 = float(y1)
        self.x2 = float(x2)
        self.y2 = float(y2)
        self.width = abs(self.x2 - self.x1)
        self.height = abs(self.y1 - self.y2)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return (
            f"[Прямоугольник] Углы: ({self.x1}, {self.y1})-({self.x2}, {self.y2}) "
            f"(размер: {self.width:.2f}x{self.height:.2f}) | "
            f"Цвет: {self.color} | Дата: {self.date} | "
            f"Площадь: {self.area():.2f} | Периметр: {self.perimeter():.2f}"
        )


class Triangle(Figure):
    """Класс Треугольник: дробные координаты трех вершин."""

    def __init__(self, x1, y1, x2, y2, x3, y3, color, date):
        super().__init__(color, date)
        self.x1 = float(x1)
        self.y1 = float(y1)
        self.x2 = float(x2)
        self.y2 = float(y2)
        self.x3 = float(x3)
        self.y3 = float(y3)

        # Вычисляем длины трех сторон по теореме Пифагора
        self.side_a = math.hypot(self.x2 - self.x1, self.y2 - self.y1)
        self.side_b = math.hypot(self.x3 - self.x2, self.y3 - self.y2)
        self.side_c = math.hypot(self.x1 - self.x3, self.y1 - self.y3)

    def area(self):
        # Площадь треугольника по координатам вершин (формула Гаусса)
        return 0.5 * abs(
            self.x1 * (self.y2 - self.y3)
            + self.x2 * (self.y3 - self.y1)
            + self.x3 * (self.y1 - self.y2)
        )

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def __str__(self):
        return (
            f"[Треугольник] Вершины: ({self.x1}, {self.y1}), ({self.x2}, {self.y2}), ({self.x3}, {self.y3}) | "
            f"Цвет: {self.color} | Дата: {self.date} | "
            f"Площадь: {self.area():.2f} | Периметр: {self.perimeter():.2f}"
        )


class Container:
    """Контейнер для хранения фигур."""

    def __init__(self):
        self.items = []

    def add(self, figure):
        """Добавить фигуру в контейнер."""
        self.items.append(figure)

    def print_all(self):
        """Вывести все фигуры на экран."""
        if not self.items:
            print("Контейнер пуст.")
            return

        print("=" * 75)
        print(f"Список фигур в контейнере (всего: {len(self.items)}):")
        print("=" * 75)
        for i, fig in enumerate(self.items, 1):
            print(f"{i}. {fig}")
        print("=" * 75)

    def remove_by_condition(self, condition):
        """
        Удаляет фигуры, удовлетворяющие условию (например: area > 20 или color == 'красный').
        """
        remaining = []
        removed = []

        for fig in self.items:
            # Создаем контекст с переменными фигуры для проверки условия
            context = {
                "area": fig.area(),
                "perimeter": fig.perimeter(),
                "color": fig.color,
                "date": fig.date,
                "type": type(fig).__name__,
                "r": getattr(fig, "r", 0),
                "width": getattr(fig, "width", 0),
                "height": getattr(fig, "height", 0),
            }
            try:
                # Если условие истинно — фигура удаляется
                if eval(condition, {}, context):
                    removed.append(fig)
                else:
                    remaining.append(fig)
            except Exception:
                # Если в условии опечатка или свойство отсутствует — фигуру не удаляем
                remaining.append(fig)

        self.items = remaining
        print(f"Команда REM [{condition}]: удалено {len(removed)} объект(ов).")
        for r in removed:
            print(f"  -> Удален: {r}")
