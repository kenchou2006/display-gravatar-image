import hashlib

def get_gravatar_hash(email):
    email = email.strip().lower()
    return hashlib.md5(email.encode('utf-8')).hexdigest()

def get_gravatar_url(email):
    hash = get_gravatar_hash(email)
    return f"https://www.gravatar.com/avatar/{hash}"

print(get_gravatar_url("test@example.com"))
