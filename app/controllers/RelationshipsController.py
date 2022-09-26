from app import db
from app.models import User, Post, Page, Tag

def userPostRelation():
    user = User.query.filter(User.username == "mtorres").first()

    try:
        posts = []
        for i in range(5):
            body = "body #" + str(i)
            newPost = Post(body=body, user_id=user.id)
            posts.append(newPost)
        
        db.session.add_all(posts)
        db.session.commit()
    except Exception as err:
        pass

    print(user)
    print(user.posts.all())
    print(Post.query.all)
    return ""

def pageTagRelation():
    try:
        page1 = Page()
        page2 = Page()
        tag1 = Tag()
        tag2 = Tag()

        db.session.add_all([page1, page2, tag1, tag2])
        db.session.commit()

        page1.tags = [tag1, tag2]
        tag1.pages = [page1, page2]

        db.session.commit()

    except Exception as err:
        print(err)
        return ""
    page3 = Page.query.filter(Page.id == page1.id).first()
    page4 = Page.query.filter(Page.id == page2.id).first()
    tag3 = Tag.query.filter(Tag.id == tag1.id).first()
    print(page3)
    print(page4)
    print(page3.tags)
    print(tag3.pages)

    sometag = Tag.query.filter(Tag.id == 1).first()

    print(sometag.pages)
    print(sometag.pages[0].tags)
    print(sometag.pages[1].tags)

    sometag.pages = [page3, page4]

    db.session.commit()
    print(sometag.pages)

    return ""