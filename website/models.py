from django.db import models
from django.contrib.auth.models import User

PERIOD_CHOICES = (
    ('week', 'week'),
    ('month', 'month'),
)

class Task(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	hours = models.IntegerField()
	period = models.CharField(max_length=10, choices=PERIOD_CHOICES)
	users = models.ManyToManyField(User, limit_choices_to = {'is_active__exact': True}, blank=True, null=True)

	def __unicode__(self):
		return self.name

class Assignment(models.Model):
	user = models.ForeignKey(User, limit_choices_to = {'is_active__exact': True})
	task = models.ForeignKey(Task)
	time = models.IntegerField(blank=True, null=True)
	report = models.TextField(blank=True)
	when = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s %s %s" % (str(self.when), str(self.user), str(self.task))
