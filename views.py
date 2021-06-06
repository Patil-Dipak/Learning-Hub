from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
 
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
  
#IMPORT for models
from .models import Contact,Signup,Notes

# Create your views here.

def index(request):
      return render(request,'index.html')
     
def about(request):
    return render(request,'about.html')


def servises(request):
    return render(request,'servises.html')

def contact(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        comment=request.POST.get('comment')
        contact=Contact(fname=fname,lname=lname,email=email,comment=comment,date=datetime.today())
        contact.save()
    return render(request,'contact.html')

def bca(request):
    return render(request,'bca.html')

def imca(request):
    return render(request,'imca.html')

def mca(request):
    return render(request,'mca.html')

def userlogin(request):
    error= ""
    if request.method=="POST":
        u=request.POST.get('emailid')
        user_pass=request.POST.get('pwd')
        user= authenticate(username=u, password=user_pass)
        try:
            if user is not None:
                login(request, user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error': error}  
    return render(request,'login.html',d)

   

def signup(request):
    error=""
    if request.method == "POST":
        fn=request.POST.get('fname')
        ln=request.POST.get('lname')
        co=request.POST.get('cont')
        em=request.POST.get('email')
        pa=request.POST.get('pass')
        br=request.POST.get('branch') 
        ro=request.POST.get('role')

        try:
            user=User.objects.create_user(username=em, password=pa, first_name=fn, last_name=ln)
            user.save()
            data=Signup(user=user,contact=co, branch=br, role=ro)
            data.save()
            error="no"
        except:
            error="yes"
    d={'error': error}
    return render(request,'signup.html',d)  

#user home after user login
def user_home(request):
    if request.user is None:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    data=Signup.objects.get(user=user)
    d= {'data':data, 'user':user}
    #d= {'user':user }
    return render(request,'user_home.html',d)

#user Profile
def user_profile(request):
    if request.user is None:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    data=Signup.objects.get(user=user)
    d= {'data':data, 'user':user}
    return render(request,'user_profile.html',d)

#view notes for user
def view_notes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        br=request.POST.get('branch') 
        yr=request.POST.get('year')    
    #user=User.objects.get(id=request.user.id)
    data=Notes.objects.filter(branch=br, clg_yr=yr)
    return render(request,'view_notes.html',{'data':data})


#view all notes for admin
def view_all_notes(request):
    if not request.user.is_staff:
        return redirect('adlogin')
    data=Notes.objects.all()
    return render(request,'view_all_notes.html',{'data':data})


#delete notes for admin
def delete_notes(request,pid):
    if not request.user.is_staff:
        return redirect('adlogin')
    notes=Notes.objects.get(id=pid)
    notes.delete()
    return redirect('view_all_notes')

#view user for admin
def view_user(request):
    if not request.user.is_staff:
        return redirect('adlogin')
    data=Signup.objects.all()
    return render(request,'view_user.html',{'data':data})


#delete user for admin
def delete_user(request,pid):
    if not request.user.is_staff:
        return redirect('adlogin')
    val=User.objects.get(id=pid)
    val.delete()
    return redirect('view_user')


#admin Login
def adlogin(request):
    error= ""
    if request.method=="POST":
        u=request.POST.get('emailid')
        p=request.POST.get('pwd')
        user= authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error': error}  
    return render(request,'adlogin.html',d)

#for the admin home page after login
def admin_profile(request):
    if not request.user.is_staff:
        return redirect('adlogin.html')
    return render(request,'admin_profile.html')

#LogOut
def Logout(request):
    logout(request)
    return render(request,'index.html')

#user change password
def changepass(request):
    error=""
    if request.user is None:
        return redirect('login')
        
    if request.method=="POST":
        #oldpass=request.POST['old']
        newpass =request.POST['new']
        conpass =request.POST['confirm']
        #if user_pass==oldpass:
        if newpass == conpass:
            query= User.objects.get(username__exact=request.user.username)
            query.set_password(newpass)
            query.save()
            error="no"
        else:
            error="yes"
       # else:
           # error="yes"        
    d= {'error':error}
    return render(request,'changepass.html',d)

#edit_user Profile
def edit_user_profile(request):
    if request.user is None:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    data=Signup.objects.get(user=user)
    error= False
    if request.method == "POST":
        user.first_name=request.POST.get('Fname')
        user.last_name=request.POST.get('Lname')
        data.contact=request.POST.get('Contact')
        data.branch=request.POST.get('branch') 
        data.role=request.POST.get('role')
        user.save()
        data.save()
        error=True
    d= {'data':data, 'user':user, 'error':error}
    return render(request,'edit_user_profile.html',d)

# Upload notes
def upload_notes(request):
    if not request.user.is_staff:
        return redirect('adlogin.html')
    error=""
    if request.method == "POST":
        #uname=request.user.objects.filter(username=request.user.username).first()
        bnch=request.POST.get('branch') 
        sub=request.POST.get('subject')
        notefile=request.FILES.get('note_file')
        yr=request.POST.get('Year')
       
        try:
            if bnch=="" or sub=="" or notefile==None or yr=="":
                error="yes"
            else:    
                val=Notes(uploadingdate=datetime.today(), branch=bnch, subject=sub, notesfilr=notefile, clg_yr=yr)
                val.save()
                error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_notes.html',d)
   