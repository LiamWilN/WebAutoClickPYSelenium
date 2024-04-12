import webbrowser
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service("C:\\Users\\IT-William\\Downloads\\edgedriver_win64\\msedgedriver.exe")
    #Edge WebDriver download it if not download then Link (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads)
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument("user-data-dir=C:\\Users\\IT-William\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default")
    # Microsoft User Path

edge_options.add_argument("profile-directory=Work")
    # Microsoft Profile

driver = webdriver.Edge(service = ser,options = edge_options)

driver.get('https://app.powerbi.com/groups/b026ee74-e376-4221-a5d5-4779af0ddf72/reports/e969bfac-298a-4453-8d1c-75c59cf8abaa/ReportSection2aa23ee0d8eda11d3dc0?experience=power-bi')
    #Link to Website 

time.sleep(20) #Adjust based on PC and Internet Speed

#elips = driver.find_element(By.ID, "email"); TESTING 
#elips.send_keys("william.calda@readymaninc.com"); TESTING

element = driver.find_element(By.ID, "reportAppBarRefreshBtn");
element.click()
    #Clicking of Element must be an ID, or Modify it by CLASSNAME 


print(f"Refresh is Available: {bool(element)}");
print(f"Refresh is Visible: {bool(element.is_displayed)}");
print(f"Refresh is Selected: {bool(element.click)}");

#element.submit()

time.sleep(20) # #Adjust based on PC and Internet Speed
driver.quit()


