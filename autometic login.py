# pip install selenium
# pip install webdriver-manager
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

username = input("enter your username: ")
password = input("enter your password: ")


# chrome browser take download ba install korar  korar jonno ai line likhbo
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# mi jei website a jete cai jaoar jonno ai line
driver.get("https://www.codecademy.com")

# web ta open hoar jonno opekkha korte hobe MANE AMI TIME SET KORBO er jonno impor korte hobe sleep, time
# time ta ami nirdaron korbo
sleep(10)

''' any wb te probesh korar jonno login click korte hoi kintu  AI KAJ TA AMRA PROGRAM ER MADDOME KORBO nicer ai line diya
 mane login korar jonno age login button click korte hoi ata korar jonno ai line'''
login_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='header-sign-in']")
# program jehetu nij theke click korbe click koranor jonno ei line
login_button.click()

# username_box ememail ba number deoar jonno
username_box = driver.find_element(By.ID, "user_login")
# upore batton a click koraisi kintu  username_box a uporer username input ke dukate hobe er jonno
username_box.send_keys(username) # autometic type korar jonno send_keys f ta use korbo

# abar amra password_box niya kaj korbo password deoar joono
password_box = driver.find_element(By.ID, "login__user_password")
# input pasword take password box a dibo
password_box.send_keys(password)

# username , password deoa hole final login click kori atai korbo program er maddome
final_login = driver.find_element(By.CSS_SELECTOR, "button[data-testid='login-button']")

final_login.click()

