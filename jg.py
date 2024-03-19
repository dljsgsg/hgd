#1
def print_menu():
    print("Меню:")
    print("1. Отсортировать по идентификационным кодам")
    print("2. Отсортировать по номерам телефона")
    print("3. Вывести список пользователей с кодами и телефонами")
    print("4. Выход")


def sort_by_ids(ids, phone_numbers):
    sorted_data = sorted(zip(ids, phone_numbers))
    sorted_ids, sorted_phone_numbers = zip(*sorted_data)
    return list(sorted_ids), list(sorted_phone_numbers)


def sort_by_phone_numbers(ids, phone_numbers):
    sorted_data = sorted(zip(phone_numbers, ids))
    sorted_phone_numbers, sorted_ids = zip(*sorted_data)
    return list(sorted_ids), list(sorted_phone_numbers)


# Пример инициализации списков
ids = [101, 102, 103, 104]
phone_numbers = ["555-7789", "555-83978", "555-9865276", "555-5255254"]

while True:
    print_menu()
    choice = input("Выберите действие (1-4): ")

    if choice == '1':
        sorted_ids, sorted_phone_numbers = sort_by_ids(ids, phone_numbers)
        print("Список пользователей по идентификационным кодам:")
        for i in range(len(sorted_ids)):
            print(f"Код: {sorted_ids[i]}, Номер: {sorted_phone_numbers[i]}")

    elif choice == '2':
        sorted_ids, sorted_phone_numbers = sort_by_phone_numbers(ids, phone_numbers)
        print("Список пользователей по номерам телефонов:")
        for i in range(len(sorted_ids)):
            print(f"Код: {sorted_ids[i]}, Номер: {sorted_phone_numbers[i]}")

    elif choice == '3':
        print("Список пользователей с кодами и телефонами:")
        for i in range(len(ids)):
            print(f"Код: {ids[i]}, Номер: {phone_numbers[i]}")

    elif choice == '4':
        print("Выход из программы.")
        break

    else:
        print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 4.")
    #2


def print_menu():
    print("Меню:")
    print("1. Отсортировать по названию книг")
    print("2. Отсортировать по годам выпуска")
    print("3. Вывести список книг с названиями и годами выпуска")
    print("4. Выход")


def sort_by_titles(titles, release_years):
    sorted_data = sorted(zip(titles, release_years))
    sorted_titles, sorted_release_years = zip(*sorted_data)
    return list(sorted_titles), list(sorted_release_years)


def sort_by_years(titles, release_years):
    sorted_data = sorted(zip(release_years, titles))
    sorted_release_years, sorted_titles = zip(*sorted_data)
    return list(sorted_titles), list(sorted_release_years)


# Пример инициализации списков
titles = ["Война и мир", "Преступление и наказание", "Гордость и предубеждение"]
release_years = [1869, 1866, 1813]

while True:
    print_menu()
    choice = input("Выберите действие (1-4): ")

    if choice == '1':
        sorted_titles, sorted_release_years = sort_by_titles(titles, release_years)
        print("Список книг отсортированный по названию:")
        for i in range(len(sorted_titles)):
            print(f"Название: {sorted_titles[i]}, Год выпуска: {sorted_release_years[i]}")

    elif choice == '2':
        sorted_titles, sorted_release_years = sort_by_years(titles, release_years)
        print("Список книг отсортированный по годам выпуска:")
        for i in range(len(sorted_titles)):
            print(f"Название: {sorted_titles[i]}, Год выпуска: {sorted_release_years[i]}")

    elif choice == '3':
        print("Список книг с названиями и годами выпуска:")
        for i in range(len(titles)):
            print(f"Название: {titles[i]}, Год выпуска: {release_years[i]}")

    elif choice == '4':
        print("Выход из программы.")
        break

    else:
        print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 4.")
