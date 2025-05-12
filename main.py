# This entrypoint file to be used in development. Start by reading README.md
import password_cracker
from unittest import main

cracked_password1 = password_cracker.crack_sha1_hash(
    "fbbe7e952d1050bfb09dfdb71d4c2ff2b3d845d2")
print(cracked_password1)

#test

cracked_password2 = password_cracker.crack_sha1_hash(
    "da5a4e8cf89539e66097acd2f8af128acae2f8ae", True)
print(cracked_password2)

# Run unit tests automatically
main(module = "test_module", exit = False)
