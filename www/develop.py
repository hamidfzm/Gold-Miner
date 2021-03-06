#!/usr/bin/env python
# -*- coding: utf-8 -*-

# flaks import
from flask.ext.script import Manager

from app import create_app
from config import DevelopmentConfig

app = create_app(DevelopmentConfig)

manager = Manager(app)


@manager.command
def run():
    """
    :run server on port 5000
    """
    app.run(host='0.0.0.0', port=5000, debug=True)


@manager.command
def dbc():
    # project import
    from mongoengine import DoesNotExist
    from app.blueprints.user.models import Role
    from app.blueprints.user.models import User

    """ create full website admin """
    try:
        User.objects.get(username='admin')

    except DoesNotExist:
        admin_role = Role(name="admin", abilities=[])  # admin has all abilities!
        User(username='admin',
             name=u'مدیر کل',
             password='0212526',
             roles=[admin_role]).save()

        app.logger.info("Admin user created!\nUsername: admin\nPassword: 0212526")


@manager.command
def routes():
    import urllib

    output = [urllib.unquote("\033[1m{:50s} {:20s} {}\033[0;0m".format('Endpoint', 'Methods', 'Rule'))]
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    for line in sorted(output):
        print(line)

if __name__ == '__main__':
    manager.run()