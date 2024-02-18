from django.shortcuts import render
from .forms import SignUpUserForm


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpUserForm()
    return render(request, 'user/sign-up.html', {'form': form})
