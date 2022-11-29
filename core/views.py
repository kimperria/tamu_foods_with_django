from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, NonCustomerRegistrationForm, LoginForm, UserUpdateForm, CustomerInformationForm, VendorInformationForm, UpdateUserProfilePicForm
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
            print(f'User {user}')
            if user.is_customer == True:
                username = form.cleaned_data.get('username')
                customer = Customer.objects.create(user=user)
                print(customer)
            return redirect('SignIn')
        else:
            system_message = 'Form is not Valid'
    else:
        form = UserRegistrationForm()


    context = {'form': form, 'systemMessage': system_message}
    return render(request, 'core/registerCustomer.html', context)

def customer_profile(request):
    '''
    Profile page view function
    '''

    if request.method == 'POST':
        user_information_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        current_user = request.user
        print(current_user)
        # customer = current_user.customer
        # print(current_user.customer.phone_number)
        customer_information_form = CustomerInformationForm(request.POST, instance=request.user.customer)
        if user_information_form.is_valid() and customer_information_form.is_valid:
            user_information_form.save()
            customer_information_form.save()
            ## Messages
            return redirect('customer-profile')
    else:
        user_information_form = UserUpdateForm(instance=request.user)
        customer_information_form = CustomerInformationForm(instance=request.user.customer)
    context = {
        "user_form": user_information_form,
        "customer_form": customer_information_form
        }
    return render(request, 'core/customerProfile.html', context)

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
                return redirect('dashboard')
            elif user.is_merchant == True:
                print(f' Merchant {user.is_merchant} ')
                merchant = Merchant.objects.create(user=user)
                print(f'Merchant {merchant}')
                return redirect('dashboard')
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
            print(f'Account {user}')
            print(user.is_vendor)
            print(f'Merchant: {user.is_merchant}')

            if user is not None and user.is_vendor is True:
                print(user.is_vendor)
                # new_user = User.objects.filter(username=username).first()
                # print(new_user)
                print('Ran as vendor')
                login(request, user)
                return redirect('dashboard')
  
            elif user is not None and user.is_customer is True:
                print('Ran as customer')
                login(request, user)
                return redirect('customer-profile')

            elif user is not None and user.is_merchant is True:
                print('Ran as merchant')
                login(request, user)
                return redirect('dashboard')
            else:
                system_message = 'Invalid form'
        else:
            system_message = 'An error occcured.'

    context = {'form': form, 'systemMessage': system_message}
                
    return render(request, 'core/login.html', context)


def dashboard(request):
    '''
    Non customers dashboard
    '''
    if request.method == 'POST':
        user_profile_photo_form = UpdateUserProfilePicForm(request.FILES, instance=request.user)
        vendor_information_form = VendorInformationForm(request.POST, instance=request.user.vendor)
        if user_profile_photo_form.is_valid() and vendor_information_form.is_valid():
            user_profile_photo_form.save()
            vendor_information_form.save()
            return redirect('dashboard')
    else:
        user_profile_photo_form = UpdateUserProfilePicForm(instance=request.user)
        vendor_information_form = VendorInformationForm(instance=request.user.vendor)

    context = {
        'user_profile_pic_form': user_profile_photo_form,
        'vendor_form':vendor_information_form
    }
    return render(request, 'core/dashboard.html', context)