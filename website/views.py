from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from website.models import Task, Assignment
from website.forms import AssignmentForm

def home(request):
	"""
	Returns the list of tasks and users who are signed up for them.
	If the user is logged in, it includes links to join/quit the task.
	"""
	tasks = Task.objects.all()
	return render_to_response('home.html', locals(), context_instance=RequestContext(request))

@login_required
def jointask(request, taskid):
	"""
	Adds a user to a task.
	"""
	t = Task.objects.get(id = taskid)
	t.users.add(request.user)
	messages.success(request, 'You have joined the task "%s"' % (t.name))
	return HttpResponseRedirect(reverse('home'))

@login_required
def quittask(request, taskid):
	"""
	Removes a user from a task.
	"""
	t = Task.objects.get(id = taskid)
	t.users.remove(request.user)
	messages.success(request, 'You have quit the task "%s"' % (t.name))
	return HttpResponseRedirect(reverse('home'))

@login_required
def report(request):
	"""
	Users file a report for what they did.
	"""
	a = Assignment.objects.all().order_by('-when')
	if request.method == "GET":
		form = AssignmentForm(instance=a[0])
	elif request.method == "POST":
		form = AssignmentForm(request.POST, instance=a[0])
		if form.is_valid():
			form.save()
			messages.success(request, 'You have filed your report, thanks!')
			return HttpResponseRedirect(reverse('home'))
	return render_to_response('report.html', locals(), context_instance=RequestContext(request))
