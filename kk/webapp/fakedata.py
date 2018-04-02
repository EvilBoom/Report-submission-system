import random
import datetime 
from main import app, db, User, Post, Tag

user = User.query.get(1)
tag_one = Tag('python')
tag_two = Tag('Flask')
tag_three = Tag('SQLALechemy')
tag_four = Tag('jinja')
tag_list = [tag_one, tag_two, tag_three, tag_four]

s = "Eample text"

for i in range(100):
    new_post = Post("Post " + str(i))
    new_post.user = user
    new_post.publish_date = datetime.datetime.now()
    new_post.text = s
    new_post.tags = random.sample(tag_list, random.randint(1, 3))
    db.session.add(new_post)

db.session.commit()
