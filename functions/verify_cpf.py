import sqlite3

def verificar_cpf_existente(cpf):
    try:
        conn = sqlite3.connect('academia_3.db')
        cursor = conn.cursor()

        cursor.execute('SELECT cpf FROM Aluno WHERE cpf = ?', (cpf,))
        resultado = cursor.fetchone()

        return resultado is not None

    except sqlite3.Error as error:
        print(f"Erro ao verificar CPF: {error}")
        return False
    
    finally:
        if conn:
            conn.close()