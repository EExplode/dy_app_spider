from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep, time

server = 'http://localhost:4723/wd/hub'
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'OPPO_A53m',
    'appPackage': 'com.ss.android.ugc.aweme',
    'appActivity': '.main.MainActivity'
}

# 启动会话
t1 = time()
driver = webdriver.Remote(server, desired_caps)
t2 = time()
print('启动会话完成: ' + str(t2-t1))

sleep(5)

# 关闭提示，上滑
t1 = time()
TouchAction(driver).tap(x=360, y=1024).perform()  # 关闭提示
sleep(1)
TouchAction(driver).tap(x=374, y=564).perform()  # 关闭上滑
t2 = time()
print("关闭提示、上滑完成: " + str(t2-t1))

while True:
    #'''
    sleep(1)
    t1 = time()
    # 为什么点进关注页面？
    # TouchAction(driver).tap(x=653, y=370).perform()
    driver.tap([(650, 360)], 500)
    t2 = time()
    print("进入用户主页完成: " + str(t2-t1))
    sleep(2)
    #'''

    '''
    # 太耗时了，40s
    sleep(1)
    t1 = time()
    try:
        user = driver.find_element_by_id('com.ss.android.ugc.aweme:id/emq')
    except Exception:
        driver.swipe(340, 918, 340, 230)
        print("跳过直播，下滑完成")
        continue
    else:
        user.click()
    t2 = time()
    print("进入用户主页完成: " + str(t2-t1))
    sleep(2)
    '''

    t1 = time()
    # 返回推荐
    try:
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/aae')
    except Exception:
        try:
            driver.find_element_by_id('com.ss.android.ugc.aweme:id/dag')
        except Exception:
            print("关闭直播")
            TouchAction(driver).tap(x=374, y=564).perform()  # 关闭提示
            sleep(1)
            TouchAction(driver).tap(x=675, y=50).perform()  # 关闭直播
        else:
            print('关闭广告')
            TouchAction(driver).tap(x=45, y=103).perform()
    else:
        print('正常返回')
        TouchAction(driver).tap(x=40, y=100).perform()
    t2 = time()
    print("返回推荐完成: " + str(t2-t1))

    sleep(1)

    t1 = time()
    # 滑动下一个视频
    # TouchAction(driver).press(x=342, y=938).move_to(x=368, y=267).release().perform() # 有时点成长按？
    driver.swipe(340, 918, 340, 230)
    t2 = time()
    print("下滑完成: " + str(t2-t1))
    print("\n")