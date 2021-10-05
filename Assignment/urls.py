"""Assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from Partner.views import GetMemberDetailsByMemberIdAPI, GetPartnerDetailsByPartnerIdAPI, GetPartnersAPI,GetMemberDetailsAPI,InsertMemberDetails,InsertPartnerDetails,UpdateMemberDetailsAPI,UpdatePartnerDetailsAPI 
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', GetPartnersAPI.as_view(),name='home'),
    url(r'^get_memberdetails/$', GetMemberDetailsAPI.as_view()),
    url(r'^insert_memberdetails/$', InsertMemberDetails.as_view(),name="insert_memberdetails"),
    url(r'^insert_partnerdetails/$', InsertPartnerDetails.as_view(),name='insert_partnerdetails'),
    url(r'^update_partnerdetails/$', UpdatePartnerDetailsAPI.as_view()),
    url(r'^update_memberdetails/$', UpdateMemberDetailsAPI.as_view()),
    url(r'^fetch_member_details_by_id/$', GetMemberDetailsByMemberIdAPI.as_view()),
    url(r'^fetch_partner_details_by_id/$', GetPartnerDetailsByPartnerIdAPI.as_view())

]
