from django.shortcuts import render, redirect
from .models import Password
from cryptography.fernet import Fernet
from django.conf import settings
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home_view(request):
    return render(request, 'home.html')  # Create a home.html template in your templates folder


@csrf_protect
def password_list(request):
    passwords = Password.objects.filter(user=request.user)

    for password in passwords:
        key = settings.ENCRYPTION_KEY.encode()
        cipher_suite = Fernet(key)
        password.display_password = "*****"  # Display the password as a series of stars
        
        try:
            decrypted_password = cipher_suite.decrypt(password.encrypted_password).decode()
            password.decrypted_password = decrypted_password
        except Exception as e:
             print(f"Error decrypting password: {e}")
             password.decrypted_password = "Decryption failed"

    return render(request, 'password_list.html', {'passwords': passwords})

@csrf_protect
def pass_view(request):
    if request.method == 'POST':
        website = request.POST.get('website')
        username = request.POST.get('username')
        password = request.POST.get('password')

        key = settings.ENCRYPTION_KEY.encode()
        cipher_suite = Fernet(key)
        encrypted_password = cipher_suite.encrypt(password.encode())

        user = request.user
        new_password = Password(user=user, website=website, username=username, encrypted_password=encrypted_password)
        new_password.save()

        return redirect('password_list')  # replace with the appropriate URL to redirect after saving the password

    return render(request, 'password_form.html')
