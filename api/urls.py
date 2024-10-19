from .views import (BanksAPIView, BranchesAPIView,BranchesDetailsAPIView,BanksDetailsAPIView,)
from django.urls import path

urlpatterns = [
    path('banks/',BanksAPIView.as_view(),name='banks'),
    path('banks/<int:id>',BanksDetailsAPIView.as_view(),),
    path('branches/',BranchesAPIView.as_view(),name='branches',),
    path('branches/<int:id>',BranchesDetailsAPIView.as_view(),)
]
