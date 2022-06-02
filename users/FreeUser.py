from users.User import User

class FreeUser(User):
    def add_post(self):
        if len(self._post) > 2:
            return "Only 2 posts for Free User"