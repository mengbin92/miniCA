from django.shortcuts import render
from django.http import HttpResponse
from .forms import CSRForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    return HttpResponse('<h1>Welcome</h1>')

@csrf_exempt
def CSR(request):
    if request.method == 'POST':
        csr = CSRForm(request.POST)
        return HttpResponse('thank')
    else:
        csr = CSRForm()
        return render(request,'CA/ca.html',{'form':csr})