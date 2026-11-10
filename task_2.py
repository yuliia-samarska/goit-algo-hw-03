import random

def get_numbers_ticket(min, max, quantity):
   
  if not (1 <= min <= max <= 100):
        return []
   
  if not (1 <= quantity <= max - min + 1):
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)

number_range = input("Введіть бажаний діапазон чисел від 1 до 100 у форматі min-max: ")

if number_range.count("-") == 1:
    min_number, max_number = number_range.split("-")

    if min_number.isdigit() and max_number.isdigit():
        min_number = int(min_number)
        max_number = int(max_number)

        quantity = input("Скільки чисел потрібно згенерувати? ")

        if quantity.isdigit():
            quantity = int(quantity)

            lottery_numbers = get_numbers_ticket(min_number, max_number, quantity)

            if lottery_numbers:
                print(f"Ваші лотерейні числа: {lottery_numbers}")
            else:
                print("Помилка. Перевірте введені параметри.")
        else:
            print("Помилка. Кількість повинна бути цілим додатним числом.")
    else:
        print("Помилка. Введіть два цілих додатних числа через дефіс.")
else:
    print("Помилка. Використовуйте формат min-max, наприклад 1-65.")
