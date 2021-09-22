from selenium import webdriver

drv = webdriver.Chrome()
drv.get('https://web.whatsapp.com/')
im = input('enter the name of the gorup')
msg = input('enter your massage')
cnt = int(input('how many'))
input('what shall be after qr')
usr = drv.find_element_by_xpath('//span[@title="{}"]'.format(im))
usr.click()
msgbox = drv.find_element_by_class_name('_2S1VP ')  # fild selector
for i in range(cnt):
    msgbox.send_keys(msg)
    btn = drv.find_element_by_class_name('_35EW6')  # button selector
btn.click()
# test a selector
