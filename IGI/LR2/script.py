# script.py
import os
import sys
import circle
import square

def main():
    # Получаем тип фигуры из переменной окружения, по умолчанию 'circle'
    figure = os.getenv('FIGURE', 'circle').lower()
    
    try:
        if figure == 'circle':
            radius = float(os.getenv('RADIUS', 0))
            if radius <= 0:
                raise ValueError("Radius must be positive")
            area = circle.area(radius)
            perimeter = circle.perimeter(radius)
            print(f"Circle (radius={radius}):")
            
        elif figure == 'square':
            side = float(os.getenv('SIDE', 0))
            if side <= 0:
                raise ValueError("Side must be positive")
            area = square.area(side)
            perimeter = square.perimeter(side)
            print(f"Square (side={side}):")
            
        elif figure == 'rectangle':
            side_a = float(os.getenv('SIDE_A', 0))
            side_b = float(os.getenv('SIDE_B', 0))
            if side_a <= 0 or side_b <= 0:
                raise ValueError("Sides must be positive")
            # В репозитории нет отдельного файла для прямоугольника,
            # но для примера можно использовать формулу из документации
            area = side_a * side_b
            perimeter = 2 * (side_a + side_b)
            print(f"Rectangle (side_a={side_a}, side_b={side_b}):")
        else:
            print(f"Unknown figure: {figure}")
            print("Supported: circle, square, rectangle")
            sys.exit(1)
            
        print(f"  Area: {area}")
        print(f"  Perimeter: {perimeter}")
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
