from bloques import Bloque
from plantilla import Plantilla
from matplotlib_gen import MatplibGen

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
Herr_datos = [
	{'herramienta':'B-113-W', 'profundidad':2.0},
	{'herramienta':'T-101-D', 'profundidad':4.0},
	{'herramienta':'B-553-W', 'profundidad':6.0},
	{'herramienta':'T-707-D', 'profundidad':15.0}
	]
Av_datos = [
	{'profundidad':3.0, 'fecha':'2001-01-31'},
	{'profundidad':5.0, 'fecha':'2006-03-31'},
	{'profundidad':7.5, 'fecha':'2011-05-31'},
	{'profundidad':15.0, 'fecha':'2017-07-31'}
	]
Reves_datos = [
	{'profundidad':5.0, 'revestimiento':100},
	{'profundidad':8, 'revestimiento':150}
	]
Notas_datos = [
	{'herramienta':'B-113-W', 'profundidad':2.0},
	{'herramienta':'B-113-W', 'profundidad':2.0},
	{'herramienta':'B-113-W', 'profundidad':2.0},
	{'herramienta':'B-113-W', 'profundidad':2.0}	
	]
Litologia_datos = [
	{'colum':'Brecha tectónica',
	'descr':'Relleno Qxp. Relleno de camino. Grava en matriz arcillo limosa marrón y clara (medianamente densa). A 0,6 m presenta únicamente limo',
	'profundidad':2},
	{'colum':'Marga',
	'descr':'Relleno Qxp. Relleno de camino. Grava en matriz arcillo limosa marrón clara (medianamente densa). A 0,6 m presenta únicamente limo',
	'profundidad':3.5},
	{'colum':'Grava arenosa',
	'descr':'Relleno Qxp. Relleno de camino. Grava en matriz arcillo limosa marrón clara (medianamente densa). A 0,6 m presenta únicamente limo',
	'profundidad':7},
	{'colum':'Arena',
	'descr':'Relleno Qxp. Relleno de camino. Grava en matriz arcillo limosa marrón clara (medianamente densa). A 0,6 m presenta únicamente limo',
	'profundidad':10},
	{'colum':'Carbon',
	'descr':'aaaaa bbbb cccc ddd Qxp. Relleno de camino. Grava en matriz arcillo limosadta marrón clara (medianamente densa). A 0,6 m presenta únicamente limo',
	'profundidad':15}
	]
Maniobras_datos = [
	{'lon_maniobra':3.0, 'rqd':0.0, 'profundidad':0.4, 'recuperacion':100, 'lon_piezas':2.0},
	{'lon_maniobra':3.0, 'rqd':0.0, 'profundidad':1.2, 'recuperacion':95, 'lon_piezas':2.0},
	{'lon_maniobra':3.0, 'rqd':40.0, 'profundidad':3.4, 'recuperacion':90, 'lon_piezas':2.0},
	{'lon_maniobra':3.0, 'rqd':75.0, 'profundidad':6.4, 'recuperacion':85, 'lon_piezas':2.0},
	{'lon_maniobra':3.0, 'rqd':60.0, 'profundidad':9.5, 'recuperacion':80, 'lon_piezas':2.0},
	{'lon_maniobra':3.0, 'rqd':40.0, 'profundidad':15.0, 'recuperacion':75, 'lon_piezas':2.0}
	]
Meteorizacion_datos = [
	{'meteorizacion':1, 'profundidad':1.82},
	{'meteorizacion':2, 'profundidad':2.0},
	{'meteorizacion':2, 'profundidad':2.8},
	{'meteorizacion':4, 'profundidad':3.42},
	{'meteorizacion':4, 'profundidad':3.9},
	{'meteorizacion':5, 'profundidad':4.1},
	{'meteorizacion':5, 'profundidad':5.7},
	{'meteorizacion':5, 'profundidad':6.45},
	{'meteorizacion':6, 'profundidad':6.9},
	{'meteorizacion':6, 'profundidad':9.3},
	{'meteorizacion':6, 'profundidad':15.0}
	]
N_juntas_datos = [
	{'juntas':33, 'profundidad':1.82},
	{'juntas':15, 'profundidad':2.8},
	{'juntas':21, 'profundidad':3.42},
	{'juntas':33, 'profundidad':3.9},
	{'juntas':15, 'profundidad':6.45},
	{'juntas':33, 'profundidad':6.9},
	{'juntas':15, 'profundidad':9.3},
	{'juntas':30, 'profundidad':15.0}
	]
Rmr_datos = [
    # {'tipo_graf': 'doblebar', 'titulo1':'RMR (básico)', 'titulo2':'RMR (seco)'},
	{'profundidad':1.82, 'rmrb': 20, 'rmrs': 0},
	{'profundidad':2.0, 'rmrb': 37, 'rmrs': 0},
	{'profundidad':2.8, 'rmrb': 32, 'rmrs': 10},
	{'profundidad':3.42, 'rmrb': 37, 'rmrs': 0},
	{'profundidad':3.9, 'rmrb': 22, 'rmrs': 15},
	{'profundidad':4.1, 'rmrb': 45, 'rmrs': 0},
	{'profundidad':5.7, 'rmrb': 50, 'rmrs': 0},
	{'profundidad':6.45, 'rmrb': 40, 'rmrs': 5},
	{'profundidad':6.9, 'rmrb': 20, 'rmrs': 15},
	{'profundidad':15.0, 'rmrb': 36, 'rmrs': 6}
	]
Q_de_barton_datos = [
	{'barton':0.001, 'profundidad':1.82},
	{'barton':4, 'profundidad':3.42},
	{'barton':0.001, 'profundidad':3.9},
	{'barton':10, 'profundidad':6.45},
	{'barton':0.001, 'profundidad':6.9},
	{'barton':10, 'profundidad':15}	
	]

perfo = {
	'herr': Herr_datos,
	'avances': Av_datos,
	'reves': Reves_datos,
	'notas': Notas_datos,
	'lito': Litologia_datos,
	'maniobras': Maniobras_datos,
	'meteor': Meteorizacion_datos,
	'juntas': N_juntas_datos,
	'rmr': Rmr_datos,
	'barton': Q_de_barton_datos
	}
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #	
	
class Sondeo:
	def __init__(self, prof_agua, perforacion):
		self.prof_agua = prof_agua
		self.perforacion = perforacion

sondeo = Sondeo(5.69, perfo)


prof_por_pag = (6, 4)
ruta = './'

Bloque(sondeo.prof_agua, sondeo.perforacion, ruta, prof_por_pag)

obj1 = MatplibGen('marga', sondeo, ruta)

print(obj1.prof_agua())
print(obj1.prof_max())


'''
Bloque(prof_agua, perforacion, ruta, prof_por_pag)

img_1 = './images/image.jpg'
trabajo = '<b>PROYECTO DE CONSTRUCCIÓN LAV CANTÁBRICO-MEDITERRANEO. TRAMO: OLITE-TAFALLA</b>'
img_2 = './images/Negro_10mm.jpg'
datos_usr_cli = [
	'Antonio Muñoz Algobia (IDOM)',
	'IDOM',
	'Jose M.',
	'TP-50 Oruga'
	]
datos_geom = [
	'312+439',
	'607773,18',
	'4711123,55',
	'452,6'
	]
datos_sondeo = [
	'STU 312+439 (I:25º)',
	'1',
	'25/02/11',
	'30/02/11'
	]

Plantilla(img_1, trabajo, img_2, datos_usr_cli, datos_geom, datos_sondeo)

def report_generador(app, datos):
	print(app)
	#print(perf)

report_generador('marga', perforacion)
'''
