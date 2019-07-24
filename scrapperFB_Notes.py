
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


                fehcaInicial = datetime.datetime.strptime(env['fechaInicial'], '%d/%m/%Y %H:%M')

                if 

                #dateLimit = datetime.datetime.strptime( date, '%d/%m/%Y' )
                #now = datetime.datetime.now()
                print("Fecha encontrada:", fechaAbbr.get_attribute("title"))
                if datetimePost > fechaInicial:



                    print("Entra en el rango")
                else:
                    print("Esta ya no entra")

            except Exception as e:
                print(e)
            
            #input("Pasó algo=??")












            #games = []
            #print("gameslist:",gamesList)
            for g in gamesList:
                print('g-------------',g)
                gameNum+=1
                game = {}
                game['teetime'] = str(tt2)

                game['game'] = str(gameNum)
                game['jugadoresNombre'] = [ str(j['nombre']).replace("None", "") + ' ' + str(j['apellidoPaterno']).replace("None", "") + ' ' + str(j['apellidoMaterno']).replace("None", "") for j in jugadores if str(j['game'])==str(g) ] #Tener cuidado con los Nulls que existen en la BD

                game['lenJugadores'] = str(len(game['jugadoresNombre']))
                hoyo = self.bd.getFields('pairings',['hoyoDeSalida'], whereParams={'id':g})
                print("hoyo:",hoyo)
                #print("Hoyo:",hoyo)
                #Si hoyo es una lista vacía, verificar la que estén los datos bien en pairings
                try:
                    game['hoyo'] = hoyo[0]['hoyoDeSalida']
                    games.append(game)
                except Exception as ex:
                    print("Excepción para game['hoyo'] getDataPairings",ex)
                    pass
            
            return games