#-*- coding: utf-8 -*-
import pymysql
import datetime
import random
import CRequester
from CRepairer import CRepairer

class CAdmin(CRepairer):   
    
    ############Glowne Menu Admina ########################################
    def Admin(self): 
        print('Logowanie poprawne Admin')
        self.i = input('Co robimy: \n (1)-Operacje na uzytkownikach, \n (2)-Operacje na zgłoszeniach, \n (3)-Operacje na systemie, \n (Q)-wyjście \n Wybór: ')
        if(self.i=='1'):
            #print("Przelaczam do obslugi uzytkownika")
            self.Admin_Users()
        elif(self.i=='2'):
            #print("Przelaczam do obslugi Zgłoszen")
            self.Admin_Reports()
        elif(self.i=='3'):
            #print("Przelaczam do obsługe systemu")
            self.Admin_Sys()        
        elif(self.i=='q' or self.i=='Q'):
            print("Koniec")
        else:
            print("Podano nie prawidlowy parametr dozwolone (1,2,3,q)")
            self.Admin()
            
    #################### Pedmenu Admina odnoszace sie do uzytkownikow ##########################       
    def Admin_Users(self): 
        self.j = input(" (1)-Pokaz serwisantow, \n (2)-Pokaz uzytkownikow, \n=====================\n (3)-Dodaj uzytkownika, \n=====================\n (4)-Zaktualizuj serwisanta, \n (5)-Zaktualizuj uzytkownika, \n===================== \n (6)-Usun serwisanta, \n (7)-Usun uzytkownika, \n=====================\n (8)-Wyświetl loginy, \n (9)-Zmien hasło, \n (A)-Odblokuj konto, \n (S)-Zablokuj konto, \n=====================\n (B)-cofnij \n Wybor: ")
        if(self.j=='1'):
            #print("Pokazuje serwisantow")
            self.ShowRepairers()
            self.Admin_Users()
        elif(self.j=='2'):
            #print("Pokazuje uzytkownika")
            self.ShowRequesters()
            self.Admin_Users()            
        elif(self.j=='3'):
            #print("Dodaje uzytkownika")
            self.AddUser()
            self.Admin_Users()
        elif(self.j=='4'):
            #print("Modyfikuje Serwisanta")
            self.ShowRepairers()
            self.UpdateRepairer()
            self.Admin_Users()
        elif(self.j=='5'):
            #print("Modyfikuje Uzytkowniak")
            self.ShowRequesters()
            self.UpdateRequester()
            self.Admin_Users()            
        elif(self.j=='6'):
            #print("Usuwam serwisanta")
            self.ShowRepairers()
            self.DeleteRepairer()
            self.Admin_Users()
        elif(self.j=='7'):
            #print("Usuwam Uzytkownika")
            self.ShowRequesters()
            self.DeleteRequester()
            self.Admin_Users()
        elif(self.j=='8'):
            #print("Wyświetlam Loginy")
            self.ShowLogins()
            self.Admin_Users()
        elif(self.j=='9'):
            #print("Zmieniam hasło")
            self.ShowLogins()
            self.ChangePass()
            self.Admin_Users()
        elif(self.j=='a' or self.j=='A'):
            #print("Odblokuj konto")
            self.ShowLogins()
            self.UnBlockAccount()
            self.Admin_Users()
        elif(self.j=='s' or self.j=='S'):
            #print("Odblokuj konto")
            self.ShowLogins()
            self.BlockAccountSelf()
            self.Admin_Users()            
        elif(self.j=='b' or self.j=='B'):
            #print("Cofam do poprzedniego Menu")
            self.Admin()
        else:
            print("Podano nieprawidlowa opcje dozwolone(1,2,3,4,5,6,7,8,9,B,A,S)");
            self.Admin_Users()
   
    ################# Podmenu Administrator słuzace do obslugi zadan    
    def Admin_Reports(self):
        self.j = input(" (1)-Wyświetl Zgłoszenia, \n (2)-Zaktualizuj zgłoszenie, \n (3)-Zamknij zgłoszenie, \n (4)-Usun zgłoszenie, \n (B)-cofnij \n Wybor: ")
        if(self.j=='1'):
            #print("Wyświetlam Zgłoszenia")
            self.ShowAllReports()
            self.Admin_Reports()
        elif(self.j=='2'):
            #print("Modyfikuje Zgłoszenia")
            self.ShowAllReports()
            self.UpdateReport()
            self.Admin_Reports()
        elif(self.j=='3'):
            #print("Zamykam Zgłoszenie")
            self.ShowAllReports()
            self.CloseReport()
            self.Admin_Reports()
        elif(self.j=='4'):
            #print("Usuwam Zgłoszenie")
            self.ShowAllReports()
            self.DeleteReport()
            self.Admin_Reports()
        elif(self.j=='b' or self.j=='B'):
            #print("Cofam do poprzedniego Menu")
            self.Admin()
        else:
            print("Podano nieprawidlowa opcje dozwolone(1,2,3,4,B)");
            self.Admin_Reports()        
            
    ###################### Podmenu Admina sluzace do obslugi systemu ###############################        
    def Admin_Sys(self):    
        self.j = input(" (1)-Wyświetl wszystkie statusy, \n (2)-Dodaj Nowy status, \n (3)-Usun status \n  ================================= \n (4)-Wyświetl wszystkie Priorytety, \n (5)-Dodaj Priorytet, \n (6)-Usun Priorytet, \n  ================================= \n (7)-Wyświetl wszystkie dzialy, \n (8)-Dodaj dzial, \n (9)-Usun dzial, \n=====================\n (B)-cofnij \n Wybor: ")
        if(self.j=='1'):
            #print("Wyświetlam Wszystkie statusy")
            self.AllStatus()
            self.Admin_Sys()
        elif(self.j=='2'):
            #print("Dodaje nowy status")
            self.AddStatus()
            self.Admin_Sys()
        elif(self.j=='3'):
            #print("Usuwam status")
            self.AllStatus() 
            self.DeleteStatus()
            self.Admin_Sys()
        elif(self.j=='4'):
            #print("Wyświetlam Wszystkie priorytety")
            self.AllPriority()
            self.Admin_Sys()
        elif(self.j=='5'):
            #print("Dodaje nowy Priorytet")
            self.AddPriority()
            self.Admin_Sys()
        elif(self.j=='6'):
            #print("Usuwam Priorytet")
            self.AllPriority()
            self.DeletePriority()
            self.Admin_Sys()
        elif(self.j=='7'):
            #print("Wyświetlam Wszystkie dzialy")
            self.AllDivisions()
            self.Admin_Sys()
        elif(self.j=='8'):
            #print("Dodaje nowy dzial")
            self.AddDivision()
            self.Admin_Sys()
        elif(self.j=='9'):
            #print("Usuwam dzial")
            self.AllDivisions()
            self.DeleteDivision()
            self.Admin_Sys()
        elif(self.j=='b' or self.j=='B'):
            #print("Cofam do poprzedniego Menu")
            self.Admin()        
        else:
            print("Podano nieprawidlowa opcje, dozwolone(1,2,3,4,5,6,7,8,9,B)");
            self.Admin_Sys() 
            
     #######################   Metoda dodawania uzytkownikow ###################    
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

    ###### Metoda ktora jest wywolywana gdy przy zakladaniu uzytkownika podany jest jako rep lub req sluzy do uzupelniania danych kontaktowych ##########    
    def AddRequester(self): 
        self.ID_Login_req=''
        self.sql26 = "SELECT * FROM logins left join requester on requester.ID_Login_req=logins.ID_L where logins.login=%s"
        self.cursor.execute(self.sql26,(self.NLogin))
        self.results = self.cursor.fetchall() 
        for row in self.results:
            self.ID_Login_req = row[0] 
        #print(self.ID_Login_req)
        
        self.name_req = input("Podaj Imie uzytkownika: ")
        self.surname_req = input("Podaj Nazwisko uzytkownika: ")
        self.Email_req = input("Podaj e-mail uzytkownika: ")
        self.sql25 = "INSERT INTO requester (ID_Login_req,Name_req,Surname_req,E_mail_req) VALUES (%s,%s,%s,%s)"
        self.cursor.execute(self.sql25,(self.ID_Login_req,self.name_req,self.surname_req,self.Email_req))
        self.conn.commit()
        print("Wprowadzanie nowego usera przebieglo pomyslnie")

        ######Metoda ktora jest wywolywana gdy przy zakladaniu uzytkownika podany jest jako rep lub req sluzy do uzupelniania danych kontaktowych ##########  
    def AddRepairer(self): 
        self.ID_Login_rep=''
        self.sql27 = "SELECT * FROM logins left join repairers on repairers.ID_Login_rep=logins.ID_L where logins.login=%s"
        self.cursor.execute(self.sql27,(self.NLogin))
        self.results = self.cursor.fetchall() 
        for row in self.results:
            self.ID_Login_rep = row[0] 
        #print(self.ID_Login_rep)
        
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
            print("Podano nieprawidłowy numer dzialu")
            self.AddRepairer()
    
    ################# Metoda sluzy do zabezpieczenia wpisywania nieporzadanej dywizji ################        
    def CountDivision(self):
        self.number_of_branches =''
        self.sql29= "select count(ID_D) from divisions"
        self.cursor.execute(self.sql29)
        self.results = self.cursor.fetchall() 
        for row in self.results:
            self.number_of_branches = row[0]
            
        #print(self.number_of_branches)    
        
        
        ###################### Metoda sluzaca do zmiany hasla uzytkownika #############
        
    def ChangePass(self):
        self.ID_L = input("Podaj ID uzytkownika do zmiany hasła: ") 
        self.NPass = input("Podaj nowe hasło: ")
        self.sql14 = "UPDATE Logins SET password =%s WHERE ID_L=%s"
        self.cursor.execute(self.sql14,(self.NPass, self.ID_L))
        self.conn.commit()
        print("Hasło zostało zmienione pomyślnie")
    

        ###################### Metoda pokazujaca wszystkich Serwisantow ################
    def ShowRepairers(self):
        self.sql30  = "SELECT * FROM repairers"
        self.cursor.execute(self.sql30)
        self.results = self.cursor.fetchall() 
        print ("%5s%5s%15s%15s%25s%20s" % ("ID_Rep","ID_L","Name","Surname","E-mail","Division"))
        for row in self.results:
            self.ID_rep = row[0]
            self.ID_Login_repp = row[1]
            self.Name_repp = row[2]
            self.Surname_repp = row[3]
            self.Email_repp = row[4]
            self.division_repp = row[5]
            print ("%5s%5s%15s%15s%25s%20s" % (self.ID_rep,self.ID_Login_repp, self.Name_repp,self.Surname_repp,self.Email_repp,self.division_repp))
    
        ########### Metoda pokazuja wszystkich urzytkownikow ######################   
    def ShowRequesters(self):
        self.sql31  = "SELECT * FROM requester"
        self.cursor.execute(self.sql31)
        self.results = self.cursor.fetchall() 
        print ("%5s%5s%15s%15s%25s" % ("ID_Req","ID_L","Name","Surname","E-mail"))
        for row in self.results:
            self.ID_req = row[0]
            self.ID_Login_reqq = row[1]
            self.Name_reqq = row[2]
            self.Surname_reqq = row[3]
            self.Email_reqq = row[4]
            print ("%5s%5s%15s%15s%25s" % (self.ID_req,self.ID_Login_reqq, self.Name_reqq,self.Surname_reqq,self.Email_reqq))        
        
        
        ################ Metoda sluzaca do zaktualizowania danych kontaktowych serwisanta ##############
    def UpdateRepairer(self):
        self.ID_repp = input("Podaj ID serwisanta którego chcesz zaktualizować: ")
        self.name_repp = input("Podaj imie: ")
        self.surname_repp = input("Podaj nazwisko: ")
        self.Email_repp = input("Podaj e-mail: ")
        self.AllDivisions()
        self.division_repp = input("Podaj dział: ")
        self.CountDivision()
        if(int(self.division_repp)>=1 and int(self.division_repp) <=int(self.number_of_branches)):        
            self.sql32 = "UPDATE repairers SET name_rep=%s,surname_rep=%s,E_mail_rep=%s,division=%s WHERE ID_rep=%s"
            self.cursor.execute(self.sql32,(self.name_repp, self.surname_repp,self.Email_repp,self.division_repp,self.ID_repp))
            self.conn.commit()
            print("UPDATE przebiegł pomyślnie")
        else:
            print("Podano nieprawidłowy numer dzialu")
            self.UpdateRepairer()
            
            ################ Metoda sluzaca do zaktualizowania danych kontaktowych Uzytkownika ##############    
    def UpdateRequester(self):
        self.ID_reqq = input("Podaj ID Uzytkownika którego chcesz zaktualizować: ")
        self.name_reqq = input("Podaj imie: ")
        self.surname_reqq = input("Podaj nazwisko: ")
        self.Email_reqq = input("Podaj e-mail: ")
        self.sql33 = "UPDATE requester SET name_req=%s,surname_req=%s,E_mail_req=%s WHERE ID_req=%s"
        self.cursor.execute(self.sql33,(self.name_reqq, self.surname_reqq,self.Email_reqq,self.ID_reqq))
        self.conn.commit()
        print("UPDATE przebiegł pomyślnie")
        
        
        ########## Metoda pokazująca wszystkie statusy ##############
    def AllStatus(self): 
        self.sql16 = "SELECT * FROM statusy"
        self.cursor.execute(self.sql16)
        self.results = self.cursor.fetchall() 
        print ("%5s%30s" % ("ID","Status") )
        for row in self.results:
            self.ID_S = row[0]
            self.Statuss = row[1]           	 
            print("%5s%30s" % (self.ID_S,self.Statuss))    
            
        ########## Metoda pozwalająca dodać nowy status ############
    def AddStatus(self):
        self.NStatus = input("Podaj nowy status:")
        self.sql17 ="INSERT INTO statusy (Status_s) VALUES (%s)"
        self.cursor.execute(self.sql17,(self.NStatus))
        self.conn.commit()
        print("Status dodano prawidłowo")
        
        
        ################### Metoda ktora usuwa status #############
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
            
            
        
        #################### Metoda wyswietlajaca Wszystkie Priorytety #################
    def AllPriority(self): 
        self.sql19 = "SELECT * FROM priorities"
        self.cursor.execute(self.sql19)
        self.results = self.cursor.fetchall() 
        print ("%5s%20s" % ("ID","priority") )
        for row in self.results:
            self.ID_P = row[0]
            self.priority  = row[1]           	 
            print ("%5s%20s" % (self.ID_P, self.priority ))
            
        
        ################## Metoda która dodaje nowy priorytet ########################
    def AddPriority(self):
        self.NPriority = input("Podaj nowy Priorytet:")
        self.sql20 ="INSERT INTO priorities (priority_p) VALUES (%s)"
        self.cursor.execute(self.sql20,(self.NPriority))
        self.conn.commit()
        print("Priorytet dodano prawidłowo")
        
        
        ################## Metoda pozwalająca na usunie cie priorytetu ###############
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


        ################## Metoda wyswietlajaca wszystkie oddzialy #################
    def AllDivisions(self):
        self.sql22 = "SELECT * FROM Divisions"
        self.cursor.execute(self.sql22)
        self.results = self.cursor.fetchall()
        print ("%5s%15s" % ("ID","priority"))
        for row in self.results:
            self.ID_d = row[0]
            self.TDivision = row[1]
            print ("%5s%15s" % (self.ID_d,self.TDivision))
        
        
        
        ################ Metoda pozwalajaca dodać nowy dzial #########################
    def AddDivision(self):
        self.NTDivision = input("Podaj nowy Oddzial:")
        self.sql23 ="INSERT INTO Divisions (Type_Division) VALUES (%s)"
        self.cursor.execute(self.sql23,(self.NTDivision))
        self.conn.commit()
        print("Oddział dodano prawidłowo")
        
        
        ################# Metoda usuwajaca dzial #################################
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
    ####################### Metoda usuwajaca Serwisanta #########################        
    def DeleteRepairer(self):
        self.ID_rep = input("Podaj id serwisanta do usuniecia: ")
        self.decyzja = input("Czy napewno chce usunac(t/n): ")        
        if(self.decyzja=='t'):
            self.permissionDeleteOff()
            self.SelectDeleteLoginRep()
            self.sql34 = "DELETE FROM repairers WHERE ID_rep=%s"
            self.cursor.execute(self.sql34,(self.ID_rep))
            self.DeleteLogin()            
            self.conn.commit()
            self.permissionDeleteOn()
            print("Serwisanta Usunięto prawidłowo")
        else:
            self.DeleteRepairer()
    
    
    
    ####################### Metoda usuwająca uzytkownika #####################        
    def DeleteRequester(self):
        self.ID_req = input("Podaj id uzytkownika do usuniecia: ")
        self.decyzja = input("Czy napewno chce usunac(t/n): ")       
        if(self.decyzja=='t'): 
            self.permissionDeleteOff()
            self.SelectDeleteLoginReq()
            self.sql35 = "DELETE FROM requester WHERE ID_req=%s"
            self.cursor.execute(self.sql35,(self.ID_req))
            self.DeleteLogin()            
            self.conn.commit()
            self.permissionDeleteOn()
            print("Uzytkownika Usunięto prawidłowo")
        else:
            self.DeleteRequester()
     
    ################### Pomocnicza metoda ktora wyswietla ID serwisanta ktory jest usuwany  ################  
    def SelectDeleteLoginRep(self):
        self.ID_to_del=''
        self.sql36 = "SELECT * FROM logins LEFT JOIN repairers ON logins.ID_L=repairers.ID_Login_rep WHERE ID_rep=%s"
        self.cursor.execute(self.sql36,(self.ID_rep))
        self.results = self.cursor.fetchall()
        for row in self.results:
            self.ID_to_del = row[0]
        #print(self.ID_to_del)  
    
    
        ################### Pomocnicza metoda ktora wyswietla ID uzytkownika ktory jest usuwany  ################      
    def SelectDeleteLoginReq(self):
        self.ID_to_del=''
        self.sql36 = "SELECT * FROM logins LEFT JOIN requester ON logins.ID_L=requester.ID_Login_req WHERE ID_req=%s"
        self.cursor.execute(self.sql36,(self.ID_req))
        self.results = self.cursor.fetchall()
        for row in self.results:
            self.ID_to_del = row[0]            
        #print(self.ID_to_del)
    
    ###################### Usuwa login uzytkownika lub serwisanta ktory zostal usuniety z bazy ######################## 
    def DeleteLogin(self):
        #print("DelLogin")
        #print(self.ID_to_del)
        self.sql37 = "DELETE FROM logins WHERE ID_L=%s"
        self.cursor.execute(self.sql37,(self.ID_to_del))
        self.conn.commit()
   
    ################### Pomocnicza metoda ktora wylacza sprawdzanie relacji miedzy tabelami w celu umozliwienia usuniecia rekordu#################     
    def permissionDeleteOff(self):
        self.sql38 = "SET foreign_key_checks = 0"
        self.cursor.execute(self.sql38)
        
        
    ################### Pomocnicza metoda ktora ponownie wlacza sprawdzanie relacji miedzy tabelami #################
    def permissionDeleteOn(self):
        self.sql39 = "SET foreign_key_checks = 1"
        self.cursor.execute(self.sql39)        
    ################### Metoda pokazująca wszystkie loginy ale # haslo ###################################    
    def ShowLogins(self):
        self.sql40 = "SELECT * FROM logins"
        self.cursor.execute(self.sql40)
        self.results = self.cursor.fetchall()
        print("%5s%10s%10s%5s%3s" % ("ID_L","Login","Password","Role","Lock"))
        for row in self.results:
            self.ID_L = row[0]
            self.Login = row[1]
            self.Password = "********"
            self.role = row[3]
            self.Lock = row[4]
            print("%5s%10s%10s%5s%3s" % (self.ID_L,self.Login,self.Password,self.role,self.Lock))
    
    ##### Blokowanie konta automatycznie"""""   
    def BlockAccountAuto(self): 
        self.sql41 = "UPDATE Logins SET Locked=True where Login=%s"
        self.cursor.execute(self.sql41,(self.login))
        self.conn.commit()     
    
    ####### Metoda ktora sluzy do Odblokowania Konta ##################################
    def UnBlockAccount(self):
        self.ID_UnBlock_A = input("Podaj ID który chciał bys odblokować ")
        self.sql42 = "UPDATE Logins SET Locked=False where ID_L=%s"
        self.cursor.execute(self.sql42,(self.ID_UnBlock_A))
        self.conn.commit()   
    
    ################## Reczne blokowanie konta #################################
    def BlockAccountSelf(self): 
        self.ID_Block_A = input("Podaj ID który chciał bys zablokować ")
        self.sql43 = "UPDATE Logins SET Locked=True where ID_L=%s"
        self.cursor.execute(self.sql43,(self.ID_Block_A))
        self.conn.commit() 