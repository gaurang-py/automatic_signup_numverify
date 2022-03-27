from selenium import webdriver
import random,string,names,random_address

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))
email = random_char(5)+"@gmail.com"


try: 
       driver =  webdriver.Chrome(".\chromedriver.exe")
       url = "https://numverify.com/signup?plan=102"

       driver.get(url)
       driver.find_element_by_name("email_address").send_keys(email)
       driver.find_element_by_name("email_address_repeat").send_keys(email)
       driver.find_element_by_name("password").send_keys("Patel4717@")
       driver.find_element_by_name("first_name").send_keys(names.get_first_name(gender='male'))
       driver.find_element_by_name("last_name").send_keys(names.get_last_name())
       driver.find_element_by_name("address").send_keys(random_address.real_random_address_by_postal_code('32409')['address1'])
       driver.find_element_by_name("post_code").send_keys("32409")
       driver.find_element_by_name("country_code").send_keys("country_code")
       driver.find_element_by_name("city").send_keys(random_address.real_random_address_by_postal_code('32409')['city'])
       driver.find_element_by_name("company_name").send_keys(names.get_last_name()+"Son's")
       driver.find_element_by_id("billing_type_2").click()
       print("Please Solve The Captcha Key And Hit Enter!")
       enter = input()
       driver.get("https://numverify.com/dashboard")
       print(driver.find_elements_by_class_name("alert accesskey").text())
except:
       print("Error Try Again")