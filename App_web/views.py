from django.shortcuts import render
from .views import *
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView 
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment
from .forms import CommentForm
from App_user.models import User

class HomeView(TemplateView):
    template_name = 'start.html'
    
class Aboutus(TemplateView):
    template_name = 'aboutus.html'

def KitsView(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    comments = product.comments.all()
    if request.method == 'POST':
        print(request.POST)
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.product = product
                comment.user = request.user  # Referencia al usuario logueado desde tu modelo personalizado
                comment.save()
                return redirect('kits', product_id=product.id)
        else:
            return redirect('login')
    else:
        form = CommentForm()
    
        context = {
        'product': product,
        'comments': comments,
        'form': form,
    }
    return render(request, 'kits.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


def kits(request):
    product_name = request.GET.get('name')  # Captura el valor del parámetro 'name'
    
    # Lógica para manejar el producto con el nombre 'product_name'
    
    return render(request, 'kits.html', {'product_name': product_name})