from keycloak import KeycloakOpenID, KeycloakOpenIDConnection, KeycloakAdmin
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


def get_client():
    return KeycloakOpenID(
        server_url='http://localhost:8080/auth/',
        realm_name='django_realm',
        client_id='django_client',
        client_secret_key='xl3QPGvyQ6kOro3AbD4DFrVeuBoZIE56',
    )


def get_auth_url(client, **kwargs):
    auth_url = client.auth_url(
        redirect_uri='http://localhost:8000/keycloak_callback',
    )
    return auth_url


def get_access_token(client, code):
    access_token = client.token(
        grand_type='authorization_code',
        code=code,
        redirect_url='http://localhost:8000/keycloak_callback'
    )
    return access_token


def get_token(client, user, passwd):
    token = client.token(user, passwd)
    return token
