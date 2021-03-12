import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8) # 64 bits.
    assert 8 == len(salt)
    # assert isinstance(salt, str)

    # if isinstance(password, ):
    # if isinstance(password,str):
    #     password = password.encode('UTF-8')

    # assert isinstance(password, str)

    result = password.encode('utf-8')
    for i in range(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result

hashed = encrypt_password('majunshiwo')
print(hashed)
# 验证函数
def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])
#
assert validate_password(hashed, 'majunshiwo')
print(validate_password(hashed, 'majunshiwo'))