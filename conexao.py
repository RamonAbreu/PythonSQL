import pyodbc




class SQLPython:
    #Conexão com servidor
    Driver = r'Driver={SQL Server};'
    Server = r'Server=RamonUltra;'
    Database = r'Database=sistema_de_funcionarios;'
    valor = None
    #Comandos SQL
    sel = """SELECT * FROM dbo.cargos WHERE id IN (14)"""
    inserir = """INSERT INTO dbo.cargos(id, nome)
                 VALUES
                     (14, 'Supervisor_CCO')"""
    ident = "SET IDENTITY_INSERT dbo.cargos ON"

    def __init__(self):
        try:
            self.conn = pyodbc.connect(self.Driver + self.Server + self.Database)
            print("Conexão bem sucedida")
        except Exception:
            print("Erro na conexão")
        self.cursor = self.conn.cursor()


    def inserir(self):
        inserir = """INSERT INTO dbo.cargos(id, nome)
             VALUES
                 (14, 'Supervisor_CCO')"""
        return inserir

    def selecionar(self):
        sel = """SELECT * FROM dbo.cargos WHERE id IN (14)"""
        return sel
    # cursor.commit()