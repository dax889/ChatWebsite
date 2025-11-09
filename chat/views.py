from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import Http404
from django.contrib import messages
from .models import Message
from .forms import MessageForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser

User = get_user_model() # This is the fix

def home(request):
    users = CustomUser.objects.exclude(id=request.user.id)
    if users.exists():
        return redirect('chat_view', receiver_id=users.first().id)
    else:
        return redirect('dashboard_view')

# def room(request, room_name, username):
#     try:
#         user = User.objects.get(username=username)
#     except User.DoesNotExist:
#         raise Http404("User not found!")

#     return render(request, 'chat.html', {
#         'room_name': room_name,
#         'other_user': user,
#     })

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Signed up successfully!")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required
def dashboard_view(request):
    users = CustomUser.objects.exclude(id=request.user.id)
    return render(request, 'dashboard.html', {'users': users})


@login_required
def chat_view(request, receiver_id):
    receiver = User.objects.get(id=receiver_id)

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = receiver
            message.save()
            return redirect('chat_view', receiver_id=receiver.id)
    else:
        form = MessageForm()

    messages = Message.objects.filter(
        sender=request.user, receiver=receiver
    ) | Message.objects.filter(
        sender=receiver, receiver=request.user
    ).order_by('timestamp')

    return render(request, 'chat.html', {
        'form': form,
        'messages': messages,
        'receiver': receiver,

    })

