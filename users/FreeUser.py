from users.User import User

class FreeUser(User):
    def add_post(self,val):
        
        if len(self._post) > 1:
            print("Only 2 posts for Free User")
        else:
            User.add_post(self,val)
        