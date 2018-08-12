from selenium import webdriver

chromedriver = 'C:\Users\Lenovo\Desktop\Project_python\chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('https://www.flipkart.com/search?q=laptops&marketplace=FLIPKART&otracker=start&as-show=on&as=off')

names = driver.find_elements_by_xpath('//div[@class="_3wU53n"]')
prices = driver.find_elements_by_xpath('//div[@class="_1uv9Cb"]')

for i in range(len(names)):
    print ('Name : ' + names[i].text + '\nPrice :' + prices[i].text)
driver.close()
