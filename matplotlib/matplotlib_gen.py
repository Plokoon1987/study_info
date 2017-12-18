'''
Modulo que gestionará la creación de imagenes (svg) de los distintos bloques
usados en informes gráficos de sondeos geotécnicos.
'''
class MatplibGen:
    '''
    Clase creada para desglosar los objetos (ej: sondeo) y sacar los parámetros
    que se utilizarán posteriormente para crear las imagenes (svg). También
    incluye funciones para la creación de dichas imagenes.
    '''

    def __init__(self, app, datos, ruta_svgs):
        if app == 'marga':
            self.ruta_svgs = ruta_svgs
            self.datos = datos
            self.prof_por_pag = self.profundidades(10)
            self.tipo_perforacion = self.plot_data('herr')
            self.avances = self.plot_data('avances')
            self.revestimiento = self.plot_data('reves')

            self.litologia = self.plot_data('lito')

        elif app == 'margo':
            pass

        else:
            pass

    def prof_agua(self):
        ''' Función para obtener la prof_agua en self.datos, devuelve float'''
        return self.datos.prof_agua

    def prof_max(self):
        '''
        Función para obtener la prof_max de entre todas las que hay en
        self.datos, devuelve float
        '''
        prof_max = 0
        if self.datos.prof_agua:
            prof_max = self.datos.prof_agua
        for key in self.datos.perforacion.keys():
            if self.datos.perforacion[key]:
                for elem in self.datos.perforacion[key]:
                    if elem['profundidad'] > prof_max:
                        prof_max = elem['profundidad']
        return prof_max

    def profundidades(self, metr_por_pag):
        '''
        Función para crear una tupla que reflejará los límites de
        profundidad en cada svg.
        '''
        prof_max = 0
        if self.datos.prof_agua:
            prof_max = self.datos.prof_agua
        for key in self.datos.perforacion.keys():
            if self.datos.perforacion[key]:
                for elem in self.datos.perforacion[key]:
                    if elem['profundidad'] > prof_max:
                        prof_max = elem['profundidad']

        if prof_max % metr_por_pag == 0:
            num_pags = int(prof_max / metr_por_pag)
        else:
            num_pags = int(prof_max / metr_por_pag) + 1

        prof_pag = ()
        for num in range(0, num_pags):
            if num != num_pags - 1:
                min_max_pag = (num * metr_por_pag, (num + 1) * metr_por_pag)
            else:
                min_max_pag = (num * metr_por_pag, prof_max)
            prof_pag = prof_pag + (min_max_pag,)

        return prof_pag

    def plot_data(self, variable):
        '''
        Función para crear una tupla con los datos a ser dibujados con el
        formato (profundidad, valor).
        '''
        plot_data = self.datos.perforacion[variable]
        if plot_data:
            keys = ()
            for key in plot_data[0].keys():
                if key != 'profundidad':
                    keys = keys + (key,)

        tupla_datos = ()
        for elem in plot_data:
            elem_tupla = (elem['profundidad'], )
            for key in keys:
                elem_tupla = elem_tupla + (elem[key],)
            tupla_datos = tupla_datos + (elem_tupla,)
        print(tupla_datos)

        return tupla_datos
