from django.urls import path
from my_first_app.views import home, not_found, HomeView, NotFoundView

urlpatterns = [
    path('home/', home, name='home'),  # Maps the root URL to the home view
    path('not_found/', not_found, name='not_found'),
    path('class_home_page', HomeView.as_view(), name='class_home_page'),
    path('class_not_found', NotFoundView.as_view(), name='class_not_found'),
]
