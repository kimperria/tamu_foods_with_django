from django.shortcuts import render

def register_account(request):
    '''
        View function to handle user registration
    '''
    return render(request, 'core/register.html')

def login_account(request):
    '''
        View function to handle user authentication
    '''
    return render(request, 'core/login.html')
