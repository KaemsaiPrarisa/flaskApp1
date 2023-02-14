
from flask.cli import FlaskGroup
from app import app, db
from app.models.contact import Contact
from app.models.blog import BlogEntry


cli = FlaskGroup(app)




@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()




@cli.command("seed_db")
def seed_db():
    db.session.add(Contact(firstname='สมชาย', lastname='ทรงแบด', phone='081-111-1111'))
    db.session.add(BlogEntry(name='ลูกแมว',message='0951467159', email='meaw12@gmail.com'))
    db.session.commit()


if __name__ == "__main__":
    cli()

