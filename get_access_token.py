import time, jwt, requests

APP_ID = "2033097"
PRIVATE_KEY_PATH = "myapp-divyansh-vj.2025-09-29.private-key.pem"
INSTALLATION_ID = "87962835"

# build JWT (same as earlier)
now = int(time.time())
payload = {"iat": now - 60, "exp": now + (9*60), "iss": APP_ID}
with open(PRIVATE_KEY_PATH, "r") as f:
    private_key = f.read()
jwt_token = jwt.encode(payload, private_key, algorithm="RS256")

# exchange for installation token
url = f"https://api.github.com/app/installations/{INSTALLATION_ID}/access_tokens"
headers = {
    "Authorization": f"Bearer {jwt_token}",
    "Accept": "application/vnd.github+json"
}
r = requests.post(url, headers=headers)
r.raise_for_status()
data = r.json()
installation_token = data["token"]
expires_at = data.get("expires_at")
print("installation_token:", installation_token)
print("expires_at:", expires_at)

# example authenticated request as the installation
r2 = requests.get("https://api.github.com/installation/repositories",
                  headers={"Authorization": f"Bearer {installation_token}",
                           "Accept": "application/vnd.github+json"})
print(r2.status_code, r2.text)

