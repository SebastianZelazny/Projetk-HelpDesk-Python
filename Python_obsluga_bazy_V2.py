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
        
        if(self.Locked==False):            
            if(self.cursor.rowcount == 1):
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
            else:
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
        else:
            print("Podany login nie istnieje w bazie")
            self.logowanie()
            
o1 = MenuDB()            
"""            
    def ID_login_rep(self):
        self.ID_log=""
        
        self.sql12 ="SELECT * FROM repairers left join logins on repairers.ID_Login_rep=logins.ID_L where logins.login=%s"
        self.cursor.execute(self.sql12,(self.login))  
        self.results = self.cursor.fetchall()   					 
        
        for row in self.results:
            self.ID_log = row[0]
        
        print("Wyciagniety ID LOG: "+str(self.ID_log))
        
    def ID_login_req(self):
        self.ID_log=""
        
        self.sql15 ="SELECT * FROM requester left join logins on requester.ID_Login_req=logins.ID_L where logins.login=%s"
        self.cursor.execute(self.sql15,(self.login))  
        self.results = self.cursor.fetchall()   					 
        
        for row in self.results:
            self.ID_log = row[0]
        
        print("Wyciagniety ID LOG: "+str(self.ID_log))                             
        
        
    def requester(self):
        print('logowanie poprawne reqester')
        self.i = input('Co chcesz zrobić: \n 1.-Dodaj zgłoszenie \n 2. Podejrzj zgłoszenie \n 3.Otwrzo ponownie zgłoszenie \n(Q)-wyjście \n Wybor: ')
        if(self.i == '1'):
            print("Dodaje zgłoszenie")
            self.list_of_repairers()
            self.AddReports()
            self.logowanie()
        elif(self.i == '2'):
            print("Wyswietlam zgłoszenie")         
            self.ShowReportsReq()
            self.logowanie()
        elif(self.i=='3'):
            print("Otwieram zgłoszenie")
            self.ShowReportsReq()
            self.OpenReport()
            self.logowanie()
        elif((self.i == 'q') or (self.i == 'Q')):
            print("Koniec")
        else:
            print("Podano zły znak proszę wybrać (1,2,q)")
            self.requester()
            
    def Admin(self): 
        print('Logowanie poprawne Admin')
        self.i = input('Co robimy: \n (1)-Operacje na uzytkownikach, \n (2)-Operacje na zgłoszeniach, \n (3)-Operacje na systemie, \n (Q)-wyjście \n Wybór: ')
        if(self.i=='1'):
            print("Przelaczam do obslugi uzytkownika")
            self.Admin_Users()
        elif(self.i=='2'):
            print("Przelaczam do obslugi Zgłoszen")
            self.Admin_Reports()
        elif(self.i=='3'):
            print("Przelaczam do obsługe systemu")
            self.Admin_Sys()        
        elif(self.i=='q' or self.i=='Q'):
            print("Koniec")
        else:
            print("Podano nie prawidlowy parametr dozwolone (1,2,3,q)")
            self.Admin()
            
           
    def Admin_Users(self):
        self.j = input("(1)-Dodaj uzytkownika, \n (2)-Zaktualizuj uzytkownika, \n (3)-Usun uzytkownika, \n (4)-Zmien hasło,(B)-cofnij \n Wybor: ")
        if(self.j=='1'):
            print("Dodaje uzytkownika")
            self.AddUser()
        elif(self.j=='2'):
            print("Modyfikuje uzytkownika")
            self.UpdateUser()
        elif(self.j=='3'):
            print("Usuwam uzytkownika")
            self.deleteUser()
        elif(self.j=='4'):
            print("Zmieniam hasło")
            self.ChangePass()
        elif(self.j=='b' or self.j=='B'):
            print("Cofam do poprzedniego Menu")
            self.Admin()
        else:
            print("Podano nieprawidlowa opcje dozwolone(1,2,3,4,b)");
            self.Admin_Users()
        
    def Admin_Reports(self):
        self.j = input(" (1)-Wyświetl Zgłoszenia, \n (2)-Zaktualizuj zgłoszenie, \n (3)-Zamknij zgłoszenie, \n (4)-Usun zgłoszenie, \n (B)-cofnij \n Wybor: ")
        if(self.j=='1'):
            print("Wyświetlam Zgłoszenia")
            self.ShowAllReports()
            self.Admin_Reports()
        elif(self.j=='2'):
            print("Modyfikuje Zgłoszenia")
            self.ShowAllReports()
            self.UpdateReport()
            self.Admin_Reports()
        elif(self.j=='3'):
            print("Zamykam Zgłoszenie")
            self.ShowAllReports()
            self.CloseReport()
            self.Admin_Reports()
        elif(self.j=='4'):
            print("Usuwam Zgłoszenie")
            self.ShowAllReports()
            self.DeleteReport()
            self.Admin_Reports()
        elif(self.j=='b' or self.j=='B'):
            print("Cofam do poprzedniego Menu")
            self.Admin()
        else:
            print("Podano nieprawidlowa opcje dozwolone(s,u,c,d,B)");
            self.Admin_Reports()        
            
            
    def Admin_Sys(self):    
        self.j = input("(1)- Wyświetl wszystkie statusy, \n (2)-Dodaj Nowy status, \n (3)-Usun status \n  ================================= \n (4)- Wyświetl wszystkie Priorytety, \n (5)-Dodaj Priorytet, \n (6)-Usun Priorytet, \n  ================================= \n (7)- Wyświetl wszystkie dzialy, \n (8)-Dodaj dzial, \n (9)-Usun dzial, \n (B)-cofnij \n Wybor: ")
        if(self.j=='1'):
            print("Wyświetlam Wszystkie statusy")
            self.AllStatus()
            self.Admin_Sys()
        elif(self.j=='2'):
            print("Dodaje nowy status")
            self.AddStatus()
            self.Admin_Sys()
        elif(self.j=='3'):
            print("Usuwam status")
            self.AllStatus() 
            self.DeleteStatus()
            self.Admin_Sys()
        elif(self.j=='4'):
            print("Wyświetlam Wszystkie priorytety")
            self.AllPriority()
            self.Admin_Sys()
        elif(self.j=='5'):
            print("Dodaje nowy Priorytet")
            self.AddPriority()
            self.Admin_Sys()
        elif(self.j=='6'):
            print("Usuwam Priorytet")
            self.AllPriority()
            self.DeletePriority()
            self.Admin_Sys()
        elif(self.j=='7'):
            print("Wyświetlam Wszystkie dzialy")
            self.AllDivisions()
            self.Admin_Sys()
        elif(self.j=='8'):
            print("Dodaje nowy dzial")
            self.AddDivision()
            self.Admin_Sys()
        elif(self.j=='9'):
            print("Usuwam dzial")
            self.AllDivisions()
            self.DeleteDivision()
            self.Admin_Sys()
        elif(self.j=='b' or self.j=='B'):
            print("Cofam do poprzedniego Menu")
            self.Admin()        
        else:
            print("Podano nieprawidlowa opcje, dozwolone(1,2,3,4,5,6,B)");
            self.Admin_Sys()            
        
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
        
        
 
#####################################      REQUESTER         ##########################################
 
 
 
    def OpenReport(self):
        self.ID = input("Podaj ID Zgłoszenia do Otwarcia: ")
        self.status_z = input("Zmien Status na (2 - W realizacji )")
        if(self.status_z=="2"):
            self.sql11 = "UPDATE reports SET Status=%s WHERE (ID_Z=%s and requester=%s)"
            self.cursor.execute(self.sql11,(self.status_z,self.ID,self.ID_log))
            self.conn.commit()
            print("Status zmieniono pomyślnie")
        else:
            print("Podano zły parametr dozwolony tylko 2 - W realizacji")
            self.OpenReport        
    
    
        
    def list_of_repairers(self):
        self.Lista=[]
        self.sql = "SELECT * FROM list_of_repairers"   						 
        self.cursor.execute(self.sql)   						 
        self.results = self.cursor.fetchall()   					 
        #print ("%1s" % ("Logins") )
        for row in self.results:
            self.Login1 = row[0]
            self.Lista.append(self.Login1)    
        #print(self.Lista)
            
    def AddReports(self):
        self.title = input("Podaj tytul Zgłoszenia: ")
        self.descr = input("Podaj opis zgłoszenia: ")
        self.logrep = random.choice(self.Lista)
        #print(self.logrep)
        self.data=datetime.date.today()
        #print(self.data)
        self.prior = input("Podaj Priorytet: ") 
        self.sql5 = "INSERT INTO reports (Title, description,Requester,Repairer,Data_R,priority) VALUES (%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(self.sql5,(self.title,self.descr,self.ID_log,self.logrep,self.data,self.prior))
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
            print ("%5s%40s%40s%15s%25s%25s%15s%15s" % (self.lp, self.Title, self.description,self.priority,self.repairerr,self.requesterr,self.Status,self.Data_R,))    
     
     
    
    ############################################# ADMIN ################################################## 
     
     
    def AddUser(self):
        self.NLogin=input("Podaj nowy Login: ")
        self.NPass=input("Podaj hasło: ")
        self.NRole=input("Podaj role((rep)-repairer,(req)-requester) : ")
        if(self.NRole=='rep' or self.NRole=='req'):
            self.sql13 = "INSERT INTO Logins (Login,password) VALUES (%s,%s)"
            self.cursor.execute(self.sql13,(self.NLogin, self.NPass))
            self.conn.commit()
            print("Dodano prawidłowo")
            if(self.NRole=='req'):
                self.UpdateRequester()
            else:
                self.UpdateRepairer()
        else:
            print("Podano nieprawidłowy parametr dozwolone(rep,req) ")
            self.AddUser()
     
 ######Uzupełnic ##########    
    def UpdateRequester(self): 
        print()
        
    def UpdateRepairer(self): 
        print()   
        
    def ChangePass(self):
        self.ID_L = input("Podaj ID uzytkownika do zmiany hasła: ") 
        self.NPass = input("Podaj nowe hasło: ")
        self.sql14 = "UPDATE Logins SET password =%s WHERE ID_L=%s"
        self.cursor.execute(self.sql14,(self.NPass, self.ID_L))
        self.conn.commit()
        print("Hasło zostało zmienione pomyślnie")
       
       
    def AllStatus(self): 
        self.sql16 = "SELECT * FROM statusy"
        self.cursor.execute(self.sql16)
        self.results = self.cursor.fetchall() 
        print ("%5s%15s" % ("ID","Status") )
        for row in self.results:
            self.ID_S = row[0]
            self.Status = row[1]           	 
            print ("%5s%15" % (self.ID_S, self.Status))    
            
    def AddStatus(self):
        self.NStatus = input("Podaj nowy status:")
        self.sql17 ="INSERT INTO statusy (Status) VALUES (%s)"
        self.cursor.execute(self.sql17,(self.NStatus))
        self.conn.commit()
        print("Status dodano prawidłowo")
        
    def DeleteStatus(self):
        self.ID_S = input("Podaj ID Statusu do usunięcia: ")
        self.decyzja = input("Czy napewno chce usunac(t/n): ")        
        if(self.decyzja=='t'):
            self.sql18 = "DELETE FROM statusy WHERE ID_S=%s"
            self.cursor.execute(self.sql18,(self.ID_S))            
            self.conn.commit()
            print("Status usunieto prawidłowo")
        else:
            self.DeleteStatus()
            
    def AllPriority(self): 
        self.sql19 = "SELECT * FROM priorities"
        self.cursor.execute(self.sql19)
        self.results = self.cursor.fetchall() 
        print ("%5s%20s" % ("ID","priority") )
        for row in self.results:
            self.ID_P = row[0]
            self.priority  = row[1]           	 
            print ("%5s%20" % (self.ID_P, self.priority ))
    
    def AddPriority(self):
        self.NPriority = input("Podaj nowy Priorytet:")
        self.sql20 ="INSERT INTO priorities (priority) VALUES (%s)"
        self.cursor.execute(self.sql20,(self.NPriority))
        self.conn.commit()
        print("Priorytet dodano prawidłowo")
        
    def DeletePriority(self):
        self.Id_P = input("Podaj ID Priorytetu do usunięcia: ")
        self.decyzja = input("Czy napewno chce usunac(t/n): ")        
        if(self.decyzja=='t'):
            self.sql21 = "DELETE FROM priorities WHERE Id_P=%s"
            self.cursor.execute(self.sql21,(self.Id_P))            
            self.conn.commit()
            print("Priorytet Usunięto prawidłowo")
        else:
            self.DeletePriority()
            
    def AllDivisions(self):
        self.sql22 = "SELECT * FROM Divisions"
        self.cursor.execute(self.sql22)
        self.results = self.cursor.fetchall()
        print ("%5s%15s" % ("ID","priority"))
        for row in self.results:
            self.ID_d = row[0]
            self.TDivision = row[1]
            print ("%5s%15s" % (self.ID_d,self.TDivision))
    
    def AddDivision(self):
        self.NTDivision = input("Podaj nowy Oddzial:")
        self.sql23 ="INSERT INTO Divisions (Type_Division) VALUES (%s)"
        self.cursor.execute(self.sql23,(self.NTDivision))
        self.conn.commit()
        print("Oddział dodano prawidłowo")
              
    def DeleteDivision(self):
        self.ID_d = input("Podaj ID oddziału który chcesz usunąć: ")
        self.decyzja = input("Czy napewno chce usunac(t/n): ")        
        if(self.decyzja=='t'):
            self.sql24 = "DELETE FROM Divisions WHERE ID_d=%s"
            self.cursor.execute(self.sql24,(self.ID_d))            
            self.conn.commit()
            print("Oddział Usunięto prawidłowo")
        else:
            self.DeletePriority()
    
    
        
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
            print ("%5s%10s" % (self.name, self.surname)) """
        

