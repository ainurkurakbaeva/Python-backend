from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect

from .decorators import unathenticated_user,allowed_users,admin_only
from .models import Seeds
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.core.mail import send_mail
from django.contrib.auth.models import Group


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {
                'name':name,
                'email':email,
                'message': message
        }
        message = '''
        New message : {}

        From:{}
        '''.format(data['message'],data['email'])
        send_mail(data['name'], message,'',['mamirovbegzad5@gmail.com'])
    return render(request,'./index.html',{})


def elements(request):
    return render(request,'./elements.html')

def prost(request):
    object_list = Seeds.objects.all()
    return render(request,'./prost.html' , {'object_list' : object_list})

def generic(request):
    poster = Post.objects.all()
    return render(request,'./generic.html' , {'poster' : poster})

def landing(request):
    object_list = Seeds.objects.all()
    genre  = Genre.objects.all()

    context = {
        'object_list': object_list,
        'genre': genre,
        'genre_selected':0,
    }
    return render(request,'./landing.html' , context=context)

@unathenticated_user
def signup(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name = 'customer')
            user.groups.add(group)

            messages.success(request,'Account was created for  '  + username)

            return redirect('signin')
    context = {'form' : form}
    return render(request,'./sign-up.html',context)


@unathenticated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Username or password is incorrect')
    context = {}
    return render(request,'./sign-in.html',context)



def logoutUser(request):
    logout(request)
    return redirect('index')

def sendletter(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    element = Sendletter(name = name,email = email,message = message)
    element.save()
    return render(request,'./sendletter.html', {'name' : name,
                                          'email': email,
                                          'message' : message})

def show_category(request,genre_id):
    object_list = Seeds.objects.filter(genre_id=genre_id)
    genre  = Genre.objects.all()

    context = {
        'object_list': object_list,
        'genre': genre,
        'genre_selected':genre_id,
    }
    return render(request,'./prost.html' , context=context)

@allowed_users(allowed_roles=['admin'])
def adminPage(request):
    return render(request, './user-page.html')

def show_post(request,post_id):
    post = get_object_or_404(Seeds,pk = post_id)

    context = {
        'post': post,
        'name': post.specifications,
        'genre_selected':post.genre_id,
    }
    return render(request,'./post.html' , context=context)

class Edit(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        ]
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='Full name',required=False)
    username = forms.CharField(label='Username', max_length=100, required=False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('Email is required.')
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name:
            raise forms.ValidationError('Full name is required.')
        return first_name



    def clean_username(self):
        username = self.cleaned_data['username']
        if not username:
            raise forms.ValidationError('Username is required.')
        return username

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if len(password1) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError('Password must contain at least one digit.')
        if not any(char.islower() for char in password1):
            raise forms.ValidationError('Password must contain at least one lowercase letter.')
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError('Password must contain at least one uppercase letter.')
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if not password1 or not password2:
            raise forms.ValidationError('Both password fields are required.')
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match.')

        return cleaned_data

    def edit(request, pk):
        context = {}
        obj = get_object_or_404(User, pk=pk)
        form = Edit(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
        context["form"] = form

        return render(request, "edit.html", context)

def profile(request):
    return render(request, './profile.html')

def edit(request):
    return render(request, './edit.html')