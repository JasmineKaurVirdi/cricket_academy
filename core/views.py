from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Coach
from .models import Program
from .models import GalleryImage
from .models import ContactMessage
from .models import Admission
from django.contrib.auth.models import User
from .models import Admission, StudentFee

def home(request):
    programs = Program.objects.all().order_by('-id')[:3]    
    coaches = Coach.objects.all().order_by('-id')[:3]       
    gallery = GalleryImage.objects.all().order_by('-id')[:6]
    return render(request, 'core/index.html', {
        'programs': programs,
        'coaches': coaches,
        'gallery': gallery
    })


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact')

        else:
            messages.error(request, 'All fields are required.')

    return render(request, 'core/contact.html')


def admission_form(request):
    programs = Program.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        program_id = request.POST.get('program')

        if name and email and phone and dob and address and program_id:
            program = Program.objects.get(id=program_id)
            Admission.objects.create(
                name=name,
                email=email,
                phone=phone,
                dob=dob,
                address=address,
                program=program
            )
            messages.success(request, 'Your admission form has been submitted successfully.')
            return redirect('admission_form')
        else:
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'core/admission_form.html', {'programs': programs})



def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Registration successful. Please log in.')
        return redirect('login')

    return render(request, 'core/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')



@login_required(login_url='login')
def student_dashboard(request):
    user = request.user
    admission = Admission.objects.filter(email=user.email).order_by('-date_applied').first()
    fees = StudentFee.objects.filter(student__email=user.email).order_by('-payment_date')
    return render(request, 'core/dashboard.html', {
        'admission': admission,
        'fees': fees
    })


# Check if user is staff (admin)
def is_admin(user):
    return user.is_staff

def admin_login_view(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid credentials or not authorized.')

    return render(request, 'admin/admin_login.html')

@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def manage_coaches(request):
    from .models import Coach

    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        image = request.FILES.get('image')

        Coach.objects.create(
            name=name,
            gender=gender,
            contact_number=contact_number,
            email=email,
            bio=bio,
            image=image
        )
        return redirect('manage_coaches')

    coaches = Coach.objects.all().order_by('-id')
    return render(request, 'admin/manage_coaches.html', {'coaches': coaches})

@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def edit_coach(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)

    if request.method == 'POST':
        coach.name = request.POST.get('name')
        coach.gender = request.POST.get('gender')
        coach.contact_number = request.POST.get('contact_number')
        coach.email = request.POST.get('email')
        coach.bio = request.POST.get('bio')
        if request.FILES.get('image'):
            coach.image = request.FILES.get('image')
        coach.save()
        return redirect('manage_coaches')

    return render(request, 'admin/edit_coach.html', {'coach': coach})


@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def delete_coach(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    coach.delete()
    return redirect('manage_coaches')


@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def manage_programs(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        picture = request.FILES.get('picture')

        Program.objects.create(
            title=title,
            description=description,
            duration=duration,
            picture=picture
        )
        return redirect('manage_programs')

    programs = Program.objects.all().order_by('-id')
    return render(request, 'admin/manage_programs.html', {'programs': programs})


@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def edit_program(request, program_id):
    program = get_object_or_404(Program, id=program_id)

    if request.method == 'POST':
        program.title = request.POST.get('title')
        program.description = request.POST.get('description')
        program.duration = request.POST.get('duration')
        if request.FILES.get('picture'):
            program.picture = request.FILES.get('picture')
        program.save()
        return redirect('manage_programs')

    return render(request, 'admin/edit_program.html', {'program': program})


@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def delete_program(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    program.delete()
    return redirect('manage_programs')


@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def manage_gallery(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        if title and image:
            GalleryImage.objects.create(title=title, image=image)
            return redirect('manage_gallery')

    gallery = GalleryImage.objects.all().order_by('-id')
    return render(request, 'admin/manage_gallery.html', {'gallery': gallery})

@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def delete_gallery_image(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)
    image.delete()
    return redirect('manage_gallery')




@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def view_contacts(request):
    messages = ContactMessage.objects.all().order_by('-date_sent')
    return render(request, 'admin/view_contacts.html', {'messages': messages})

@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def delete_contact(request, contact_id):
    message = get_object_or_404(ContactMessage, id=contact_id)
    message.delete()
    return redirect('view_contacts')


@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def view_admissions(request):
    return render(request, 'admin/view_admissions.html')



@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def manage_fees(request):
    admissions = Admission.objects.all().order_by('-date_applied')
    fees = StudentFee.objects.all().order_by('-payment_date')

    if request.method == 'POST':
        admission_id = request.POST.get('admission_id')
        amount = request.POST.get('amount')
        status = request.POST.get('status')

        if admission_id and amount and status:
            admission = Admission.objects.get(id=admission_id)
            StudentFee.objects.create(student=admission, amount=amount, status=status)
            messages.success(request, 'Fee record added successfully.')
            return redirect('manage_fees')
        else:
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'admin/manage_fees.html', {
        'admissions': admissions,
        'fees': fees
    })

@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def edit_fee(request, fee_id):
    fee = get_object_or_404(StudentFee, id=fee_id)
    admissions = Admission.objects.all()

    if request.method == 'POST':
        admission_id = request.POST.get('admission_id')
        amount = request.POST.get('amount')
        status = request.POST.get('status')

        if admission_id and amount and status:
            admission = Admission.objects.get(id=admission_id)
            fee.student = admission
            fee.amount = amount
            fee.status = status
            fee.save()
            messages.success(request, 'Fee record updated successfully.')
            return redirect('manage_fees')

    return render(request, 'admin/edit_fee.html', {'fee': fee, 'admissions': admissions})



@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def delete_fee(request, fee_id):
    fee = get_object_or_404(StudentFee, id=fee_id)
    fee.delete()
    messages.success(request, 'Fee record deleted successfully.')
    return redirect('manage_fees')


@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def view_admissions(request):
    admissions = Admission.objects.all().order_by('-date_applied')
    return render(request, 'admin/view_admissions.html', {'admissions': admissions})

@login_required(login_url='admin_login')
@user_passes_test(is_admin)
def delete_admission(request, admission_id):
    admission = get_object_or_404(Admission, id=admission_id)
    admission.delete()
    messages.success(request, 'Admission record deleted successfully.')
    return redirect('view_admissions')

def admin_logout_view(request):
    logout(request)
    return redirect('admin_login') 


def all_programs(request):
    programs = Program.objects.all().order_by('-id')
    return render(request, 'core/programs.html', {'programs': programs})

def all_coaches(request):
    coaches = Coach.objects.all().order_by('-id')
    return render(request, 'core/coaches.html', {'coaches': coaches})

def user_gallery(request):
    gallery = GalleryImage.objects.all().order_by('-id')
    return render(request, 'core/gallery.html', {'gallery': gallery})
