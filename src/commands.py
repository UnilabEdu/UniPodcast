import click
from flask.cli import with_appcontext
from click import command
from werkzeug.security import generate_password_hash

from src.models import User,Category,News,Video,Tag,Type
from src.ext import db


@command('init_db')
@with_appcontext
def init_db():
    click.echo('creating database')
    db.create_all()
    click.echo('Creating done!')

@command('populate_db')
@with_appcontext
def populate_db():
    click.echo('Populating database...')
    db.session.query(User).delete()
    db.session.query(Category).delete()

    db.session.add( User(username = 'admin',
                      _password = generate_password_hash('12345'),
                      role='admin')
                )
    
    categories = ['ტექნოლოგიები და კარიერა',
                  'სტუდენტური ცხოვრება',
                  'განათლება და კულტურა',
                  'ზოგადი']
    
    for category in categories:
        db.session.add(Category(category=category))
    db.session.commit()

    click.echo('Done!')
