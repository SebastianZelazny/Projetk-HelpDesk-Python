#-*- coding: utf-8 -*-
import pymysql
import datetime
import random

class MenuDB:
    def __init__(self, login, haslo):
        self.conn = pymysql.connect("localhost", "root", "Seb@stian1.", "projekt1")
        self.cursor = self.conn.cursor()   						 
        self.login = login
        self.haslo = haslo
        self.logowanie()
        
    def logowanie(self):
        self.rola = ''
        self.sql2 = 'SELECT * FROM logins WHERE login=%s AND password=%s'
        self.cursor.execute(self.sql2,(self.login, self.haslo))
        self.results = self.cursor.fetchall()
        
        for row in self.results:
            self.role = row[3]
            self.rola= self.role
            
        ###Repairer###############    
        if(self.cursor.rowcount == 1 and (self.rola == 'rep')):
            self.repairer()       
        ####Reqester
        elif((self.cursor.rowcount == 1) and (self.rola == 'req')):
            self.requester()
        ####Admin    
        elif((self.cursor.rowcount == 1) and (self.rola == 'adm')):
            self.Admin()
        else:
            print('blad logowania')
            
            
    def requester(self):
        print('logowanie poprawne reqester')
        self.i = input('Co chcesz zrobić: \n 1.-Dodaj zgłoszenie \n 2. Podejrzj zgłoszenie \n(Q)-wyjście \n Wybor: ')
        if(self.i == '1'):
            print("Dodaje zgłoszenie")
            self.list_of_repairers()
            self.AddReports()
            self.logowanie()
        elif(self.i == '2'):
            print("Wyswietlam zgłoszenie")         
            self.ShowReportsReq()         
        elif((self.i == 'q') or (self.i == 'Q')):
            print("Koniec")
        else:
            print("Podano zły znak proszę wybrać (1,2,q)")
            self.requester()
            
    def Admin(self): ##Do dokonczenia 
        print('Logowanie poprawne Admin')
        self.i = input('Co robimy: (S)-select, (I)-insert,(U)-update,(D)-delete,(W)-widok ,(Q)-wyjście')         
        
    def repairer(self):
        print('logowanie poprawne repairer')
        self.i = input('Co robimy: \n (1)-Wyświetl Zgłoszenia, \n (2)-Podejrzyj swoje zgłoszenia, \n (3)-Zamknij zgłoszenie, \n (4)-Zaktualizuj zgłoszenie, \n (5)-Usun zgłoszenie, \n (Q)-wyjście \n Wybór: ')
        if (self.i =='1'):         
            self.ShowAllReports()
            self.logowanie()        
        elif(self.i == '2'):     
            self.ShowReportsRep()
            self.logowanie()
        elif(self.i=='3'):
            self.ShowAllReports()
            self.CloseReport()
            self.logowanie()
        elif(self.i=='4'):
            self.ShowAllReports()
            self.UpdateReport()
            self.logowanie()    
        elif(self.i=='5'):
            self.ShowAllReports()
            self.DeleteReport()
            self.logowanie()
        elif(self.i=='q' or self.i=='Q'):
            print('koniec')
        else:
            print("Podałeś/aś nieprawidłową wartość wybierz 1,2,3,4,5,Q")
            self.repairer()
        
        
    def list_of_repairers(self):
        self.Lista=[]
        self.sql = "SELECT * FROM list_of_repairers"   						 
        self.cursor.execute(self.sql)   						 
        self.results = self.cursor.fetchall()   					 
        #print ("%1s" % ("Logins") )
        for row in self.results:
            self.Login1 = row[0]
            self.Lista.append(self.Login1)    
        #print(self.logrep)             
            
    def AddReports(self):
        self.list_of_repairers()
        self.title = input("Podaj tytul Zgłoszenia: ")
        self.descr = input("Podaj opis zgłoszenia: ")
        self.logreq = input("Podaj swój login: ")
        self.logrep = random.choice(self.Lista)
        #print(self.logrep)
        self.data=datetime.date.today()
        #print(self.data)
        self.prior = input("Podaj Priorytet: ") 
        self.sql5 = "INSERT INTO reports (Title, description,Requester,Priority) VALUES (%s,%s,%s,%s)"
        self.cursor.execute(self.sql5(self.title,self.descr,self.logreq,str(self.prior)))
        self.conn.commit()
        
    def ShowReportsReq(self):   
        
        self.sql6 = "SELECT ID_Z,Title,description,priority_p,E_mail_rep,E_mail_req,Status_s,Data_R FROM view_request_how_requester WHERE Login=%s"   						 
        self.cursor.execute(self.sql6,(self.login))
        self.results = self.cursor.fetchall() 					 
        print ("%5s%40s%40s%15s%25s%25s%15s%15s" % ("ID","Title","Description","Priorytet","E_mail_rep","E-mail_req","Status","Data"))
        for row in self.results:
            self.lp = row[0]
            self.Title = row[1]
            self.description = row[2]
            self.priority = row[3]
            self.repairerr = row[4]
            self.requesterr = row[5]
            self.Status = row[6]
            self.Data_R = row[7]
            print ("%5s%40s%40s%15s%25s%25s%15s%15s" % (self.lp, self.Title, self.description,self.priority,self.repairerr,self.requester,self.Status,self.Data_R,))
    
    def ShowReportsRep(self):
        self.sql7 = "SELECT ID_Z,Title,description,priority_p,E_mail_rep,E_mail_req,Status_s,Data_R FROM view_request_how_repairer WHERE Login=%s"
        self.cursor.execute(self.sql7,(self.login))
        self.results=self.cursor.fetchall()
        print ("%5s%40s%40s%15s%25s%25s%15s%15s" % ("ID","Title","Description","Priorytet","E_mail_rep","E-mail_req","Status","Data"))
        for row in self.results:
            self.lp = row[0]
            self.Title = row[1]
            self.description = row[2]
            self.priority = row[3]
            self.repairerr = row[4]
            self.requesterr = row[5]
            self.Status = row[6]
            self.Data_R = row[7]
            print ("%5s%40s%40s%15s%25s%25s%15s%15s" % (self.lp, self.Title, self.description,self.priority,self.repairerr,self.requesterr,self.Status,self.Data_R,))     
            
    def ShowAllReports(self):
        self.sql8 = "SELECT ID_Z,Title,description,priority_p,E_mail_rep,E_mail_req,Status_s,Data_R FROM view_request_how_repairer"
        self.cursor.execute(self.sql8)
        self.results=self.cursor.fetchall()
        print ("%5s%40s%40s%15s%25s%25s%15s%15s" % ("ID","Title","Description","Priorytet","E_mail_rep","E-mail_req","Status","Data"))
        for row in self.results:
            self.lp = row[0]
            self.Title = row[1]
            self.description = row[2]
            self.priority = row[3]
            self.repairerr = row[4]
            self.requesterr = row[5]
            self.Status = row[6]
            self.Data_R = row[7]
            print ("%5s%40s%40s%15s%25s%25s%15s%15s" % (self.lp, self.Title, self.description,self.priority,self.repairerr,self.requesterr,self.Status,self.Data_R,))  
            
    def CloseReport(self):
        self.ID = input("Podaj ID Zgłoszenia do zamknięcia: ")
        self.status_z = input("Zmien Status : (3-Zamknięte )")
        if(self.status_z=='1' or self.status_z=='2' or self.status_z=='3'):
            self.sql3 = "UPDATE reports SET Status=%s WHERE ID_Z=%s"
            self.cursor.execute(self.sql3,(self.status_z,self.ID))
            self.conn.commit()
            print("Status zmieniono pomyślnie")
        else:
            print("Podano zły parametr dozwolone 1,2,3")
            self.CloseReport()
       
        
    def UpdateReport(self):
        self.ID = input("Podaj ID Zgłoszenie do Update: ")
        self.title = input("Podaj Tytul: ")
        self.description = input("Podaj opis: ")    
        self.priority = input("Podaj Priorytet: ")
        if(self.priority=="1" or self.priority=="2" or self.priority=="3" or self.priority=="4"):
            self.status_z = input("Zmien Status(1-Oczekuje, 2-W realizacji, 3-Zamknięte ):  ")
            if(self.status_z=='1' or self.status_z=='2' or self.status_z=='3'):
                self.sql9 = "UPDATE reports SET Title=%s,description=%s,Status=%s,priority=%s WHERE ID_Z=%s"
                self.cursor.execute(self.sql9,(self.title, self.description,self.status_z,self.priority,self.ID))
                self.conn.commit() 
                print("Update przeszedł pomyślnie")
            else:
                print("Podano zły parametr(dozwolone 1,2,3")
                self.UpdateReport()
        else:
            print("Podano zły parametr dozwolone 1,2,3,4")
            self.UpdateReport()
        
        
    def DeleteReport(self):
        self.lp = input("Podaj ID Zgłoszenia do usuniecia: ")
        self.decyzja = input("Czy napewno chce usunac(t/n): ")        
        if(self.decyzja=='t'):
            self.sql10 = "DELETE FROM reports WHERE ID_Z=%s"
            self.cursor.execute(self.sql10,(self.lp))            
            self.conn.commit()
            print("Usunięto prawidłowo")
        else:
            self.DeleteReport()
        
        
 
 
 
       
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
