import sys

class juegoCubos:
    """
        .. include:: ./README.md
    """
    pasos = 0
    aguaEnCubos = {'8': 0, '5': 0, '3': 0}

    """
    Esta es la clase que crea los cubos
    """
    def __init__(self, fobjetivo):
        """
        Este es el constructor de la clase juegoCubos
        :param fobjetivo: Char
        """
        self.objetivo = fobjetivo

    def genStrCubos(self):
        """
        Esta funcion crea la estructura de los cubos, dependiendo de si estan llenos o vacios los pone de una forma o
        de otra
        :return: String con los cubos
        """
        caracterAgua = '~'
        visualizadorCubos = []

        for i in range(1, 9):
            if self.aguaEnCubos['8'] < i:
                visualizadorCubos.append('      ')
            else:
                visualizadorCubos.append(caracterAgua * 6)

        for i in range(1, 6):
            if self.aguaEnCubos['5'] < i:
                visualizadorCubos.append('      ')
            else:
                visualizadorCubos.append(caracterAgua * 6)

        for i in range(1, 4):
            if self.aguaEnCubos['3'] < i:
                visualizadorCubos.append('      ')
            else:
                visualizadorCubos.append(caracterAgua * 6)

        # Devuelve una cadena con los cubos y su contenido de agua
        return '''
        8|{7}|
        7|{6}|
        6|{5}|
        5|{4}|  5|{12}|
        4|{3}|  4|{11}|
        3|{2}|  3|{10}|  3|{15}|
        2|{1}|  2|{9}|  2|{14}|
        1|{0}|  1|{8}|  1|{13}|
         +------+   +------+   +------+
            8L         5L         3L
        '''.format(*visualizadorCubos)

    def mostrarEstadoCubos(self):
        """
        Muestra el objetivo del juego y el estado de los cubos (como de llenos/vacios estan)
        :return: String
        """
        print()
        print('Intenta conseguir ' + str(self.objetivo) + ' litros de agua en uno de estos cubos')
        print(self.genStrCubos())

    def checkObjetivo(self):
        # Comprueba si uno de los cubos ha conseguido el objetivo
        """
        Comprueba si has conseguido el objetivo
        :return: String
        """
        for cantidadAgua in self.aguaEnCubos.values():
            if cantidadAgua == self.objetivo:
                print('Bien hecho! Lo has resuelto en', self.pasos, 'pasos!')
                sys.exit()

    def selecOpcion(self):
        # Selección de una opción
        """
        Te printea el menu con las opciones para que elijas
        :return: Char
        """
        print('Elige una opción:')
        print('  (T)odos los cubos llenos')
        print('  (L)lenar un cubo')
        print('  (V)aciar un cubo')
        print('  (B)Vaciar todos los cubo')
        print('  (M)over el agua de un cubo a otro')
        print('  (S)alir')

        while True:
            move = input('> ').upper()
            if move == 'SALIR' or move == 'S':
                print('Gracias por jugar!')
                sys.exit()

            if move in ('L', 'V', 'M', 'T','B'):

                return move

    def selecCubo(self, mensaje):
        """
        El menu que te dice hacia que cubo quieres dirijir la accion
        :param mensaje:String
        :return: Char
        """
        while True:
            print(mensaje)
            cuboOrigen = input('> ').upper()

            if cuboOrigen in ('8', '5', '3'):
                return cuboOrigen

    def llenarCubo(self, cuboOrigen):
        """
        Llena el cubo seleccionado hasta su tamaño maximo
        :param cuboOrigen:Char
        :return: Int
        """
        cuboOrigenTam = int(cuboOrigen)
        self.aguaEnCubos[cuboOrigen] = cuboOrigenTam
        self.pasos += 1

    def vaciarCubo(self, cuboOrigen):
        """
        Vacia el cubo seleccionado
        :param cuboOrigen: Char
        :return: nada
        """
        self.aguaEnCubos[cuboOrigen] = 0
        self.pasos += 1

    def moverCubo(self, cuboOrigen, cuboDestino):
        """
        Mueve el agua de un cubo a otro
        :param cuboOrigen: Char
        :param cuboDestino: Char
        :return: nada
        """
        cuboDestinoTam = int(cuboDestino)
        espacioVacioCuboDestino = cuboDestinoTam - self.aguaEnCubos[cuboDestino]
        aguaEnCuboOrigen = self.aguaEnCubos[cuboOrigen]
        cantidadAMover = min(espacioVacioCuboDestino, aguaEnCuboOrigen)

        # Saco el agua de este cubo
        self.aguaEnCubos[cuboOrigen] -= cantidadAMover

        # Introduzco el agua en este cubo
        self.aguaEnCubos[cuboDestino] += cantidadAMover
        self.pasos += 1

    def jugar(self):
        """
        Dependiendo de la opcion que hayas selecionado hace una u otra opcion
        :return: nada
        """
        self.mostrarEstadoCubos()
        while True:
            opcion = self.selecOpcion()
            if opcion == 'L':
                cubo = self.selecCubo('Selecciona el cubo 8, 5, 3 o SALIR:')
                self.llenarCubo(cubo)
            elif opcion == "V":
                cubo = self.selecCubo('Selecciona el cubo 8, 5, 3 o SALIR:')
                self.vaciarCubo(cubo)
            elif opcion == "B":
                self.vaciarCubo('8')
                self.vaciarCubo('5')
                self.vaciarCubo('3')
            elif opcion == "M":
                cuboOrigen = self.selecCubo('Selecciona el cubo ORIGEN 8, 5, 3 o SALIR:')
                cuboDestino = self.selecCubo('Selecciona el cubo DESTINO 8, 5, 3 o SALIR:')
                self.moverCubo(cuboOrigen, cuboDestino)
            elif opcion == "T":
                self.llenarCubo('8')
                self.llenarCubo('5')
                self.llenarCubo('3')
            self.mostrarEstadoCubos()
            self.checkObjetivo()


if __name__ == "__main__":
    juego = juegoCubos(4)
    juego.jugar()
