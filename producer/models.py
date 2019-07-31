from django.db import models

class Bankprod(models.Model):

   user_name = models.CharField(max_length = 50)
   email = models.CharField(max_length = 50)
   acc_number = models.IntegerField()
   phonenumber = models.IntegerField()
   payment = models.IntegerField()

   class Meta:
      db_table = "Bankprod"