from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from linkedin_login_info import email,password

print(email)
print(password)

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.linkedin.com/')

driver.implicitly_wait(3)

driver.find_element(By.ID, 'session_key').send_keys(email)
driver.find_element(By.ID, 'session_password').send_keys(password + Keys.ENTER)

driver.get('https://www.linkedin.com/search/results/people/?keywords=software%20developer')
driver.implicitly_wait(5)

driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[2]/div/div/div[3]/div/button').click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]').click()
driver.implicitly_wait(3)
modal = driver.find_element(By.ID, 'artdeco-modal-outlet')
driver.implicitly_wait(3)
modal.find_element(By.ID, 'custom-message').send_keys('Hi!' + Keys.ENTER + Keys.ENTER + "I'm a new software developer that's in the Greater Seattle Area and wanted to ask you if you had any advice for someone, like myself, that doesn't have a lot of work experience!" + Keys.ENTER + Keys.ENTER + "Thank you for taking the time to read this message. I appreciate it a lot 😊")
# driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').send_keys(Keys.ENTER)

# for x in range(2,6):
    # driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[1]/div/div/div[3]/div/button').send_keys(Keys.ENTER)
    # driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]').send_keys(Keys.ENTER + 'Hi!' + Keys.ENTER + Keys.ENTER + "I'm a new software developer that's in the Greater Seattle Area and wanted to ask you if you had any advice for someone, like myself, that doesn't have a lot of work experience!" + Keys.ENTER + Keys.ENTER + "Thank you for taking the time to read this message. I appreciate it a lot 😊")
    # driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').send_keys(Keys.ENTER)
