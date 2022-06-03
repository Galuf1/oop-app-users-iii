from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser
from users.User import User

free = FreeUser("Daniel","email.email.com","2131")
free.add_post("hello")
print(free._post)
print(User.user_posts)
free.add_post("hello again")
print(free._post)
print(User.user_posts)
free.add_post("can i say hello again?")
print(free._post)
print(User.user_posts)
free.add_post("asas")