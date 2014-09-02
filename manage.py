#!/usr/bin/env python
import os
from flask_script import Manager, Shell
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate, MigrateCommand


basedir = os.path.abspath(os.path.dirname(__file__))

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)
migrate = Migrate(app)


def make_shell_context():
    """make app, db available to the command line"""
    return dict(app=app, db=db, User=User, Role=Role)

@manager.command
def deploy():
    """Run deployment tasks"""
    from flask_migrate import upgrade
    from app.models import User, Role

    # migrate database to the latest revision
    upgrade()

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()