from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime
from django.contrib.auth.models import User
@pytest.mark.django_db
class TestTaskApi:
    def test_get_task_response_200(self):
        client = APIClient()
        response = client.get('http://127.0.0.1:8000/tasks/api/v1/task/')
        assert response.status_code == 200
    def test_create_task_response_401(self):
        user = User.objects.create_user(email='test2@gmail.com',username="test2",password="test@1234567")
        client = APIClient()
        data = {
            'author' : user,
            'title' : 'test',
            'done' : True,
        }
        response = client.post('http://127.0.0.1:8000/tasks/api/v1/task/',data)
        assert response.status_code == 401
        