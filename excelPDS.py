from libs.pydocsxl import DocumentoExcel


archivoExcel = DocumentoExcel("ejemplo3.xlsx")
archivoExcel.abreArchivo([{'id':'Resumen', 'name':'Resumen'},{'id':'ProxLib', 'name':'Próximas Liberaciones'},{'id':'Nuevos', 'name':'Nuevos'},{'id':'MejorasRel', 'name':'Mejoras Relevantes'},{'id':'MejorasCal', 'name':'Mejoras Calidad'},{'id':'MejorasCos', 'name':'Mejoras Costos'},{'id':'Corporativos', 'name':'Corporativos'},{'id':'Regulatorios', 'name':'Regulatorios'},{'id':'Liberados', 'name':'Liberados'},{'id':'Terminados', 'name':'Terminados'}])

# ESTILOS

titulo = {
			'fuente': { 'nombre':"Tahoma", 'color':'0070C2'},
			'bold'	: True,
			'italic': False,
			'fill'	: { 'colorHex':'ffffff', 'tipo':'solid'},
			'size'	: 12,
			'border': {'tipo':"borders.BORDER_THIN", 'color':'ffffff'},
			'alignment':{'horiz':"left",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}

subtitulo = {
			'fuente': { 'nombre':"Tahoma", 'color':'0070C2'},
			'bold'	: False,
			'italic': False,
			'fill'	: { 'colorHex':'ffffff', 'tipo':'solid'},
			'size'	: 12,
			'alignment':{'horiz':"left",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}

subtitulo2 = {
			'fuente': { 'nombre':"Tahoma", 'color':'000000'},
			'bold'	: True,
			'italic': False,
			'fill'	: { 'colorHex':'D3D3D3', 'tipo':'solid'},
			'size'	: 11,
			'border': {'tipo':"borders.BORDER_THIN", 'color':'ffffff'},
			'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}

subtitulo3 = {
			'fuente': { 'nombre':"Tahoma", 'color':'000000'},
			'bold'	: True,
			'italic': False,
			'fill'	: { 'colorHex':'ffffff', 'tipo':'solid'},
			'size'	: 14,
			'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}

tituloAzulBlanco = {
			'fuente': { 'nombre':"Tahoma", 'color':'ffffff'},
			'bold'	: True,
			'italic': False,
			'fill'	: { 'colorHex':'00286C', 'tipo':'solid'},
			'size'	: 11,
			'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}
		
tituloAzulBlancoBorde = {
			'fuente': { 'nombre':"Tahoma", 'color':'ffffff'},
			'bold'	: True,
			'italic': False,
			'fill'	: { 'colorHex':'00286C', 'tipo':'solid'},
			'size'	: 10,
			'border': {'tipo':"borders.BORDER_THIN", 'color':'ffffff'},
			'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}

tituloAzulClaroBlanco = {
			'fuente': { 'nombre':"Tahoma", 'color':'ffffff'},
			'bold'	: True,
			'italic': False,
			'fill'	: { 'colorHex':'0070C2', 'tipo':'solid'},
			'size'	: 9,
			'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}

tituloAzulClaroBlancoBorde = {
			'fuente': { 'nombre':"Tahoma", 'color':'ffffff'},
			'bold'	: True,
			'italic': False,
			'fill'	: { 'colorHex':'0070C2', 'tipo':'solid'},
			'size'	: 9,
			'border': {'tipo':"borders.BORDER_THIN", 'color':'ffffff'},
			'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}


tituloRojo = {
			'fuente': { 'nombre':"Tahoma", 'color':'ffffff'},
			'bold'	: True,
			'italic': False,
			'fill'	: { 'colorHex':'D70002', 'tipo':'solid'},
			'size'	: 9,
			'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}


cuerpo = {
			'fuente': { 'nombre':"Tahoma", 'color':'000000'},
			'bold'	: False,
			'italic': False,
			'fill'	: { 'colorHex':'ffffff', 'tipo':'solid'},
			'size'	: 9,
			'border': {'tipo':"borders.BORDER_THIN", 'color':'000000'},
			'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}


cuerpoBold = {
			'fuente': { 'nombre':"Tahoma", 'color':'000000'},
			'bold'	: True,
			'italic': False,
			'fill'	: { 'colorHex':'ffffff', 'tipo':'solid'},
			'size'	: 9,
			'border': {'tipo':"borders.BORDER_THIN", 'color':'000000'},
			'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}

cuerpoIzq = {
			'fuente': { 'nombre':"Tahoma", 'color':'000000'},
			'bold'	: False,
			'italic': False,
			'fill'	: { 'colorHex':'ffffff', 'tipo':'solid'},
			'size'	: 9,
			'border': {'tipo':"borders.BORDER_THIN", 'color':'000000'},
			'alignment':{'horiz':"left",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}

cuerpoVertical = {
			'fuente': { 'nombre':"Tahoma", 'color':'000000'},
			'bold'	: False,
			'italic': False,
			'fill'	: { 'colorHex':'E7E7E7', 'tipo':'solid'},
			'size'	: 9,
			'border': {'tipo':"borders.BORDER_THIN", 'color':'000000'},
			'alignment':{'horiz':"center",'vert':"center", 'rotation':90,'wrap':True, 'shrink':False,'indent':0}
		}

cuerpoNoVertical = {
			'fuente': { 'nombre':"Tahoma", 'color':'000000'},
			'bold'	: False,
			'italic': False,
			'fill'	: { 'colorHex':'E7E7E7', 'tipo':'solid'},
			'size'	: 9,
			'border': {'tipo':"borders.BORDER_THIN", 'color':'000000'},
			'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}


cuerpoVerde = {
			'fuente': { 'nombre':"Tahoma", 'color':'ffffff'},
			'bold'	: False,
			'italic': False,
			'fill'	: { 'colorHex':'00AE02', 'tipo':'solid'},
			'size'	: 9,
			'border': {'tipo':"borders.BORDER_THIN", 'color':'000000'},
			'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}


cuerpoVerdeClaro = {
			'fuente': { 'nombre':"Tahoma", 'color':'000000'},
			'bold'	: False,
			'italic': False,
			'fill'	: { 'colorHex':'90FA96', 'tipo':'solid'},
			'size'	: 9,
			'border': {'tipo':"borders.BORDER_THIN", 'color':'000000'},
			'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}

cuerpoVerdeBold = {
			'fuente': { 'nombre':"Tahoma", 'color':'ffffff'},
			'bold'	: True,
			'italic': False,
			'fill'	: { 'colorHex':'00AE02', 'tipo':'solid'},
			'size'	: 9,
			'border': {'tipo':"borders.BORDER_THIN", 'color':'000000'},
			'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}


cuerpoVerdeClaroBold = {
			'fuente': { 'nombre':"Tahoma", 'color':'000000'},
			'bold'	: True,
			'italic': False,
			'fill'	: { 'colorHex':'90FA96', 'tipo':'solid'},
			'size'	: 9,
			'border': {'tipo':"borders.BORDER_THIN", 'color':'000000'},
			'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
		}

rellenoGris = {
		'fill'	: { 'colorHex':'696969', 'tipo':'solid'}
}


cuerpoRellenoGris = {
		'fuente': { 'nombre':"Tahoma", 'color':'ffffff'},
		'bold'	: True,
		'italic': False,
		'fill'	: { 'colorHex':'696969', 'tipo':'solid'},
		'size'	: 10,
		'border': {'tipo':"borders.BORDER_THIN", 'color':'ffffff'},
		'alignment':{'horiz':"center",'vert':"center", 'rotation':0,'wrap':True, 'shrink':False,'indent':0}
}





# Json en forma de Dict
jsonRoadmap = {
	

	'Resumen':{
		'EnProceso':[
			{
				'MERCADO': 'Empresarial',
				'Nuevos':5,
				'MejorasIng':2,
				'MejorasCal':9,
				'MejorasCos':10,
				'TOTAL':24
			},
			{
				'MERCADO': 'PyME',
				'Nuevos':15,
				'MejorasIng':3,
				'MejorasCal':17,
				'MejorasCos':1,
				'TOTAL':28
			},
			{
				'MERCADO': 'Residencial',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'DT y AR',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'Finanzas',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'Recursos Humanos',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'Regulatorio',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'TOTAL',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			}

		],
		'Liberados':[
			{
				'MERCADO': 'Empresarial2',
				'Nuevos':15,
				'MejorasIng':3,
				'MejorasCal':23,
				'MejorasCos':1,
				'TOTAL':34
			},
			{
				'MERCADO': 'PyME2',
				'Nuevos':7,
				'MejorasIng':2,
				'MejorasCal':7,
				'MejorasCos':3,
				'TOTAL':19
			},
			{
				'MERCADO': 'Residencial',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'DT y AR',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'Finanzas',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'Recursos Humanos',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'Regulatorio',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'TOTAL',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			}
		],
		'TOTAL':[
			{
				'MERCADO': 'Empresarial3',
				'Nuevos':15,
				'MejorasIng':3,
				'MejorasCal':23,
				'MejorasCos':1,
				'TOTAL':34
			},
			{
				'MERCADO': 'PyME3',
				'Nuevos':7,
				'MejorasIng':2,
				'MejorasCal':7,
				'MejorasCos':3,
				'TOTAL':19
			},
			{
				'MERCADO': 'Residencial',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'DT y AR',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'Finanzas',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'Recursos Humanos',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'Regulatorio',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			},
			{
				'MERCADO': 'TOTAL',
				'Nuevos':45,
				'MejorasIng':13,
				'MejorasCal':31,
				'MejorasCos':19,
				'TOTAL':127
			}
		],
		'Info':'ROADMAP 2018'
	},
	
	'ProxLib':{
		'Datos':[

			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},


			{	
				'MERCADO':'Empresarial',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{	
				'MERCADO':'Empresarial',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{	
				'MERCADO':'Empresarial',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{	
				'MERCADO':'Empresarial',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},


			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{	
				'MERCADO':'Empresarial',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{	
				'MERCADO':'Empresarial',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},


			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{	
				'MERCADO':'Empresarial',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{	
				'MERCADO':'Empresarial',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			}
		],
		'Info':
			{
				'TABLA':'STATUS DE LAS PRÓXIMAS LIBERACIONES AL 10/09/2018',
				'TOTAL':9
			}
	},


	'Nuevos':{

		'Datos':[

			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},


			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			}


		], #fin datos de nuevos

		'Info':
			{
				'TABLA':'ROADMAP 2018: Proyectos Nuevos',
				'TOTAL':12
			}

	}, #fin nuevos

	'MejorasRel':{

		'Datos':[

			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},


			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			}
		], #fin datos 

		'Info':
			{
				'TABLA':'ROADMAP 2018: Proyectos Nuevos',
				'TOTAL':12
			}

	}, #fin nuevos


	'MejorasCal':{

		'Datos':[


			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},


			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			}
		], #fin datos 

		'Info':
			{
				'TABLA':'ROADMAP 2018: Proyectos Nuevos',
				'TOTAL':12
			}

	}, #fin nuevos



	'MejorasCos':{

		'Datos':[


			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},


			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			}
		], #fin datos 

		'Info':
			{
				'TABLA':'ROADMAP 2018: Proyectos Nuevos',
				'TOTAL':12
			}

	}, #fin nuevos


	'Corporativos':{

		'Datos':[


			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},


			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			}
		], #fin datos 

		'Info':
			{
				'TABLA':'ROADMAP 2018: Proyectos Nuevos',
				'TOTAL':12
			}

	}, #fin nuevos


	'Regulatorios':{

		'Datos':[


			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'4°',
				'SOLUCION':'Grabación Telmex',
				'TIPO':'Ingresos',
				'VALOR':'38.80',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},


			{
				'MERCADO':'Empresarial',
				'Q':'1° 2019',
				'SOLUCION':'Nube SAP HEC',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'10/10/2018',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'PYME-2',
				'Q':'4°',
				'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
				'TIPO':'Ingresos',
				'VALOR':'38',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			},
			{
				'MERCADO':'Residencial',
				'Q':'4°',
				'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
				'TIPO':'Ingresos',
				'VALOR':'38.00',
				'LIDER':'Oscar Arreola',
				'STATUS':'Diseño',
				'LIBERACION':'Por Definir',
				'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
			}
		], #fin datos 

		'Info':
			{
				'TABLA':'ROADMAP 2018: Proyectos Nuevos',
				'TOTAL':12
			}

	}, #fin nuevos


	'Liberados':{
		'Nuevos':{

			'Datos':[


				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},


				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				}
			], #fin datos de nuevos

			'Info':
				{
					'TABLA':'ROADMAP 2018: Proyectos Nuevos',
					'TOTAL':12
				}

		}, #fin nuevos

		'MejorasRel':{

			'Datos':[

				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},


				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				}
			], #fin datos 

			'Info':
				{
					'TABLA':'ROADMAP 2018: Proyectos Nuevos',
					'TOTAL':12
				}

		}, #fin nuevos


		'MejorasCal':{

			'Datos':[

				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},


				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				}
			], #fin datos 

			'Info':
				{
					'TABLA':'ROADMAP 2018: Proyectos Nuevos',
					'TOTAL':12
				}

		}, #fin nuevos



		'MejorasCos':{

			'Datos':[

				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},


				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				}
			], #fin datos 

			'Info':
				{
					'TABLA':'ROADMAP 2018: Proyectos Nuevos',
					'TOTAL':12
				}

		}, #fin nuevos


		'Corporativos':{

			'Datos':[

				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},


				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				}
			], #fin datos 

			'Info':
				{
					'TABLA':'ROADMAP 2018: Proyectos Nuevos',
					'TOTAL':12
				}

		}, #fin nuevos


		'Regulatorios':{

			'Datos':[

				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},


				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				}
			], #fin datos 

			'Info':
				{
					'TABLA':'ROADMAP 2018: Proyectos Nuevos',
					'TOTAL':12
				}

		},

		'Info':'Liberados 179'

	}, #fin liberados

	'Terminados':{

		'Nuevos':{

			'Datos':[

				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},


				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				}
			], #fin datos de nuevos

			'Info':
				{
					'TABLA':'ROADMAP 2018: Proyectos Nuevos',
					'TOTAL':12
				}

		}, #fin nuevos

		'MejorasRel':{

			'Datos':[

				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},


				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				}
			], #fin datos 

			'Info':
				{
					'TABLA':'ROADMAP 2018: Proyectos Nuevos',
					'TOTAL':12
				}

		}, #fin nuevos


		'MejorasCal':{

			'Datos':[

				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},


				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				}
			], #fin datos 

			'Info':
				{
					'TABLA':'ROADMAP 2018: Proyectos Nuevos',
					'TOTAL':12
				}

		}, #fin nuevos



		'MejorasCos':{

			'Datos':[

				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},


				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				}
			], #fin datos 

			'Info':
				{
					'TABLA':'ROADMAP 2018: Proyectos Nuevos',
					'TOTAL':12
				}

		}, #fin nuevos


		'Corporativos':{

			'Datos':[

				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},


				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				}
			], #fin datos 

			'Info':
				{
					'TABLA':'ROADMAP 2018: Proyectos Nuevos',
					'TOTAL':12
				}

		}, #fin nuevos


		'Regulatorios':{

			'Datos':[

				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'4°',
					'SOLUCION':'Grabación Telmex',
					'TIPO':'Ingresos',
					'VALOR':'38.80',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},


				{
					'MERCADO':'Empresarial',
					'Q':'1° 2019',
					'SOLUCION':'Nube SAP HEC',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'10/10/2018',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'PYME-2',
					'Q':'4°',
					'SOLUCION':'Comunicaciones Unificadas Avanzadas - Microsoft',
					'TIPO':'Ingresos',
					'VALOR':'38',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				},
				{
					'MERCADO':'Residencial',
					'Q':'4°',
					'SOLUCION':'INFINITUM + PREMIUM - (Promociones)',
					'TIPO':'Ingresos',
					'VALOR':'38.00',
					'LIDER':'Oscar Arreola',
					'STATUS':'Diseño',
					'LIBERACION':'Por Definir',
					'DEPENDENCIA':'- Inicio de prueba de concepto CUAD Microsoft en laboratorio. | Mario López/ Jaime Alfaro | 10/09/2018'
				}
			], #fin datos 

			'Info':
				{
					'TABLA':'ROADMAP 2018: Proyectos Nuevos',
					'TOTAL':12
				}

		},

		'Info':'Liberados 179'

	} #fin termiandos
}





