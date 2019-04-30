from scrapper import *
from scrapper import Scrapper


#-----------------------------paths de elementos-----------------------------------------------

btnOkSiNoExisteContacto='//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div'
mensajeNoExiste="//*[contains(text(), 'El número de teléfono compartido a través de la dirección URL es inválido')]"
btnEnviarApi='//*[@id="action-button"]'

#------------------------------------------------------------------------------------------------


class FacebookScrapper(Scrapper):
    def __init__(self,driver=None, cPath=None, mainPage = None):
        super.__init__()
        if mainPage:
            self.mainPage = mainPage

    def searchFacebookPage( name, alias = None, url=None ):
        """ Busca en Facebook a la página que se desea scrappear. Estaría de lujo si se tuvieran los alias o url's 
        ya que eso minimizaría la probabilidad de fallo de scrappear una página que no es la que esperamos"""
