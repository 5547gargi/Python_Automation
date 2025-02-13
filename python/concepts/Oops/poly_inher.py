class Tomcat(object):
     def __init__(self,home,ver):
         self.home=home
         self.version=ver
         return None
     
     def display(self):
          print("This is from Tomcat Calss")
          print(self.home)
          print(self.version)
          return None 
class Apache(Tomcat):
     def __init__(self,home,ver):
         self.home=home
         self.version=ver
         return None     
     
tomcat_ob=Tomcat("/home/tomcat9",'9.8.2')
apache_ob=Apache("/etc/httpd",'2.4')     
tomcat_ob.display()
apache_ob.display()
