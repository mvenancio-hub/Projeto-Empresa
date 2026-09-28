from banco import conectar

def inserir_departamento():
    nome = input("Digite o nome do seu departamento: ")
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO departamento(nome)
        VALUES (%s)
    """

    cursor.execute(sql, (nome,))
    conexao.commit()
    cursor.close()
    conexao.close()
    
    print("Departamento inserido com sucesso!")