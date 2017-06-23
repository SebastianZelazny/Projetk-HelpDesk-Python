#-*- coding: utf-8 -*-
import pymysql
import datetime
import random
import CRequester
from CRequester import CRequester
class CRepairer():  
    
    
    #################### Pomocnicza Metoda sluzaca okreslenie ID Loginu serwisanta ###########################      
    def ID_login_rep(self):
        self.ID_log=""
        
        self.sql12 ="SELECT * FROM repairers left join logins on repairers.ID_Login_rep=logins.ID_L where logins.login=%s"
        self.cursor.execute(self.sql12,(self.login))  
        self.results = self.cursor.fetchall()   					 
        
        for row in self.results:
            self.ID_log = row[0]
        
        #print("Wyciagniety ID LOG: "+str(self.ID_log))
    
    
    ############################ Glowne Menu serwisanta ############################
    def repairer(self):
        #print('logowanie poprawne repairer')
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
    
    
    ############################# Metoda która Pokazuje wszystkie zgloszenia zalogwanego serwisanta ###################################
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
     
    #################################### Metoda pokazujaca wszystkie zgloszenia ####################################
    def ShowAllReports(self):
        self.sql8 = "SELECT ID_Z,Title,description,priority_p,E_mail_rep,E_mail_req,Status_s,Data_R FROM view_request_how_repairer group by ID_Z"
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
            
    ###################### Metoda sluzaca do zamkniecia zglszenia #####################################        
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
            
    ################################ Metoda sluzaca do aktualizacji opisu zgloszen ###########################        
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
        
    ############################ Metoda pozwalajaca na usuniecie zgloszenia ################################    
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