####   RESUMEN --------------------------¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡----------------------¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡

archivoExcel.mergeCeldas('Resumen',1,1,1,4)
archivoExcel.mergeCeldas('Resumen',1,5,1,6)
archivoExcel.mergeCeldas('Resumen',2,1,2,5)
archivoExcel.mergeCeldas('Resumen',3,1,3,6)
#ROWS
archivoExcel.dimensionaRows('Resumen',1,25)
archivoExcel.dimensionaRows('Resumen',2,25)
archivoExcel.dimensionaRows('Resumen',3,25)
#COLS
archivoExcel.dimensionaCols('Resumen','A',25)
archivoExcel.dimensionaCols('Resumen','B',20)
archivoExcel.dimensionaCols('Resumen','C',20)
archivoExcel.dimensionaCols('Resumen','D',20)
archivoExcel.dimensionaCols('Resumen','E',20)
archivoExcel.dimensionaCols('Resumen','F',20)

# LOGOS
archivoExcel.addImageToCell('Resumen','tmx_logo.png','E1')

# TITLE
archivoExcel.escribeEnHoja('Resumen', 'A', 1, 'Dirección de Desarrollo Tecnológico', traceback=False, formato=titulo)
archivoExcel.escribeEnHoja('Resumen', 'A', 2, 'Subdirección de Desarrollo de Soluciones', traceback=False, formato=subtitulo)
archivoExcel.escribeEnHoja('Resumen', 'E', 1, '', traceback=False, formato=subtitulo)
archivoExcel.escribeEnHoja('Resumen', 'F', 2, '', traceback=False, formato=subtitulo)
archivoExcel.escribeEnHoja('Resumen', 'A', 3, jsonRoadmap['Resumen']['Info'], traceback=False, formato=subtitulo3)

