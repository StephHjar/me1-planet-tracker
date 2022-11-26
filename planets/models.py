from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

file = open('planets/planets.txt', 'r')
PLANET_CHOICES = [[x.rstrip('\n'), x.rstrip('\n')] for x in file]
print(PLANET_CHOICES)


class Planet(models.Model):
    name = models.CharField(max_length=200, choices=PLANET_CHOICES, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='planets', null=True)
    fully_explored = models.BooleanField(default=False)
    turian_insignia = models.BooleanField(default=False)
    asari_writing = models.BooleanField(default=False)
    prothean_disc = models.BooleanField(default=False)
    mineral = models.BooleanField(default=False)
    medallion = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
