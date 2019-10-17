def taobao():
    import time
    from selenium import  webdriver
    driver=webdriver.Chrome()
    url="https://www.baidu.com"
    # 打开百度
    driver.get(url)
    driver.find_element_by_id("kw").send_keys("淘宝")
    driver.find_element_by_id("su").click()
    # 打开淘宝
    time.sleep(2)
    driver.find_element_by_xpath("//font[contains(text(),'淘宝网')]").click()
    time.sleep(3)
    print(driver.current_url)
    driver.switch_to.window(driver.window_handles[1])#转换窗口至最高的句柄
    result_url = driver.current_url#获取当前句柄之后的url
    driver.find_element_by_link_text("亲，请登录").click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    driver.find_element_by_link_text("密码登录").click()
    driver.find_element_by_id("TPL_username_1").clear()
    driver.find_element_by_id("TPL_username_1").send_keys("lianjiashun")
    time.sleep(2)
    driver.find_element_by_id("TPL_password_1").clear()
    driver.find_element_by_id("TPL_password_1").send_keys("12323432")
    time.sleep(2)
    driver.find_element_by_id("J_SubmitStatic").click()
#QQ邮箱登入
def qq():
    emailurl=r"https://mail.qq.com/cgi-bin/loginpage"
    import time
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.get(emailurl)
    iframe1=driver.find_element_by_xpath("//iframe[@id='login_frame']")
    driver.switch_to.frame(iframe1)
    driver.find_element_by_id("switcher_plogin").click()
    # driver.find_element_by_xpath("//a[text()='帐号密码登录']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='u' and @name='u']").send_keys("自己填QQ")
    time.sleep(1)
    driver.find_element_by_xpath("//input[@id='p' and @name='p']").send_keys("密码自己写")
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='login_button' and @value='登 录']").click()
    driver.back()
# 天涯论坛
def tt():
    import time
    from selenium import webdriver
    driver=webdriver.Firefox()
    url="https://www.tianya.cn/"
    driver.get(url)
    try:# driver.find_element_by_link_text("密码登录").click()
        time.sleep(3)
        driver.find_element_by_class_name("normal-login-tab").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='vwriter']").send_keys("1314312")
        time.sleep(1)
        driver.find_element_by_id("vpassword").send_keys("132123214")
        driver.find_element_by_class_name("loginWin-submit-btn").click()
    except Exception as e:
        print(e)
        driver.close()
        driver.quit()
# 网易
from  selenium import webdriver
import time
def email_test(url):
    driver=webdriver.Firefox()
    driver.get(url)
    try:
        a=driver.find_element_by_link_text("密码登录")
        a.click()
    except Exception as e:
        print("222222222",a)
    # driver.find_element_by_xpath("//*[@class='u-login-entry' and @class='u-163-login-entry']").click()
    time.sleep(2)
    # 设置账号

    iframe=driver.find_element_by_xpath("//iframe[@frameborder='0' and @scrolling='no']")
    driver.switch_to.frame(iframe)
    driver.find_element_by_xpath("//input[@name='email']").send_keys("160")
    # 设置密码
    driver.find_element_by_class_name("j-inputtext").send_keys("123456")
    driver.find_element_by_class_name("u-checkbox ").click()
    driver.find_element_by_link_text("登  录").click()
# emailurl=r"https://mail.163.com"
# email_test(emailurl)