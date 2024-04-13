import sqlite3

# Перевірка наявності таблиці і її створення, якщо вона ще не існує
def create_table():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            name TEXT PRIMARY KEY,
            available BOOLEAN
        )
    ''')
    conn.commit()
    conn.close()

# Функція для перевірки наявності книги
def search(name):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT available FROM books WHERE name = ?', (name,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return True
    else:
        return False

# Функція для додавання книги
def add_book(name):
    if not search(name):
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (name, available) VALUES (?, ?)', (name, 1))
        conn.commit()
        conn.close()
        print(f"Ви додали книгу {name}")
    else:
        print(f"Книга {name} вже існує в базі даних")

# Функція для видалення книги
def remove_book(name):
    if search(name):
        conn = sqlite3.connect('books.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE name = ?', (name,))
        conn.commit()
        conn.close()
        print(f"Ви прибрали книгу {name}")
    else:
        print(f"Книги {name} відсутня в базі даних")

def show_all_books():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    # Виконання запиту для отримання всіх книг
    cursor.execute('SELECT name FROM books')
    
    # Отримання результатів запиту
    books = cursor.fetchall()

    # Виведення всіх книг
    if books:
        print("Наявні книги:")
        for book in books:
            print(book[0])
    else:
        print("У базі даних немає жодної книги")

    # Закриття підключення
    conn.close()


# Основна функція для взаємодії з користувачем
def main():
    create_table()
    request = input("Введіть 'add', 'remove', 'search' або 'stop': ").strip().lower()
    while request != 'stop':
        if request == 'add':
            book_name = input("Введіть назву книги для додавання: ").strip()
            add_book(book_name)
        elif request == 'remove':
            book_name = input("Введіть назву книги для видалення: ").strip()
            remove_book(book_name)
        elif request == 'search':
            book_name = input("Введіть назву книги для пошуку: ").strip()
            if search(book_name):
                print("Така книга вже є!")
            else:
                print("Такої книги в нас немає")
        elif request== 'show':
            show_all_books()
        else:
            print("Невідома команда. Будь ласка, спробуйте ще раз.")
        request = input("Введіть 'add', 'remove', 'search' або 'stop': ").strip().lower()

if __name__ == "__main__":
    main()
