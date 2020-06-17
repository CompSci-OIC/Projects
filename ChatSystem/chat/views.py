# chat/views.py
from django.shortcuts import render, redirect

from .forms import NameForm , GroupForm, JoinGroupForm
from .models import CustomGroup


def index(request):
    # has to create an instance of an group class
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            request.session['username'] = name
            return redirect('group_selection')
    if request.method == 'GET':
        request.session.flush()
        form = NameForm()
    return render(request, 'chat/index.html',{
        'nameForm': form
    })

def create_name(request):#!!!!
    # check if session has started and delete it if yes
    # take the room_name
    # create CustomUser instance
    # start session
    # render the page

    pass


def group_selection(request):#!!!!
    # check if session started go to create_name page in case not
    # render the page
    form = JoinGroupForm()
    if not('username' in request.session):
        return redirect('index')

    if request.method == 'POST':
        form = JoinGroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['group_name']
            return redirect('../room/' +name )


    return render(request, 'chat/select.html', {
        'username': request.session['username'],
        'groupForm': form
    })

def create_group(request):
    # generate the id and create an instance of the group
    # create group button should set joined_group parameter of a user to the created group
    if not('username' in request.session):
        return redirect('index')
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['group_name']
            print(name)
            groupInfo = CustomGroup(group_name = name)
            groupInfo.save()
            return redirect('../room/' + str(groupInfo.id))
    if request.method == 'GET':
        form = GroupForm()

    # create custom group instance
    # instance.save()

    return render(request, 'chat/createGroup.html', {
            'username': request.session['username'],
            'groupForm': form

    })

def not_found(request):
    # display 404 not found
    # render

    pass

def room(request, room_name):
    # check if session started go to create_name page in case not
    # check if group exists, if not group selection screen
    # check if user is in the group if not add him
    # render


    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
