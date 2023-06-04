from mysqlconnection import connectToMySQL

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at= data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user ;"
        results = connectToMySQL('userdb').query_db(query)
        user = []
        for u in results:
            user.append( cls(u) )
        return user

    @classmethod
    def save(cls, data):
        query = """INSERT INTO user (first_name,last_name,email) 
        VALUES (%(first_name)s,%(last_name)s,%(email)s)"""

        # comes back as the new row id
        result = connectToMySQL('userdb').query_db(query,data)
        return result
    
    @classmethod
    def show_one(cls, data):

        query = """
                    SELECT * FROM user
                    WHERE id = %(id)s;
                """
        results = connectToMySQL("userdb").query_db(query, data)
        # print(results)
        result = cls(results[0])

        return result
    
   
    @classmethod
    def update_user(cls, data):

        query = """
                UPDATE user 
                SET first_name = %(first_name)s,
                last_name = %(last_name)s,
                email = %(email)s
                WHERE id = %(id)s;
                """
        
        return   connectToMySQL("userdb").query_db(query, data)
    

    @classmethod
    def delete(cls,data):
        query  = "DELETE FROM user WHERE id = %(id)s;"
        
        return connectToMySQL("userdb").query_db(query,data)

        