import os
import re
import time
from appium import webdriver

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723/wd/hub',
    desired_capabilities={
        'app': os.path.expanduser('C:/Users/abhishekp/vidyanext/quiznext-auto-script/apk/app-x86-release.apk'),
        'platformName': 'Android',
        'deviceName': 'Nexus S API 23',
    })

def selectOptionAndMoveNext():
    print("Selecting option")
    try:
        correctOption = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[4]"
        correctOptionDriverText = driver.find_element_by_xpath(correctOption).text
        correctAnswerIndex = str(int(re.search(r'\d+', correctOptionDriverText).group()) + 1)
        time.sleep(2)
        option = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.support.v4.view.ViewPager/android.view.ViewGroup/android.view.ViewGroup[--index--]"
        option = option.replace("--index--", correctAnswerIndex);
        optionDriver = driver.find_element_by_xpath(option)
        optionDriver.click()
        time.sleep(0.5)
        check = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup"
        checkDriver = driver.find_element_by_xpath(check)
        checkDriver.click()
        time.sleep(0.5)
        next = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup"
        nextDriver = driver.find_element_by_xpath(next)
        nextDriver.click()
        time.sleep(0.5)
    except Exception as e:
        print(e)     

def selectQuiz():
    time.sleep(0.5)
    el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.support.v4.view.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]")
    el1.click()
    time.sleep(0.5)
    el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.support.v4.view.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]")
    el2.click()
    time.sleep(0.5)

def openPractice():
    practiceBtn = '//android.widget.Button[@content-desc="Practice"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
    el1 = driver.find_element_by_xpath(practiceBtn)
    el1.click()

def executePracticeQuiz():    
    time.sleep(0.5)
    openPractice()
    time.sleep(0.5)
    selectQuiz()
    time.sleep(6)


    playAgain = '//*[@text="Play Again"]'
    
    loop = True
    while loop:
        try:
            el1 = driver.find_element_by_xpath(playAgain)
            loop = False
            print("No more quizzess")
        except:
            loop = True
            selectOptionAndMoveNext()
        print(loop)
        time.sleep(2)

        
def init():
    # wait for app to load
    time.sleep(2)

    loop = True
    while loop:
        homeXPath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.support.v4.view.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView'
        try:
            el1 = driver.find_element_by_xpath(homeXPath)
            loop = False
            print("setting false")
            executePracticeQuiz()
        except:
            loop = True       
        print(loop)
        time.sleep(2)

init()        