#CUERPO
n = 4

tabls = ['EnProceso','Liberados','TOTAL']

try:
	for tabl in tabls:
	#for j in range(1,len(jsonRoadmap['Resumen'])):
		# espacio en blanco
		archivoExcel.mergeCeldas('Resumen',n,1,n,6) 
		archivoExcel.escribeEnHoja('Resumen', 'A', n, '', traceback=False, formato=subtitulo)
		 #EN proceso, Liberados, Total
		archivoExcel.mergeCeldas('Resumen',n+1,1,n+1,6)
		archivoExcel.dimensionaRows('Resumen',n+1,20)

		#formato headers
		archivoExcel.mergeCeldas('Resumen',n+2,3,n+2,5)
		archivoExcel.mergeCeldas('Resumen',n+2,1,n+3,1)
		archivoExcel.mergeCeldas('Resumen',n+2,2,n+3,2)
		archivoExcel.mergeCeldas('Resumen',n+2,6,n+3,6)

		#Headers
		archivoExcel.escribeEnHoja('Resumen', 'A', n+2, 'Cliente', traceback=False, formato=tituloAzulClaroBlancoBorde)
		archivoExcel.escribeEnHoja('Resumen', 'B', n+2, 'Nuevos', traceback=False, formato=tituloAzulClaroBlancoBorde)
		archivoExcel.escribeEnHoja('Resumen', 'C', n+2, 'Mejoras', traceback=False, formato=tituloAzulClaroBlancoBorde)
		archivoExcel.escribeEnHoja('Resumen', 'F', n+2, 'Total', traceback=False, formato=tituloAzulClaroBlancoBorde)
		archivoExcel.escribeEnHoja('Resumen', 'C', n+3, 'Ingresos', traceback=False, formato=tituloAzulClaroBlancoBorde)
		archivoExcel.escribeEnHoja('Resumen', 'D', n+3, 'Calidad', traceback=False, formato=tituloAzulClaroBlancoBorde)
		archivoExcel.escribeEnHoja('Resumen', 'E', n+3, 'Costos', traceback=False, formato=tituloAzulClaroBlancoBorde)
		#Para que los bordes no se vean cheucos
		archivoExcel.escribeEnHoja('Resumen', 'A', n+3, '', traceback=False, formato=tituloAzulClaroBlancoBorde)
		archivoExcel.escribeEnHoja('Resumen', 'B', n+3, '', traceback=False, formato=tituloAzulClaroBlancoBorde)
		archivoExcel.escribeEnHoja('Resumen', 'D', n+2, '', traceback=False, formato=tituloAzulClaroBlancoBorde)
		archivoExcel.escribeEnHoja('Resumen', 'E', n+2, '', traceback=False, formato=tituloAzulClaroBlancoBorde)
		archivoExcel.escribeEnHoja('Resumen', 'F', n+3, '', traceback=False, formato=tituloAzulClaroBlancoBorde)
		
		d = 4
		for j in range(0,len(jsonRoadmap['Resumen'][tabl])):
			if jsonRoadmap['Resumen'][tabl][j]['MERCADO'] == 'TOTAL':
				archivoExcel.escribeEnHoja('Resumen', 'A', d+n, jsonRoadmap['Resumen'][tabl][j]['MERCADO'], traceback=False, formato=cuerpoRellenoGris)
				archivoExcel.escribeEnHoja('Resumen', 'B', d+n, jsonRoadmap['Resumen'][tabl][j]['Nuevos'], traceback=False, formato=cuerpoRellenoGris)
				archivoExcel.escribeEnHoja('Resumen', 'C', d+n, jsonRoadmap['Resumen'][tabl][j]['MejorasIng'], traceback=False, formato=cuerpoRellenoGris)
				archivoExcel.escribeEnHoja('Resumen', 'D', d+n, jsonRoadmap['Resumen'][tabl][j]['MejorasCal'], traceback=False, formato=cuerpoRellenoGris)
				archivoExcel.escribeEnHoja('Resumen', 'E', d+n, jsonRoadmap['Resumen'][tabl][j]['MejorasCos'], traceback=False, formato=cuerpoRellenoGris)
				archivoExcel.escribeEnHoja('Resumen', 'F', d+n, jsonRoadmap['Resumen'][tabl][j]['TOTAL'], traceback=False, formato=cuerpoRellenoGris)
				archivoExcel.dimensionaRows('Resumen', d+n, 18)

			else: 
				archivoExcel.escribeEnHoja('Resumen', 'A', d+n, jsonRoadmap['Resumen'][tabl][j]['MERCADO'], traceback=False, formato=cuerpoNoVertical)
				archivoExcel.escribeEnHoja('Resumen', 'B', d+n, jsonRoadmap['Resumen'][tabl][j]['Nuevos'], traceback=False, formato=cuerpo)
				archivoExcel.escribeEnHoja('Resumen', 'C', d+n, jsonRoadmap['Resumen'][tabl][j]['MejorasIng'], traceback=False, formato=cuerpo)
				archivoExcel.escribeEnHoja('Resumen', 'D', d+n, jsonRoadmap['Resumen'][tabl][j]['MejorasCal'], traceback=False, formato=cuerpo)
				archivoExcel.escribeEnHoja('Resumen', 'E', d+n, jsonRoadmap['Resumen'][tabl][j]['MejorasCos'], traceback=False, formato=cuerpo)
				archivoExcel.escribeEnHoja('Resumen', 'F', d+n, jsonRoadmap['Resumen'][tabl][j]['TOTAL'], traceback=False, formato=cuerpo)
			d+=1
			
		n+= 12

	archivoExcel.escribeEnHoja('Resumen', 'A', 5, 'EN PROCESO', traceback=False, formato=tituloAzulBlanco)
	archivoExcel.dimensionaRows('Resumen',4,12)
	archivoExcel.dimensionaRows('Resumen',5,28)

	archivoExcel.escribeEnHoja('Resumen', 'A', 17, 'LIBERADOS', traceback=False, formato=tituloAzulBlanco)
	archivoExcel.dimensionaRows('Resumen',16,24)
	archivoExcel.dimensionaRows('Resumen',17,28)

	archivoExcel.escribeEnHoja('Resumen', 'A', 29, 'TOTAL', traceback=False, formato=tituloAzulBlanco)
	archivoExcel.dimensionaRows('Resumen',28,24)
	archivoExcel.dimensionaRows('Resumen',29,28)


