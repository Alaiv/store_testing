# #РЕГИСТРАЦИЯ АККАУНТА
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# # Регистрация
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# e_mail = driver.find_element_by_id("reg_email")
# e_mail.send_keys("test25@mail.com")
# password = driver.find_element_by_id("reg_password")
# time.sleep(3)
# password.send_keys("Ntcnbv157Ntcn")
# register = driver.find_element_by_name("register")
# register.click()
#
# driver.quit()


# #ЛОГИН В СИСТЕМУ
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# # Логин
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# username = driver.find_element_by_id("username")
# username.send_keys("test25@mail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Ntcnbv157Ntcn")
# login = driver.find_element_by_name("login")
# login.click()
# logout = driver.find_element_by_link_text("Logout")
# logout_get_text = logout.text
# assert "Logout" in logout_get_text
#
# driver.quit()