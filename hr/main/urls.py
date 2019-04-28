from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'index/', views.index, name='index'),
    url(r'main/', views.main, name='main'),
    url(r'hr/', views.hr, name='hr'),
    url(r'accept/', views.accept, name='accept'),
    url(r'reject/', views.reject, name='reject'),
    #url(r'applications/', views.ApplicationListView.as_view(), name='all'),
    #url(r'application/<int:pk>', views.ApplicationDetailView.as_view(), name='application-detail')
]

"""
urlpatterns = [
path('', views.index, name='index'),
path('today/', views.today, name='today'),
path('all/', views.all, name='all'),
path('latest/', views.latest, name='latest'),
path('match/', views.TodaymatchListView.as_view(), name='match'),
path('todaymatch/<int:pk>', views.TodaymatchDetailView.as_view(), name='todaymatch-detail'),
]


"""