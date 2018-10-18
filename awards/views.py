from .forms import NewProjectForm,ProfileForm,Votes
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse
from .models import Project,Profile,Ratings
from django.contrib.auth.models import User
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .serializer import MerchSerializer,ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
@login_required
def index(request):
    posts = Project.objects.all()
    return render(request,'all-awards/index.html',{"posts":posts})

def awards(request):
    return render(request,'awards.html')

@login_required(login_url='/accounts/login/')
def projects(request, projects_id):
    project = Project.objects.get(id=projects_id)
    likes = Ratings.objects.filter(post=project)
    design = []
    usability = []
    creativity = []
    content = []
    for x in likes:
                design.append(x.design)
                usability.append(x.usability)
                creativity.append(x.creativity)
                content.append(x.content)
    de = []
    us = []
    cre = []
    con = []

    if len(usability)>0:
            usa = (sum(usability)/len(usability))
            us.append(usa)
    if len(creativity)>0:
            crea = (sum(creativity)/len(creativity))
            cre.append(crea)
    if len(design)>0:
            des = (sum(design)/len(design))
            de.append(des)
    if len(content)>0:
            cont = (sum(content)/len(content))
            con.append(cont)
    vote = Votes()
    if request.method == 'POST':

            vote_form = Votes(request.POST)
            if vote_form.is_valid():

                    design = vote_form.cleaned_data['design']
                    usability = vote_form.cleaned_data['usability']
                    content = vote_form.cleaned_data['content']
                    creativity = vote_form.cleaned_data['creativity']
                    rating = Ratings(design=design,usability=usability,
                                    content=content,creativity=creativity,
                                    user=request.user,post=project)
                    rating.save()
                    return redirect('/')
    return render(request,"awards.html",{"post":project,"des":de,"usa":us,"cont":con,"crea":cre,"vote":vote})


    # try:
    #     project = Project.objects.get(id = project_id)
    # except DoesNotExist:
    #     raise Http404()
    # return render(request,"all-awards/awards.html", {"project":project})

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
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
            print('saved')
            
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

class MerchList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_merch = Project.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)
   
    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
       
class MerchDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return Profile.objects.get(id=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProfileSerializer(merch)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        merch = self.get_merch(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)