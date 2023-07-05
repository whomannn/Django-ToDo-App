from rest_framework.test import APIClient
import pytest
from django.contrib.auth.models import User


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="test2@gmail.com",
        username="test2",
        password="test@1234567",
        is_staff=True,
    )
    return user


@pytest.mark.django_db
class TestTaskApi:
    def test_get_task_response_200(self):
        client = APIClient()
        response = client.get("http://127.0.0.1:8000/tasks/api/v1/task/")
        assert response.status_code == 200

    def test_create_task_response_201(self, common_user):
        client = APIClient()
        data = {
            "title": "test",
            "done": True,
        }
        client.force_login(user=common_user)
        response = client.post("http://127.0.0.1:8000/tasks/api/v1/task/", data)
        assert response.status_code == 201

    def test_create_task_invaliddata_response_201(self, common_user):
        client = APIClient()
        data = {}
        client.force_login(user=common_user)
        response = client.post("http://127.0.0.1:8000/tasks/api/v1/task/", data)
        assert response.status_code == 400
