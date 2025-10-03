from django.contrib import admin
from .models import Coach, Program, GalleryImage, ContactMessage, Admission, StudentFee

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'contact_number', 'email')
    search_fields = ('name', 'email')
    list_filter = ('gender',)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration')
    search_fields = ('title',)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_sent')
    search_fields = ('name', 'email')
    readonly_fields = ('date_sent',)

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'program', 'date_applied')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('program',)
    readonly_fields = ('date_applied',)

@admin.register(StudentFee)
class StudentFeeAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'status', 'payment_date')
    list_filter = ('status',)
    search_fields = ('student__name',)
    readonly_fields = ('payment_date',)
