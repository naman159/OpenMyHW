from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

input1 = 0

def main():

    global input1
    input1 = input()

    if(input1 == "5151"):                                                       #A specific string that opens your homework, put your own details in "" to run this for webwork courses: https://courses1.webwork.maa.org/webwork2
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        driver.get("https://webwork.math.umass.edu/webwork2/S20_STAT_515_4/")   #The link to the login of that homework page
        driver.find_element_by_id("uname").send_keys("")                        #username/email
        driver.find_element_by_id("pswd").send_keys("")                         #password
        driver.find_element_by_id("none").click()                               #Login, Sign in or submmit button
        print("logged in to stats 515 webwork!")
        main()


    elif(input1 == "5152"):                                                     #repeat, implementation for cengage webassign courses
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.webassign.net/wa-auth/login")
        driver.find_element_by_id("email").send_keys("")
        driver.find_element_by_id("cengagePassword").send_keys("")
        driver.find_element_by_name("Login").click()
        print("logged in to stats 515 cengage!")
        main()

    elif(input1 == "235"):                                                      #repeat, implementation for Pearson - MyLab, MasteringPhysics courses
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        driver.get("https://pi.pearsoned.com/v1/piapi/piui/signin?client_id=dN4bOBG0sGO9c9HADrifwQeqma5vjREy&okurl=https:%2F%2Fportal.mypearson.com%2Fcourse-home&siteid=8313")
        driver.find_element_by_id("username").send_keys("")
        driver.find_element_by_id("password").send_keys("")
        driver.find_element_by_id("mainButton").click()
        print("logged in to Math 235 MyLab!")
        main()

    elif(input1 == "close"):
        print("Enjoy your homework :)")


    else:
        print("Wrong command!")
        main()

main()
