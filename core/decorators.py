from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    '''
    If user isnt logged in
    '''
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            # return redirect('dashboard')
            instance = request.user
            print(instance)
            if instance.is_customer:
                return redirect('customer-profile')
            if instance.is_vendor :
                print('Huyu ni vendor')
                return redirect('dashboard')
            if instance.is_merchant:
                print('Huyu ni merchant ')
                return redirect('dashboard')
            else:
                return redirect('HomePage')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func