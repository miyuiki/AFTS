from selenium import webdriver                                  
from selenium.webdriver.chrome.options import Options                                                              
from selenium.webdriver.common.by import By                     
from selenium.webdriver.support.ui import WebDriverWait                                                            
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random

retryCount = 0;
def autoFill(id):
    options = Options()
    options.add_argument("--no-sandbox")                                                                               
    options.add_argument("--headless") 
    try:
        chrome = webdriver.Chrome(options=options)
        chrome.get("https://zh.surveymonkey.com/r/EmployeeHealthCheck")
        agreexpath = "//div[contains(@class,'radio-button-container')]//label//span[contains(@class,'radio-button-display')]"
        agreeCheck = WebDriverWait(chrome, 15).until(EC.visibility_of_element_located((By.XPATH, agreexpath)))
        #agreeCheck
        agreeCheck.click();                                                                                                
                                                                                                                        
        #employId
        employeeId = chrome.find_elements_by_xpath("//div[contains(@class,'question-body open-ended-single')]//input")[0]
        employeeId.send_keys(id);

        #foreheadTemp check
        foreheadCheckBtn = chrome.find_elements_by_xpath("//div[contains(@class,'radio-button-container')]//label//span[contains(@class,'radio-button-display')]")[2];
        foreheadCheckBtn.click();

        #foreheadTemp
        Temperature = chrome.find_elements_by_xpath("//div[contains(@class,'question-body open-ended-single')]//input")[1]
        foreheadDegree=str(round(random.uniform(34.1, 36.9), 1))
        Temperature.send_keys(foreheadDegree);

        #contacted people who returned from aboard in the last 14 days
        noContactBtn = chrome.find_elements_by_xpath("//div[contains(@class,'radio-button-container')]//label//span[contains(@class,'radio-button-display')]")[5];
        noContactBtn.click();

        #declaration radio button
        declarationBtn = chrome.find_elements_by_xpath("//div[contains(@class,'radio-button-container')]//label//span[contains(@class,'radio-button-display')]")[6];
        declarationBtn.click();

        #submit btn to next page
        submitBtn = chrome.find_elements_by_xpath("//button[contains(text(), '下一頁')]")[0];
        submitBtn.click();                                          
                                                                                                                        
        #successful landing page                                                                                     
        compleredTxtPath = "(//span[@class='title-text'])"                                                                 
        compleredTxt = WebDriverWait(chrome, 10, 1).until(EC.visibility_of_element_located((By.XPATH, compleredTxtPath))).text                         
        print(compleredTxt+id+" degree :"+foreheadDegree);
        chrome.quit() 
    except TimeoutException:
        chrome.quit()
        global retryCount;
        retryCount+=1
        if(retryCount == 2):
            print(id+" Write to error log")
            retryCount = 0
            pass;
        else:
            print(id+" Try again")
            autoFill(id)

def readFile(): 
    fileHandler = open("Id.txt", "r");
    IdList = fileHandler.read().splitlines();
    fileHandler.close();
    return IdList;

if __name__ == "__main__":
    IdList = readFile();
    print(IdList)
    for id in IdList:
        autoFill(id);