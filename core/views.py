from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, NonCustomerRegistrationForm, LoginForm
from .models import User, Vendor, Merchant
## Dependant to tamueats
from tamueats.models import Customer

def register_customer_account(request):
    '''
        View function to handle customer registration
    '''
    system_message = None

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.is_customer == True:
                username = form.cleaned_data.get('username')
                customer = Customer.objects.create(username=username,user=user)
                print(customer)
            else:
                print('Not a customer')
            # return redirect('SignIn')
        else:
            system_message = 'Form is not Valid'
    else:
        form = UserRegistrationForm()


    context = {'form': form, 'systemMessage': system_message}
    return render(request, 'core/registerCustomer.html', context)

def register_non_customer_account(request):
    '''
    View function to hanlde non customer accounts registration
    i.e vendor and merchant A/C
    '''
    system_message = None

    if request.method == 'POST':
        form = NonCustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            if user.is_vendor == True:
                print(f' Vendor {user.is_vendor} ')
                vendor = Vendor.objects.create(user=user)
                print(f'Vendor {vendor}')
            elif user.is_merchant == True:
                print(f' Merchant {user.is_merchant} ')
                merchant = Merchant.objects.create(user=user)
                print(f'Merchant {merchant}')
            return redirect('SignIn')
        else:
            system_message = 'Form is not Valid'
    else:
        form = NonCustomerRegistrationForm()

    context = {'form': form, 'systemMessage': system_message}
    return render(request, 'core/registerNonCustomer.html', context)

def login_account(request):
    '''
        View function to handle user authentication
    '''
    system_message = None 
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None and user.is_customer:
                login(request, user)
                return redirect('customer-profile')
            elif user is not None and user.is_vendor:
                login(request, user)
                return redirect('dashboard')
            elif user is not None and user.is_merchant:
                login(request, user)
                return redirect('dashboard')
            else:
                system_message = 'Invalid form'

    context = {'form': form, 'systemMessage': system_message}
                
    return render(request, 'core/login.html', context)

def customer_profile(request):
    '''
    Profile page view function
    '''


    # context = 'Customer profile'
    return render(request, 'core/customerProfile.html')

def dashboard(request):
    '''
    Non customers dashboard
    '''

    return render(request, 'core/dashboard.html')