import jwt
from datetime import datetime, timedelta


class TokenManager:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def generate_verification_token(self, user):
        payload = {
            'username': user.username,
            'exp': datetime.utcnow() + timedelta(days=1)
        }
        verification_token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return verification_token

    def verify_token_and_get_username(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            if type(payload) == dict and payload.get('username') and payload.get('exp'):
                return payload.get('username')
            return None

        except jwt.DecodeError:
            return None
        except jwt.ExpiredSignatureError:
            return None
