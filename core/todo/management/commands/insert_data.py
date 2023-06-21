from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from todo.models import Task
import random
class Command(BaseCommand):
    help = "inserting dummy data"
    def __init__(self,*args, **kwargs):
        super(Command,self).__init__(*args, **kwargs)
        self.fake=Faker()


    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(),username=self.fake.user_name(),password="test@1234567")
        for _ in range(5):
            Task.objects.create(
                author = user,
                title = self.fake.paragraph(nb_sentences = 10),
                done = random.choice([True,False])
            )