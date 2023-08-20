from fastapi.testclient import TestClient 

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Job"}



def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == True

def test_predict():
    response = client.post("/predict/", json={"features": [1,2,21,1,3]})
    assert response.status_code == 200
    assert response.json() == {"prediction": 2}