from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER=(
        ("f","female"),
        ("m","male"),
        ("u","undisclosed")
    )
    name=models.CharField(max_length=200)
    roll_no=models.IntegerField(unique=True)
    email=models.EmailField(max_length=200)
    gender=models.CharField(max_length=1,choices=GENDER)
    percenatge=models.FloatField()

    institute=models.ForeignKey("Institute",on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.name

class Institute(models.Model):
    TYPES=(
        ("c","college"),
        ("h","high school")
    )

    institute=models.CharField(max_length=255)
    type_of_institute=models.CharField(max_length=1,choices=TYPES)

    def __str__(self):
        return self.institute