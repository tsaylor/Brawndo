from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.list_detail import object_list
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
def report_list(request):
	"""
	Wrapper around the object_list generic view, filtered by request.user.
	List a user's assignments/reports
	"""
	qs = Assignment.objects.filter(user__exact=request.user).order_by('-when')
	return object_list(request, qs, template_name="report_list.html")

@login_required
def report_edit(request, reportid):
	"""
	Users file a report for what they did.
	"""
	try:
		a = Assignment.objects.get(id=reportid)
	except:
		message.error(request, 'There was a problem finding the requested report (id=%d)' % reportid)
		return HttpResponseRedirect(reverse('report_list'))
	if request.method == "GET":
		form = AssignmentForm(instance=a)
	elif request.method == "POST":
		form = AssignmentForm(request.POST, instance=a)
		if form.is_valid():
			form.save()
			messages.success(request, 'You have filed your report, thanks!')
			return HttpResponseRedirect(reverse('home'))
	return render_to_response('report_form.html', locals(), context_instance=RequestContext(request))

@login_required
def report_new(request):
	"""
	The user files a report for a task to which they were not previously assigned.
	"""
	if request.method == "GET":
		form = AssignmentForm()
	elif request.method == "POST":
		form = AssignmentForm(request.POST)
		if form.is_valid():
			a = form.save(commit=False)
			a.user = request.user
			a.save()
			messages.success(request, 'You have filed your report, thanks!')
			return HttpResponseRedirect(reverse('home'))
	return render_to_response('report_form.html', locals(), context_instance=RequestContext(request))
