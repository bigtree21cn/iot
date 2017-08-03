# encoding: utf-8
"""
App management tool
--------------------
"""
from flask_script import Manager, Command
from app import create_app

myapp = create_app()
manager = Manager(myapp)


class CreateDB(Command):
    "create the database objects"
    def run(self):
        from app.extensions import db
        db.create_all()

class StartApp(Command):
    "start to run the application"
    def run(self):
        myapp.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == "__main__":
    manager.add_command('CreateDB', CreateDB())
    manager.add_command('StartApp', StartApp())
    manager.run()
    #CreateDB().run()
    #StartApp().run()