from django.conf import settings
from django.db.models import Q

from cards.models import Set



def settings_context(_request):
    # Put global template variables here.
    return {"DEBUG": settings.DEBUG}  # explicit

filter_params = ['core','expansion','masters','draft_innovation','commander']
def recent_set_list(request):
    recent_set = Set.objects.filter(set_type__in=filter_params).values('img_url','code','name').order_by('-released_at')[:9]
    # recent_set = Set.objects.exclude(tcgplayer_id=None).values('img_url','code','name').order_by('-released_at')[:9]
    return {'nav_sets': recent_set}