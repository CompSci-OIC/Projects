from django.db import models

class CustomUser(models.Model):
    name = models.CharField(max_length = 200)
    joined_group = models.CharField(max_length = 5)





    pass

class CustomGroup(models.Model):
    group_name = models.CharField(max_length = 50)



    pass


class Message(models.Model):
    group = models.ForeignKey(CustomGroup, on_delete = models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length = 50)
    #time_stamp = models.TimeField()



    pass
