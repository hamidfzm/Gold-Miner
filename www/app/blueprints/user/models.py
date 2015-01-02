# -*- coding: utf-8 -*-
__author__ = 'hamid'

# flask imports
from flask import current_app, request, g

# python imports
from mongoengine import (Document, EmbeddedDocument, DoesNotExist, ValidationError,
                         StringField, DateTimeField, ReferenceField, BooleanField, ListField, EmbeddedDocumentField)
from functools import wraps
from hashlib import sha384
from datetime import datetime
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


class Role(EmbeddedDocument):
    """
    Subclass this for your roles
    """
    name = StringField(unique=True)
    abilities = ListField(StringField())

    def add_abilities(self, *abilities):
        for ability in abilities:
            if ability not in self.abilities:
                self.abilities.append(ability)
        return self

    def remove_abilities(self, *abilities):
        for ability in abilities:
            if ability in self.abilities:
                self.abilities.remove(ability)
        return self

    def __repr__(self):
        return '<Role {}>'.format(self.name)

    def __str__(self):
        return self.name

    def to_json(self):
        return dict(name=self.name, abilities=[ability for ability in self.abilities])


class User(Document):
    name = StringField(required=True)
    address = StringField()
    phone = StringField()
    username = StringField(required=True)
    password_hash = StringField(required=True)
    created_on = DateTimeField(default=datetime.utcnow)
    created_by = ReferenceField('User')
    is_active = BooleanField(default=True)
    note = StringField()
    roles = ListField(EmbeddedDocumentField(Role))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.password = kwargs['password']

    @property
    def password(self):
        raise IOError('No read access to this property!')

    @password.setter
    def password(self, password):
        self.password_hash = sha384(password).hexdigest()

    def verify_password(self, password):
        return sha384(password).hexdigest() == self.password_hash

    def change_password(self, old_password, new_password):
        if self.verify_password(old_password):
            self.password_hash = sha384(new_password).hexdigest()
            return True
        return False

    def generate_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': str(self.id)})

    @staticmethod
    def auth(f):
        @wraps(f)
        def wrapper():
            s = Serializer(current_app.config['SECRET_KEY'], 3600)
            try:
                data = s.loads(request.headers.get('token'))
                g.user = User.objects.get(id=data['id'])
                return f
            # BadSignature is invalid token, SignatureExpired is valid token, but expired
            # DoesNotExist is for when user doesn't exists and ValidationError is for when id is invalid
            except (BadSignature, SignatureExpired, ValidationError, DoesNotExist, KeyError, TypeError):
                return "", 401
        return wrapper

    def add_roles(self, *roles):
        self.roles.extend([role for role in roles if role not in self.roles])

    def remove_roles(self, *roles):
        self.roles = [role for role in self.roles if role not in roles]