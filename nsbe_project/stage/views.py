from django.shortcuts import render, reverse, redirect
from .models import Event, Member, Post
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, connection
from django.http import HttpResponseRedirect
from .forms import MemberSignUpForm

from rest_framework import generics, status
from .serializers import EventSerializer, MemberSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Case, When, Value, BooleanField

# Create your views here.
def index(request):
    all_users = Member.objects.all()
    return render(request, 'stage/index.html', {'all': all_users})


def about(request):
    return render(request, 'stage/about.html')

def directory(request):
    return render(request, 'stage/directory.html')

def events(request):
    return render(request, 'stage/events.html')

def help(request):
    return render(request, 'stage/help.html')

def points(request):
    context = {
        'posts': Post.objects.all(),
        'members': Member.objects.all(),
    }
    return render(request, 'stage/points.html', context)

def profile(request):
    all_users = Member.objects.all()
    return render(request, 'stage/profile.html', {'all': all_users})

def login_view(request):
    if request.method == "POST":
        mcneese_email = request.POST.get("mcneese_email")
        password = request.POST.get("password")
        print(mcneese_email, password)

        # I made sure username is the same as mcneese_email!!!
        member = authenticate(request, username=mcneese_email, password=password)

        if member is not None:
            login(request, user=member)
            return HttpResponseRedirect(reverse("stage-index"))

        else:
            print("Member not found")
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


class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get(self.lookup_field)
        try:
            event = Event.objects.get(slug=slug)
            serializer = self.get_serializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)



class EventsListView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        event_type = self.kwargs.get("event_type")
        if event_type == "upcoming":
            queryset = Event.objects.upcoming()
        elif event_type == "past":
            queryset = Event.objects.past()
        else:
            queryset = Event.objects.none()
        
        return queryset
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "No events found"}, status=status.HTTP_404_NOT_FOUND)


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
def register_for_event(request, id):
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return Response({"message": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    member = request.user

    if member in event.attendees.all():
        return Response({"message": "Member already registered for this event"}, status=status.HTTP_400_BAD_REQUEST)
    
    event.attendees.add(member)
    return Response(EventSerializer(event).data, status=status.HTTP_200_OK)


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
def unregister_from_event(request, id):
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return Response({"message": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    member = request.user

    if member not in event.attendees.all():
        return Response({"message": "Member not registered for this event"}, status=status.HTTP_400_BAD_REQUEST)
    
    event.attendees.remove(member)
    return Response(EventSerializer(event).data, status=status.HTTP_200_OK)