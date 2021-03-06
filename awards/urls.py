from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    # url(r'^project/(\d+)',views.project,name ='project'),
    url(r'^$',views.awards,name = 'home'),
    url(r'^awards/$',views.awards,name = 'awards'),
    url(r'^post/(\d+)/$',views.projects,name = 'home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^profile/(\w+)/$', views.profile, name='profile'),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
    url(r'^api/merch/$', views.MerchList.as_view()),
    url(r'api/merches/(?P<pk>[0-9]+)/$',
        views.MerchDescription.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)