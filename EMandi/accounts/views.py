from django.shortcuts import render,redirect, HttpResponse
from .forms import add_registration_form,RegistrationForm, ChangeProfileForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken, ProfileSerializer
from rest_framework.permissions import IsAdminUser, AllowAny

def index(request):
    return render(request,'accounts/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def register(request):
    registered = False
    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)
        profile_form = add_registration_form(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'image' in request.FILES:
                print('found it')
                profile.image = request.FILES['image']
            profile.save()
            registered = True
            # return redirect("/")
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = RegistrationForm()
        profile_form = add_registration_form()
    return render(request,'accounts/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

@login_required
def view_profile(request,pk=None):
    if pk:
        user=User.objects.get(pk=pk)
    else:
        user=request.user
    args={'user':user}
    return render(request,'accounts/profile.html',args)

@login_required
def edit_profile(request):        #edit profile view
    if request.method=='POST':
        form=EditProfileForm(request.POST, instance=request.user)
        form1 = ChangeProfileForm(request.POST, instance=request.user)
        if form.is_valid() and form1.is_valid():
            form.save()
            UserProfile.objects.filter(user=request.user).update(city=request.POST['city'])
            UserProfile.objects.filter(user=request.user).update(phone=request.POST['phone'])
            # UserProfile.objects.filter(user=request.user).update(image=request.POST['image'])

            return redirect('/accounts/profile')
        else:
            return HttpResponse("form  is invalid")

    else:
        form=EditProfileForm(instance=request.user)
        form1=ChangeProfileForm(request.POST,instance=request.user)
        args={'form':form, 'form1':form1}
        return render(request,'accounts/edit_profile.html', args)


@login_required
def change_password(request):        #change password view
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change-password')

    else:
        form=PasswordChangeForm(user=request.user)

        args={'form':form}
        return render(request,'accounts/change_password.html',args)

#====================API PART========================================================================

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    print('&&')
    serializer = UserSerializer(request.user)
    print(request.user)
    user_instance = User.objects.get(username=request.user)
    print(getattr(user_instance,'email'))
    return Response(serializer.data)

class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Signup(generics.ListCreateAPIView):
    serializer_class = UserSerializerWithToken
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return User.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializerWithToken(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print('hello')
        return super().create(request, *args, **kwargs)

        

class profile(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    
    