except:
	print('Resumen no tiene datos'+str(n))



####   PROX LIBERACIONES--------------------------¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡----------------------¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡

archivoExcel.mergeCeldas('ProxLib',1,1,1,7)
archivoExcel.mergeCeldas('ProxLib',2,1,2,7)
archivoExcel.mergeCeldas('ProxLib',3,1,3,7)
#Rows' height
archivoExcel.dimensionaRows('ProxLib',1,25)
archivoExcel.dimensionaRows('ProxLib',2,25)
archivoExcel.dimensionaRows('ProxLib',3,25)
archivoExcel.dimensionaRows('ProxLib',4,25)
#Cols' width
archivoExcel.dimensionaCols('ProxLib','A',13)
archivoExcel.dimensionaCols('ProxLib','B',42)
archivoExcel.dimensionaCols('ProxLib','C',13)
archivoExcel.dimensionaCols('ProxLib','D',13)
archivoExcel.dimensionaCols('ProxLib','E',13)
archivoExcel.dimensionaCols('ProxLib','F',13)
archivoExcel.dimensionaCols('ProxLib','G',13)
archivoExcel.dimensionaCols('ProxLib','H',56)

# LOGOS
archivoExcel.addImageToCell('ProxLib','tmx_logo.png','H1')

# TITLE
archivoExcel.escribeEnHoja('ProxLib', 'A', 1, 'Dirección de Desarrollo Tecnológico', traceback=False, formato=titulo)
archivoExcel.escribeEnHoja('ProxLib', 'A', 2, 'Subdirección de Desarrollo de Soluciones', traceback=False, formato=subtitulo)
archivoExcel.escribeEnHoja('ProxLib', 'H', 1, '', traceback=False, formato=subtitulo)
archivoExcel.escribeEnHoja('ProxLib', 'H', 2, '', traceback=False, formato=subtitulo)

