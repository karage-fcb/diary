from django.urls import path
from .views import DiaryList, DiaryDetail, DiaryCreate, DiaryDelete, DiaryUpdate, DiaryYearArchiveView, DiaryMonthArchive

urlpatterns = [
    path('list/', DiaryList.as_view(), name='list'),
    path('detail/<int:pk>/', DiaryDetail.as_view(), name='detail'),
    path('create/', DiaryCreate.as_view(), name='create'),
    path('delete/<int:pk>/', DiaryDelete.as_view(), name='delete'),
    path('update/<int:pk>/', DiaryUpdate.as_view(), name='update'),
    path('<int:year>/', DiaryYearArchiveView.as_view(), name="diarymodel_year_archive"),
    path('<int:year>/<int:month>/', DiaryMonthArchive.as_view(), name='month'),
]