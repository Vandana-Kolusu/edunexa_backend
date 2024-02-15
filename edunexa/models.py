from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    secquestion = models.CharField(max_length=255)
    secanswer = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return self.email  # or any other field you prefer for string representation
