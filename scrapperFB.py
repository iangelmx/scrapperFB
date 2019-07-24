from scrapper import *
from scrapper import Scrapper
import selenium
## Para el page down en el infinite scroller
from selenium.webdriver.common.keys import Keys

import datetime
## Las siguientes librerías son para el leído del archivo de Excel en donde estarán las páginas a Scrappear
## No hagan lo que estas personas y lo pongan en un archivo de Excel ._.
## "Excel es horrible." (Abraham Lincoln, 2019)

import openpyxl
from openpyxl import Workbook 								#permite trabajar con archivos de excel
from openpyxl import load_workbook							#permite importar un archivo de excel

## para escribir resultados en excel
from libs.pydocsxl import DocumentoExcel

import urllib.request


#-----------------------------paths de elementos-----------------------------------------------

#btnOkSiNoExisteContacto='//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div'
#mensajeNoExiste="//*[contains(text(), 'El número de teléfono compartido a través de la dirección URL es inválido')]"
#btnEnviarApi='//*[@id="action-button"]'

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
        

    def searchFacebookPage(self, registros, fbScrap):
        invalidos = {}
        # Se crea objeto "posts" que se utilizará en la función getPost
        posts = []
        fechaInicio = fbScrap.getFechaInicio()
        for r in registros:
            alias = r['alias'] 
            if alias:
                # Busca en Facebook a la página que se desea scrappear
                super().goToUrl( env['scrappingPage']+ "/pg/" +alias +"/posts/?ref=page_internal" )
                # si no halla la pagina, agregar el alias erróneo al diccionario de inválidos
                pagError = super().tryToGetByPath('//*[@id="content"]/div/div/h2', times=3) 
                if pagError != None:
                    print(alias + ": alias incorrecto")
                    invalidos[alias] = r['id']
                else:
                    fechaStart = fbScrap.scrollToDate(registro=r,fechaInicio=fechaInicio)
                    posts = fbScrap.getPost(registro=r, posts=posts, elements=fechaStart)

        return posts, invalidos 


    def getFechaInicio(self):
        fechaDadaFormato = False
        while fechaDadaFormato == False:
            try:
                print('----------------------------------------------\nIntroduce la fecha de inicio para la búsqueda. ¡Favor de incluir sólo caracteres numéricos!\n----------------------------------------------\nAño: ')
                anho = input()
                if len(anho) != 4:
                    print('----------------------------------------------\nFavor de revisar que el formato del año sea de 4 dígitos.\n----------------------------------------------')
                    continue
                anho = int(anho)
                print('Mes: ')
                mes = input()
                if len(mes) > 2:
                    print('----------------------------------------------\nFavor de revisar que el formato del mes no sea de más de 2 dígitos.\n----------------------------------------------')
                    continue
                mes = int(mes)
                if mes > 12:
                    print('----------------------------------------------\nFavor de revisar que el valor del mes no sea mayor a 12.\n----------------------------------------------')
                    continue
                print('Día: ')
                dia = input()
                if len(dia) > 2:
                    print('----------------------------------------------\nFavor de revisar que el formato del día no sea de más de 2 dígitos.\n----------------------------------------------')
                    continue
                dia = int(dia)
                if dia > 31:
                    print('----------------------------------------------\nFavor de revisar que el valor del dia no sea mayor a 31.\n----------------------------------------------')
                    continue
                fechaDada = datetime.datetime(anho, mes, dia, 00, 00)
                fechaDadaFormato = True
                fechaDadaTexto = str(fechaDada)
                fechaDadaTexto = fechaDadaTexto.split(" ")[0]
                print('----------------------------------------------\nSe obtendrán las publicaciones a partir del',fechaDadaTexto,'\n----------------------------------------------')
            except:
                continue

        return fechaDada



    def scrollToDate(self,registro,fechaInicio):

        driver = super().getDriver()
        rangoFecha = True

        while rangoFecha == True:
            # Revisar que no cambien este tipo de nombres de clases
            cuerpoPublicaciones = driver.find_elements_by_class_name("_1xnd")
            elements = cuerpoPublicaciones[0].find_elements_by_class_name("userContentWrapper")
            # Buscar el año del último elemento de la lista y, si es mayor a 2018, seguir scrolleando
            lastElement = elements[-1]
            fechaPost = lastElement.find_element_by_tag_name("abbr").get_attribute("title")
            fechaPost = datetime.datetime.strptime(fechaPost,'%d/%m/%y %H:%M')

            if fechaPost > fechaInicio:
                driver.find_element_by_tag_name('body').send_keys(Keys.END) 

            # cuando encuentra una fecha más antigua detiene el scrolleo
            else:

                # si se colaron posts más antiguos que la fecha dada en el último scroll down, removerlos de la lista de elementos
                for ele in reversed(elements):
                    extras = ele.find_element_by_tag_name("abbr").get_attribute("title")
                    extras = datetime.datetime.strptime(extras,'%d/%m/%y %H:%M')
                    # extras = extras.split(" ")[0]
                    # extras = int(extras.split("/")[2])
                    if extras < fechaInicio:
                        elements.remove(ele)
                    else: 
                        break
                rangoFecha = False
        # lista de los posts que se van a scrappear
        return elements



    def getPost(self,registro,posts,elements):
        driver = super().getDriver()
        # Revisar que no cambien este tipo de nombres de clases
        cuerpoPublicaciones = driver.find_elements_by_class_name("_1xnd")
        # Se genera un objeto posts, que contiene los datos de cada post de cada página
        for element in elements:
            # Se extrae la info para cada post de una página. Al final se appendean los "post" en el objeto "posts"
            post = {}
            post['idRegistro'] = registro['id']
            post['alias'] = registro['alias']
            post['nombreCom'] = registro['nombreCom']
            post['fecha'] = element.find_element_by_tag_name("abbr").get_attribute('title')

            # Obtener y juntar todos los <p> que hay en un solo post
            txts = element.find_elements_by_tag_name("p")
            texto = ''
            for t in txts:
                texto += t.text + ' '
            if texto == '':
                post['texto'] = 'NULL'
            else:
                post['texto'] = texto

            # Revisar que no cambien este tipo de nombres de clases
            shares = element.find_elements_by_class_name("_3rwx")
            if len(shares) != 0:
                #print(shares[0].text)
                post['shares'] = shares[0].text
            else:
                post['shares'] = 'NULL'


            # Revisar que no cambien este tipo de nombres de clases
            comments = element.find_elements_by_class_name("_3hg-")
            if len(comments) != 0:
                #print(shares[0].text)
                post['comentarios'] = comments[0].text
            else:
                post['comentarios'] = 'NULL'


            # Revisar que no cambien este tipo de nombres de clases
            reacts = element.find_elements_by_class_name("_3dlh")
            if reacts == []:
                post['reacts'] = 'NULL'
            else:
                post['reacts'] = reacts[1].text


                # for e in reacts:
                #     r = e.find_elements_by_tag_name("span")
                #     print(r)
                    # if len(r) != 0:
                    #     post['reacts'] = r[0].text
                    #     print (r[0])
                    # else:
                    #     post['reacts'] = 'NULL'


            # Revisar que no cambien este tipo de nombres de clases
            reactsEmoji = ''
            reactsEm = element.find_elements_by_class_name("_1n9k")
            post['reactsEmoji'] = 'NULL' 
            for i in range(0,len(reactsEm)):
                re = reactsEm[i].get_attribute('data-testid')
                re = re.split("tooltip_")[1]
                if reactsEmoji == '':
                    reactsEmoji += re
                elif re != '':
                    reactsEmoji += ', '+ re
            if reactsEmoji == '':
                post['reactsEmoji'] = 'NULL'
            else:
                post['reactsEmoji'] = reactsEmoji


            # reactsEmoji = []
            # emojis = {'Me gusta':3,'Me encanta':4,'Me enoja':5,'Me asombra':6,'Me divierte':7,'Me entristece':8}
            # for i in range(3,9):
            #     className = '_7j0'+str(i)
            #     try:
            #         emoji = element.find_element_by_class_name(className)
            #         for key,value in emojis.items():    
            #             if value == i:
            #                 reactsEmoji.append(key)
            #                 #print(key)
            #     except:
            #         continue



            # Revisar que no cambien este tipo de nombres de clases
            linkPost = element.find_elements_by_class_name("_5pcq")
            for l in range(0,len(linkPost)):
                link = linkPost[l].get_attribute('href')
                if 'ref=page_internal#' in link:
                    continue
                else:
                    post['link'] = link


            linkImagenes = ''
            descripcionImagenes = ''
            clasesImg = ['scaledImageFitWidth','scaledImageFitHeight']


            for clase in clasesImg:

                linkMedia = element.find_elements_by_class_name(clase)
                #linkMedia = driver.find_elements_by_xpath("//img[contains(@class,'scaledImageFitWidth') or contains(@class, 'scaledImageFitHeight')]")

                for l in range(0,len(linkMedia)):
                    # para obtener el link a la imagen
                    link = linkMedia[l].get_attribute('src')
                    #print('link', link)
                    # Para obtener lo que viene en el alt de la imagen
                    desc = linkMedia[l].get_attribute('alt')
                    #print('descr', desc)

                    # el link a la imagen
                    if linkImagenes == '':
                        linkImagenes += link
                    elif l != '':
                        linkImagenes += ' , '+ link
                    # lo que viene en el alt de la imagen
                    if descripcionImagenes == '':
                        descripcionImagenes += desc
                    elif l != '':
                        descripcionImagenes +='. / '+ desc

                # el link a la imagen
                if linkImagenes == '':
                    post['linkMedia'] = 'NULL'
                else:
                    post['linkMedia'] = linkImagenes
                # lo que viene en el alt de la imagen
                if descripcionImagenes == '':
                    post['descripcionImg'] = 'NULL'
                else:
                    post['descripcionImg'] = descripcionImagenes


            posts.append(post)

            # #crear nuevo objeto para los posts, asociales el reg en cuestión
            # post['fecha'] = element.find_element_by_tag_name("abbr").get_attribute('title')


        return posts




