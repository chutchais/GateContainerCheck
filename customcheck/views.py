from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm

from .forms import ContainerForm,RejectForm
from .models import container,reject
from django.core.urlresolvers import reverse

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


# @login_required(login_url="login/")
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

            return HttpResponseRedirect(reverse('home'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContainerForm()

    return render(request, 'container.html', {'form': form,'form_type':'add'})

def CotainerReject(request):
    print ('CotainerReject')
    # if not request.user.is_staff or not request.user.is_superuser:
    #         raise Http404('Require Login...')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print ('User request is : %s' % request.user)

        
        # create a form instance and populate it with data from the request:
        form = RejectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            container_no = form.cleaned_data['container']
            comment = form.cleaned_data['comment']
            no_shore = form.cleaned_data['no_shore']
            no_paid = form.cleaned_data['no_paid']
            no_customs = form.cleaned_data['no_customs']
            no_vgm = form.cleaned_data['no_vgm']
            late_gate = form.cleaned_data['late_gate']
            other = form.cleaned_data['other']

            obj = reject.objects.create(container_no=container_no,
                    description=comment,
                    no_shore=no_shore,no_paid=no_paid,no_customs=no_customs,
                    no_vgm=no_vgm,late_gate=late_gate,other=other,
                    user=request.user)

            print ('Rejected Container is %s' % obj.container_no)
            # redirect to a new URL:

            # messages.error(request, 'Container : %s is upload successful' % obj.container_no)
            messages.success(request, 'Rejected Container : %s is upload successful' % obj.container_no)

            return HttpResponseRedirect(reverse('reject'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RejectForm()

    return render(request, 'container.html', {'form': form,'form_type':'reject'})

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response