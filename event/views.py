from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Event
from django.contrib import messages
from .forms import CreateEventForm
from datetime import datetime



# Create your views here.

# Sets Home page
def home_page(request):
    return render(
        request,
        "event/index.html"
    )


# Sets About page
def AboutPage(request):
    return render(
        request,
        "event/about.html",
    )


# List view for all Event items
class EventList(generic.ListView):
    queryset = Event.objects.all().order_by("event_host_date")
    template_name = "event_list.html"
    paginate_by = 6


# View for individual event pages
def event_detail(request, slug):
    queryset = Event.objects
    event = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "event/event_detail.html",
        {
            "event": event,
        }
    )


# View to handle the Create Event page
def create_event(request):
    event_form = CreateEventForm()

    

    if request.method == "POST":
        print("This is the poas r: ",request.POST)
        event_form = CreateEventForm(request.POST)

        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.organizer = request.user
            try:
                event.save()
                messages.success(request, "You have created an event")
                return redirect("success/")
                
            except ValueError:
                messages.error(request, "Invalid time format. Please use Hour:Minute:Second format. f.e. 10:00:00")

    else:
        event_form = CreateEventForm()

    return render(request, "event/form_create_event.html", {"event_form":event_form})


# The page that the user is redirected to on valid form submission
def create_success(request):
    return render(request, "event/form_create_success.html")