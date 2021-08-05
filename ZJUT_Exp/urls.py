"""ZJUT_Exp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from exp.view import views

from exp.view import operate

urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'login', views.to_login),
    path(r'logout', views.to_logout),

    # page
    path(r'study', views.to_study),
    path(r'report_detail', views.to_report_detail),

    path(r'run_code', views.run_code),
    path(r'index', views.to_index),
    re_path(r'^$', views.to_index),
    path(r'exp_six', views.to_exp_six),
    path(r'exp_five', views.to_exp_five),
    path(r'exp_three', views.to_exp_three),
    path(r'exp_four', views.to_exp_four),
    path(r'exp_one', views.to_exp_one),
    path(r'exp_two', views.to_exp_two),
    path(r'exp_seven', views.to_exp_seven),
    path(r'exp_eight', views.to_exp_eight),
    path(r'exp_nine', views.to_exp_nine),
    path(r'exp_thirteen', views.to_exp_thirteen),
    path(r'exp_fourteen', views.to_exp_fourteen),
    path(r'exp_fifteen', views.to_exp_fifteen),
    path(r'exp_twenteen', views.to_exp_twenteen),
    path(r'download_exp', views.download_exp, name='download_exp'),

    # operate
    path(r'chanshengshi', operate.chanshengshi),
    path(r'xiyiji', operate.xiyiji),
    path(r'bashuma', operate.bashuma),
    path(r'migong', operate.migong),
    path(r'gp_max', operate.gp_max),
    path(r'gp_tsp', operate.gp_tsp),
    path(r'hop_tsp', operate.hop_tsp),
    path(r'qpso', operate.get_qpso),
    path(r'qea_run', operate.get_qea_run),
    path(r'pso_tsp', operate.get_pso_tsp)

]
