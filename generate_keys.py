from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server.auth.providers.bearer import RSAKeyPair

# Generate a new key pair
key_pair = RSAKeyPair.generate()
print(f"Public Key: {key_pair.public_key}")

# Configure the auth provider with the public key
auth = BearerAuthProvider(
    public_key=key_pair.public_key,
    issuer="https://dev.example.com",
    audience="my-dev-server"
)

# Generate a token for testing
token = key_pair.create_token(
    subject="dev-user",
    issuer="https://dev.example.com",
    audience="my-dev-server",
    scopes=["read", "write"]
)

print(f"Test token: {token}")

# Write public key to a .pem file
with open("public_key.pem", "w") as pub_file:
    pub_file.write(key_pair.public_key)

# Write private key to .env file as API_KEY variable
with open("token.secret", "w") as env_file:
    env_file.write(token)
