from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_new_member, name='add'),
    path('delete_member/<member_id>', views.delete_member, name='deletemember'),
    path('delete_all_members', views.delete_all, name='deleteall'),
    path('members/', include('ards_site.members.urls'))
]
