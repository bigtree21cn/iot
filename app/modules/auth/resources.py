#!/usr/bin/env python
import os

from flask import abort, request, jsonify, g, url_for, make_response
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource

from app.extensions import auth
from .models import db, User, Device


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return user.enabled


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

class UserAPI(Resource):
    @auth.login_required
    def get(self, id):
        uname = request.json.get('username')
        user = User.query.filter_by(username=uname)
        if not user:
            abort(400)
        return make_response({'username': uname}, 200)

    def put(self):
        pass

    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        if username is None or password is None:
            abort(400)  # missing arguments
        if User.query.filter_by(username=username).first() is not None:
            abort(400)  # existing user
        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return (jsonify({'username': user.username}), 201,
                {'Location': url_for('get_user', id=user.id, _external=True)})

class TokenAPI(Resource):
    @auth.login_required
    def get(self):
        token = g.user.generate_auth_token()
        return make_response({'username': token}, 200)

'''
@db.app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


@db.app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.username})
'''