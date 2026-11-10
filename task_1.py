from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()

        today = datetime.today().date()

        difference = today - input_date

        return difference.days

    except ValueError:
        return "Некоректно введена дата. Використовуйте формат РРРР-ММ-ДД."

user_date = input("Введіть дату у форматі РРРР-ММ-ДД: ")

result = get_days_from_today(user_date)

print(f"Кількість днів між заданою датою та поточною: {result}")
