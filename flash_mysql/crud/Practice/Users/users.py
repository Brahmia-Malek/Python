from config import connectToMySQL
class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

@classmethod
def get_all(cls):
        query = "SELECT * FROM Users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('Users').query_db(query)
        # Create an empty list to append our instances of users
        Users = []
        # Iterate over the db results and create instances of users with cls.
        for Users in results:
            Users.append( cls(Users) )
        return Users
                    