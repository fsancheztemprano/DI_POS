import sqlite3

from app import Globals
from app.model.Venta import Venta

debug: bool = False


def get_all() -> list:
    ventas = []
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.execute("SELECT * FROM ventas")
    for row in cursor:
        venta = Venta(row[1], row[2], row[0])
        ventas.append(venta)
        if debug:
            print(str(venta))

    conn.close()
    return ventas


def get_id(idd) -> Venta:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.execute("SELECT * FROM ventas where id = ?", (str(idd),))
    row = cursor.fetchone()
    venta = Venta(row[1], row[2], row[0])
    if debug:
        print(str(venta))

    conn.close()
    return venta


def insert(venta) -> int:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.cursor()
    if (venta.fecha_hora is None):
        sql = 'INSERT INTO ventas(id_cliente) VALUES (?)'
        values = (int(venta.id_cliente),)
    else:
        sql = 'INSERT INTO ventas(id_cliente, fecha_hora) VALUES (?,datetime(?))'
        values = (int(venta.id_cliente), venta.fecha_hora)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    venta.idd = cursor.lastrowid
    if debug:
        print("Venta insertada: " + str(venta))
    return venta.idd


def remove_id(idd) -> bool:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.execute("DELETE FROM ventas where id = ?", (str(idd),))
    conn.commit()
    conn.close()
    if debug:
        print('Venta eliminada: ' + str(cursor.rowcount))
    return cursor.rowcount > 0


def remove(venta) -> bool:
    return remove_id(venta.idd)


def update(venta) -> bool:
    conn = sqlite3.connect(Globals.db_src)
    cursor = conn.cursor()
    sql = 'UPDATE ventas SET id_cliente=?, fecha_hora=? WHERE id = ?'
    values = (venta.id_cliente, venta.fecha_hora, venta.idd)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    if debug:
        print("Venta actualizada: " + str(venta))
    return cursor.rowcount > 0


def get_dia(dia: int, mes: int, ano: int) -> list:
    ventas = []
    conn = sqlite3.connect(Globals.db_src)
    month_str = str(mes) if len(str(mes)) > 1 else str(0) + str(mes)
    day_str = str(dia) if len(str(dia)) > 1 else str(0) + str(dia)
    date = str(ano) + "-" + month_str + "-" + day_str
    sql = "select * from ventas where date(fecha_hora) = date(?)"
    cursor = conn.execute(sql, (date,))
    for row in cursor:
        venta = Venta(row[1], row[2], row[0])
        ventas.append(venta)
        if debug:
            print(str(venta))
    conn.close()
    return ventas


def get_mes(mes: int, ano: int) -> list:
    ventas = []
    conn = sqlite3.connect(Globals.db_src)
    sql = "select * from ventas where date(fecha_hora) >= date(?) and date(fecha_hora) < date(?, 'start of month', '+1 months', 'start of month')"
    month_str = str(mes) if len(str(mes)) > 1 else str(0) + str(mes)
    date = str(ano) + '-' + month_str + '-01'
    values = (date, date)
    cursor = conn.execute(sql, values)
    for row in cursor:
        venta = Venta(row[1], row[2], row[0])
        ventas.append(venta)
        if debug:
            print(str(venta))
    conn.close()
    return ventas
