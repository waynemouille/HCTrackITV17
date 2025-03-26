from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
from .models import *
from .forms import AddTicketForm, UpdateTicketForm, CompleteTicketForm







# LOGIN
#------------------------------------------------------------------------------------------------------------------------#
def loginMain(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tickets_createnew')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'login.html', context)
#------------------------------------------------------------------------------------------------------------------------#


# LOGOUT
#------------------------------------------------------------------------------------------------------------------------#
def logoutUser(request):
    logout(request)
    return redirect('login')
#------------------------------------------------------------------------------------------------------------------------#


# DASHBOARD
#------------------------------------------------------------------------------------------------------------------------#
#def ticketsDashboard(request):
    #open_ticket_count = Ticket.objects.filter(Q(status='NEW')
                             #| Q(status='ASSIGNED / PENDING')
                             #| Q(status='SCHEDULED')
                             #| Q(status='IN PROGRESS')
                             #| Q(status='ON HOLD - Waitin on Parts')
                             #| Q(status='ON HOLD - Waiting on Parts')
                             #| Q(status='ON HOLD - User Unavailable')
                             #| Q(status='ON HOLD - Research')
                             #| Q(status='ON HOLD - Misc')
                             #).count()
    #onhold_ticket_count = Ticket.objects.filter(Q(status='ON HOLD - Waitin on Parts')
                             #| Q(status='ON HOLD - User Unavailable')
                             #| Q(status='ON HOLD - Research')
                             #| Q(status='ON HOLD - Misc')
                             #).count()
    
    #completed_ticket_count = Ticket.objects.filter(Q(status='COMPLETED')
                             #| Q(status='CANCELLED')
                             #).count()

    #if request.method == 'POST':
        #username = request.POST['username']
        #password = request.POST['password']
        #user = authenticate(request, username=username, password=password)
        #if user is not None:
            #login(request, user)
            #return redirect('tickets_dashboard')
        #else:
            #messages.warning(request, "There was a problem logging in.  Please try again.")
            #return redirect('login')
    #else:
        #return render (request, 'tickets_dashboard.html', {'open_ticket_count':open_ticket_count, 'onhold_ticket_count':onhold_ticket_count, 'completed_ticket_count':completed_ticket_count})
#------------------------------------------------------------------------------------------------------------------------#


# CREATE NEW REQUEST
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def ticketsCreatenew(request):
    form = AddTicketForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                instance = form.save(commit=False)
                instance.created_by = request.user
                instance.save()
                return redirect('tickets_home')
        return render (request, 'tickets_createnew.html', {'form':form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('login')
#------------------------------------------------------------------------------------------------------------------------#


# ALL SERVICE REQUESTS PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def ticketsHome(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    tickets = tickets.filter(Q(status='NEW')
                             | Q(status='ASSIGNED / PENDING')
                             | Q(status='SCHEDULED')
                             | Q(status='IN PROGRESS')
                             | Q(status='ON HOLD - Waitin on Parts')
                             | Q(status='ON HOLD - Waiting on Parts')
                             | Q(status='ON HOLD - User Unavailable')
                             | Q(status='ON HOLD - Research')
                             | Q(status='ON HOLD - Misc')
                             )
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tickets_home')
        else:
            messages.warning(request, "There was a problem logging in.  Please try again.")
            return redirect('login')
    else:
        return render (request, 'tickets_home.html', {'tickets':tickets})
#------------------------------------------------------------------------------------------------------------------------#


# CURRENT SERVICE REQUESTS PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def ticketsCurrent(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    tickets = tickets.filter(Q(status='NEW')
                             | Q(status='ASSIGNED / PENDING')
                             | Q(status='SCHEDULED')
                             | Q(status='IN PROGRESS')

                             )
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tickets_home')
        else:
            messages.warning(request, "There was a problem logging in.  Please try again.")
            return redirect('login')
    else:
        return render (request, 'tickets_current.html', {'tickets':tickets})
#------------------------------------------------------------------------------------------------------------------------#


# ON HOLD SERVICE REQUESTS PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def ticketsOnhold(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    tickets = tickets.filter(Q(status='ON HOLD - Waitin on Parts')
                             | Q(status='ON HOLD - Waiting on Parts')
                             | Q(status='ON HOLD - User Unavailable')
                             | Q(status='ON HOLD - Research')
                             | Q(status='ON HOLD - Misc')
                             )
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tickets_home')
        else:
            messages.warning(request, "There was a problem logging in.  Please try again.")
            return redirect('login')
    else:
        return render (request, 'tickets_onhold.html', {'tickets':tickets})
#------------------------------------------------------------------------------------------------------------------------#


# COMPLETED SERVICE REQUESTS PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def ticketsCompleted(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    tickets = tickets.filter(Q(status='COMPLETED')
                             | Q(status='CANCELLED')
                             )
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tickets_home')
        else:
            messages.warning(request, "There was a problem logging in.  Please try again.")
            return redirect('login')
    else:
        return render (request, 'tickets_completed.html', {'tickets':tickets})
#------------------------------------------------------------------------------------------------------------------------#


# SERVICE REQUEST INFORMATION PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def ticketsInfo(request, pk):
    ticket = Ticket.objects.get(id=pk)


    context = {'ticket':ticket}
    return render(request, 'tickets_info.html', context)


def ticketsDelete(request, pk):
    delete_it = Ticket.objects.get(id=pk)
    delete_it.delete()
    context = {}
    return render(request, 'delete.html', context)
#------------------------------------------------------------------------------------------------------------------------#


# UPDATE REQUEST
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def ticketsUpdate(request, pk):
    ticket = Ticket.objects.get(id=pk)
    form = UpdateTicketForm(instance=ticket)
    if request.method == "POST":
        form = UpdateTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('tickets_home')

    context = {'form':form}
    return render(request, 'tickets_update_update.html', context)
#------------------------------------------------------------------------------------------------------------------------#


# COMPLETE REQUEST
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def completeTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    form = CompleteTicketForm(instance=ticket)
    if request.method == "POST":
        form = CompleteTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('tickets_home')

    context = {'form':form}
    return render(request, 'tickets_update_complete.html', context)
#------------------------------------------------------------------------------------------------------------------------#


# COMPLETED TICKET INFORMATION PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def ticketsCompletedinfo(request, pk):
    ticket = Ticket.objects.get(id=pk)


    context = {'ticket':ticket}
    return render(request, 'tickets_info_completed.html', context)
#------------------------------------------------------------------------------------------------------------------------#


# SUBMIT TICKET CONFIRMATION PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def confirmation(request):

    context = {}

    return render(request, 'confirmation.html', context)
#------------------------------------------------------------------------------------------------------------------------#


# CREDENTIALS PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def credentials(request):

    context = {}

    return render(request, 'credentials.html', context)
#------------------------------------------------------------------------------------------------------------------------#


# SUPPORT DIRECTORY PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def supportDirectory(request):

    context = {}

    return render(request, 'support_directory.html', context)
#------------------------------------------------------------------------------------------------------------------------#


# USER DASHBOARD PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def userdashboardPage(request):
    tickets = Ticket.objects.all().order_by('-id')
    tickets = tickets.filter(Q(created_by=request.user))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
            messages.warning(request, "There was a problem logging in.  Please try again.")
            return redirect('login')

    else:
        return render (request, 'user_dashboard.html', {'tickets':tickets})
#------------------------------------------------------------------------------------------------------------------------#