from scrapper import *
from scrapper import Scrapper
import selenium
import datetime
## Las siguientes librerías son para el leído del archivo de Excel en donde estarán las páginas a Scrappear
## No hagan lo que estas personas y lo pongan en un archivo de Excel ._.

import openpyxl
from openpyxl import Workbook 								#permite trabajar con archivos de excel
from openpyxl import load_workbook							#permite importar un archivo de excel


#-----------------------------paths de elementos-----------------------------------------------

btnOkSiNoExisteContacto='//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div'
mensajeNoExiste="//*[contains(text(), 'El número de teléfono compartido a través de la dirección URL es inválido')]"
btnEnviarApi='//*[@id="action-button"]'

#------------------------------------------------------------------------------------------------

ficheroDatos = open("creds.json", "r").read()
env = json.loads(ficheroDatos)

pagesToScrapp = []


class FacebookScrapper(Scrapper):
    def __init__(self, credenciales, driver=None, cPath=None, mainPage = None):
        super().__init__(disableAlerts=True)
        if mainPage:
            self.mainPage = mainPage
        super().start()
        self.loginFB(credenciales)
        
    def loginFB(self, credenciales):
        username = super().tryToGetByPath('//*[@id="email"]', clic=True)
        username.send_keys( credenciales['usuario'] )
        password = super().tryToGetByPath('//*[@id="pass"]', clic=True)
        password.send_keys( credenciales['password'] )
        super().tryToGetByPath('//*[@id="loginbutton"]', clic=True) #Click a entrar 
        #super().tryToGetByPath('//*[@id="loginbutton"]', clic=True,times = 5) #Click a entrar 
        

    def searchFacebookPage( name=None, alias = None):
        """ Busca en Facebook a la página que se desea scrappear. Estaría de lujo si se tuvieran los alias o url's 
        ya que eso minimizaría la probabilidad de fallo de scrappear una página que no es la que esperamos"""

        if alias:
            super().goToUrl( env['scrappingPage']+ "/pg/" +alias +"/posts/?ref=page_internal" )
        
    def scrollToDate( self, date ):
        driver = super().getDriver()
        #Obtiene todos los hijos que serían publicaciones
        #cuerpoPublicaciones = super().esperarElemento(path='//*[@id="u_0_4a"]/div')
        driver = super().getDriver()
        cuerpoPublicaciones = driver.find_elements_by_class_name("_1xnd")
        for element in cuerpoPublicaciones:
            try:
                fechaAbbr = element.find_element_by_tag_name("abbr")
                datetimePost = datetime.datetime.strptime(fechaAbbr.get_attribute("title"), '%d/%m/%Y %H:%M')
                dateLimit = datetime.datetime.strptime( date, '%d/%m/%Y' )
                #now = datetime.datetime.now()
                print("Fecha encontrada:", fechaAbbr.get_attribute("title"))
                if datetimePost > dateLimit():
                    print("Entra en el rango")
                else:
                    print("Esta ya no entra")

            except Exception as e:
                print(e)
            
            input("Pasó algo=??")

            

def obtieneAliasFromExcel():
    return load_workbook(env['pathFileExcel']).active

def main():
    hoja = obtieneAliasFromExcel()
    rowStart = 1
    rAux = 0
    alias = hoja['A'+str(rowStart+rAux)].value
    tiempo = hoja['B'+str(rowStart+rAux)].value
    while alias:
        alias = str(alias).replace("@", "").replace("'", "")
        pagesToScrapp.append( { 'alias':alias, 'sinceDate':tiempo } )
        rAux+=1
        alias = hoja['A'+str(rowStart+rAux)].value
        tiempo = hoja['B'+str(rowStart+rAux)].value
    
    fbScrap = FacebookScrapper( env['credenciales'] )
    fbScrap.start()
    
    for page in pagesToScrapp:
        fbScrap.searchFacebookPage( alias=page['alias'] )
        fbScrap.scrollToDate( page['sinceDate'] )

    print("Terminé")

if __name__ == "__main__":
    main()