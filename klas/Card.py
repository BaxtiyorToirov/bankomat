
class Card1:
    def __init__(self,name,balans,parol):
        self.name=name
        self.__balans=balans
        self.__parol=parol
    
    def get_balans(self):
        return self.__balans
        pass
    def set_balans_minus(self,nech_pul:int):
        self.__balans-=nech_pul

    def set_balans_plyus(self,nech_pul:int):
        self.__balans+=nech_pul

    def get_parol(self):
        return(self.__parol)
        pass
    def set_parol(self,new_parol:int):
        self.__parol=new_parol
        print("parol uzgardi")
            
    
