from django.urls import path
from .views import *

urlpatterns = [
    path('', login , name='login'),
    path('logout/', logout_user , name='logout'),
    path('forgot-password/', forgot_password , name='forgotpassword'),
    path('change-password/<token>/', change_password , name='changepassword'),
    
    # ------------------------------------------------------------------------------------ 
    
    path('register/', register , name='register'),
    path('dashboard/', dashboard , name='dashboard'),
    path('token/', toke_send , name='token'),
    path('success/', success , name='success'),
    path('verify/<auth_token>', verify , name='verify'),
    path('error/', error_page , name='error'),


    # ------------------------------------------------------------------------------------ 

    path('students/', student , name='students'),

    # ------------------------------------------------------------------------------------ 
    
    path('profile/',profile , name='profile'),
    
    # ------------------------------------------------------------------------------------ 
    path('prospectus-payment-verification/',prospectus_success,name="prospectus"),
    
    # ------------------------------------------------------------------------------------ 
    
    path('send-admission-form/',send_admission_form , name='send_admission_form'),
    
    # ------------------------------------------------------------------------------------ 
    path('update-student-detail/<str:username>/',update_student_detail,name='update_student_detail'),
    
    # ------------------------------------------------------------------------------------ 
    path('delete-student/<str:username>/',delete_student,name='delete_student'),
] 