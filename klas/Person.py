from Card import Card1

class Person:
    def __init__(self,name:str,card:Card1,karmon:int):
        self.name=name
        self.card=card
        self.karmon=karmon
        
    def Karmon_minus(self,nech_pul):
        self.karmon-=nech_pul

    def karmon_plyus(self,nech_pul):
        self.karmon+=nech_pul




