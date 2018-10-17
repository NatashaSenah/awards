from .forms import NewProjectForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse
from .models import Project,Profile
from django.contrib.auth.models import User

# Create your views here.
@login_required
def home(request):
    user = request.user
    return render(request, 'awards.html', {'user':user})


@login_required(login_url='/accounts/login/')
def Projects(request, projects_id):
    try:
        project = Project.objects.get(id = project_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-awards/awards.html", {"project":project})


def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_project = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-awards/search.html',{"message":message,"project": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-awards/search.html',{"message":message})
@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.editor = current_user
            project.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})


def profile(request, username):
    profile = get_object_or_404(User,username=username)
 
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    # images = Project.get_profile_images(profile.id)
    title = f'@{profile.username} Instagram photos and videos'

    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details})


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            username = request.user.username
            return redirect('profile', username=username)
    else:
        form = ProfileForm()

    return render(request, 'profile/edit_profile.html', {'form': form})