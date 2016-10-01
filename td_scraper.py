from selenium import webdriver
import time

username = ''
password = ''
secretanswer = ['','','','','','','','','','','','','']
secretquestionkey = ['','','','','','','','','','','']

def get_driver(usernam, passwrd):
    """Return a logged-in TD card selenium driver instance."""
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get("https://easyweb.td.com/waw/idp/login.htm?execution=e1s1")

    
    inputElement = driver.find_element_by_name("login:AccessCard")
    inputElement.send_keys(username)

    time.sleep(1)
    pwdElement = driver.find_element_by_name("login:Webpassword")
    pwdElement.send_keys(password)
    

    submitElement = driver.find_element_by_name("login")
    submitElement.submit()
   
    return driver

def prettify_string(string):
    string = string.replace("\t","")
    string = string.replace(",","")
    string = string.replace("\n","")
    string = string.replace("$","")
    string = string.replace(" ","")
    return string

def get_activity(username, password):
    """For a given username, retrieve recent investment amount"""
    rows = None
    d = get_driver(username, password)
    
    """Determine if intermediate step is required"""
    if ("InitSecondaryAuth.do" in d.current_url):
    	formElement = d.find_elements_by_css_selector(".normaltext_SIDE");

    	pswd = d.find_element_by_name('hintanswer');
    	#pswd.send_keys('visnagar')
    	time.sleep(3)
    	if (secretquestionkey[0] in formElement[0].get_attribute('innerHTML')):
    		pswd.send_keys(secretanswer[0])
    		submitbtn = d.find_element_by_name('submitNext')
    		submitbtn.submit()
    	else:
    		print ("nothing to see here")
    		sleep(500)
        

    table_path = "/html/body"

    #d.switch_to()
    d.switch_to.frame(d.find_element_by_name("tddetails"))
    xm = d.find_elements_by_xpath(table_path)
    vm = d.find_elements_by_css_selector('.td-target-investing')

    all_children_by_xpaths = vm[0].find_elements_by_css_selector('.td-copy-align-right');
    amt = all_children_by_xpaths[1].get_attribute('innerHTML')

    amt = prettify_string(amt)
    print (amt)
    
    d.quit()

    
    
if __name__ == '__main__':
    print get_activity('', '')
