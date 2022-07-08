from django.shortcuts import render, redirect

from user.forms import RegisterUserForm


def signup(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:get_all_posts')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/sign_up.html', {'form': form})




