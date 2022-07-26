# 1_1 - Ítala
def show_students(
    conexao
):
    codigoSQL = "SELECT * FROM estudante order by nome;"
    consulta = conexao.cursor()
    consulta.execute(codigoSQL)
    for c, n in consulta:
        print(c, n)
    consulta.close()

# 1_2 - Newdon
def show_students_with(
    conexao
):
    nome = input('Digite um texto: ')

    codigoSQL = "SELECT * FROM estudante where nome like '%" + nome + "%'"
    consulta = conexao.cursor()
    consulta.execute(codigoSQL)
    for c, n in consulta:
        print(c, n)
    consulta.close()

# 1_3 - Linda
def create_student(conexao):
    nome = input('Digite o nome do estudante: ')

    codigoSQL = "insert into estudante(nome) values('" + nome + "')"

    consulta = conexao.cursor()
    consulta.execute(codigoSQL)
    conexao.commit()
    consulta.close()

# 1_4 - Elian
def delete_student_by_code(
    conexao
):
    cod = str(input('Digite o código do elemento a ser deletado: '))
    codSQL = "DELETE FROM estudante WHERE codigo = "+cod+";"

    consulta = conexao.cursor()
    consulta.execute(codSQL)
    conexao.commit()
    consulta.close()

# 1_5 - Mateus
def change_student_by_code(
    connection
):
    code: str = int(input('Digite o código do estudante: '))
    new_name: str = input('Digite seu novo nome: ')

    codigoSQL = \
        f'''
        UPDATE
            estudante
        SET
            nome = '{new_name}'
        WHERE
            codigo = {str(code)};
        '''
    consulta = connection.cursor()
    consulta.execute(codigoSQL)
    connection.commit()
    consulta.close()