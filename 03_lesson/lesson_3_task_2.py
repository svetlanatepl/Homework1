from smartphone import Smartphone

catalog = [
    Smartphone("Sumsung", "GalaxyS25", "+79501238569"),
    Smartphone("iPhone", "iPhone 11 Pro", "+79821197352"),
    Smartphone("Honor", "Honor Magic 7 Pro", "+79635354985"),
    Smartphone("Huawei", "Huawei Nova 14 Pro", "+79096542893"),
    Smartphone("Infinix", "Infinix GT 30 Pro", "+79123967412")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. "
          f"{smartphone.phone_number}")
