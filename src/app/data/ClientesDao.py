import sqlite3

from src.app import Globals
from src.app.model.Cliente import Cliente

debug: bool = False


def get_all() -> list:
    clientes = []
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.execute("SELECT * FROM clientes")
    for row in cursor:
        cliente = Cliente(row[1], row[2], row[3], row[4], row[5], row[0])
        clientes.append(cliente)
        if debug:
            print(str(cliente))
    conn.close()
    return clientes


def get_id(idd) -> Cliente:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.execute("SELECT * FROM clientes where id = ?", (str(idd),))
    row = cursor.fetchone()
    cliente = Cliente(row[1], row[2], row[3], row[4], row[5], row[0])
    conn.close()
    if debug:
        print(str(cliente))
    return cliente


def insert(cliente) -> int:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.cursor()
    sql = 'INSERT INTO clientes(dni, nombre, apellido, telefono, direccion) VALUES ( ?,?,?,?,?)'
    values = (cliente.dni, cliente.nombre, cliente.apellido, int(cliente.telefono), cliente.direccion)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    cliente.idd = cursor.lastrowid
    if debug:
        print("Clientes insertado: " + str(cliente))
    return cliente.idd


def remove_id(idd) -> bool:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.execute("DELETE FROM clientes where id = ?", (str(idd),))
    conn.commit()
    conn.close()
    if debug:
        print('Cliente eliminado: ' + str(cursor.rowcount))
    return cursor.rowcount > 0


def remove(cliente) -> bool:
    return remove_id(cliente.idd)


def update(cliente) -> bool:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.cursor()
    sql = 'UPDATE clientes SET dni=?, nombre=?, apellido=?, telefono=?, direccion=? WHERE id = ?'
    values = (cliente.dni, cliente.nombre, cliente.apellido, cliente.telefono, cliente.direccion, cliente.idd)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    if debug:
        print("Cliente actualizado: " + str(cliente))
    return cursor.rowcount > 0
