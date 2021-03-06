from src.app.data import ProductosDao


class Producto:
    """
    Clase modelo Producto
    """

    def __init__(self, nombre, descripcion, precio=0, stock=0, idd=0):
        """
        Constructor unico, un objeto de este tipo ser inicializara
        con id 0 y al insertarse en sqlite se le asigna un id

        :param nombre:
        :type nombre:
        :param descripcion:
        :type descripcion:
        :param precio:
        :type precio:
        :param stock:
        :type stock:
        :param idd:
        :type idd:
        """
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.idd = idd

    def insert(self):
        """
        insertar en base de datos
        :param self:
        :type self:
        :return: id asignado
        :rtype: int
        """
        return ProductosDao.insert(self)

    def remove(self):
        """
        eliminar de la base de datos
        :param self:
        :type self:
        :return: confirmacion de eliminacion
        :rtype: bool
        """
        return ProductosDao.remove(self)

    def update(self):
        """
        actualizar en base de datos

        :param self:
        :type self:
        :return: confirmacion de actualizacion
        :rtype: bool
        """
        return ProductosDao.update(self)

    def __str__(self) -> str:
        return 'Producto { ' + \
               str(self.idd) + ', ' + \
               self.nombre + ', ' + \
               str(self.precio) + ', ' + \
               self.descripcion + ' };'
