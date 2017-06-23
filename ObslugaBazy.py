#-*- coding: utf-8 -*-
import pymysql
import datetime
import random
from CAdmin import CAdmin
from CRepairer import CRepairer
from CRequester import CRequester


class MenuDB(CAdmin,CRepairer,CRequester):
    
    def __init__(self):
        try:
            self.conn = pymysql.connect("localhost", "root", "Seb@stian1.", "projekt1")
            self.cursor = self.conn.cursor()
        except:
            print("Nie udało sie nawiazac polaczenia z baza")
        
        self.licznik=0
        self.proby=3  
        self.logowanie()           
               
    def logowanie(self):
        self.login = input("Podaj login: ")
        self.haslo = input("Podaj haslo: ")
        self.Locked=''
        self.rola = ''
        self.sql2 = 'SELECT * FROM logins WHERE login=%s AND password=%s'
        self.cursor.execute(self.sql2,(self.login, self.haslo))
        self.results = self.cursor.fetchall()
        
        for row in self.results:
            self.Locked = row[4]
            
        if(self.cursor.rowcount == 1 and self.Locked==False):
            
            
                print("Logowanie przebieglo pomyslnie")
            
                for row in self.results:
                    self.role = row[3]
                    self.rola= self.role
                    
                ###Repairer###############    
                if(self.rola == 'rep'):
                    CRepairer.repairer(self)       
                ####Reqester
                elif(self.rola == 'req'):
                    CRequester.requester(self)
                ####Admin    
                elif(self.rola == 'adm'):
                    CAdmin.Admin(self)
        elif(self.cursor.rowcount == 0):
                self.licznik=self.licznik+1
                self.proby=self.proby-1
                if(self.licznik<3):
                    print('blędne hasło lub login !!!! Zostało: '+str(self.proby))
                    self.logowanie()
                else:
                    CAdmin.BlockAccountAuto(self)
                    print("Konto zostało zablokowane")
        elif(self.Locked==True):
            print("Konto jest zablokowane proszę o kontakt z Administratorem @SebastianŻelazny")
            
o1 = MenuDB()            

