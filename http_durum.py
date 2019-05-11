import requests



def http_durum():

    with open("siteler.txt", "r", encoding="utf-8") as file:
        siteler = [i.replace('\n', '') for i in file.readlines()]
        for i in siteler:

                try:
                    response = requests.get(i)

                    if response.status_code == 200:
                        with open("200.txt", "w", encoding="utf-8") as file2:
                            file2.write(i)

                    elif response.status_code == 404:
                        with open("404.txt", "w", encoding="utf-8") as file3:
                            file3.write(i)

                    elif response.status_code == 500:
                        with open("500.txt", "w", encoding="utf-8") as file4:
                            file4.write(i)

                except (ConnectionError and requests.exceptions.ConnectionError) as hata:
                    print("Sitelere erişilemedi..")


print(""""
HTTP DURUM BELİRLEYİCİ - TEGİN
""")

işlem = input ("İşlem yapmak istiyorsanız 'durum' yazınız: ")

if (işlem == "durum"):
    http_durum()
