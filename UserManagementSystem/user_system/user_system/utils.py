import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def check_password(input,stored_password):
    return hash_password(input)==stored_password