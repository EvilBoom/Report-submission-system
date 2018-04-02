import os
from app import create_app
from app.models import User, Role, db
from flask_migrate import Migrate
from flask_script import Manager

@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
if __name__ == '__main__':
    manager.run()
