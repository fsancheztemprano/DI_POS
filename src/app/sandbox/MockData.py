from random import random, randint

from src.app.data import ClientesDao, ProductosDao, VentasDao, VendidosDao
from src.app.model.Cliente import Cliente
from src.app.model.Producto import Producto
from src.app.model.Vendido import Vendido
from src.app.model.Venta import Venta


def mock_clientes():
    """
    genera 999 clientes con datos incrementales
    :return:
    :rtype:
    """
    for i in range(1, 1000):
        Cliente('DNI' + str(i), "Cliente " + str(i), "Apellido " + str(i), i * 555, 'Direccion ' + str(i)).insert()


def mock_productos():
    """
    genera 999 productoss con datos incrementales
    :return:
    :rtype:
    """
    for i in range(1, 1000):
        Producto('Producto ' + str(i), 'Descripcion ' + str(i), i).insert()


def mock_ventas():
    """
    determinando el rango en :for year in range(2019, 2020):
    genera 5 ventas con 5 productos cada una, por cada dia de cada año
    :return:
    :rtype:
    """
    vendidos = list()
    for year in range(2019, 2020):
        print("Start year " + str(year))
        for month in range(1, 13):
            print("Start month " + str(month))
            for day in range(1, 29):
                print("Start day " + str(day))
                for i in range(1, 6):
                    month_str = str(month) if len(str(month)) > 1 else str(0) + str(month)
                    day_str = str(day) if len(str(day)) > 1 else str(0) + str(day)
                    id_venta = Venta(randint(1, 999), str(year) + '-' + month_str + '-' + day_str).insert()
                    for j in range(1, 6):
                        vendidos.append(Vendido(id_venta, randint(1, 999), 1, randint(1, 8)))
    print('insertando ' + str(len(vendidos)) + ' vendidos')
    VendidosDao.insert_list(vendidos)
    print('insercion terminada')

# mock_clientes()
# mock_productos()
# mock_ventas()
