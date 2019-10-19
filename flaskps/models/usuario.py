class usuario(object):
    db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM usuario"

        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def create(cls, em, us, pa, ac, up, cr, fi, la): #1° no esten vacios (verificar desde el controlador, resources > usuario.py).
        sql = """
            INSERT INTO usuario (email, username, password, activo, updated_at, created_at, first_name, last_name )
            VALUES (@em, @us, @pa, @ac, @up, @cr, @fi, @la) 
        """
        cursor = cls.db.cursor()
        cursor.execute(sql)
        cls.db.commit()

        return True

    @classmethod
    def select_activos(cls):
        sql = "SELECT * FROM usuario WHERE activo = 1"

        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def find_by_email_and_pass(cls,e,p):
        sql = "SELECT * FROM usuario WHERE email = @e AND password = @p" 
        #asegurar que compare con las variables, no con el string

        cursor = cls.db.cursor()
        resultado = cursor.execute(sql) 
        return resultado

#por cada metodo va su equivalente en el controlador, ahi aseguro q no este vacio. redirigir desde el mismo controlador.