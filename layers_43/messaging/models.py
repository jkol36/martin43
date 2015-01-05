from django.db import models
from layers_43.consumer.models import Project, ProjectUpdate, ProjectUpdateItem
from django.contrib.auth.models import User


# Create your models here.

class Message(models.Model):
	text = models.CharField(max_length=250, null = True, blank = True)
	recipient = models.ForeignKey(User, related_name = "recipient")
	sender = models.ForeignKey(User, related_name = "sender")
	project = models.ForeignKey(Project, null=True, blank=True, related_name = "Projects")

	def __unicode__(self):
		return self.text

	def get_recipient(self):
		return self.recipient.username

	def get_sender(self):
		return self.sender.username

	def get_project(self):
		user = self.project.user.username
		title = self.project.title

		return ("User: %s, Title: %s") %(user, title)


