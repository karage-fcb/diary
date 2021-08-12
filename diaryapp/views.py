from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView,ArchiveIndexView, YearArchiveView, MonthArchiveView
from .models import DiaryModel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class ArchiveListMixin:
    model = DiaryModel
    paginate_by = 12
    date_field = 'date'
    template_name = 'list.html'
    allow_empty = True
    make_object_list = True


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのユーザー情報ページのpkが同じか、又はスーパーユーザーなら許可
        user = self.request.user
        # return user.pk == self.kwargs['pk']
        return user.pk == self.kwargs['pk']


class DiaryList(LoginRequiredMixin, ListView, ArchiveIndexView):
    login_url = '/accounts/login/'
    template_name = 'list.html'
    model = DiaryModel
    date_field = 'date'

class DiaryDetail(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    template_name = 'detail.html'
    model = DiaryModel

class DiaryCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    template_name = 'create.html'
    model = DiaryModel
    fields = ('date', 'dream', 'event', 'submitter')
    success_url = reverse_lazy('list')

class DiaryDelete(OnlyYouMixin, LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    template_name = 'delete.html'
    model = DiaryModel
    success_url = reverse_lazy('list')

class DiaryUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    template_name = 'update.html'
    model = DiaryModel
    fields = ('date', 'dream', 'event', 'submitter')
    success_url = reverse_lazy('list')

class DiaryYearArchiveView(LoginRequiredMixin, YearArchiveView):
    login_url = '/accounts/login/'
    template_name = 'DiaryModel_archive_year.html'
    queryset = DiaryModel.objects.all()
    date_field = "date"
    make_object_list = True
    allow_empty = True

class DiaryMonthArchive(LoginRequiredMixin, MonthArchiveView):
    login_url = '/accounts/login/'
    template_name = 'DiaryModel_archive_month.html'
    model = DiaryModel
    date_field = 'date'
    make_object_list = True
    month_format='%m'