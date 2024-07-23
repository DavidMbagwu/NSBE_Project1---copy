from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, connection
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from .models import Member
from .forms import MemberSignUpForm


def signup(request):
    if request.method == "POST":
        form = MemberSignUpForm(request.POST)

        if form.is_valid():
            member = Member.objects.create(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                mcneese_id=form.cleaned_data["mcneese_id"],
                username=form.cleaned_data["mcneese_id"],  # Set mcneese_id as username
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


def login_view(request):
    if request.method == "POST":
        mcneese_id = request.POST.get("mcneese_id")
        password = request.POST.get("password")

        # I made sure username is the same as mcneese_id!!!
        member = authenticate(request, username=mcneese_id, password=password)

        if member is not None:
            print(member)
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

def change_password(request):
    pass

def profile(request):
    pass


def index(request):
    return render(request, "stage/index.html")


def about(request):
    return render(request, "stage/about.html")


def directory(request):
    return render(request, "stage/directory.html")


def events(request):
    return render(request, "stage/events.html")


def help(request):
    return render(request, "stage/help.html")


def points(request):
    return render(request, "stage/points.html")
