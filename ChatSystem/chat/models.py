from django.db import models
from django import forms

class CustomUser(models.Model):
    name = models.CharField(max_length = 200)
    joined_group = models.CharField(max_length = 5)





    pass

class CustomGroup(models.Model):
    group_name = models.CharField(max_length = 50)
    joined_users = models.TextField(default = "")# space separated string of user_ids


    def add_user(self, user):
        self.joined_users = self.joined_users + str(user) + str(" ")

        pass

    def user_count(self):
        return len(self.joined_users.strip().split(" "))



class Message(models.Model):
    group = models.ForeignKey(CustomGroup, on_delete = models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length = 50)
    #time_stamp = models.TimeField()



    pass
