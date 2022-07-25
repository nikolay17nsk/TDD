from dadata import Dadata
from SQL_osn import vh, otvet, exit_1

token = input("Введите token => ")
secret = input("Введите API ключ => ")
language = input("Введите язык ответ ru или en => ")
if language != "ru" and language != "en":    
    language = "ru"
else:
    pass
print("!!!Для выхода введите exit!!! ")
try:
    vh(token, secret, language)
    #print(otvet()[0][0])

    def osn():    
        otv = otvet()
        token = otvet()[0][0]
        secret = otvet()[0][1]
        lan = otvet()[0][2]
        
        while True:
            value = input("Ввидите адрес => ")
            osn = []
            if value == "exit":
                exit_1()
                break
            else:
                
                dadata = Dadata(token, secret)
                result = dadata.suggest(name="address", query=value, language=lan, count=20)
                x = 0

                for i in result:
                    x =x + 1
                    osn.append(i['value'])

                    
                    print(f"№{x} => {i['value']}")
                

                y = input("Введите номер подходего адреса цифрой => ")
                if y == "exit":
                    exit_1()
                    break
                else:
                    print(y)
                    a = int(y)
                    #print(a)
                    


                    result = dadata.clean("address", osn[a - 1])
                    print(result["result"])
                    print(f"Широта {result['geo_lat']}, Долгота {result['geo_lon']} ")
except Exception as e:
    print(f"Произошла ошибка => {e}")     

if __name__ == '__main__':
    osn()
