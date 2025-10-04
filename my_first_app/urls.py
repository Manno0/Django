from django.urls import path
from my_first_app.views import home , not_found


urlpatterns = [
    path('home/', home, name='home'),  # Maps the root URL to the home view
    path('not_found/', not_found, name='not_found')
]