from django.contrib import messages, auth
from accounts.forms import UserLoginForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.template.context_processors import csrf

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


