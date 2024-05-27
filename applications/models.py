from django.db import models

class Application(models.Model):
    FULLSTACK = 'fullstack'
    FRONTEND = 'frontend'
    BACKEND = 'backend'
    QA = 'qa'

    EXPERTISE_CHOICES = [
        (FULLSTACK, 'Fullstack Developer'),
        (FRONTEND, 'Front End Developer'),
        (BACKEND, 'Backend Developer'),
        (QA, 'QA Engineer'),
    ]

    name = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    expertise = models.CharField(max_length=50, choices=EXPERTISE_CHOICES)
    cv = models.FileField(upload_to='cvs/')

    def __str__(self):
        return self.name
