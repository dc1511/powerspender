
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

usr = ''
pwd = ''

chrome_options = Options()
chrome_options.add_argument("--headless")
union_to_organize_in = 'https://oppressive.games/power/union.php?union=1'

def loggedinLoop():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://oppressive.games/power/pol.php?pol=5030')
    time.sleep(2)
    power = float(driver.find_element_by_xpath('/html/body/div[3]/div[2]/center/div[1]/div[3]/div[1]/div/p/table/tbody/tr[4]/td[2]').text)
    time.sleep(2)
    driver.get('https://oppressive.games/power/pol.php?pol=5030')
    hsi = driver.find_element_by_xpath('/html/body/div[3]/div[2]/center/div[1]/div[3]/div[1]/div/p/table/tbody/tr[7]/td[2]').text.replace("%","")
    hsi_float = float(hsi)
    
    
    if power >= 7:
        print('power greater than 7, logging in!')
        driver.get('https://oppressive.games/power/index.php')
        log_in_box = driver.find_element_by_xpath("/html/body/nav/ul/li/button").click()
        usr_box = driver.find_element_by_name('username')
        usr_box.send_keys(usr)
        pwd_box = driver.find_element_by_name('password')
        pwd_box.send_keys(pwd)
        driver.find_element_by_name('login').click()
        if hsi_float < 100:
            driver.get('https://oppressive.games/power/actions.php')
            driver.execute_script("window.scrollTo(0, 100)")
            driver.find_element_by_xpath('/html/body/div[3]/div[2]/center/div/div[1]/div/ul/button').click()
            print('spent power on an ad')
        else: 
            if power >= 10:
                driver.get(union_to_organize_in)
                time.sleep(1)
                driver.execute_script("window.scrollTo(0, 100)")
                driver.find_element_by_name('organize').click()
                print('spent power on union influence')
            else:
                driver.close()
    else: 
        print('Power below 7, no actions required.')
        driver.close()
    time.sleep(60)   #the time it will wait (seconds)
while True:
    loggedinLoop()