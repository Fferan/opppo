import math
import sys
from figures import Circle, Container, Rectangle, Triangle

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


def test_figures():
    # 1. Тест круга
    c = Circle(0, 0, 5, "красный", "2024-01-01")
    assert math.isclose(c.area(), math.pi * 25), "Неверная площадь круга"
    assert math.isclose(c.perimeter(), 2 * math.pi * 5), "Неверный периметр круга"

    # 2. Тест прямоугольника
    r = Rectangle(0, 4, 6, 0, "зеленый", "2024-02-01")
    assert math.isclose(r.area(), 24.0), "Неверная площадь прямоугольника"
    assert math.isclose(r.perimeter(), 20.0), "Неверный периметр прямоугольника"

    # 3. Тест треугольника
    t = Triangle(0, 0, 3, 0, 0, 4, "синий", "2024-03-01")
    assert math.isclose(t.area(), 6.0), "Неверная площадь треугольника"
    assert math.isclose(t.perimeter(), 12.0), "Неверный периметр треугольника"

    print("[OK] Тесты классов геометрических фигур пройдены.")


def test_container():
    cont = Container()
    c1 = Circle(0, 0, 5, "красный", "2024-01-01")     # S ~ 78.54
    c2 = Circle(0, 0, 2, "желтый", "2024-01-02")      # S ~ 12.57
    r = Rectangle(0, 2, 2, 0, "синий", "2024-01-03")  # S = 4.0

    cont.add(c1)
    cont.add(c2)
    cont.add(r)
    assert len(cont.items) == 3, "Ошибка добавления в контейнер"

    # Удаление по условию
    cont.remove_by_condition("area > 50")
    assert len(cont.items) == 2, "Ошибка удаления по площади"

    cont.remove_by_condition("color == 'желтый'")
    assert len(cont.items) == 1, "Ошибка удаления по цвету"
    assert cont.items[0] == r

    print("[OK] Тесты контейнера и условий удаления пройдены.")


if __name__ == "__main__":
    test_figures()
    test_container()
    print("\n>>> Все проверки успешно пройдены! <<<")