def saveImage(posts):
    m = 0
    print('----------------------------------------------\nGuardando imágenes...')
    for p in posts:
        m+=1
        links = p['linkMedia']
        if links != 'NULL':
            links=links.split(' , ')
            n = 0
            for l in links:
                n+=1
                for attempt in range(0,3):
                    try:
                        urllib.request.urlretrieve(l, "./imagenesPosts/"+str(m)+"_"+str(n)+".png")
                        break
                    except Exception as i:
                        print('Error guardando imagen',str(m)+"_"+str(n)+".png")
                        print(i)


         # extras = extras.split(" ")[0]
                    # extras = int(extras.split("/")[2])



def exportResultsExcel(posts,invalidos):
    archivoExcel = DocumentoExcel("resultadosScrapperFB.xlsx")
    #Se generan dos pestañas, una para los posts extraídos y otra para identificar los alias FB inválidos
    archivoExcel.abreArchivo([{'id':'Posts', 'name':'Posts'},{'id':'AliasInvalido', 'name':'Alias Inválido'}])
    # Títulos del cols: Pestaña de posts extraídos
    archivoExcel.escribeEnHoja('Posts', 'A', 1, 'id', traceback=False, formato=None)
    archivoExcel.escribeEnHoja('Posts', 'B', 1, 'id Registro', traceback=False, formato=None)
    archivoExcel.escribeEnHoja('Posts', 'C', 1, 'Nombre Comercial', traceback=False, formato=None)   
    archivoExcel.escribeEnHoja('Posts', 'D', 1, 'Alias FB', traceback=False, formato=None)
    archivoExcel.escribeEnHoja('Posts', 'E', 1, 'Fecha', traceback=False, formato=None)
    archivoExcel.escribeEnHoja('Posts', 'F', 1, 'Texto', traceback=False, formato=None)
    archivoExcel.escribeEnHoja('Posts', 'G', 1, 'Shares', traceback=False, formato=None)
    archivoExcel.escribeEnHoja('Posts', 'H', 1, 'Comentarios (cant.)', traceback=False, formato=None)
    archivoExcel.escribeEnHoja('Posts', 'I', 1, 'Reacciones (cant.)', traceback=False, formato=None)
    archivoExcel.escribeEnHoja('Posts', 'J', 1, 'Reacciones (emojis)', traceback=False, formato=None)
    archivoExcel.escribeEnHoja('Posts', 'K', 1, 'Link Post', traceback=False, formato=None)
    archivoExcel.escribeEnHoja('Posts', 'L', 1, 'Link(s) Media', traceback=False, formato=None)
    archivoExcel.escribeEnHoja('Posts', 'M', 1, 'Contenido Media', traceback=False, formato=None)

    # Títulos del cols: Pestaña de alias FB inválidos
    archivoExcel.escribeEnHoja('AliasInvalido', 'A', 1, 'id Registro', traceback=False, formato=None)
    archivoExcel.escribeEnHoja('AliasInvalido', 'B', 1, 'Alias FB', traceback=False, formato=None)

    # Para llenar la info de los posts
    j = 1
    # Tiene que pasar de recorrer los registros a recorrer los posts (y a ellos asociarles el registro)
    for r in posts:
        j+=1
        archivoExcel.escribeEnHoja('Posts', 'A', j, j-1, traceback=False, formato=None)
        archivoExcel.escribeEnHoja('Posts', 'B', j, r['idRegistro'], traceback=False, formato=None)
        archivoExcel.escribeEnHoja('Posts', 'C', j, r['nombreCom'], traceback=False, formato=None)
        archivoExcel.escribeEnHoja('Posts', 'D', j, r['alias'], traceback=False, formato=None)
        archivoExcel.escribeEnHoja('Posts', 'E', j, r['fecha'], traceback=False, formato=None)
        archivoExcel.escribeEnHoja('Posts', 'F', j, r['texto'], traceback=False, formato=None)
        archivoExcel.escribeEnHoja('Posts', 'G', j, r['shares'], traceback=False, formato=None)
        archivoExcel.escribeEnHoja('Posts', 'H', j, r['comentarios'], traceback=False, formato=None)
        archivoExcel.escribeEnHoja('Posts', 'I', j, r['reacts'], traceback=False, formato=None)
        archivoExcel.escribeEnHoja('Posts', 'J', j, r['reactsEmoji'], traceback=False, formato=None)
        archivoExcel.escribeEnHoja('Posts', 'K', j, r['link'], traceback=False, formato=None)
        archivoExcel.escribeEnHoja('Posts', 'L', j, r['linkMedia'], traceback=False, formato=None)
        archivoExcel.escribeEnHoja('Posts', 'M', j, r['descripcionImg'], traceback=False, formato=None)

    # Para llenar lo de los alias inválidos
    j = 1
    # Key: id, Value: alias FB
    for key, value in invalidos.items():
        j+=1
        archivoExcel.escribeEnHoja('AliasInvalido', 'A', j, value, traceback=False, formato=None)
        archivoExcel.escribeEnHoja('AliasInvalido', 'B', j, key, traceback=False, formato=None)

    archivoExcel.guardaArchivo()


