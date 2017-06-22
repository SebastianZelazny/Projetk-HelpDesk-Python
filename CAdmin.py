#-*- coding: utf-8 -*-
import pymysql
import datetime
import random
import CRequester
from CRepairer import CRepairer

class CAdmin(CRepairer):   
    
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
        self.j = input(" (1)-Dodaj uzytkownika, \n (2)-Zaktualizuj uzytkownika, \n (3)-Usun uzytkownika, \n (4)-Zmien hasło, \n (B)-cofnij \n Wybor: ")
        if(self.j=='1'):
            print("Dodaje uzytkownika")
            self.AddUser()
            self.Admin_Users()
        elif(self.j=='2'):
            print("Modyfikuje uzytkownika")
            self.UpdateUser()
            self.Admin_Users()
        elif(self.j=='3'):
            print("Usuwam uzytkownika")
            self.deleteUser()
            self.Admin_Users()
        elif(self.j=='4'):
            print("Zmieniam hasło")
            self.ChangePass()
            self.Admin_Users()
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
            
    def AddUser(self):
        self.NLogin=input("Podaj nowy Login: ")
        self.NPass=input("Podaj hasło: ")
        self.NRole=input("Podaj role((rep)-repairer,(req)-requester) : ")
        if(self.NRole=='rep' or self.NRole=='req'):
            self.sql13 = "INSERT INTO Logins (Login,password,Role) VALUES (%s,%s,%s)"
            self.cursor.execute(self.sql13,(self.NLogin, self.NPass,self.NRole))
            self.conn.commit()
            print("Dodano prawidłowo")
            if(self.NRole=='req'):
                self.AddRequester()
            else:
                self.AddRepairer()
        else:
            print("Podano nieprawidłowy parametr dozwolone(rep,req) ")
            self.AddUser()

    ######Uzupełnic ##########    
    def AddRequester(self): 
        self.ID_Login_req=''
        self.sql26 = "SELECT * FROM logins left join requester on requester.ID_Login_req=logins.ID_L where logins.login=%s"
        self.cursor.execute(self.sql26,(self.NLogin))
        self.results = self.cursor.fetchall() 
        for row in self.results:
            self.ID_Login_req = row[0] 
        print(self.ID_Login_req)
        
        self.name_req = input("Podaj Imie uzytkownika: ")
        self.surname_req = input("Podaj Nazwisko uzytkownika: ")
        self.Email_req = input("Podaj e-mail uzytkownika: ")
        self.sql25 = "INSERT INTO requester (ID_Login_req,Name_req,Surname_req,E_mail_req) VALUES (%s,%s,%s,%s)"
        self.cursor.execute(self.sql25,(self.ID_Login_req,self.name_req,self.surname_req,self.Email_req))
        self.conn.commit()
        print("Wprowadzanie nowego usera przebieglo pomyslnie")

    def AddRepairer(self): 
        self.ID_Login_rep=''
        self.sql27 = "SELECT * FROM logins left join repairers on repairers.ID_Login_rep=logins.ID_L where logins.login=%s"
        self.cursor.execute(self.sql27,(self.NLogin))
        self.results = self.cursor.fetchall() 
        for row in self.results:
            self.ID_Login_rep = row[0] 
        print(self.ID_Login_rep)
        
        self.name_rep = input("Podaj Imie serwisanta: ")
        self.surname_rep = input("Podaj Nazwisko serwisanta: ")
        self.Email_rep = input("Podaj e-mail serwisanta: ")
        self.AllDivisions()
        self.division_rep = input("Podaj dział który będzie obsługiwał: ")
        self.CountDivision()
        if(int(self.division_rep)>=1 and int(self.division_rep) <=int(self.number_of_branches)):
            self.sql28 = "INSERT INTO repairers (ID_Login_rep,Name_rep,Surname_rep,E_mail_rep,division) VALUES (%s,%s,%s,%s,%s)"
            self.cursor.execute(self.sql28,(self.ID_Login_rep,self.name_rep,self.surname_rep,self.Email_rep,self.division_rep))
            self.conn.commit()
            print("Wprowadzanie nowego serwisanta przebieglo pomyslnie")
        else:
            print("Podano nieprawidłowy numer dywizji")
            self.AddRepairer()
            
    def CountDivision(self):
        self.number_of_branches =''
        self.sql29= "select count(ID_D) from divisions"
        self.cursor.execute(self.sql29)
        self.results = self.cursor.fetchall() 
        for row in self.results:
            self.number_of_branches = row[0]
            
        print(self.number_of_branches)    
    def ChangePass(self):
        self.ID_L = input("Podaj ID uzytkownika do zmiany hasła: ") 
        self.NPass = input("Podaj nowe hasło: ")
        self.sql14 = "UPDATE Logins SET password =%s WHERE ID_L=%s"
        self.cursor.execute(self.sql14,(self.NPass, self.ID_L))
        self.conn.commit()
        print("Hasło zostało zmienione pomyślnie")

    def ShowRepairers(self):
        self.sql30  = "SELECT *"
        print()
    def ShowRequesters(self):
        print()

    def AllStatus(self): 
        self.sql16 = "SELECT * FROM statusy"
        self.cursor.execute(self.sql16)
        self.results = self.cursor.fetchall() 
        print ("%5s%30s" % ("ID","Status") )
        for row in self.results:
            self.ID_S = row[0]
            self.Statuss = row[1]           	 
            print("%5s%30s" % (self.ID_S,self.Statuss))    

    def AddStatus(self):
        self.NStatus = input("Podaj nowy status:")
        self.sql17 ="INSERT INTO statusy (Status_s) VALUES (%s)"
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
            print ("%5s%20s" % (self.ID_P, self.priority ))

    def AddPriority(self):
        self.NPriority = input("Podaj nowy Priorytet:")
        self.sql20 ="INSERT INTO priorities (priority_p) VALUES (%s)"
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
            
            
