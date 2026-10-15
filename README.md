# Python Banco de Dados 🐍

Projeto simples criado para praticar manipulação de banco de dados relacional usando **Python** e **SQLite**. A ideia é testar os conceitos básicos de CRUD (Criar, Inserir, Atualizar, Consultar e Deletar) direto pelo terminal, sem frescura.

---

##  Tecnologias Utilizadas

* **Python 3**
* **SQLite3** (nativo do Python)

---

##  O que o código faz?

O script principal (`main.py`) executa o seguinte fluxo:
1. Conecta (ou cria) um banco de dados local chamado `banco.db`.
2. Cria a tabela `contas_bancarias` caso ela ainda não exista (com campos para ID, titular, saldo e CPF).
3. Insere alguns registros de teste no banco.
4. Faz uma atualização (`UPDATE`) de saldo pelo ID.
5. Consulta todos os registros cadastrados (`SELECT`) e imprime formatadinho no terminal.
6. Limpa a tabela (`DELETE`) no final para reiniciar os testes, salvando tudo com `commit()`.

---

##  Como rodar no seu PC

1. Certifique-se de ter o **Python** instalado na sua máquina.
2. Clone este repositório ou baixe os arquivos.
3. Abra a pasta do projeto no seu editor de código (como o VS Code).
4. Rode o arquivo principal pelo terminal:

```bash
python main.py
