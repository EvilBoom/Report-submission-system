from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from app.models import db, User, Post, Tag, Comment 


migrate = Migrate(create_app, db)

manager = Manager(create_app)
manager.add_command("server", Server())
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(
        create_app=create_app, 
        db=db, 
        User=User, 
        Post=Post, 
        Tag=Tag,
        Comment=Comment
    )


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    manager.run()
