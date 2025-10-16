from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class mentor(models.Model):
    photo=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.BigIntegerField()
    gender=models.CharField(max_length=200)
    LOGIN=models.ForeignKey(login,default=1, on_delete=models.CASCADE)

class user(models.Model):
    photo=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.BigIntegerField()
    gender=models.CharField(max_length=200)
    LOGIN=models.ForeignKey(login,default=1, on_delete=models.CASCADE)

class complaint(models.Model):
    complaint=models.CharField(max_length=200)
    Cdate=models.CharField(max_length=200)
    reply=models.CharField(max_length=200)
    Rdate=models.CharField(max_length=200)
    USER=models.ForeignKey(user,default=1, on_delete=models.CASCADE)

class mentor_review(models.Model):
    review=models.CharField(max_length=300)
    rating = models.CharField(max_length=100, default=1)
    date=models.CharField(max_length=200)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    MENTOR=models.ForeignKey(mentor,default=1,on_delete=models.CASCADE)

class app_review(models.Model):
    review=models.CharField(max_length=200)
    rating=models.CharField(max_length=100,default=1)
    date=models.CharField(max_length=200)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)


class requests(models.Model):
    status=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    MENTOR=models.ForeignKey(mentor,default=1,on_delete=models.CASCADE)

class emotions(models.Model):
    photo=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    emotion=models.CharField(max_length=200)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)

class diary(models.Model):
    content=models.CharField(max_length=2000)
    emotion=models.CharField(max_length=200)
    date=models.CharField(max_length=200, default="0000-00-00")
    time=models.CharField(max_length=200, default="00:00")
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)

class chat(models.Model):
    message=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    type=models.CharField(max_length=200,default=1)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    MENTOR=models.ForeignKey(mentor,default=1,on_delete=models.CASCADE)

class tips(models.Model):
    tip=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    MENTOR=models.ForeignKey(mentor,default=1,on_delete=models.CASCADE)

class motivation(models.Model):
    content=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    MENTOR=models.ForeignKey(mentor,default=1,on_delete=models.CASCADE)
