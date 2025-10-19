from address import Address
from mailing import Mailing

# Создаём адреса
to_address = Address("427960", "Сарапул", "Интернациональная", "57", "25")
from_address = Address("426035", "Ижевск", "Красногеройская", "109", "114")


# Создаём экземпляр класса Mailing
mailing = Mailing(to_address, from_address, 1000, "35005145009747")

# Выводим информацию
print(mailing)
