from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404

from tournaments_app.models import Tournament


class AllTournamentsView(ListView):
    model = Tournament

    def get_context_data(self, **kwargs):
        return {'Tournaments':  Tournament.objects.all()}


class DetailTournamentView(DetailView):
    model = Tournament


class CreateTournamentView(LoginRequiredMixin, CreateView):
    model = Tournament
    login_url = reverse_lazy('login')
    fields = ['name', 'start_date', 'end_date',
              'max_number_of_players', 'registered_teams']

    def get_success_url(self):
        return reverse('tournaments-home')


class UpdateTournamentView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tournament
    fields = ['name', 'start_date', 'end_date',
              'max_number_of_players', 'registered_teams']
    login_url = reverse_lazy('login')
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('tournament_detail')

    def get_success_url(self):
        return reverse('tournaments-home')


class DeleteTournamentView(LoginRequiredMixin, DeleteView):
    model = Tournament
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('tournaments-home')
