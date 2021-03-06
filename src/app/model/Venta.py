from src.app.data import VentasDao


class Venta:
    """
    Clase modelo Venta
    """

    def __init__(self, id_cliente, fecha_hora=None, idd=0):
        """
        Constructor unico, un objeto de este tipo ser inicializara
        con id 0 y al insertarse en sqlite se le asigna un id

        :param id_cliente:
        :type id_cliente:
        :param fecha_hora:
        :type fecha_hora:
        :param idd:
        :type idd:
        """
        self.idd: int = idd
        self.id_cliente: int = id_cliente
        self.fecha_hora: str = fecha_hora

    def insert(self):
        """
        insertar en base de datos
        :param self:
        :type self:
        :return: id asignado
        :rtype: int
        """
        return VentasDao.insert(self)

    def remove(self):
        """
        eliminar de la base de datos
        :param self:
        :type self:
        :return: confirmacion de eliminacion
        :rtype: bool
        """
        return VentasDao.remove(self)

    def update(self):
        """
        actualizar en base de datos

        :param self:
        :type self:
        :return: confirmacion de actualizacion
        :rtype: bool
        """
        return VentasDao.update(self)

    def __str__(self) -> str:
        return 'Venta { ' + \
               str(self.idd) + ', ' + \
               str(self.id_cliente) + ', ' + \
               str(self.fecha_hora) + ' };'
