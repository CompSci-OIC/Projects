# chat/views.py
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

from .forms import NameForm , GroupForm, JoinGroupForm
from .models import CustomGroup, CustomUser


def index(request):
    # has to create an instance of an group class
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            user = CustomUser(name = name)
            user.save()
            request.session['userId'] = user.id
            return redirect('group_selection')
    if request.method == 'GET':
        if 'userId' in request.session:
            userId = request.session['userId']
            print(len(CustomUser.objects.all()))
            CustomUser.objects.get(id = userId).delete()
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
    errorFlag = 0
    if 'errorFlag' in request.session:
        if request.session['errorFlag'] == 1:
            request.session['errorFlag'] = 0
            errorFlag = 1
    print(request.session['userId'])


    form = JoinGroupForm()
    if not('userId' in request.session):
        return redirect('index')

    if request.method == 'POST':
        form = JoinGroupForm(request.POST)
        if form.is_valid():

            groupId = form.cleaned_data['group_id']
            if groupId.isnumeric():
                if CustomGroup.objects.filter(id = int(groupId)).exists():
                    group = CustomGroup.objects.get(id = int(groupId))
                    group.save()
                    return redirect('../room/' + groupId)
                else:
                    errorFlag = 1
                    request.session['errorFlag'] = 1
                    return redirect('.')
            else:
                errorFlag = 1
                request.session['errorFlag'] = 1
                return redirect('.')

    return render(request, 'chat/select.html', {
        'username': CustomUser.objects.get(id = request.session['userId']).name,
        'groupForm': form,
        'errorFlag': errorFlag
    })

def create_group(request):
    # generate the id and create an instance of the group
    # create group button should set joined_group parameter of a user to the created group
    if 'group_id' in request.session:
        group = CustomGroup.objects.get(id = request.session['group_id'])
    else:
        group = CustomGroup()
        group.save()
        request.session['group_id'] = group.id

    if not('userId' in request.session):
        return redirect('index')
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['group_name']
            request.session.pop('group_id')
            group.group_name = name
            group.save()

            return redirect('../room/' + str(group.id))
    if request.method == 'GET':
        form = GroupForm()

    # create custom group instance
    # instance.save()

    return render(request, 'chat/createGroup.html', {
            'username':  CustomUser.objects.get(id = request.session['userId']).name,
            'groupForm': form,
            'group_id': group.id

    })

def not_found(request):
    # display 404 not found
    # render

    pass

def room(request, room_id):
    # check if session started go to create_name page in case not
    # check if group exists, if not group selection screen
    # check if user is in the group if not add him
    # render
    userString = ""
    group = CustomGroup.objects.get(id = room_id)
    newList = group.get_users()
    newList = list(map(lambda x: CustomUser.objects.get(id = int(x)).name + "#"+ x, newList ))

    return render(request, 'chat/room.html', {
        'room_id': group.id,
        'room_name': group.group_name,
        'Participants': newList,
        'user_id': request.session['userId'],
        'user_name': CustomUser.objects.get(id = request.session['userId']).name
    })