# HEADERS
archivoExcel.escribeEnHoja('ProxLib', 'A', 4, '', traceback=False, formato=tituloAzulClaroBlancoBorde)
archivoExcel.escribeEnHoja('ProxLib', 'B', 4, 'SOLUCIÓN', traceback=False, formato=tituloAzulClaroBlancoBorde)
archivoExcel.escribeEnHoja('ProxLib', 'C', 4, 'TIPO', traceback=False, formato=tituloAzulClaroBlancoBorde)
archivoExcel.escribeEnHoja('ProxLib', 'D', 4, 'VALOR (MDP a 3 años)', traceback=False, formato=tituloAzulClaroBlancoBorde)
archivoExcel.escribeEnHoja('ProxLib', 'E', 4, 'LÍDER DE PRODUCTO', traceback=False, formato=tituloAzulClaroBlancoBorde)
archivoExcel.escribeEnHoja('ProxLib', 'F', 4, 'STATUS', traceback=False, formato=tituloAzulClaroBlancoBorde)
archivoExcel.escribeEnHoja('ProxLib', 'G', 4, 'LIBERACIÓN', traceback=False, formato=tituloAzulClaroBlancoBorde)
archivoExcel.escribeEnHoja('ProxLib', 'H', 4, 'DEPENDENCIA CRÍTICA', traceback=False, formato=tituloRojo)

# CUERPO
# Declarar vars 
l1=[]
l2=[]
cl=''
mk = ''
x = 5
y = 0

# En caso de que no haya datos para alguna de las páginas del archivo (mientras hago pruebas)
try:
	archivoExcel.escribeEnHoja('ProxLib', 'A', 3, jsonRoadmap['ProxLib']['Info']['TABLA'], traceback=False, formato=tituloAzulBlancoBorde)
	# Para poenr borde blanco a todas las columnas de las celdas mergeadas del título de la tabla
	archivoExcel.escribeEnHoja('ProxLib', 'B', 3, '', traceback=False, formato=tituloAzulBlancoBorde)
	archivoExcel.escribeEnHoja('ProxLib', 'C', 3, '', traceback=False, formato=tituloAzulBlancoBorde)
	archivoExcel.escribeEnHoja('ProxLib', 'D', 3, '', traceback=False, formato=tituloAzulBlancoBorde)
	archivoExcel.escribeEnHoja('ProxLib', 'E', 3, '', traceback=False, formato=tituloAzulBlancoBorde)
	archivoExcel.escribeEnHoja('ProxLib', 'F', 3, '', traceback=False, formato=tituloAzulBlancoBorde)
	archivoExcel.escribeEnHoja('ProxLib', 'G', 3, '', traceback=False, formato=tituloAzulBlancoBorde)

	archivoExcel.escribeEnHoja('ProxLib', 'H', 3, 'TOTAL = '+str(jsonRoadmap['ProxLib']['Info']['TOTAL']), traceback=False, formato=tituloAzulBlancoBorde)
	archivoExcel.escribeEnHoja('ProxLib', 'H', len(jsonRoadmap['ProxLib']['Datos'])+5, 'TOTAL = '+str(jsonRoadmap['ProxLib']['Info']['TOTAL']), traceback=False, formato=tituloAzulBlancoBorde)
	archivoExcel.mergeCeldas('ProxLib',len(jsonRoadmap['ProxLib']['Datos'])+5,1,len(jsonRoadmap['ProxLib']['Datos'])+5,7)
	archivoExcel.dimensionaRows('ProxLib',len(jsonRoadmap['ProxLib']['Datos'])+5,20)
	archivoExcel.escribeEnHoja('ProxLib', 'A', len(jsonRoadmap['ProxLib']['Datos'])+5, '', traceback=False, formato=rellenoGris)

	
	for j in range(0,len(jsonRoadmap['ProxLib']['Datos'])):
		
		archivoExcel.escribeEnHoja('ProxLib', 'A', j+5, jsonRoadmap['ProxLib']['Datos'][j]['MERCADO'], traceback=False, formato=cuerpoNoVertical)
		archivoExcel.escribeEnHoja('ProxLib', 'B', j+5, jsonRoadmap['ProxLib']['Datos'][j]['SOLUCION'], traceback=False, formato=cuerpoBold)
		archivoExcel.escribeEnHoja('ProxLib', 'C', j+5, jsonRoadmap['ProxLib']['Datos'][j]['TIPO'], traceback=False, formato=cuerpo)
		#cambiar a formato currency en el excel. No hay una funcion para hacerlo directo, lo más cercano es self.__excelFile[ hoja ].number_format = u'"$ "#,###.00'
		archivoExcel.escribeEnHoja('ProxLib', 'D', j+5, jsonRoadmap['ProxLib']['Datos'][j]['VALOR'], traceback=False, formato=cuerpo)
		archivoExcel.escribeEnHoja('ProxLib', 'E', j+5, jsonRoadmap['ProxLib']['Datos'][j]['LIDER'], traceback=False, formato=cuerpo)
		archivoExcel.escribeEnHoja('ProxLib', 'F', j+5, jsonRoadmap['ProxLib']['Datos'][j]['STATUS'], traceback=False, formato=cuerpo)
		# bold cuendo fecha ya nob está Por Definir
		if '/' in jsonRoadmap['ProxLib']['Datos'][j]['LIBERACION']:
			archivoExcel.escribeEnHoja('ProxLib', 'G', j+5, jsonRoadmap['ProxLib']['Datos'][j]['LIBERACION'], traceback=False, formato=cuerpoBold)
		else:
			archivoExcel.escribeEnHoja('ProxLib', 'G', j+5, jsonRoadmap['ProxLib']['Datos'][j]['LIBERACION'], traceback=False, formato=cuerpo)
		archivoExcel.escribeEnHoja('ProxLib', 'H', j+5, jsonRoadmap['ProxLib']['Datos'][j]['DEPENDENCIA'], traceback=False, formato=cuerpoIzq)


except:
	print('Prox. Liberaciones no tiene datos')




# loop through pestañas del archivo que tienen la misma estructura-----------------------¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡----------------------¡¡¡¡¡¡¡¡¡¡¡¡¡¡
tabs = ['Nuevos', 'MejorasRel','MejorasCal', 'MejorasCos', 'Corporativos', 'Regulatorios']


#Para tablas en pestaña de liberados y termiandos
iniLib = 4
iniTer = 4

