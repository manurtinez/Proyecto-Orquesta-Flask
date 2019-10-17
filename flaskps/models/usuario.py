class usuario(object)
db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM usuario"

        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def create(cls, data):
        sql = """
            INSERT INTO usuario (email, username, password, activo, updated_at, created_at, first_name, last_name )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, list(data.values()))
        cls.db.commit()

        return True

    def select_activos(cls):
        sql = "SELECT * FROM usuario WHERE activo = 1"

        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()