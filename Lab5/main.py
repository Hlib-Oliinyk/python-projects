from datetime import datetime

def task1():
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_primes(N):
        primes = []
        for i in range(N + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def format_result(primes, format):
        if format == 'list':
            return primes
        elif format == 'column':
            return '\n'.join(map(str, primes))
        elif format == 'count':
            return len(primes)
        else:
            return "Неправильний формат"

    def find_primes(n, output_format):
        primes = generate_primes(n)
        return format_result(primes, output_format)

    print("list:")
    print(find_primes(20, 'list'))
    print("\ncolumn:")
    print(find_primes(20, 'column'))
    print("\ncount:")
    print(find_primes(20, 'count'))


def task2():
    def process(element, categories, totals):
        if isinstance(element, list):
            for item in element:
                process(item, categories, totals)
        elif isinstance(element, dict):
            for key, value in element.items():
                if key not in categories:
                    categories.append(key)
                totals[key] = totals.get(key, 0) + value

    def analyze_nested_categories(data):
        categories = []
        totals = {}
        process(data, categories, totals)
        return (categories, totals)

    nested_data = [
        [
            {"офіс": 100},
            {"маркетинг": 200}
        ],
        [
            [
                {"офіс": 50},
                {"маркетинг": 150}
            ],
            {"офіс": 200}
        ],
        {"офіс": 300},
        [{"офіс": 100, "extra": 1}]
    ]

    result = analyze_nested_categories(nested_data)
    for i in result: print(i)


def task3():
    def analyze_clients(clients):
        status_count = {}
        invalid_emails = []
        new_clients = set()
        errors = []
        seen_emails = set()

        for client in clients:
            if not isinstance(client, tuple) or len(client) != 3:
                errors.append(client)
                continue

            name, status, email = client

            name_ok = isinstance(name, str) and name.strip()
            status_ok = isinstance(status, str) and status in {"новий", "постійний"}
            email_is_string = isinstance(email, str)
            email_not_empty = email_is_string and email.strip()
            email_has_at = email_is_string and "@" in email

            if not name_ok or not status_ok or not email_is_string or not email_not_empty:
                errors.append(client)

            if name_ok and status_ok and email_is_string:
                status_count[status] = status_count.get(status, 0) + 1
                if status == "новий":
                    new_clients.add(name)

                if email_not_empty and not email_has_at and email not in seen_emails:
                    invalid_emails.append(email)
                    seen_emails.add(email)
                elif not email_not_empty and email not in seen_emails:
                    invalid_emails.append(email)
                    seen_emails.add(email)

        return {
            "status_count": status_count,
            "invalid_emails": invalid_emails,
            "new_clients": list(new_clients),
            "errors": errors
        }

    result = analyze_clients([
        ("Іван", "новий", "ivan@email.com"),
        ("Олена", "постійний", "olena[at]mail.com"),
        ("", "новий", "ivan@email.com"),  # некоректне ім'я
        ("Олена", "", "olena[at]mail.com"),  # некоректний статус
        ("Іван", "новий", ""),  # некоректний email
        ("", "", ""),  # два некоректних поля (ім'я і статус)
        ("Петро", "", ""),  # два некоректних поля (статус і email)
        "не кортеж",  # невірний формат даних
        123,  # невірний формат даних
        None,  # невірний формат даних
        ("Олена",),  # невірний формат всередині кортежу
        ("Іван", "новий"),  # невірний формат всередині кортежу
        (123, "новий", "ivan@email.com"),  # невірний тип для імені
        ("Іван", 123, "ivan@email.com"),  # невірний тип для статусу
        ("Іван", "новий", 123),  # невірний тип для email
    ])

    print(f'status_count: {result["status_count"]},')
    print(f'invalid_emails: {result["invalid_emails"]},')
    print(f'new_clients: {result["new_clients"]},')
    print('errors:')
    for err in result["errors"]:
        print(f'{err}')


def task4():
    def is_valid_date(date_str, date_format="%Y-%m-%d"):
        try:
            datetime.strptime(date_str, date_format)
            return True
        except (ValueError, TypeError):
            return False

    def analyze_expenses(expenses):
        category_totals = {}
        max_expense = None
        invalid_dates = []
        errors = []
        seen_dates = set()

        for expense in expenses:
            if not isinstance(expense, tuple) or len(expense) != 3:
                errors.append(expense)
                continue

            amount, category, date = expense

            amount_ok = isinstance(amount, (int, float)) and amount is not None
            category_ok = isinstance(category, str) and category
            date_is_string = isinstance(date, str)
            date_valid = date_is_string and is_valid_date(date)

            if not amount_ok or not category_ok or not date_is_string:
                errors.append(expense)
            else:
                category_totals[category] = category_totals.get(category, 0) + amount

                if max_expense is None or amount > max_expense[0]:
                    max_expense = expense

                if not date_valid and date not in seen_dates:
                    invalid_dates.append(date)
                    seen_dates.add(date)

        return {
            "category_totals": category_totals,
            "max_expense": max_expense,
            "invalid_dates": invalid_dates,
            "errors": errors
        }

    result = analyze_expenses([
        (100, "офіс", "2024-06-01"),
        (200, "маркетинг", "2024-06-02"),
        (50, "офіс", "2024-13-01"),
        (None, "маркетинг", "2024-06-02"),  # некоректна сума
        (100, None, "2024-06-01"),  # некоректна категорія
        (100, "офіс", None),  # некоректна дата
        "не кортеж",  # невірний формат даних
        123,  # невірний формат даних
        None,  # невірний формат даних
        (100, "офіс"),  # невірний формат всередині кортежу
        (100,),  # невірний формат всередині кортежу
        (100, "офіс", "2024-06-01", "extra")  # зайвий елемент у кортежі
    ])

    print(f'category_totals: {result["category_totals"]},')
    print(f'max_expense: {result["max_expense"]},')
    print(f'invalid_dates: {result["invalid_dates"]},')
    print('errors:')
    for err in result["errors"]:
        print(f'{err}')


def task5():
    def filter_reports(reports, output_format, keyword):
        filtered_reports = []
        errors = []

        for report in reports:
            if not isinstance(report, tuple) or len(report) != 3:
                errors.append(report)
                continue

            name, author, format_type = report

            name_ok = isinstance(name, str) and name.strip()
            author_ok = isinstance(author, str) and author.strip()
            format_ok = isinstance(format_type, str) and format_type.strip()

            if not name_ok or not author_ok or not format_ok:
                errors.append(report)
            else:
                if format_type == output_format and (keyword in name or keyword in author):
                    filtered_reports.append(report)

        count = len(filtered_reports)

        return (filtered_reports, count, errors)

    result = filter_reports(
        [
            ("Звіт1", "Іван Іванов", "pdf"),
            ("Звіт2", "Олена Петрівна", "docx"),
            ("", "Іван Іванов", "pdf"),  # некоректна назва
            ("Звіт3", "", "pdf"),  # некоректний автор
            ("Звіт4", "Петро Сидоров", ""),  # некоректний формат
            "не кортеж",  # невірний формат даних
            123,  # невірний формат даних
            None,  # невірний формат даних
            ("Звіт5",),  # невірний формат всередині кортежу
            ("Звіт6", "Іван Іванов"),  # невірний формат всередині кортежу
            ("Звіт7", "Іван Іванов", 123),  # невірний тип для формату
        ],
        "pdf",
        "Іва"
    )

    print(f'{result[0]},')
    print(f'{result[1]},')

    for err in result[2]:
        print(f'{err}')

def main():
    while True:
        try:
            choice = int(input("Виберіть номер функції (0 - вихід): "))
            match choice:
                case 0:
                    break
                case 1:
                    task1()
                case 2:
                    task2()
                case 3:
                    task3()
                case 4:
                    task4()
                case 5:
                    task5()
                case _:
                    print("Функції з таким номером не має")
        except ValueError:
            print("Ви ввели не число")

if __name__ == "__main__":
    main()

