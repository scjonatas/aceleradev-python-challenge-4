import main
from main import create_token, verify_signature
from datetime import datetime
from time import sleep


class TestChallenge4:
    token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsYW5ndWFnZSI6IlB5dGhvbiJ9.sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M'

    def test_create_token(self):
        assert create_token({"language": "Python"}, 'acelera') == self.token

    def test_verify_token_success(self):
        assert verify_signature(self.token) == {"language": "Python"}

    def test_verify_token_invalid_signature(self):
        invalid_token = create_token({"language": "Python"}, 'wrong_secret')
        assert verify_signature(invalid_token) == {
            "error": main.ERROR_CODE_INVALID_SIGNATURE}

    def test_verify_token_expired(self):
        payload = {"language": "Python",
                   "exp": datetime.utcnow()}
        token = create_token(payload, 'acelera')
        assert verify_signature(token) == payload
        sleep(1)
        assert verify_signature(token) == {
            "error": main.ERROR_CODE_EXPIRED_SIGNATURE}
