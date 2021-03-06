from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from airline_app.admin_flights_list import add_flight, delete_flight, get_flights
from airline_app.admin_users_list_view import delete_user, confirm_user, get_users
from airline_app.dispatcher_views import get_dispatcher, view_team, create_team, save_team
from airline_app.user_view import user_flights, user_team
from airline_app.views import RegistrationView, LoginView, GetUsersView, GetFlightsView, GetFlightsDispView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^registration$', RegistrationView.as_view()),
    url(r'^registration_handler$', RegistrationView.as_view()),
    url(r'^login$', LoginView.as_view()),
    url(r'^login_handler$', LoginView.as_view()),
    url(r'^admin$', TemplateView.as_view(template_name='admin.html')),
    url(r'^get_users_list$', GetUsersView.as_view()),
    url(r'^users$', get_users),
    url(r'^delete_user/([\w]+)$', delete_user),
    url(r'^confirm_user/([\w]+)$', confirm_user),
    url(r'^get_flights_list$', GetFlightsView.as_view()),
    url(r'^flights$', get_flights),
    url(r'^add_flight$', add_flight),
    url(r'^delete_flight/([\w]+)$', delete_flight),
    url(r'^dispatcher$', TemplateView.as_view(template_name='dispatcher.html')),
    url(r'^get_flights_dispatcher$', GetFlightsDispView.as_view()),
    url(r'^get_dispatcher$', get_dispatcher),
    url(r'^view_team/([\w]+)$', view_team),
    url(r'^create_team$', create_team),
    url(r'^save_team/([\w]+)$', save_team),
    url(r'^user_flights/([\w]+)$', user_flights),
    url(r'^user_team/([\w]+)$', user_team),
]