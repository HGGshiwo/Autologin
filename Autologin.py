#coding=utf-8  
from selenium import webdriver
import time
# 打开网址登陆
try:
    driver = webdriver.Chrome()
    driver.get("https://healthreport.zju.edu.cn/ncov/wap/default/index")
    driver.find_element_by_id("username").send_keys("nananana")
    driver.find_element_by_id("password").send_keys("nananana")
    driver.find_element_by_id("dl").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div")
except :
    print("登录失败。。。")
# 填写信息
try:
    # 今日是否在校
    #driver.find_element_by_xpath("//div[@name='sfzx']/div[1]/div[1]").click() #是
    driver.find_element_by_xpath("//div[@name='sfzx']/div[1]/div[2]").click() #否
    # 点击获得地理信息
    driver.find_element_by_xpath("//div[@name='area']/input[1]").click()
    # 是否从以下地区返回
    driver.find_element_by_xpath("//div[@name='jrdqtlqk']/div[1]/div[3]").click() #否
    # 本人家庭成员是否有近14日入境的情况 
    element=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[25]/div/div/div[2]").click()#否
    # webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
    # 本人承诺
    driver.find_element_by_xpath("//div[@name='sfqrxxss']").click() 
    # 提交信息
    driver.find_element_by_xpath("//div[@class='footers']").click() 
    # 确定提交
    driver.find_element_by_xpath("//div[@class='wapcf-btn wapcf-btn-ok']").click()
    print("恭喜，今天填写成功！")
except Exception:    
    try:
        driver.find_element_by_xpath("//*[@id='wapat']/div/div[2]/div").click()
        print("今天已经填报过了。。。")
    except Exception:
       print("填写错误。。。")     
# 退出
driver.close()