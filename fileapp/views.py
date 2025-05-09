from django.shortcuts import render, redirect
from .models import User, File_Upload
from django.contrib import messages

# Create your views here.
def index(request):
    if 'user' in request.session:
        all_files = File_Upload.objects.all()
        data = {'files': all_files}
        return render(request, 'index.html', data)
    else:
        return redirect('login')
    
def login(request):
    if 'user' not in request.session:
        if request.method == 'POST':
            email = request.POST['email']
            pwd = request.POST['pwd']
            
            try:
                # Get the user by email first
                user = User.objects.get(email=email)
                
                # Then use Django's check_password method to verify the password
                if user.check_password(pwd):
                    request.session["user"] = email
                    return redirect('index')
                else:
                    messages.warning(request, "Incorrect password.")
            except User.DoesNotExist:
                messages.warning(request, "Email not registered.")
                
        return render(request, 'login.html')
    else:
        return redirect('index')

def logout(request):
    del request.session['user']
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        username_from_form = request.POST['name'] 
        email = request.POST['email']
        pwd = request.POST['pwd'] # Keep reading 'pwd' from the form
        gender = request.POST['gender']

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email is already registered!")
        elif User.objects.filter(username=username_from_form).exists():
             messages.warning(request, "Username is already taken!")
        else:
            User.objects.create_user(username=username_from_form, email=email, password=pwd, gender=gender)
            messages.success(request, "Your account is created successfully!")
            return redirect('login')

    return render(request, 'signup.html')


def settings(request):
    if 'user' in request.session:
        user_obj = User.objects.get(email = request.session['user'])
        user_files = File_Upload.objects.filter(user = user_obj)

        img_list = []
        audio_list = []
        videos_list = []
        pdfs_list = []

        for file in user_files:
            if str(file.file_field)[-3:] == 'mp3':
                audio_list.append(file)
            elif str(file.file_field)[-3:] == 'mp4' or str(file.file_field)[-3:] == 'mkv':
                videos_list.append(file)
            elif str(file.file_field)[-3:] == 'jpg' or str(file.file_field)[-3:] == 'png' or str(file.file_field)[-3:] == 'jpeg':
                img_list.append(file)
            elif str(file.file_field)[-3:] == 'pdf':
                pdfs_list.append(file)  

        data = {'user_files': user_files, 'videos': len(videos_list), 'audios': len(audio_list), 'images': len(img_list), 'pdf': len(pdfs_list), 'img_list': img_list, 'audio_list': audio_list, 'videos_list': videos_list, 'pdfs_list': pdfs_list}
        return render(request, 'settings.html', data)

def file_upload(request):
    if request.method == 'POST':
        # Check if the file exists in the request
        if 'file_to_upload' not in request.FILES:
            messages.warning(request, "No file selected for upload.")
            # Re-render the form, showing the warning
            return render(request, 'file_upload.html') 

        # Proceed only if a file was actually uploaded
        title_name = request.POST['title']
        description_name = request.POST['description']
        file_name = request.FILES['file_to_upload']

        user_obj = User.objects.get(email=request.session['user'])
        # .create() already saves the object, no need for new_file.save()
        File_Upload.objects.create(user = user_obj, title=title_name, description=description_name, file_field = file_name) 
        messages.success(request, "File is uploaded successfully!")
        # Redirect after successful POST to prevent re-submission
        return redirect('file_upload') 

    # Handle GET request or if POST failed validation (though validation is basic here)
    return render(request, 'file_upload.html')

def delete_file(request, id):
    if 'user' in request.session:
        file_obj = File_Upload.objects.get(id = id)
        file_obj.delete()
        return redirect('settings')
    else:
        return redirect('login')