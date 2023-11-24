from django.shortcuts import render, redirect, get_object_or_404
from .models import Cat
from .forms import NameForm, InteractionForm

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            cat_name = form.cleaned_data['name']
            cat = Cat.objects.create(name=cat_name)
            return redirect('cat_info', cat_id=cat.id)
    else:
        form = NameForm()
    return render(request, 'home.html', {'form': form})


def cat_info(request, cat_id):
    cat = get_object_or_404(Cat, pk=cat_id)
    form = InteractionForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        action = form.cleaned_data['action']
        if action == 'feed':
            cat.feed()
        elif action == 'play':
            cat.play()
        elif action == 'sleep':
            cat.sleep()

    return render(request, 'cat_info.html', {'cat': cat, 'form': form})




