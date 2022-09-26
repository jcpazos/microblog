from app import db
from app.models import User, Post, Page, Tag

def userPostRelation():
    #usuario para agregar posts
    user = User.query.filter(User.username == "bcasas").first()

    try:
        #agregar posts al usuario
        posts = []
        for i in range(5):
            body = "body #" + str(i)
            newPost = Post(body=body, user_id=user.id)
            posts.append(newPost)
        
        db.session.add_all(posts)
        db.session.commit()
    except Exception as err:
        pass

    #comparar posts del usuario con todos los posts
    print(user)
    print(user.posts.all())
    print(Post.query.all())

    #usar el backref para referir al autor de un post
    firstPost = user.posts.all()[0]
    print(firstPost)
    print(firstPost.author)

    #funciona con cualquier post
    post = Post.query.filter(Post.id==10).first()
    print(post.author)

    #modificar los posts del usuario, mira lo que pasa en la DB cuando se hace esto
    newPost = Post(body="my new post", user_id=user.id)

    user.posts = [newPost]

    try:
        db.session.commit()
    except:
        pass

    print(User.query.filter(User.username == "bcasas").first().posts.all())

    #borrar el usuaario, mira lo que pasa en la DB cuando se hace esto
    db.session.delete(user)
    db.session.commit()
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