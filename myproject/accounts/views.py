from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid credentials"}
            return render(request,"accounts/login.html", context=context)
        login(request,user)
        return redirect('/')
        
        
        
    
            
            
    return render(request,"accounts/login.html", context=context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/users/login')
    print("logout")
    return render(request, 'accounts/logout.html')
        
