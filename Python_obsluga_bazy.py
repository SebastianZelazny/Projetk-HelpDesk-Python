#-*- coding: utf-8 -*-
import pymysql


class MenuDB:
    def __init__(self, login, haslo):
        self.conn = pymysql.connect("localhost", "root", "Seb@stian1.", "projekt1")
        self.cursor = self.conn.cursor()   						 
        self.login = login
        self.haslo = haslo
        self.logowanie()
    def logowanie(self):
        self.sql2 = 'SELECT * FROM logins WHERE login=%s AND password=%s'
        self.cursor.execute(self.sql2,(self.login, self.haslo))
        if(self.cursor.rowcount == 1):
            print('logowanie poprawne')
            self.i = input('Co robimy: (S)-select, (I)-insert,(U)-update,(D)-delete,(W)-widok ,(Q)-wyjście')
            if (self.i =='s'):
                self.odczyt()
                self.logowanie()
            elif(self.i == 'i'):
                self.wprowadzanie()
                self.odczyt()
                self.logowanie()
            elif(self.i=='u'):
                self.odczyt()
                self.update()
                self.odczyt()
                self.logowanie()
            elif(self.i=='d'):
                self.odczyt()
                self.delete()
                self.odczyt()
                self.logowanie()    
            elif(self.i=='w'):
                self.widok()
                self.logowanie()
            else:
                print('koniec')
        else:
            print('blad logowania')
    def wprowadzanie(self):   	 
        self.name = input('wprowadź imie: ')
        self.last = input('wprowadź nazwisko: ')
        self.date = input('wprowadź datę urodzenia: ')
        self.PESEL = input('wprowadź pesel: ')
        self.sql1 = "INSERT INTO empl (name, last, date, PESEL) VALUES (%s,%s,%s,%s)"
        self.cursor.execute(self.sql1,(self.name, self.last, self.date, self.PESEL))
        self.conn.commit()
    def odczyt(self):
        self.sql = "SELECT * FROM empl"   						 
        self.cursor.execute(self.sql)   						 
        self.results = self.cursor.fetchall()   					 
        print ("%5s%10s%15s%15s%15s" % ("ID","Name","Surname","Date","PESEL") )   		 
        for row in self.results:
            self.lp = row[0]
            self.name = row[1]
            self.last = row[2]
            self.date = row[3]
            self.PESEL = row[4]             	 
            print ("%5s%10s%15s%15s%15s" % (self.lp, self.name, self.last, self.date, self.PESEL))
            
    def update(self):
        self.lp = input("Podaj ID uzytkownika do modyfikacji: ")
        self.name = input("Zmien imie: ")
        self.last = input("Zmien nazwisko: ")
        self.sql3 = "UPDATE empl SET name=%s,last=%s WHERE lp =%s"
        self.cursor.execute(self.sql3,(self.name, self.last,self.lp))
        self.conn.commit()
    def delete(self):
        self.lp = input("Podaj ID uzytkownika do usuniecia: ")
        self.decyzja = input("Czy napewno chce usunac(t/n): ")        
        if(self.decyzja=='t'):
            self.sql4 = "DELETE FROM empl WHERE lp=%s"
            self.cursor.execute(self.sql4,(self.lp))            
            self.conn.commit()
        else:
            self.delete()
    def widok(self):
        self.sql5='SELECT * From info' 						 
        self.cursor.execute(self.sql5)   						 
        self.results = self.cursor.fetchall()   					 
        print ("%5s%10s" % ("Name","Surname") )   		 
        for row in self.results:
            self.name = row[0]
            self.surname = row[1]        	 
            print ("%5s%10s" % (self.name, self.surname))
        
o1 = MenuDB(input("Podaj login: "),input("Podaj haslo: "))
