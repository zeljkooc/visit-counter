import os

import requests

PORT = os.getenv("APP_PORT", "8080")

#Test koji proverava stanje visits pre i posle inkrementiranja i poredi ih
def testVisits():
    response1 = requests.get(f"http://127.0.0.1:{PORT}/visits")
    assert response1.status_code == 200

    visits1 = response1.json()["visits"]

    response = requests.get(f"http://127.0.0.1:{PORT}/visits")
    assert response.status_code == 200

    visits2 = response.json()["visits"]

    assert visits2 == visits1 + 1

#Test koji proverava da li aplikacija radi i da li na index stranici prikazuje poruku
def testIndex():
    response = requests.get(f"http://127.0.0.1:{PORT}/")
    assert response.status_code == 200

    msg = response.json()["message"]

    assert msg == "Hello DevOps"
