choosen =  input("apa yang anda ingin konversikan ?\nCelcius ke Fahrenheit (1)\nFahrenheit ke Celcius (2)\nPilih 1 atau 2 : ")

if choosen == "1" :
    celcius = input("masukan suhu celcius yang ingin dikonversikan : ")
    celcius = float(celcius)
    result = (celcius * 1.8) + 32
    print(f"{celcius} celcius sama dengan {result} fahrenheit")
elif choosen == "2" :
    fahrenheit = input("masukan suhu fahrenheit yang ingin dikonversikan : ")
    fahrenheit = float(fahrenheit)
    result = (fahrenheit - 32.0) * 5.0/9.0
    print(f"{fahrenheit} celcius sama dengan {result} fahrenheit")
else:
    print("hanya masukan pilihan 1 atau 2")