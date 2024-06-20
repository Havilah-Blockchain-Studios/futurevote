from django.db import models
from users.models import User


# Create your models here.
class Election(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()
    party = models.CharField(max_length=100)
    image = models.ImageField(upload_to="candidates/")
    manifesto = models.FileField(upload_to="manifesto/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " - " + self.election.name


class Vote(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            self.user.email + " - " + self.candidate.name + " - " + self.election.name
        )
