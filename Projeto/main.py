import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    titular TEXT NOT NULL,
                    saldo FLOAT NOT NULL,
                    cpf TEXT NOT NULL UNIQUE
                )""")

cursor.execute("""INSERT INTO contas_bancarias
                (titular, saldo, cpf) VALUES
                ("Silva", 7200, "12312673817")
                """)
cursor.execute("""INSERT INTO contas_bancarias
                (titular, saldo, cpf) VALUES
                ("Michell", 4200, "98712673817")
                """)
cursor.execute("""INSERT INTO contas_bancarias
                (titular, saldo, cpf) VALUES
                ("Fred", 9200, "56712673817")
                """)

cursor.execute("""UPDATE contas_bancarias
                SET saldo = 7200
                WHERE id = 5
                """)

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

cursor.execute("DELETE FROM contas_bancarias")

conexao.commit()