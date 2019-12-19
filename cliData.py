import sqlite3

def clienteData():
    con=sqlite3.connect("cliente.db")
    con.execute("CREATE TABLE IF NOT EXISTS cliente (id INTEGER PRIMARY KEY, Name text NOT NULL, Idade text NOT NULL, Sexo text NOT NULL, Mail text NOT NULL, Fone text NOT NULL)")
    con.commit()
    con.close()

def putClient(Name, Idade, Sexo, Mail, Fone):
    con = sqlite3.connect("cliente.db")
    cur = con.cursor()
    cur.execute("INSERT INTO cliente VALUES (NULL, ?,?,?,?,?)",(Name, Idade, Sexo, Mail, Fone))
    con.commit()
    con.close()

def viewDate():
    con = sqlite3.connect("cliente.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM cliente")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteCli(id):
    con = sqlite3.connect("cliente.db")
    cur = con.cursor()
    cur.execute("DELETE FROM cliente WHERE id=?", (id,))
    con.commit()
    con.close()

def searcDat(Name = "" , Idade = "" , Sexo = "" , Mail = "" ,Fone  = ""):
    con = sqlite3.connect("cliente.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM cliente WHEREName = ? OR Idade = ? OR Sexo = ? OR Mail = ? OR Fone = ? OR  WHERE id=?", (Name, Idade, Sexo, Mail, Fone))
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,Name = "" , Idade = "" , Sexo = "" , Mail = "" ,Fone  = ""):
    con = sqlite3.connect("cliente.db")
    cur = con.cursor()
    cur.execute("UPDATE cliente SET Name = ?, Idade = ?, Sexo = ?,Mail = ?, Telefone = ?, WHERE id=?", (Name, Idade, Sexo, Mail, Fone, id))
    con.commit()
    con.close()
clienteData()
