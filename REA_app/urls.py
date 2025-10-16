"""REA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from REA_app import views

urlpatterns = [
    path('app_reviews',views.app_reviews),
    path('approved_mentor',views.approved_mentor),
    path('change_password',views.change_password),
    path('change_password_POST', views.change_password_POST),
    path('view_complaint',views.view_complaint),
    path('mentor_approval',views.mentor_approval),
    path('approve_mentor/<id>',views.approve_mentor),
    path('reject_mentor/<id>',views.reject_mentor),

    path('rejected_mentor',views.rejected_mentor),
    path('send_reply/<id>',views.send_reply),
    path('send_reply_POST/<id>',views.send_reply_POST),
    path('view_mentor_review',views.view_mentor_review),
    path('video_call/<id>',views.video_call),
    path('new_video_call',views.new_video_call),
    path('admin_home',views.admin_home),
    path('',views.loginn),
    path('login_POST',views.login_POST),
    path('logout',views.logout),
    # ==================================================
    path('mentor_home',views.mentor_home),
    path('add_motivational_content',views.add_motivational_content),
    path('add_tips', views.add_tips),
    path('change_mentor_password',views.change_mentor_password),
    path('edit_motivational_content/<id>',views.edit_motivational_content),
    path('mentor_register',views.mentor_register),
    path('view_approved_request',views.view_approved_request),
    path('view_motivational_content',views.view_motivational_content),
    path('view_motivational_content_delete/<id>',views.view_motivational_content_delete),
    path('view_profile_edit_profile',views.view_profile_edit_profile),
    path('view_request_approve_reject',views.view_request_approve_reject),
    path('view_review',views.view_review),
    path('view_tips',views.view_tips),
    path('add_motivational_content_post',views.add_motivational_content_post),
    path('add_tips_post',views.add_tips_post),
    path('change_mentor_password_post',views.change_mentor_password_post),
    path('edit_motivational_content_post/<id>',views.edit_motivational_content_post),
    path('mentor_register_post',views.mentor_register_post),
    path('view_motivational_content_post',views.view_motivational_content_post),
    path('view_profile_edit_profile_post',views.view_profile_edit_profile_post),
    path('request_approve/<id>', views.request_approve),
    path('request_reject/<id>', views.request_reject),
    path('view_tips_delete/<id>',views.view_tips_delete),
    path('chatt/<u>',views.chatt),
    path('chatsnd/<u>',views.chatsnd),
    path('chatrply',views.chatrply),
    path('view_emotion_graph/<id>',views.view_emotion_graph),
    path('view_image_emotion_graph/<id>',views.view_image_emotion_graph),



    path('and_login',views.and_login),
    path('and_guest_login',views.and_guest_login),
    path('and_Registration',views.and_Registration),
    path('and_view_mentor',views.and_view_mentor),
    path('and_sent_mentor_request',views.and_sent_mentor_request),
    path('and_our_mentor',views.and_our_mentor),
    path('and_view_motivation_content',views.and_view_motivation_content),
    path('and_view_tips',views.and_view_tips),
    path('and_view_mentor_review',views.and_view_mentor_review),
    path('and_send_mentor_review',views.and_send_mentor_review),
    path('and_send_app_review',views.and_send_app_review),
    path('and_Change_Password',views.and_Change_Password),
    path('and_view_profile',views.and_view_profile),
    path('and_update_profile',views.and_update_profile),
    path('and_send_complaint',views.and_send_complaint),
    path('and_view_complaint_reply',views.and_view_complaint_reply),
    path('and_delete_complaint',views.and_delete_complaint),
    path('and_view_request_status',views.and_view_request_status),
    path('and_custom_delete_request',views.and_custom_delete_request),
    path('add_chat',views.add_chat),
    path('view_chat',views.view_chat),
    path('and_view_diary_content',views.and_view_diary_content),
    path('and_add_diary_content',views.and_add_diary_content),
    path('and_delete_content',views.and_delete_content),
    path('insertmood',views.insertmood),
    # path('predict',views.predict),
    ]


