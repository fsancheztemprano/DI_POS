from src.app.data import ClientesDao



class Cliente:
    """
    Clase modelo cliente
    """

    def __init__(self, dni, nombre, apellido, telefono, direccion, idd=0):
        """
        Constructor unico, un objeto de este tipo ser inicializara
        con id 0 y al insertarse en sqlite se le asigna un id

        :param self:
        :type self:
        :param dni:
        :type dni:
        :param nombre:
        :type nombre:
        :param apellido:
        :type apellido:
        :param telefono:
        :type telefono:
        :param direccion:
        :type direccion:
        :param idd:
        :type idd:
        :return:
        :rtype:
        """
        self.idd = idd
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion

    def insert(self):
        """
        insertar en base de datos
        :param self:
        :type self:
        :return: id asignado
        :rtype: int
        """
        return ClientesDao.insert(self)

    def remove(self):
        """
        eliminar de la base de datos
        :param self:
        :type self:
        :return: confirmacion de eliminacion
        :rtype: bool
        """
        return ClientesDao.remove(self)

    def update(self):
        """
        actualizar en base de datos

        :param self:
        :type self:
        :return: confirmacion de actualizacion
        :rtype: bool
        """
        return ClientesDao.update(self)

    def __str__(self) -> str:
        return 'Cliente { ' + \
               str(self.idd) + ', ' + \
               self.dni + ', ' + \
               self.nombre + ', ' + \
               self.apellido + ', ' + \
               str(self.telefono) + ', ' + \
               self.direccion + ' };'
