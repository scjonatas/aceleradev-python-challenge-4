import jwt

SECRET = 'acelera'
ALGORITHM_HS256 = 'HS256'
ERROR_CODE_GENERIC_EXCEPTION = 1
ERROR_CODE_INVALID_SIGNATURE = 2
ERROR_CODE_EXPIRED_SIGNATURE = 3


def create_token(data: dict, secret: str) -> bytes:
    """Returns a JWT Token encoded with HS256 algorithm"""
    return jwt.encode(data, secret, algorithm=ALGORITHM_HS256)


def verify_signature(token: bytes) -> dict:
    """
    Decode a JWT Token and returns the decoded data if succeeds,
    or an error code otherwise.
    """
    try:
        return jwt.decode(token, SECRET, algorithms=ALGORITHM_HS256)
    except jwt.ExpiredSignatureError:
        return {"error": ERROR_CODE_EXPIRED_SIGNATURE}
    except jwt.InvalidSignatureError:
        return {"error": ERROR_CODE_INVALID_SIGNATURE}
    except Exception:
        return {"error": ERROR_CODE_GENERIC_EXCEPTION}
