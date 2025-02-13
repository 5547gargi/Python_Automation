# Using Oops concept
# If we want to find tomcat file cluepoint is 'server.xml' ; for apache clue point is 'http.conf' ; for weblogic 'weblogic.xml'
# find / -iname server.xml  ; based on the number of files that many tomcats are running on the host.

import os

class Tomcat(object):
     def get_home_conf_file(self,server_xml):
         self.tomcat_home=os.path.dirname(os.path.dirname(server_xml))
         self.conf_file=server_xml
         return None
     def display_details(self):
         print(f"Tomcat home is : ",self.tomcat_home)
         print(f"Tomcat conf file is : ",self.conf_file)
         return None

def get_all_tomcats():
    list_of_configFiles=[]
    for r,d,f in os.walk("/"):  # for root,directories,files in os.walk in-entire-filesystem ("/")
            for each_file in f:
                 if each_file=='server.xml':
                      list_of_configFiles.append(os.path.join(r,each_file))
    return list_of_configFiles

def main():
     print("Finding lists of tomcats .....")
     list_of_tomcats=get_all_tomcats()
     # print(list_of_tomcats)
     tomcat_objects=[]
     for each_file in list_of_tomcats:
         tomcat_object=Tomcat()
         tomcat_object.get_home_conf_file(each_file)
         tomcat_objects.append(tomcat_object)
     #print(tomcat_objects)
     for each_obj in tomcat_objects:
         each_obj.display_details()
     return None

if __name__=="__main__":
     main() 