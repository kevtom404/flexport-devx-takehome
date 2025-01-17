import json

from rock_paper_scissors.app import app

"""
    Test Flask Application and API for Rock Paper Scissors
"""


def test_app_health():
    with app.test_client() as test_client:
        response = test_client.get("/health")
        assert response.status_code == 200
        assert b"OK" in response.data


def test_rps_valid_move():
    with app.test_client() as test_client:
        response = test_client.post(
            "/rps", data=json.dumps(dict(move="Rock")), content_type="application/json"
        )
        assert response.status_code == 200


def test_rps_invalid_move():
    with app.test_client() as test_client:
        response = test_client.post(
            "/rps", data=json.dumps(dict(move="Stone")), content_type="application/json"
        )
        assert response.status_code == 500
