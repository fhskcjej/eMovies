"""
URL configuration for eMovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from eMovies_app.views import home  # view-функция home
from eMovies import settings
from django.conf.urls.static import static
from cart.views import view_cart
from purchases.views import purchase_history_view
from cart import views

from eMovies_app.views import movie_detail, movie_list, import_movies


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # именно сюда при заходе на / идёт запрос
    path('import_movies', import_movies, name="import movies"),
    path('movie/', include(('eMovies_app.urls', 'eMovies'), namespace='eMovies')),

    path('movies/', movie_list, name='movie_list'),

    path('user/', include('users.urls', )),

    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),

    path('comments/', include('comments.urls')),

    path('purchases/', include('purchases.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
