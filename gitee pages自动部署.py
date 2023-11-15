import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
# 模拟浏览器打开到gitee登录界面
driver = webdriver.Chrome(options=options)

driver.get('https://gitee.com/login')

# 将窗口最大化
# driver.maximize_window("chromedriver.exe")
time.sleep(2)

# 输入账号--通过html的id属性定位输入位置--改为你的账号
user_login = driver.find_element('id','user_login')
user_login.send_keys("ihmod")
# 输入密码--通过html的id属性定位输入位置--改为你的密码
driver.find_element('id','user_password').send_keys("tjx887755")
# 点击登录按钮--通过xpath确定点击位置
driver.find_element('xpath',
    '//input[@class="ui fluid orange submit button large"]').click()
time.sleep(2)

# 切换到gitee pages界面--改为you_gitee_id
driver.get('https://gitee.com/ihmod/ihmod/pages')


# 点击更新按钮--通过xpath确定点击位置
driver.find_element('xpath', '//div[@class="button orange redeploy-button ui update_deploy"]').click()

time.sleep(2)
# 确认更新提示框--这个函数的作用是确认提示框
Alert(driver).accept()

# 等待5秒更新
time.sleep(5)

# 这个print其实没事什么用,如果真的要测试脚本是否运行成功，可以用try来抛出异常
print("成功")

# 脚本运行成功,退出浏览器
driver.quit()

# 写上更新日志
# 我这里是写在D盘，可以改为自己喜欢的目录
fp = open("T:\工作台\gitee-deploy.txt", "a+")
now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
fp.write("部署时间:{0}\n".format(now_time))
fp.close()