# iterar por las pestañas del archivo
for tab in tabs:
	#CELL FORMAT 
	#Merge
	archivoExcel.mergeCeldas(tab,1,1,1,8)
	archivoExcel.mergeCeldas(tab,2,1,2,8)
	archivoExcel.mergeCeldas(tab,3,1,3,8)
	#Rows' height
	archivoExcel.dimensionaRows(tab,1,25)
	archivoExcel.dimensionaRows(tab,2,25)
	archivoExcel.dimensionaRows(tab,3,25)
	archivoExcel.dimensionaRows(tab,4,25)
	#Cols' width
	archivoExcel.dimensionaCols(tab,'A',5)
	archivoExcel.dimensionaCols(tab,'B',5)
	archivoExcel.dimensionaCols(tab,'C',42)
	archivoExcel.dimensionaCols(tab,'D',13)
	archivoExcel.dimensionaCols(tab,'E',13)
	archivoExcel.dimensionaCols(tab,'F',13)
	archivoExcel.dimensionaCols(tab,'G',13)
	archivoExcel.dimensionaCols(tab,'H',13)
	archivoExcel.dimensionaCols(tab,'I',56)


	# LOGOS
	archivoExcel.addImageToCell(tab,'tmx_logo.png','I1')
	
	# TITLE
	archivoExcel.escribeEnHoja(tab, 'A', 1, 'Dirección de Desarrollo Tecnológico', traceback=False, formato=titulo)
	archivoExcel.escribeEnHoja(tab, 'A', 2, 'Subdirección de Desarrollo de Soluciones', traceback=False, formato=subtitulo)
	archivoExcel.escribeEnHoja(tab, 'I', 1, '', traceback=False, formato=subtitulo)
	archivoExcel.escribeEnHoja(tab, 'I', 2, '', traceback=False, formato=subtitulo)

	# HEADERS
	archivoExcel.escribeEnHoja(tab, 'A', 4, '', traceback=False, formato=tituloAzulClaroBlancoBorde)
	archivoExcel.escribeEnHoja(tab, 'B', 4, 'Q', traceback=False, formato=tituloAzulClaroBlancoBorde)
	archivoExcel.escribeEnHoja(tab, 'C', 4, 'SOLUCIÓN', traceback=False, formato=tituloAzulClaroBlancoBorde)
	archivoExcel.escribeEnHoja(tab, 'D', 4, 'TIPO', traceback=False, formato=tituloAzulClaroBlancoBorde)
	archivoExcel.escribeEnHoja(tab, 'E', 4, 'VALOR (MDP a 3 años)', traceback=False, formato=tituloAzulClaroBlancoBorde)
	archivoExcel.escribeEnHoja(tab, 'F', 4, 'LÍDER DE PRODUCTO', traceback=False, formato=tituloAzulClaroBlancoBorde)
	archivoExcel.escribeEnHoja(tab, 'G', 4, 'STATUS', traceback=False, formato=tituloAzulClaroBlancoBorde)
	archivoExcel.escribeEnHoja(tab, 'H', 4, 'LIBERACIÓN', traceback=False, formato=tituloAzulClaroBlancoBorde)
	archivoExcel.escribeEnHoja(tab, 'I', 4, 'DEPENDENCIA CRÍTICA', traceback=False, formato=tituloRojo)

	# CUERPO
	# Declarar vars 
	l1=[]
	l2=[]
	mk = ''
	x = 5
	y = 0

	l0=[]
	x1 = 5
	y1 = 0



	# En caso de que no haya datos para alguna de las páginas del archivo (mientras hago pruebas)
	try:
		archivoExcel.escribeEnHoja(tab, 'A', 3, jsonRoadmap[tab]['Info']['TABLA'], traceback=False, formato=tituloAzulBlancoBorde)

		# Para poenr borde blanco a todas las columnas de las celdas mergeadas del título de la tabla
		archivoExcel.escribeEnHoja(tab, 'B', 3, '', traceback=False, formato=tituloAzulBlancoBorde)
		archivoExcel.escribeEnHoja(tab, 'C', 3, '', traceback=False, formato=tituloAzulBlancoBorde)
		archivoExcel.escribeEnHoja(tab, 'D', 3, '', traceback=False, formato=tituloAzulBlancoBorde)
		archivoExcel.escribeEnHoja(tab, 'E', 3, '', traceback=False, formato=tituloAzulBlancoBorde)
		archivoExcel.escribeEnHoja(tab, 'F', 3, '', traceback=False, formato=tituloAzulBlancoBorde)
		archivoExcel.escribeEnHoja(tab, 'G', 3, '', traceback=False, formato=tituloAzulBlancoBorde)
		archivoExcel.escribeEnHoja(tab, 'H', 3, '', traceback=False, formato=tituloAzulBlancoBorde)

		archivoExcel.escribeEnHoja(tab, 'I', 3, 'TOTAL = '+str(jsonRoadmap[tab]['Info']['TOTAL']), traceback=False, formato=tituloAzulBlancoBorde)
		archivoExcel.escribeEnHoja(tab, 'I', len(jsonRoadmap[tab]['Datos'])+5, 'TOTAL = '+str(jsonRoadmap[tab]['Info']['TOTAL']), traceback=False, formato=tituloAzulBlancoBorde)
		archivoExcel.mergeCeldas(tab,len(jsonRoadmap[tab]['Datos'])+5,1,len(jsonRoadmap[tab]['Datos'])+5,8)
		archivoExcel.dimensionaRows(tab,len(jsonRoadmap[tab]['Datos'])+5,20)
		archivoExcel.escribeEnHoja(tab, 'A', len(jsonRoadmap[tab]['Datos'])+5, '', traceback=False, formato=rellenoGris)

		for j in range(0,len(jsonRoadmap[tab]['Datos'])):
			# PARA MERGE CELDAS (COL A)
			if mk != jsonRoadmap[tab]['Datos'][j]['MERCADO']:
				l1.append(jsonRoadmap[tab]['Datos'][j]['MERCADO'])
				l0.append('')
			
			# PARA MERGE CELDAS (COL A)
			l2.append(jsonRoadmap[tab]['Datos'][j]['MERCADO'])
			mk = jsonRoadmap[tab]['Datos'][j]['MERCADO']
			# PARA MERGE CELDAS (COL B)
			l0.append(jsonRoadmap[tab]['Datos'][j]['Q'])

		# PARA MERGE CELDAS (COL A)
		for ele in l1:
			if l2.count(ele) > 1:
				y = x+l2.count(ele)-1
				archivoExcel.mergeCeldas(tab,x,1,y,1)
				x+=l2.count(ele)-1
			x+=1

		# PARA MERGE CELDAS (COL B)
		for ele in range(0,len(l0)):
			if l0[ele] != '' and l0[ele] == l0[ele-1]:
				if y1 == 0:
					y1 = x1
				x1+=1
				if ele == len(l0)-1:
					archivoExcel.mergeCeldas(tab,y1-1,2,x1-1,2)
			elif l0[ele] != '' and l0[ele] != l0[ele-1]:
				if y1 != 0:
					archivoExcel.mergeCeldas(tab,y1-1,2,x1-1,2)
				x1+=1
				y1 = 0

		# Si no se coloca al final (despues de los ele), los bordes no aparecen bien para las celdas con merge		
		for j in range(0,len(jsonRoadmap[tab]['Datos'])):
			
			archivoExcel.escribeEnHoja(tab, 'A', j+5, jsonRoadmap[tab]['Datos'][j]['MERCADO'], traceback=False, formato=cuerpoVertical)
			archivoExcel.escribeEnHoja(tab, 'B', j+5, jsonRoadmap[tab]['Datos'][j]['Q'], traceback=False, formato=cuerpo)
			archivoExcel.escribeEnHoja(tab, 'C', j+5, jsonRoadmap[tab]['Datos'][j]['SOLUCION'], traceback=False, formato=cuerpoBold)
			archivoExcel.escribeEnHoja(tab, 'D', j+5, jsonRoadmap[tab]['Datos'][j]['TIPO'], traceback=False, formato=cuerpo)
			#cambiar a formato currency en el excel. No hay una funcion para hacerlo directo, lo más cercano es self.__excelFile[ hoja ].number_format = u'"$ "#,###.00'
			archivoExcel.escribeEnHoja(tab, 'E', j+5, jsonRoadmap[tab]['Datos'][j]['VALOR'], traceback=False, formato=cuerpo)
			archivoExcel.escribeEnHoja(tab, 'F', j+5, jsonRoadmap[tab]['Datos'][j]['LIDER'], traceback=False, formato=cuerpo)
			archivoExcel.escribeEnHoja(tab, 'G', j+5, jsonRoadmap[tab]['Datos'][j]['STATUS'], traceback=False, formato=cuerpo)
			# bold cuendo fecha ya no está Por Definir
			if '/' in jsonRoadmap[tab]['Datos'][j]['LIBERACION']:
				archivoExcel.escribeEnHoja(tab, 'H', j+5, jsonRoadmap[tab]['Datos'][j]['LIBERACION'], traceback=False, formato=cuerpoBold)
			else:
				archivoExcel.escribeEnHoja(tab, 'H', j+5, jsonRoadmap[tab]['Datos'][j]['LIBERACION'], traceback=False, formato=cuerpo)
			archivoExcel.escribeEnHoja(tab, 'I', j+5, jsonRoadmap[tab]['Datos'][j]['DEPENDENCIA'], traceback=False, formato=cuerpoIzq)


		# PARA PESTAÑA DE LIBERADOS Y TERMINADOS
		#CELL FORMAT 
		#Merge
		tabs2 = ['Liberados','Terminados']
		for tab2 in tabs2:

			if tab2 == 'Liberados':
				ini = iniLib

			elif tab2 == 'Terminados':
				ini = iniTer

			l3=[]
			l4=[]
			mkLibTer = ''
			x2 = 2
			y2 = 0

			l00=[]
			x3 = 2
			y3 = 0



			archivoExcel.mergeCeldas(tab2,1,1,1,8)
			archivoExcel.mergeCeldas(tab2,2,1,2,8)
			archivoExcel.mergeCeldas(tab2,3,1,3,8)
			#Rows' height
			archivoExcel.dimensionaRows(tab2,1,25)
			archivoExcel.dimensionaRows(tab2,2,25)
			archivoExcel.dimensionaRows(tab2,3,25)
			#Cols' width
			archivoExcel.dimensionaCols(tab2,'A',5)
			archivoExcel.dimensionaCols(tab2,'B',5)
			archivoExcel.dimensionaCols(tab2,'C',42)
			archivoExcel.dimensionaCols(tab2,'D',13)
			archivoExcel.dimensionaCols(tab2,'E',13)
			archivoExcel.dimensionaCols(tab2,'F',13)
			archivoExcel.dimensionaCols(tab2,'G',13)
			archivoExcel.dimensionaCols(tab2,'H',13)
			archivoExcel.dimensionaCols(tab2,'I',56)

			# LOGOS
			archivoExcel.addImageToCell(tab2,'tmx_logo.png','I1')

			try:
				# TITLE
				archivoExcel.escribeEnHoja(tab2, 'A', 1, 'Dirección de Desarrollo Tecnológico', traceback=False, formato=titulo)
				archivoExcel.escribeEnHoja(tab2, 'A', 2, 'Subdirección de Desarrollo de Soluciones', traceback=False, formato=subtitulo)
				archivoExcel.escribeEnHoja(tab2, 'I', 1, '', traceback=False, formato=subtitulo)
				archivoExcel.escribeEnHoja(tab2, 'I', 2, '', traceback=False, formato=subtitulo)
				archivoExcel.escribeEnHoja(tab2, 'I', 3, 'TOTAL: '+str(jsonRoadmap[tab2]['Info']), traceback=False, formato=subtitulo2)


				archivoExcel.dimensionaRows(tab2,ini,25)
				archivoExcel.dimensionaRows(tab2,ini+1,25)
				archivoExcel.mergeCeldas(tab2,ini,1,ini,8)
			

				archivoExcel.escribeEnHoja(tab2, 'A', ini, jsonRoadmap[tab2][tab]['Info']['TABLA'], traceback=False, formato=tituloAzulBlancoBorde)

				# Para poenr borde blanco a todas las columnas de las celdas mergeadas del título de la tabla
				archivoExcel.escribeEnHoja(tab2, 'B', ini, '', traceback=False, formato=tituloAzulBlancoBorde)
				archivoExcel.escribeEnHoja(tab2, 'C', ini, '', traceback=False, formato=tituloAzulBlancoBorde)
				archivoExcel.escribeEnHoja(tab2, 'D', ini, '', traceback=False, formato=tituloAzulBlancoBorde)
				archivoExcel.escribeEnHoja(tab2, 'E', ini, '', traceback=False, formato=tituloAzulBlancoBorde)
				archivoExcel.escribeEnHoja(tab2, 'F', ini, '', traceback=False, formato=tituloAzulBlancoBorde)
				archivoExcel.escribeEnHoja(tab2, 'G', ini, '', traceback=False, formato=tituloAzulBlancoBorde)
				archivoExcel.escribeEnHoja(tab2, 'H', ini, '', traceback=False, formato=tituloAzulBlancoBorde)

				archivoExcel.escribeEnHoja(tab2, 'I', ini, 'TOTAL = '+str(jsonRoadmap[tab2][tab]['Info']['TOTAL']), traceback=False, formato=tituloAzulBlancoBorde)
				
				# HEADERS
				archivoExcel.escribeEnHoja(tab2, 'A', ini+1, '', traceback=False, formato=tituloAzulClaroBlancoBorde)
				archivoExcel.escribeEnHoja(tab2, 'B', ini+1, 'Q', traceback=False, formato=tituloAzulClaroBlancoBorde)
				archivoExcel.escribeEnHoja(tab2, 'C', ini+1, 'SOLUCIÓN', traceback=False, formato=tituloAzulClaroBlancoBorde)
				archivoExcel.escribeEnHoja(tab2, 'D', ini+1, 'TIPO', traceback=False, formato=tituloAzulClaroBlancoBorde)
				archivoExcel.escribeEnHoja(tab2, 'E', ini+1, 'VALOR (MDP a 3 años)', traceback=False, formato=tituloAzulClaroBlancoBorde)
				archivoExcel.escribeEnHoja(tab2, 'F', ini+1, 'LÍDER DE PRODUCTO', traceback=False, formato=tituloAzulClaroBlancoBorde)
				archivoExcel.escribeEnHoja(tab2, 'G', ini+1, 'STATUS', traceback=False, formato=tituloAzulClaroBlancoBorde)
				archivoExcel.escribeEnHoja(tab2, 'H', ini+1, 'LIBERACIÓN', traceback=False, formato=tituloAzulClaroBlancoBorde)
				archivoExcel.escribeEnHoja(tab2, 'I', ini+1, 'DEPENDENCIA CRÍTICA', traceback=False, formato=tituloRojo)



				# recorrer los renglones de cada una de las tablas que hay en la pestaña Liberados
				for j in range(0,len(jsonRoadmap[tab2][tab]['Datos'])):
					# Para merge Col A
					if mkLibTer != jsonRoadmap[tab2][tab]['Datos'][j]['MERCADO']:
						l3.append(jsonRoadmap[tab2][tab]['Datos'][j]['MERCADO'])
						# PARA MERGE CELDAS (COL B)
						l00.append('')

					l4.append(jsonRoadmap[tab2][tab]['Datos'][j]['MERCADO'])
					mkLibTer = jsonRoadmap[tab2][tab]['Datos'][j]['MERCADO']
					# PARA MERGE CELDAS (COL B)
					l00.append(jsonRoadmap[tab2][tab]['Datos'][j]['Q'])


				# PARA MERGE CELDAS (COL A)
				for ele in l3:
					if l4.count(ele) > 1:
						y2 = x2+l4.count(ele)-1
						archivoExcel.mergeCeldas(tab2,x2+ini,1,y2+ini,1)
						#print(y2+ini)
						x2+=l4.count(ele)-1
					x2+=1


				# PARA MERGE CELDAS (COL B)
				for ele in range(0,len(l00)):

					# ele es un campo repetido (dentro de un mismo Mercado)
					if l00[ele] != '' and l00[ele] == l00[ele-1]:
						# se define la row inicial (y3) de una cadena de ele repetidos
						if y3 == 0:
							y3 = x3
						x3+=1
						#si se trata del caso de la úlyima ele y resulta ser una repetida (needs to merge)
						if ele == len(l00)-1:
							archivoExcel.mergeCeldas(tab2,y3+ini-1,2,x3+ini-1,2)

					# ele es un campo diferente al del row anterior
					elif l00[ele] != '' and l00[ele] != l00[ele-1]:
						# if el valor de ele se había venido repitiendo en los rows anteriores a este
						if y3 != 0:
							
							archivoExcel.mergeCeldas(tab2,y3+ini-1,2,x3+ini-1,2)
						x3+=1
						# se resetea y3
						y3 = 0


				for j in range(0,len(jsonRoadmap[tab2][tab]['Datos'])):
					archivoExcel.escribeEnHoja(tab2, 'A', ini+2+j, jsonRoadmap[tab2][tab]['Datos'][j]['MERCADO'], traceback=False, formato=cuerpoVertical)
					archivoExcel.escribeEnHoja(tab2, 'B', ini+2+j, jsonRoadmap[tab2][tab]['Datos'][j]['Q'], traceback=False, formato=cuerpo)
					archivoExcel.escribeEnHoja(tab2, 'C', ini+2+j, jsonRoadmap[tab2][tab]['Datos'][j]['SOLUCION'], traceback=False, formato=cuerpoBold)
					archivoExcel.escribeEnHoja(tab2, 'D', ini+2+j, jsonRoadmap[tab2][tab]['Datos'][j]['TIPO'], traceback=False, formato=cuerpo)
					#cambiar a formato currency en el excel. No hay una funcion para hacerlo directo, lo más cercano es self.__excelFile[ hoja ].number_format = u'"$ "#,###.00'
					archivoExcel.escribeEnHoja(tab2, 'E', ini+2+j, jsonRoadmap[tab]['Datos'][j]['VALOR'], traceback=False, formato=cuerpo)
					archivoExcel.escribeEnHoja(tab2, 'F', ini+2+j, jsonRoadmap[tab2][tab]['Datos'][j]['LIDER'], traceback=False, formato=cuerpo)

					if tab2 == 'Liberados':
						archivoExcel.escribeEnHoja(tab2, 'G', ini+2+j, jsonRoadmap[tab2][tab]['Datos'][j]['STATUS'], traceback=False, formato=cuerpoVerdeClaro)
						if '/' in jsonRoadmap[tab2][tab]['Datos'][j]['LIBERACION']:
						 	archivoExcel.escribeEnHoja(tab2, 'H', ini+2+j, jsonRoadmap[tab2][tab]['Datos'][j]['LIBERACION'], traceback=False, formato=cuerpoVerdeClaroBold)
						else:
						 	archivoExcel.escribeEnHoja(tab2, 'H', ini+2+j, jsonRoadmap[tab2][tab]['Datos'][j]['LIBERACION'], traceback=False, formato=cuerpoVerdeClaro)

					elif tab2 == 'Terminados':
						archivoExcel.escribeEnHoja(tab2, 'G', ini+2+j, jsonRoadmap[tab2][tab]['Datos'][j]['STATUS'], traceback=False, formato=cuerpoVerde)
						if '/' in jsonRoadmap[tab2][tab]['Datos'][j]['LIBERACION']:
						 	archivoExcel.escribeEnHoja(tab2, 'H', ini+2+j, jsonRoadmap[tab2][tab]['Datos'][j]['LIBERACION'], traceback=False, formato=cuerpoVerdeBold)
						else:
						 	archivoExcel.escribeEnHoja(tab2, 'H', ini+2+j, jsonRoadmap[tab2][tab]['Datos'][j]['LIBERACION'], traceback=False, formato=cuerpoVerde)

					archivoExcel.escribeEnHoja(tab2, 'I', ini+2+j, jsonRoadmap[tab2][tab]['Datos'][j]['DEPENDENCIA'], traceback=False, formato=cuerpoIzq)


				# actualizar contador que marca inicio de cada tabla
				ini+=len(jsonRoadmap[tab2][tab]['Datos'])+4

				# footers de cada tabla
				archivoExcel.dimensionaRows(tab2,ini-1,25)
				archivoExcel.dimensionaRows(tab2,ini-2,20)
				archivoExcel.mergeCeldas(tab2,ini-2,1,ini-2,8)
				archivoExcel.escribeEnHoja(tab2, 'A', ini-2, '', traceback=False, formato=rellenoGris)
				archivoExcel.escribeEnHoja(tab2, 'I', ini-2, 'TOTAL = '+str(jsonRoadmap[tab2][tab]['Info']['TOTAL']), traceback=False, formato=tituloAzulBlancoBorde)
				

				if tab2 == 'Liberados':
					iniLib = ini

				elif tab2 == 'Terminados':
					iniTer = ini


			except:
				print(str(tab2)+' (tab2) no tiene datos')

	except:
		print(str(tab)+' no tiene datos')









archivoExcel.guardaArchivo()
print("Terminé...")


