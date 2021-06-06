from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#for the Contact us page
class Contact(models.Model):
    fname=models.CharField(max_length=122)
    lname=models.CharField(max_length=122)
    email=models.CharField(max_length=254)
    comment=models.TextField()
    date=models.DateField()

#for the signup page
class Signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    role=models.CharField(max_length=254)

    def __str__(self):
        return self.user


#for the notes page
class Notes(models.Model):
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    notesfilr=models.FileField(max_length=30)
    clg_yr=models.CharField(max_length=10)
    

    




