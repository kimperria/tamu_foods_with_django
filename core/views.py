from django.shortcuts import render
from .forms import CustomerRegistrationForm

def register_account(request):
    '''
        View function to handle user registration
    '''

    form = CustomerRegistrationForm()

    context = {'form': form}
    return render(request, 'core/register.html', context)

def login_account(request):
    '''
        View function to handle user authentication
    '''
    return render(request, 'core/login.html')
