from datetime import datetime

def get_days_from_today(date):

    if len(date) != 10 or date[4] != "-" or date[7] != "-":
        return "Неправильний формат дати. Використовуйте РРРР-ММ-ДД."

    year, month, day = date.split("-")

    if not (year.isdigit() and len(year) == 4 and
            month.isdigit() and len(month) == 2 and
            day.isdigit() and len(day) == 2):
        return "Неправильний формат дати. Використовуйте РРРР-ММ-ДД."

    input_date = datetime.strptime(date, "%Y-%m-%d").date()
    today_date = datetime.today().date()

    difference = today_date - input_date

    return difference.days


user_date = input("Введіть дату у форматі РРРР-ММ-ДД: ")

result = get_days_from_today(user_date)

print(f"Кількість днів між заданою та поточною датами: {result}")
