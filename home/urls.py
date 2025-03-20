from django.contrib import admin
from django.urls import path, include
from home import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')  # Redirect to home if logged in
        return super().get(request, *args, **kwargs)

urlpatterns = [
    path("", views.index, name="index"),

    path("adminclick/", views.adminClick, name="adminclick"),
    path("adminlogin/", CustomLoginView.as_view(template_name="admin_login.html",
                                            authentication_form=AuthenticationForm
                                          ), name="adminlogin"),
    path("memberclick/", views.memberClick, name="memberclick"),
    path("membersignup/", views.memberSignup, name="membersignup"),
    path("memberlogin/", CustomLoginView.as_view(template_name="member_login.html",
                                           authentication_form=AuthenticationForm
                                           ), name="memberlogin"),
    path("logout/", LogoutView.as_view(template_name="home.html"), name="logout"),

    path("adminhome/", views.adminHome, name="adminhome"),
    path("memberhome/", views.memberHome, name="memberhome"),

    path("adminapproval/", views.adminApproval, name="adminapproval"),
    path("adminapproval/<int:case_id>/", views.approvalCaseDetails, name="approval_case_details"),

    path("afterlogin/", views.afterlogin, name="afterlogin"),
    path("home", views.home, name="home"),
    path('caselist/', views.caseList, name='caselist'),
    path("cases/<int:case_id>/", views.caseDetails, name="case_details"),
    path('visitorclick/', views.visitorHome, name='visitor_home'),
]
