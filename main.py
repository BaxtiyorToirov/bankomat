import sys
from os import system
from time import sleep

sys.path.append("./klas")

from klas.ATM import ATM
from klas.Card import Card1
from klas.Person import Person

if __name__=="__main__":
    card1=Card1(input("karta nomi:"),int(input("balansingizni kiriting:")),int(input("parolingizni kiriting:")))
    pr1=Person(input("ismingizni kiriting:"),card1,int(input("Naqd pulingiz qancha:")))
    kls=ATM()
    kls.parol_tekshir(pr1)


while True:
    print("1-Balansni tekshir kartanikini")
    print("2-Naqd pul yechish")
    print("3-Pin o'zgartirish")
    print("4-Kartaga pul qushish")
    print("5-chiqish")
    karta=int(input(">>>"))
    if karta==1:
        print(f"Sizning balansingiz -> {card1.get_balans()} so'm")
        print("0-Ortga qaytish")
        karta1=int(input(">>>"))
        system("cls")
        

    elif karta==2:
        print("Nech pul yechmoqchisiz?")
        kart2=int(input(">>>"))
        if kart2<=card1.get_balans() and kart2<=kls.get_naxt_pul():
            
             print("Surovingiz amalga oshirildi")
             card1.set_balans_minus(kart2)
             kls.limit_minus(kart2)
             pr1.karmon_plyus(kart2)
             print(f"""
             {kart2} so'm pul yechildi
             Balans:{card1.get_balans()} so'm""")
               
        else:
            print("Balansingizda bunday summa mavjud emas!!!")
        sleep(3)
        system("cls") 
    elif karta==3:
        card1.set_parol(input("Yangi parol:"))
        sleep(3)
           
    elif karta==4:
        qushish=int(input("qancha pul qushmoqchisiz?"))
        card1.set_balans_plyus(qushish)
        pr1.Karmon_minus(qushish)
        kls.limit_plyus(qushish)
        print(f"Sizning hozirgi balansingiz {card1.get_balans()}")
        sleep(3)
        system("cls")
    elif karta==5:
        print("Etiboringiz uchun rahmat!!!")
        exit()