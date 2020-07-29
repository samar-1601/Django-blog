from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm # default form made alraedy in django
from django.contrib import messages #flash message is imported here like alerts in Javascript
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    print(' Inside Register function in views.py')
    if request.method == "POST" :
        form = UserRegisterForm(request.POST)
        print('Post request recieved')
        if form.is_valid():
            form.save() #user entered in the form is added to our model
            username = form.cleaned_data.get('username')
            print('Form is valid')
            #if the form is valid then, the form details are stored in the dictionary called cleaned_data and her in this case what we are actually doing id getting the username from the dictionary if the details entered in the form are valid
            messages.success(request, f'Account created for {username}, Please login')
            return redirect('login') # after all the above code, the register page will be redirected to the blog-home page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required #it is an inbuilt decorator which adds the required functionality to the function and in our case it is used for preventing the user to go to '/profile ' page without any login
def profile(request):
    return render(request, 'users/profile.html')