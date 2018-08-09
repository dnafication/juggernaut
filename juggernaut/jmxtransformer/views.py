from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404, redirect
from .forms import JmxUploadForm
from .models import Jmx


def index(request):
    jmx_list = get_list_or_404(Jmx.objects.order_by('-date_added'))

    if request.method == 'POST':
        form = JmxUploadForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            # form.save()
            jmx = Jmx(jmxfile=request.FILES['jmxfile'], name=request.POST['name'])
            jmx.save()
            return redirect('index')
        else:
            print(request.POST, request.FILES.keys())
            return redirect('index')
            
    else:
        form = JmxUploadForm()
        return render(request, "jmxtransformer/index.html", {'form': form, 'jmx_list': jmx_list})

def details(request, jmx_id):
    jmx = get_object_or_404(Jmx, pk=jmx_id)
    return render(request, 'jmxtransformer/details.html', {'jmx': jmx})
    