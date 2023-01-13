from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user
from .forms import UserRegistrationForm, NonCustomerRegistrationForm, LoginForm, UserUpdateForm, CustomerInformationForm, VendorInformationForm, UpdateUserProfilePicForm, MerchantInformationForm
from .models import User, Vendor, Merchant
## Dependant to tamueats
from tamueats.models import Customer, FoodOrder

@unauthenticated_user
def register_customer_account(request):
    '''
        View function to handle customer registration
    '''
    system_message = ''

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

@login_required()
def customer_profile(request):
    '''
    Profile page view function
    '''

    if request.method == 'POST':
        user_information_form = UserUpdateForm(request.POST, request.FILES, instance=request.user.customer)
        current_user = request.user
        print(current_user)
        # customer = current_user.customer
        # print(current_user.customer.phone_number)
        customer_information_form = CustomerInformationForm(request.POST, instance=request.user.customer)
        if user_information_form.is_valid() and customer_information_form.is_valid:
            print(f'Form: {user_information_form}')
            print(f'Form: {customer_information_form}')
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

@login_required()
def customer_dashboard(request):
    loggedIn_user = request.user
    user = Customer.objects.get(user=loggedIn_user)

    customer_order = FoodOrder.objects.filter(customer=user)

    print(f' Here is cutomer order {customer_order}')
    context = {
        'orders': customer_order
    }
    return render (request, 'core/customerDashboard.html', context)

@unauthenticated_user
def register_non_customer_account(request):
    '''
    View function to hanlde non customer accounts registration
    i.e vendor and merchant A/C
    '''
    system_message = ''

    if request.method == 'POST':
        form = NonCustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            if user.is_vendor == True:
                # print(f' Vendor {user.is_vendor} ')
                vendor = Vendor.objects.create(user=user)
                # print(f'Vendor {vendor}')
                return redirect('SignIn')
            elif user.is_merchant == True:
                # print(f' Merchant {user.is_merchant} ')
                merchant = Merchant.objects.create(user=user)
                # print(f'Merchant {merchant}')
                return redirect('SignIn')
        else:
            system_message = 'Form is not Valid'
    else:
        form = NonCustomerRegistrationForm()

    context = {'form': form, 'systemMessage': system_message}
    return render(request, 'core/registerNonCustomer.html', context)

@unauthenticated_user
def login_account(request):
    '''
        View function to handle user authentication
    '''
    system_message = ''
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_vendor is True:
                login(request, user)
                return redirect('vendor-profile')
  
            elif user is not None and user.is_customer is True:
                login(request, user)
                return redirect('customer-profile')

            elif user is not None and user.is_merchant is True:
                login(request, user)
                return redirect('merchant-profile')
            else:
                system_message = 'Invalid form'
        else:
            system_message = 'An error occcured.'

    context = {'form': form, 'systemMessage': system_message}
                
    return render(request, 'core/login.html', context)

@login_required()
def vendor_profile(request):
    '''
    Vendors profile
    '''
    user = request.user
    status = user.vendor.approval_status
    print(user, status)
    if request.method == 'POST':
        user_profile_photo_form = UpdateUserProfilePicForm(request.FILES, instance=request.user)
        vendor_information_form = VendorInformationForm(request.POST, instance=request.user.vendor)
        if user_profile_photo_form.is_valid() and vendor_information_form.is_valid():
            user_profile_photo_form.save()
            vendor_information_form.save()
            if status == 'P':
                print(vendor_information_form)
                return redirect('vendor-profile')
            else:
                return redirect('dashboard')
    else:
        user_profile_photo_form = UpdateUserProfilePicForm(instance=request.user)
        #Throws error on registration
        vendor_information_form = VendorInformationForm(instance=request.user.vendor)
    
    vendor_information_form = VendorInformationForm(instance=request.user.vendor)
    user_profile_photo_form = UpdateUserProfilePicForm()
    context = {
        'user_profile_pic_form': user_profile_photo_form,
        'vendor_form':vendor_information_form,
        'status': status
    }
    return render(request, 'core/vendorProfile.html', context)

@login_required()
def merchant_profile(request):
    '''
     Merchant view func
    '''
    merchant = request.user
    status = merchant.merchant.approval_status
    print(merchant, status)

    if request.method == 'POST':
        user_profile_photo_form = UpdateUserProfilePicForm(request.FILES, instance=merchant)
        merchant_information_form = MerchantInformationForm(request.POST, instance=merchant.merchant)
        if user_profile_photo_form.is_valid() and merchant_information_form.is_valid:
            user_profile_photo_form.save()
            merchant_information_form.save()
            print(merchant_information_form)
            if status == 'P':
                return redirect('merchant-profile')
            else:
                return redirect('dashboard')
    else:
        user_profile_photo_form = UpdateUserProfilePicForm(instance=merchant)
        merchant_information_form = MerchantInformationForm(instance=merchant.merchant)


    context = {
        'user_profile_pic_form': user_profile_photo_form,
        'merchant_form':merchant_information_form,
        'status': status
    }
    return render(request, 'core/merchantProfile.html', context)

@login_required()
def dashboard(request):
    '''
    Dashboard view function
    '''
    user = request.user
    print(user)
    if user.is_vendor is True:
        vendor = user
        print(vendor)
    elif user.is_merchant is True:
        merchant = user

    context = {
        'user': user,
    }
    return render(request, 'core/dashboard.html', context)