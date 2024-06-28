import requests
import pytest

# Appium can not test API calls, must use another library like requests
def test_API_call():
    r = requests.get('http://localhost:3000/users')
    print(r.json())
    
    assert r.status_code is 200