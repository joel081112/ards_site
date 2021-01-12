from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Member, Awards, Batting, Type
from .forms import AddMemberForm


def index(request):
    member_list = Member.objects.order_by('id')

    form = AddMemberForm()

    context = {'member_list': member_list, 'form': form}
    return render(request, 'cricket/test.html', context)


@require_POST
def add_new_member(request):
    form = AddMemberForm(request.POST)

    if form.is_valid():
        new_member = Member(name=request.POST['name'])
        new_member.save()

    return redirect('index')


def delete_member(request, member_id):
    Member.objects.get(pk=member_id).delete()

    return redirect('index')


def delete_all(request):
    Member.objects.all().delete()

    return redirect('index')



