from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Event, Member, Post
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, connection
from django.http import HttpResponseRedirect, JsonResponse
from .forms import MemberSignUpForm

from .serializers import EventSerializer
from rest_framework.decorators import api_view
from django.core.mail import send_mail 

# Create your views here.
def index(request):
    return render(request, 'stage/index.html')


def about(request):
    return render(request, 'stage/about.html')

def directory(request):
    return render(request, 'stage/directory.html')

def events(request):
    return render(request, 'stage/events.html')

def help(request):
    return render(request, 'stage/help.html')

def points(request):
    user = request.user
    # Filter posts related to the current user

    member = Member.objects.get(id = user.id)
    member_posts = member.points.all()
    events_attended = member.points.count()
    top_members = Member.objects.all().order_by('-pointsum')[:10]

    context = {
        'posts': Post.objects.all(),
        'members': Member.objects.all(),
        'memberPosts': member_posts,
        'events_attended': events_attended ,
        'top_members': top_members
        }
    return render(request, 'stage/points.html', context)

# 'points': Member.objects.values_list('points', flat=True).order_by('-points')[:5]  # Fetch top 5 users by points in descending order.


def profile(request):
    all_users = Member.objects.all()
    return render(request, 'stage/profile.html', {'all': all_users})


def login_view(request):
    if request.method == "POST":
<<<<<<< HEAD
        mcneese_email = request.POST.get("mcneese_email")
        password = request.POST.get("password")

        # I made sure username is the same as mcneese_email!!!
        member = authenticate(request, username=mcneese_email, password=password)
=======
        email = request.POST["email"]
        password = request.POST["password"]

        # I made sure username is the same as mcneese_id!!!
        member = authenticate(request, username=email, password=password)
>>>>>>> c1dd7608a194f3419fa0f0c931070579be17d7c2

        if member is not None:
            login(request, member)
            return HttpResponseRedirect(reverse("stage-index"))

        else:
           
            return render(
                request,
                "stage/login.html",
                {"message": "Invalid McNeese ID and/or password."},
            )

    else:
        return render(request, "stage/login.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("stage-login"))

def signup(request):
    if request.method == "POST":
        form = MemberSignUpForm(request.POST)

        if form.is_valid():
            member = Member.objects.create(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                mcneese_id=form.cleaned_data["mcneese_id"],
                username=form.cleaned_data["email"],  # Set Mcneese email as username
                email=form.cleaned_data["email"],
                linkedin=form.cleaned_data["linkedin"],
                major=form.cleaned_data["major"],
                class_standing=form.cleaned_data["class_standing"],
                nationality=form.cleaned_data["nationality"],
                race=form.cleaned_data["race"],
                gender=form.cleaned_data["gender"],
                password=form.cleaned_data["password1"],
            )

            member.set_password(
                form.cleaned_data["password2"]
            )  # This hashes the password
            member.save()

            # Login the user
            login(request, member)
            return HttpResponseRedirect(reverse("stage-index"))

        else:
            error_messages = []
            erroneous_fields = form.errors.get_json_data()
            for field, errors in erroneous_fields.items():
                for error in errors:
                    error_messages.append(error["message"])

            return render(
                request,
                "stage/signup.html",
                {"form": form, "error_messages": error_messages},
            )

    else:
        return render(request, "stage/signup.html", {"form": MemberSignUpForm()})


def gallery(request):
    return render(request, 'stage/gallery.html')

def adminOnly(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'stage/adminOnly.html', context)

@api_view(['GET'])
def get_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        serializer = EventSerializer(event, context={'request': request})
        return JsonResponse(serializer.data)
    except Event.DoesNotExist:
        return JsonResponse({'error': 'Event not found'}, status=404)

@api_view(['GET'])
def get_events(request, event_type):
    if event_type == "past":
        events = Event.objects.past()
    else:
        events = Event.objects.upcoming()

    serializer = EventSerializer(events, many=True, context={'request': request})
    return JsonResponse({'events': serializer.data})

@api_view(['POST'])
@login_required
def register(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.attendees.add(request.user)

    # Send confirmation email to the user
    subject = f"Registration to attend {event} confirmation!"
    message = f"This is an email to confirm that you registered to attend {event.title} " \
              f"taking place on {event.start_time} - {event.end_time} at {event.location}. " \
              "We can't wait to see you."
    from_email = "paccysan@gmail.com"
    recipient_list = [request.user.email]
    send_mail(subject, message, from_email, recipient_list)
    
    return JsonResponse({'success': True})

@api_view(['POST'])
@login_required
def unregister(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.attendees.remove(request.user)
    return JsonResponse({'success': True})
