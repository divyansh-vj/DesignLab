# create_jwt.py
import time
import jwt  # PyJWT

APP_ID = "2033097"                   # your app id (string or int)
PRIVATE_KEY_PATH = "myapp-divyansh-vj.2025-09-29.private-key.pem"  # path to downloaded .pem

now = int(time.time())
payload = {
    # issued at
    "iat": now - 60,              # recommended to set 60s in the past to allow clock skew
    "exp": now + (9 * 60),        # must be <= 10 minutes; choose <10min to be safe
    "iss": APP_ID
}

with open(PRIVATE_KEY_PATH, "r") as f:
    private_key = f.read()

jwt_token = jwt.encode(payload, private_key, algorithm="RS256")
print(jwt_token)  # save/use this value to request an installation token

