# Создайте функцию is_year_leap, принимающую 1 аргумент — год (число) — и возвращающую True, 
# если год високосный, и False — если иначе.
# Год високосный, если его номер делится на 4 без остатка. 
# Например, 2020 или 2008. 2009 или 2023 не делится на 4 без остатка, значит, год не високосный.

def is_year_leap(num_year):
    return True if (num_year % 4) == 0 else False


num_year = int(input("Введите год: "))
result = is_year_leap(num_year)
print(f"Год {num_year}: - {result}")
