from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm

from .forms import ContainerForm
from .models import container

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})


@login_required(login_url="login/")
def home(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #         raise Http404('Require Login...')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print ('User request is : %s' % request.user)

        
        # create a form instance and populate it with data from the request:
        form = ContainerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            container_no = form.cleaned_data['container']
            comment = form.cleaned_data['comment']
            obj = container.objects.create(container_no=container_no,description=comment,user=request.user)

            print ('Container is %s' % obj.container_no)
            # redirect to a new URL:

            # messages.error(request, 'Container : %s is upload successful' % obj.container_no)
            messages.success(request, 'Container : %s is upload successful' % obj.container_no)

            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContainerForm()

    return render(request, 'container.html', {'form': form})

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response