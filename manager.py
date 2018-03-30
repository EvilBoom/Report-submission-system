#!/usr/bin/env python
from flask_script import Manager
from app import create_app

manager = Manager(app)

def main():
    manager.run()

if __name__ == '__main__':
    main()
