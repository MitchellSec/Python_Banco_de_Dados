import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    titular TEXT NOT NULL,
                    saldo FLOAT NOT NULL,
                    cpf TEXT NOT NULL UNIQUE
                )""")

# cursor.execute("""INSERT INTO contas_bancarias
#                 (titular, saldo, cpf) VALUES
#                 ("Karol", 2200, "67512673817")
#                 """)

cursor.execute("""SELECT * FROM contas_bancarias""")
contas = cursor.fetchall()
print(contas)
for contas in contas: 
    id, titular, saldo, cpf = contas
    print(f"""
    Id: {id}
    Titular {titular}
    Saldo {saldo}
    CPF {cpf}
            """)

conexao.commit()