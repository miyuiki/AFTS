from selenium import webdriver                                  
from selenium.webdriver.chrome.options import Options                                                              
from selenium.webdriver.common.by import By                     
from selenium.webdriver.support.ui import WebDriverWait                                                            
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException                                                   
options = Options()                                                                                                
options.add_argument("--no-sandbox")                                                                               
options.add_argument("--headless")                        
chrome = webdriver.Chrome(options=options)                      
chrome.get("https://zh.surveymonkey.com/r/EmployeeHealthCheck") 

def retryPage():
    agreexpath = "//div[contains(@class,'radio-button-container')]//label//span[contains(@class,'radio-button-display')]"
    agreeCheck = WebDriverWait(chrome, 15).until(EC.visibility_of_element_located((By.XPATH, agreexpath)))

try:
    agreexpath = "//div[contains(@class,'radio-button-container')]//label//span[contains(@class,'radio-button-display')]"
    agreeCheck = WebDriverWait(chrome, 15).until(EC.visibility_of_element_located((By.XPATH, agreexpath)))
    # agreeCheck = chrome.find_elements_by_xpath("//div[contains(@class,'radio-button-container')]//label//span[contain
    agreeCheck.click();                                                                                                
                                                                                                                    
   #員編
    employeeId = chrome.find_elements_by_xpath("//div[contains(@class,'question-body open-ended-single')]//input")[0]
    employeeId.send_keys("100000");

    # 額溫
    measureMathod = chrome.find_elements_by_xpath("//div[contains(@class,'radio-button-container')]//label//span[contains(@class,'radio-button-display')]")[2];
    measureMathod.click();

    #體溫
    Temperature = chrome.find_elements_by_xpath("//div[contains(@class,'question-body open-ended-single')]//input")[1]
    Temperature.send_keys("35");

    #權限不關閉
    enableRight = chrome.find_elements_by_xpath("//div[contains(@class,'radio-button-container')]//label//span[contains(@class,'radio-button-display')]")[5];
    enableRight.click();

    #confirm radio button
    confirm = chrome.find_elements_by_xpath("//div[contains(@class,'radio-button-container')]//label//span[contains(@class,'radio-button-display')]")[6];
    confirm.click();

    #下一頁
    submitBtn = chrome.find_elements_by_xpath("//button[contains(text(), '下一頁')]")[0];
    submitBtn.click();                                          
                                                                                                                    
    # "(//a[@href='/image/'])[2]"                                                                                      
    compleredTxtPath = "(//span[@class='title-text'])"                                                                 
    compleredTxt = WebDriverWait(chrome, 15).until(EC.visibility_of_element_located((By.XPATH, compleredTxtPath))).text
    # msg = compleredTxt.text;                                                                                         
    # time.sleep(3);                                                                                                   
    #completeTxt..................... - ............! Employee Self-check Body Temperature has Completed!              
    # compleredTxt = chrome.find_elements_by_xpath("//span[@class='title-text']")[0].text;                             
    print(compleredTxt); 
    chrome.quit()

except TimeoutException:
    print("Loading took too much time!-Try again")
    retryPage()