import hashlib
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self._hash_password(password)
        self.is_verified = False

    def _hash_password(self, password):
        # Use a secure hashing algorithm like bcrypt or Argon2 in production
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        hashed_password = self._hash_password(password)
        return self.password == hashed_password

    def set_verified(self):
        self.is_verified = True
