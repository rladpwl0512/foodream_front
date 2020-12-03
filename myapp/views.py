from django.shortcuts import render,get_object_or_404, redirect
from upload.models import Form

# Create your views here.
def home(request):
    forms = Form.objects
    count = Form.objects.count()
    return render(request, 'home.html', {'context' : count, 'forms': forms})

def create(request):
    form = Form()
    form.title = request.GET['title']
    form.body = request.GET['body']
    form.pub_date = timezone.datetime.now()
    form.save()
    return redirect('/form/'+str(form_id))

def delete(request, form_id):
    form_detail =get_object_or_404(Form, pk = form_id)
    form_detail.delete()
    return redirect('home')

def edit(request, form_id):
    if(request.method == 'POST'):
        form_detail = get_object_or_404(Form, pk = form_id)
        return render(request, 'edit.html', {'form':form_detail})

def update(request, form_id):
    form = get_object_or_404(Form, pk = form_id)
    if(request.method == 'POST'):
        form.title = request.POST.get('title')
        form.name = request.POST.get('name')
        form.photo = request.POST.get('photo')
        form.explain = request.POST.get('explain')
        form.deal_method = request.POST.get('deal_method')
        form.deadline = request.POST.get('deadline')
        form.price = request.POST.get('price')
        form.location = request.POST.get('location')
        form.save()
    return redirect('/form/'+str(form_id))

# def detail(request, form_id):
#     form_detail =get_object_or_404(Form, pk = form_id)
#     return render(request, 'detail.html', {'form': form_detail})