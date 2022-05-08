from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    dept = models.CharField(max_length=30)
    owner = models.CharField(max_length=5)
    topik = models.CharField(max_length=100)
    problem = models.TextField()
    action = models.TextField()
    due_date = models.DateField()
    pic = models.CharField(max_length=100)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.dept


class Venue(models.Model):
    tanggal = models.DateField()
    waktu = models.TimeField()
    notulen = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.notulen
