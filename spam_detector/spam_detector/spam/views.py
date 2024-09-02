from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from . forms import NewUserCreationForm, NewUserAuthenticationForm, SpamNumberSearchForm
from . models import UserSpamNumber

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'spam.backends.EmailBackend'
            login(request, user)
            return redirect('submit_spam_number')
    else:
        form = NewUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = NewUserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('submit_spam_number')
    else:
        form = NewUserAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('logged_out1')

def logged_out(request):
    return render(request, 'registration/logged_out1.html')

@login_required
def submit_spam_number(request):
    if request.method == 'POST':
        spam_number = request.POST.get('spam_number')
        description = request.POST.get('description', '')
        UserSpamNumber.objects.create(
            user=request.user,
            spam_number=spam_number,
            description=description
        )
        return redirect('spam_success')
    return render(request, 'spam/submit_spam_number.html')

def spam_success(request):
    return render(request, 'spam/spam_success.html')

def search_spam_numbers(request):
    form = SpamNumberSearchForm(request.GET or None)
    results = None

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            results = UserSpamNumber.objects.filter(spam_number__icontains=query)
    return render(request, 'spam/search_spam_numbers.html', {'form':form, 'results': results})
