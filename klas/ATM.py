from Person import Person
from os import system
from time import sleep

class ATM:
    __name="HAMKOR BANK"
    __limit=50000000
    
    def parol_tekshir(self,person:Person):
        count=0
        for i in range(4):
            if count==3:
                print("Bloklandingiz")
                exit()
            else:
                if person.card.get_parol()==int(input("Parolni kiriting:")):
                    print("tugri parol kiritildi")
                    sleep(3)
                    system("cls")
                    break
                else:
                    count+=1
                    print("notugri parol kiritdingiz!!!")
                    
        
    def get_naxt_pul(self):
        return self.__limit
        pass
    def limit_minus(self,nech_pul):
        self.__limit-=nech_pul
    
    def limit_plyus(self,nech_pul):
        self.__limit+=nech_pul

        
    