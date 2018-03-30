#!/usr/bin/env python
from flask_script import Manager, Shell
from app import create_app, db

manager = Manager(app)
manager.add_command("shell", Shell(make_context = make_shell_context))
"""manager.add_command('db', MigrateCommand)"""

def main():
    manager.run()

if __name__ == '__main__':
    main()
