from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from ards_site.models import Member, Awards, Batting, Role, Type, Cup
from .forms import MemberForm


def member_view(request):
    member_list = Member.objects.order_by('id')

    context = {'member_list': member_list}
    return render(request, 'cricket/members.html', context)


def view_selected_member(request, member_id):
    obj = Member.objects.get(pk=member_id)
    # Role.objects.get(pk=member_id)

    context = {
        'object': obj
    }
    return render(request, 'cricket/member_selected.html', context)


def view_selected_member_role(request, role):
    role_list = Member.objects.filter(role__name__contains=role)

    context = {
        'role_list': role_list
    }
    return render(request, 'cricket/member_role.html', context)


def view_selected_member_team(request, team):
    team_list = Member.objects.filter(teamsPlayedFor__name__contains=team)

    context = {
        'team_list': team_list
    }
    return render(request, 'cricket/member_team.html', context)


def create_member(request):
    form = MemberForm()

    context = {'form': form}
    return render(request, 'cricket/member_create.html', context)


@require_POST
def add_new_member(request):

    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('members')


def member_form(request, member_id):
    obj = Member.objects.get(pk=member_id)
    form = MemberForm(instance=obj)
    if request.method == 'POST':
        print("Printing POST")
        form = MemberForm(request.POST, instance=obj)
        print(obj)
        if form.is_valid():
            print("Valid")
            form.save()
            return redirect('members')

    context = {'form': form}

    return render(request, 'cricket/member_update.html', context)



'''
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        return redirect('members')
'''