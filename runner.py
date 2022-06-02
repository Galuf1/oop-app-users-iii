class User:
    user_posts = {}

    def __init__(self, name, email, d_licence):
        self.name = name
        self.email = email
        self.licence = d_licence
        self._post=[]
    
    @property
    def post(self):
        return self._post
    # @post.setter
    # def post(self, val):
    #     self._post = self._post.append(val)
    #     return self._post
    
    def poster(self, val):
        self._post += [val]
        User.user_posts[self.name] = self._post
        return self.post
    def delete(self,index):
        self._post.pop(index)
        return self._post