def obtieneAliasFromExcel():
    return load_workbook(env['pathFileExcel']).active


def main():
    hoja = obtieneAliasFromExcel()
    rowStart = 2
    rAux = 0
    # objeto con los registros únicos
    regs = []
    # obtener info de los registros
    iD = hoja['A'+str(rowStart+rAux)].value
    nombreCom = hoja['D'+str(rowStart+rAux)].value
    alias = hoja['J'+str(rowStart+rAux)].value
    if iD != None and alias == None:
        alias = 'NA'
    #print(alias, ' alias')
    aliasAux = ''
    aliasUnicos = []

    while alias:
        if alias != 'NA':
            #print('alias válido')
            reg = {}
            alias = str(alias).replace("@", "").replace("'", "").replace("\n","")
            # Llenar objeto regs con registros únicos y != NULL
            if alias not in aliasUnicos:
                #print(regs)
                #registros[iD] = alias
                reg['id'] = iD
                reg['nombreCom'] = nombreCom
                reg['alias'] = alias
                aliasUnicos.append(alias)
                regs.append(reg)

        rAux+=1
        iD = hoja['A'+str(rowStart+rAux)].value
        nombreCom = hoja['D'+str(rowStart+rAux)].value
        alias = hoja['J'+str(rowStart+rAux)].value
        if iD != None and alias == None:
            alias = 'NA'
        #print(alias, ' alias')


    fbScrap = FacebookScrapper( env['credenciales'] )
    fbScrap.start()

    

    busquedaFB = fbScrap.searchFacebookPage(registros=regs, fbScrap=fbScrap)

    #ya incluye info extraida de los posts
    posts = busquedaFB[0]
    inv = busquedaFB[1]


    # #sinceDate = '23/04/2019'
    # #fbScrap.scrollToDate( page['sinceDate'] )


    exportResultsExcel(posts=posts,invalidos=inv)
    saveImage(posts=posts)
    print("----------------------FIN----------------------")
    #print(regs)


if __name__ == "__main__":
    main()