# If we want to find tomcat file cluepoint is 'server.xml' ; for apache clue point is 'http.conf' ; for weblogic 'weblogic.xml'
# find / -iname server.xml  ; based on the number of files that many tomcats are running on the host.

import os

def get_all_tomcats():
    list_of_configFiles=[]
    for r,d,f in os.walk("/"):  # for root,directories,files in os.walk in-entire-filesystem ("/")
            for each_file in f:
                 if each_file=='server.xml':
                      list_of_configFiles.append(os.path.join(r,each_file))
    return list_of_configFiles

def dispaly_details(home_cnf_files):
     for each_key in home_cnf_files.keys():
         print(f'The Tomcat_Home is : {home_cnf_files[each_key][0]}')
         print(f'The Tomcat Conf file is : {home_cnf_files[each_key][1]}')
     return None
     
def main():
    print("Finding lists of tomcats .....")
    list_of_tomcats=get_all_tomcats()
    # print(list_of_tomcats)
    cnt=1
    home_cnf_files={}
    for each_config_file in list_of_tomcats:
        #  print(f"Info for tomcat {cnt}")
        #  print('Tomcat home is : ',os.path.dirname(os.path.dirname(each_config_file)))
        #  print('Tomcat config file is : ',each_config_file)
        tomcat_home=os.path.dirname(os.path.dirname(each_config_file))
        tomcat_cnf=each_config_file
        home_cnf_files['tomcat'+str(cnt)]=[tomcat_home,tomcat_cnf]
        cnt+=1
    # print(home_cnf_files)
    dispaly_details(home_cnf_files)    
    return None

if __name__=='__main__':
     main()