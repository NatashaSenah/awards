from django.contrib.auth.decorators import login_required.
from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def home(request):
     return render(request, 'awards.html')
@login_required(login_url='/accounts/login/')
def article(request, article_id):