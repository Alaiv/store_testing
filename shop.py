##ОТОБРАЖЕНИЕ СТРАНИЦЫ ТОВАРА
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
# # Отображение товара
# shop_btn = driver.find_element_by_link_text("Shop").click()
# html = driver.find_element_by_css_selector("img[alt='Mastering HTML5 Forms']").click()
# title = driver.find_element_by_class_name("product_title")
# title_get_text = title.text
# assert "HTML5 Forms" in title_get_text
#
# driver.quit()



# #КОЛИЧЕСТВО ТОВАРОВ В КАТЕГОРИИ
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
# # Количество
# shop_btn = driver.find_element_by_link_text("Shop").click()
# html = driver.find_element_by_link_text("HTML").click()
# items_count = driver.find_elements_by_css_selector(".attachment-shop_catalog.size-shop_catalog.wp-post-image")
# assert len(items_count) == 3
#
# driver.quit()





# #СОРТИРОВКА ТОВАРОВ
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
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
# # Сортировка
# shop_btn = driver.find_element_by_link_text("Shop").click()
# order_by = driver.find_element_by_class_name("orderby")
# order_by_default = order_by.get_attribute("value")
# assert order_by_default == "menu_order"
# sort_order = driver.find_element_by_class_name("orderby")
# select = Select(sort_order)
# select.select_by_value("price-desc")
# order_by = driver.find_element_by_class_name("orderby")
# order_by_desc = order_by.get_attribute("value")
# assert order_by_desc == "price-desc"
#
# driver.quit()




# #ОТОБРАЖЕНИЕ, СКИДКА ТОВАРА
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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
# # Отображение товара
# shop_btn = driver.find_element_by_link_text("Shop").click()
# android_quick_book = driver.find_element_by_css_selector(".post-169 h3")
# android_quick_book.click()
# book_old_price = driver.find_element_by_css_selector(".price > del > span")
# book_old_price_text = book_old_price.text
# book_new_price = driver.find_element_by_css_selector(".price > ins > span")
# book_new_price_text = book_new_price.text
# # Проверка цен
# assert book_old_price_text == "₹600.00"
# assert book_new_price_text == "₹450.00"
# book_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")) )
# book_cover.click()
# close_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")) )
# close_btn.click()
#
# driver.quit()









# # ПРОВЕРКА ЦЕНЫ В КОРЗИНЕ
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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
# # Проверка корзины
# shop_btn = driver.find_element_by_link_text("Shop").click()
# add_book = driver.find_element_by_css_selector("a[href='/shop/?add-to-cart=182']")
# add_book.click()
# time.sleep(3)
# amount = driver.find_element_by_css_selector("a>.cartcontents")
# amount_text = amount.text
# price = driver.find_element_by_css_selector("a> .amount")
# price_text = price.text
# assert amount_text == "1 Item"
# assert price_text == "₹180.00"
# cart = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0")
# cart.click()
# # Цены в корзине
# subtotal_price = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount.amount"), "₹180.00"))
# total_price = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount.amount"), "₹189.00"))
#
# driver.quit()









# # РАБОТА В КОРЗИНЕ
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# shop_btn = driver.find_element_by_link_text("Shop").click()
# driver.execute_script("window.scrollBy(0, 300);")
# html_book = driver.find_element_by_css_selector("a[href='/shop/?add-to-cart=182")
# html_book.click()
# time.sleep(5)
# java_book = driver.find_element_by_css_selector("li>[href='/shop/?add-to-cart=180']")
# java_book.click()
# cart = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0")
# cart.click()
# time.sleep(3)
# delete_first = driver.find_element_by_css_selector("a[data-product_id='182']")
# delete_first.click()
# time.sleep(3)
# undo_btn = driver.find_element_by_css_selector(".woocommerce-message>a")
# undo_btn.click()
# quantity = driver.find_element_by_name('cart[045117b0e0a11a242b9765e79cbf113f][qty]')
# quantity.clear()
# quantity.send_keys(3)
# update_btn = driver.find_element_by_name("update_cart")
# update_btn.click()
# quantity_value = quantity.get_attribute("value")
# assert quantity_value == "3"
# time.sleep(4)
# apply_btn = driver.find_element_by_name("apply_coupon")
# apply_btn.click()
# time.sleep(3)
# error = driver.find_element_by_css_selector(".woocommerce-error>li")
# error_text = error.text
# assert error_text == "Please enter a coupon code."
#
# driver.quit()







# # ПОКУПКА ТОВАРА
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# shop_btn = driver.find_element_by_link_text("Shop").click()
# driver.execute_script("window.scrollBy(0, 300);")
# html_book = driver.find_element_by_css_selector("a[href='/shop/?add-to-cart=182")
# html_book.click()
# time.sleep(3)
# cart = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0")
# cart.click()
# checkout_button = WebDriverWait(driver, 5).until(
# EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")) )
# checkout_button.click()
# firstname_text = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "label[for='billing_first_name']"), "First Name"))
# firstname_field = driver.find_element_by_id("billing_first_name")
# firstname_field.send_keys("Aleks")
# lastname = driver.find_element_by_id("billing_last_name")
# lastname.send_keys("Andr")
# email = driver.find_element_by_id("billing_email")
# email.send_keys("test@mail.ru")
# phone = driver.find_element_by_id("billing_phone")
# phone.send_keys("5678123321")
# selector = driver.find_element_by_class_name("select2-chosen").click()
# select_input = driver.find_element_by_class_name("select2-input")
# select_input.send_keys("Samoa")
# select_country = driver.find_element_by_css_selector("#select2-result-label-380>span")
# select_country.click()
# street_address = driver.find_element_by_name("billing_address_1")
# street_address.send_keys("some street 19")
# city = driver.find_element_by_name("billing_city")
# city.send_keys("Tafua")
# state = driver.find_element_by_name("billing_state")
# state.send_keys("Fauta")
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# check_radio = driver.find_element_by_id("payment_method_cheque")
# check_radio.click()
# place_order_btn = driver.find_element_by_css_selector(".button.alt")
# place_order_btn.click()
# thank_you = WebDriverWait(driver, 15).until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# pay_check = WebDriverWait(driver, 15).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot>:nth-child(3)>td"), "Check Payments"))
#
# driver.quit()
