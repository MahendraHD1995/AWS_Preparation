from django.db import models

# Create your models here.

class EC2(models.Model):
    ID = models.AutoField(primary_key=True)
    QUESTION = models.TextField()
    OPTION_A = models.TextField()
    OPTION_B = models.TextField()
    OPTION_C = models.TextField()
    OPTION_D = models.TextField()
    OPTION_E = models.TextField()
    ANSWER = models.TextField()

    class Meta:
      db_table = "EC2"

