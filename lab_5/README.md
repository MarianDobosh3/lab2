number_to_word/  # Коренева папка проекту
    |- number_converter/  # Папка з пакетом для перетворення чисел на слова
    |   |- __init__.py  # Файл, що допомагає Python розпізнати цю папку як пакет
    |   |- converter.py  # Файл з логікою перетворення чисел на слова
    |- __init__.py  # Файл, що допомагає Python розпізнати цей проект як пакет
    |- main.py  # Основний файл програми
    |- requirements.txt  # Файл із списком необхідних пакетів
    |- README.md  # Файл з описом проекту і інструкціями

# number_converter/converter.py

def convert_number_to_word(number):
    """
    Перетворює задане число на словесне представлення.

    Args:
        number (int): Число, яке потрібно перетворити.

    Returns:
        str: Словесне представлення числа.
    """
    # Логіка перетворення числа на слово
    # ...

    return word

from number_converter.converter import convert_number_to_word

def main():
    name = input("Введіть своє ім'я: ")
    print(f"Привіт, {name}!")
    
    while True:
        number = input("Введіть число: ")
        
        try:
            number = int(number)  # перетворюємо введене значення на ціле число
            word = convert_number_to_word(number)  # викликаємо функцію для перетворення числа на словесне представлення
            print(f"{number} в словесному вигляді: {word}")
        except ValueError:
            print("Невірне введення. Будь ласка, спробуйте ще раз.")
        
        choice = input("Продовжити? (Y/N): ")
        if choice.lower() != 'y':
            break  # якщо користувач вводить "N", виходимо з циклу і завершуємо програму

if __name__ == "__main__":
    main()
