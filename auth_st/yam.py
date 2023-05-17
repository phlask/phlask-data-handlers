import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Generate hashed passwords
hashed_passwords = stauth.Hasher(['abc123', 'def456']).generate()
print(hashed_passwords)