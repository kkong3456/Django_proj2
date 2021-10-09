from django.shortcuts import render,redirect
from django.views.generic.edit import FormView 
from django.contrib.auth.hashers import make_password 
from .forms import RegisterForm,LoginForm
from .models import Dsuser

# Create your views here.

def index(request):
    return render(request,'index.html',{'user_id':request.session.get('user')})

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    return redirect('/')

class RegisterView(FormView):
    template_name='register.html'
    form_class=RegisterForm
    success_url='/'

    def form_valid(self,form):
        # print('xxxxxxxxxxxxxxxxxxxxxxxxxx')
        dsuser=Dsuser(
            user_id=form.data.get('user_id'),
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
        )
        dsuser.save()
        return super().form_valid(form) 

class LoginView(FormView):
    template_name='login.html'
    form_class=LoginForm 
    success_url='/'

    def form_valid(self,form):
        self.request.session['user']=form.data.get('user_id')
        return super().form_valid(form)


