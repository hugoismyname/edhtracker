from django.conf import settings

from MTG_cards.models import Set



def settings_context(_request):
    # Put global template variables here.
    return {"DEBUG": settings.DEBUG}  # explicit

def recent_set_list(request):
    recent_set = Set.objects.filter(parent_set_code=None)
                .exclude(set_type='box').exclude(set_type='promo')
                .exclude(set_type='funny').order_by('-released_at')[:9]
    return {'nav_sets': recent_set}