from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import RegUserForm
from django.views import View


class RegUserView(View):
    template_name = 'accounts/register-page.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        context = {}
        form = RegUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'account created')
            return redirect('login-page')
        else:
            context.update({'form': form})
        return render(request, self.template_name, context)


class LoginUserView(View):
    template_name = 'accounts/login-page.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('start-page')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'successful login')
            return redirect('start-page')
        else:
            messages.error(request, 'invalid login details')
        return render(request, self.template_name)


def logout_user(request):
    logout(request)
    messages.success(request, 'successful logout')
    return redirect('login-page')
