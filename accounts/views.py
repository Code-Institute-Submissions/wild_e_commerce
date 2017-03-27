from django.contrib import messages, auth
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.template.context_processors import csrf
from index.views import get_index
from django.contrib.auth.decorators import login_required


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse(get_index))


@login_required(login_url='/accounts/login')
def profile(request):
    return render(request, 'profile.html')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)# create an insistance of the login form
        if form.is_valid(): # check that what was inputted was valid
            user = auth.authenticate(username=request.POST.get('username_or_email'),
                                     password=request.POST.get('password')) # django authenticate the user and password. returns user object

            if user is not None:# user is an actual user. this is their password
                auth.login(request, user)#
                messages.error(request, "You have successfully logged in")# return a message

                if request.GET and 'next' in request.GET:# if there is a get in the request and a next in the string
                    next = request.GET['next']# then do a redirect to next
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('profile'))# if there isnt a next, redirect user to profile
            else:
                form.add_error(None, "Your username or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form, 'next': request.GET['next'] if request.GET and 'next' in request.GET else ''}
    args.update(csrf(request))
    return render(request, 'login.html', args)

# register function
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)
