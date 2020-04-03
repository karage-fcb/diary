from django import template
from django.utils import timezone
from diaryapp.models import DiaryModel

register = template.Library()


@register.inclusion_tag('templates/month_links.html')
def render_month_links():
    return {
        'dates': DiaryModel.objects.filter(date__lte=timezone.now()).dates('date', 'month', order='DESC'),
        'data': DiaryModel.objects.all(),
    }