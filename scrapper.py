from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import json

import pyperclip as clipboard
import time                                                 #permite manejar tiempos espera tiempo desde el inicio, etc
import datetime 
import re #Regex


ficheroDatos = open("creds.json", "r").read()
env = json.loads(ficheroDatos)

class Scrapper():
    __driver=None
    __cPath= env['chromeLocation'] #La dirección donde está chromium

    mainPage= env['scrappingPage']

    def __init__(self,driver=None, cPath=None, disableAlerts=False):  
        if driver:
            self.__driver =driver
        else:
            if disableAlerts == True:
                chrome_options = webdriver.ChromeOptions()
                prefs = {"profile.default_content_setting_values.notifications" : 2}
                chrome_options.add_experimental_option("prefs",prefs)
                self.__driver = webdriver.Chrome(self.__cPath,chrome_options=chrome_options)
            else:
                self.__driver = webdriver.Chrome(self.__cPath)
        if cPath: self.__cPath=cPath

    def goToUrl(self, url):
        try:
            #Ir a la página a scrappear
            if self.__driver.current_url != url:
                self.__driver.get(url)
                return {'success':True}
            return True
        except Exception as e:
            return {'success':False, 'error':['Error al alcanzar url: '+str(e)]}

    def start(self):
        try:
            #Ir a la página a scrappear
            if self.__driver.current_url!=self.mainPage:
                self.__driver.get(self.mainPage)
                return {'success':True}
            return True
        except Exception as e:
            return {'success':False, 'error':['Error al inicializar Facebook: '+str(e)]}
    
    def tryToGetByPath(self, myPath,webO=None, times=20, clic=False, sendKeys=None):
        """Busca un elemento por su xPath por el tiempo que se le indique """
        x=0
        if not webO:
            webO=self.__driver
        while x<times:
            try:
                result=webO.find_element_by_xpath(myPath)
                if sendKeys:
                    result.send_keys(sendKeys)
                if clic:
                    result.click()
                return result
            except Exception as e:
                x+=.1
                time.sleep(.1)
        return None
    
    
    def esperarElemento(self,webO=None, path=None, paths=[], times=30):
        """Espera a que aparezca un elemento o elementos"""
        if path: paths.append(path) #Si hay un path agregarlo a la 
        if not webO: webO=self.__driver #Seleccionar el driver
        x=0
        while x<times:
            for path in paths:
                try:
                    result=webO.find_element_by_xpath(path)
                    return {'hallado':True, 'objeto':result, 'path':path}
                except Exception as e:
                    x+=0.1
                    time.sleep(0.1)

        return  {'hallado':False}
    
    def getDriver(self):
        return self.__driver