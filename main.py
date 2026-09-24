import sys
from figures import Circle, Container, Rectangle, Triangle

if sys.platform == "win32": # для русского языка
    sys.stdout.reconfigure(encoding="utf-8")


def process_file(filename):
    """Чтение команд из файла и их выполнение."""
    container = Container()

    print(f"\n--- Открытие файла: {filename} ---")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                line = line.strip()

                # Пропуск пустых строк и комментариев
                if not line or line.startswith("#"):
                    continue

                parts = line.split()
                cmd = parts[0].upper()

                if cmd == "ADD":
                    fig_type = parts[1]
                    try:
                        if fig_type in ("Circle", "Круг"):
                            # Формат: ADD Circle x y r color date
                            x = int(parts[2])
                            y = int(parts[3])
                            r = int(parts[4])
                            color = parts[5]
                            date = parts[6]
                            fig = Circle(x, y, r, color, date)
                            container.add(fig)
                            print(f"[Строка {line_no}] Добавлен: {fig}")

                        elif fig_type in ("Rectangle", "Прямоугольник"):
                            # Формат: ADD Rectangle x1 y1 x2 y2 color date
                            x1 = float(parts[2])
                            y1 = float(parts[3])
                            x2 = float(parts[4])
                            y2 = float(parts[5])
                            color = parts[6]
                            date = parts[7]
                            fig = Rectangle(x1, y1, x2, y2, color, date)
                            container.add(fig)
                            print(f"[Строка {line_no}] Добавлен: {fig}")

                        elif fig_type in ("Triangle", "Треугольник"):
                            # Формат: ADD Triangle x1 y1 x2 y2 x3 y3 color date
                            x1 = float(parts[2])
                            y1 = float(parts[3])
                            x2 = float(parts[4])
                            y2 = float(parts[5])
                            x3 = float(parts[6])
                            y3 = float(parts[7])
                            color = parts[8]
                            date = parts[9]
                            fig = Triangle(x1, y1, x2, y2, x3, y3, color, date)
                            container.add(fig)
                            print(f"[Строка {line_no}] Добавлен: {fig}")

                        else:
                            print(f"[Строка {line_no}] Ошибка: неизвестный тип фигуры '{fig_type}'")

                    except (IndexError, ValueError) as err:
                        print(f"[Строка {line_no}] Ошибка параметров фигуры: {err}")

                elif cmd == "REM":
                    # Условие — все, что идет после REM
                    condition = line[len(parts[0]):].strip()
                    container.remove_by_condition(condition)

                elif cmd == "PRINT":
                    container.print_all()

                else:
                    print(f"[Строка {line_no}] Неизвестная команда '{cmd}'")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден!")

    print(f"--- Завершена обработка файла: {filename} ---\n")


def main():
    # Если передан аргумент командной строки — читаем его, иначе input.txt
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    process_file(filename)


if __name__ == "__main__":
    main()
