from django.shortcuts import render
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.paginator import Paginator
from .models import User, Record

# Default webpage
def index(request):
    return render(request, 'index.html', {})

#Record the time the student solved the math problem
@login_required
@csrf_exempt
def record(request, skill):
    user = request.user.username
    if request.method == "POST":
        import json
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        User = get_user_model()
        user = User.objects.get(username=user)
        #skill = request.POST.get("skill")
        record = Record()
        now = datetime.now()
        record.timestamp = now.strftime(" %d %B %Y %X ")
        record.seconds = data
        record.user = user
        record.skill = skill
        record.save()
        return JsonResponse({"status": 201})


@login_required
def profile(request, username):
    User = get_user_model()
    username = User.objects.get(username=username)
    record1 = Record.objects.filter(user=username, skill="addition1").order_by('-timestamp')
    record2 = Record.objects.filter(user=username, skill="addition2").order_by('-timestamp')
    record3 = Record.objects.filter(user=username, skill="multiplication").order_by('-timestamp')
    return render(request, 'profile.html', {
        'username': username,
        'record1': record1,
        'record2': record2,
        'record3': record3
    })


# addition for 1 digit number view
def addition1(request):
    if request.user.username:
        user = request.user.username
        #show all user record
        record = Record.objects.filter(skill="addition1").order_by('seconds')

        paginator = Paginator(record, 3)
        record = paginator.page(1)

        return render(request, 'addition1.html', {
            'username': user,
            'record': record
        })
    # if user is not loged in, send a message to remind user to log in
    else:
        return render(request, "index.html", {
                "message": "Log in to use this feature."
            })


# addition up to 2 digit number view
def addition2(request):
    if request.user.username:
        user = request.user.username
        # show all user record
        record = Record.objects.filter(skill="addition2").order_by('seconds')

        paginator = Paginator(record, 3)
        record = paginator.page(1)
        return render(request, 'addition2.html', {
            'username': user,
            'record': record,
        })
    # if user is not loged in, send a message to remind user to log in
    else:
        return render(request, "index.html", {
                "message": "Log in to use this feature."
            })

# View for user to do multiplication
def multiplication(request):
    if request.user.username:
        user = request.user.username
        # show all user record
        record = Record.objects.filter(skill="multiplication").order_by('seconds')

        paginator = Paginator(record, 3)
        record = paginator.page(1)
        return render(request, 'multiplication.html', {
            'username': user,
            'record': record,
        })
    # if user is not loged in, send a message to remind user to log in
    else:
        return render(request, "index.html", {
                "message": "Log in to use this feature."
            })

# login view
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            User = get_user_model()
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")