from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from album.forms import LoginForm
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

from album.models import Album, Photo


@login_required
def home(request):  
    albums = Album.objects.filter(user=request.user)
    data = {"albums": albums}
    return render_to_response('index.html', data, context_instance=RequestContext(request))


@login_required
def add_album(request):
    data = {}
    return render_to_response('add_album.html', data, context_instance=RequestContext(request))


@login_required
def show_album(request, pk):
    album = Album.objects.get(id=pk)
    photos = Photo.objects.filter(album=album)
    data = {"album": album, "photos": photos}
    return render_to_response('show_album.html', data, context_instance=RequestContext(request))

@login_required
def save_album(request):
    data = {}
    title = request.POST["title"]
    description = request.POST["description"]
    album = Album(user=request.user, title=title, description=description, img=request.FILES['img'])
    album.save()

    albums = Album.objects.filter(user=request.user)
    data = {"albums": albums}
    return render_to_response('index.html', data, context_instance=RequestContext(request))


################################################
#                                              #
#               LOGIN/LOGOUT                   #
#                                              #
################################################
def login_page(request):
    message = error = None
    username = password = ''
    form = LoginForm()

    # default next page is index page
    next_page = "/"

    # getting next page in get request
    if request.GET:
        next_page = request.GET.get('next')

    if request.POST:
        # a form bound to the post data
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"

                # redirect after post
                return HttpResponseRedirect(next_page)
            else:
                message = "Your account is not active, please contact the site admin."
                error = 1
        else:
            message = "Your username and/or password were incorrect."
            error = 1

    c = {'username': username, 'form': form, 'next': next_page}
    if message:
        c.update({"message": message})
    if error:
        c.update({"error": error})
    c.update(csrf(request))

    return render_to_response('login.html', c)


def logout_page(request):
    """ Log users out and re-direct them to the main page. """
    logout(request)
    return HttpResponseRedirect('/login/', {'request': request})
