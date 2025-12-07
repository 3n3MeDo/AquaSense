from django.urls import path
from . import views

urlpatterns = [
    # --- Main Pages ---
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # --- Courses & Booking ---
    path('courses/', views.courses, name='courses'),
    path('course/<slug:slug>/', views.details, name='details'),
    path('book/<int:course_id>/', views.book_course, name='book_course'),
    path('checkout/', views.checkout, name='checkout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # --- Authentication ---
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # --- Password Reset Flow ---
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('reset-password/', views.reset_password, name='reset_password'),

    # --- APIs ---
    path('api/chat/', views.chat_view, name='chat_api'),
]
