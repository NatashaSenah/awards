from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def home(request):
     return render(request, 'awards.html')
@login_required(login_url='/accounts/login/')
def Projects(request, projects_id):
    try:
        project = Project.objects.get(id = project_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-awards/awards.html", {"project":project})