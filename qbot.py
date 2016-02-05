from selenium import webdriver
qb=webdriver.PhantomJS(executable_path="C:\\phantomjs.exe")
qb.get("http://www.namegenerator.biz/random-name-generator.php")


password="QwErTy10293"
def Qbot():
    qbot=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    name=qb.find_element_by_id("rname").text
    qb.find_element_by_id("rnames").click()
    na=name.split(' ')
    email=na[0]+na[-1]+"@yopmail.com"
    qbot.get("https://quora.com")
    qbot.find_element_by_partial_link_text("Email").click()
    qbot.find_elements_by_class_name("text")[0].send_keys(name)
    qbot.find_elements_by_class_name("text")[1].send_keys(email)
    qbot.find_elements_by_class_name("text")[2].send_keys(password)
    qbot.execute_script("document.getElementsByClassName(\"CaptchaInput\")[0].parentNode.removeChild(document.getElementsByClassName(\"CaptchaInput\")[0])")
    qbot.find_elements_by_class_name("submit_button")[3].click()
    qbot.get("___LINK TO YOUR PROFILE___")
    qbot.execute_script("document.getElementsByClassName(\"modal_nux_background\")[0].parentNode.removeChild(document.getElementsByClassName(\"modal_nux_background\")[0])")
    qbot.execute_script("document.getElementsByClassName(\"follow_interests\")[0].parentNode.removeChild(document.getElementsByClassName(\"follow_interests\")[0])")
    qbot.find_elements_by_class_name("TwoStateButton")[0].click()
    qbot.quit()

for x in range(1,1000): #Change numbers depending on number of followers you want.
    Qbot()
