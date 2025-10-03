from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-logout/', views.admin_logout_view, name='admin_logout'),

    path('admin-area/manage-coaches/', views.manage_coaches, name='manage_coaches'),
    path('admin-area/edit-coach/<int:coach_id>/', views.edit_coach, name='edit_coach'),
    path('admin-area/delete-coach/<int:coach_id>/', views.delete_coach, name='delete_coach'),

    path('admin-area/manage-programs/', views.manage_programs, name='manage_programs'),
    path('admin-area/edit-program/<int:program_id>/', views.edit_program, name='edit_program'),
    path('admin-area/delete-program/<int:program_id>/', views.delete_program, name='delete_program'),

    path('admin-area/manage-gallery/', views.manage_gallery, name='manage_gallery'),
    path('admin-area/delete-gallery/<int:image_id>/', views.delete_gallery_image, name='delete_gallery_image'),

    path('admin-area/view-contacts/', views.view_contacts, name='view_contacts'),
    path('admin-area/delete-contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('contact/', views.contact, name='contact'),

    path('admission/', views.admission_form, name='admission_form'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.student_dashboard, name='dashboard'),
    path('admin-area/manage-fees/', views.manage_fees, name='manage_fees'),
    path('admin-area/edit-fee/<int:fee_id>/', views.edit_fee, name='edit_fee'),
    path('admin-area/delete-fee/<int:fee_id>/', views.delete_fee, name='delete_fee'),

    path('programs/', views.all_programs, name='all_programs'),
    path('coaches/', views.all_coaches, name='all_coaches'),
    path('gallery/', views.user_gallery, name='user_gallery'),

    path('admin-area/view-admissions/', views.view_admissions, name='view_admissions'),
    path('admin-area/delete-admission/<int:admission_id>/', views.delete_admission, name='delete_admission'),

]
