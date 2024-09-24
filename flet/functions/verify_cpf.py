import sqlite3

def verificar_cpf_existente(cpf):
    conn = None
    try:
        conn = sqlite3.connect('database/academia.db')
        cursor = conn.cursor()

        cursor.execute('SELECT cpf FROM Aluno WHERE cpf = ?', (cpf,))
        resultado = cursor.fetchone()

        return resultado is not None

    except sqlite3.Error as error:
        return f"Erro ao verificar CPF: {error}"
    
    finally:
        if conn:
            conn.close()
