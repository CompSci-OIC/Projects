# chat/views.py
from django.shortcuts import render

from .forms import NameForm

def index(request):
    # has to create an instance of an group class
    if request.method == 'POST':
        form = NameForm(request.POST)
        print(form.your_name)
    else:
        form = NameForm()
    return render(request, 'chat/index.html',{
        'nameForm': form
    })

def create_name(request,prev_url):#!!!!
    # check if session has started and delete it if yes
    # take the room_name
    # create CustomUser instance
    # start session
    # render the page

    pass


def group_selection(request):#!!!!
    # check if session started go to create_name page in case not
    # render the page
    return render(request, 'chat/select.html', {
        'username': "Adi"
    })

def create_group(request):
    # check if session started go to create_name page in case not
    # generate the id and create an instance of the group
    # create group button should set joined_group parameter of a user to the created group
    # render


    return render(request, 'chat/createGroup.html', {
            'username': "Adi"
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
