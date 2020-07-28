from django.db import models



class CardQuerySet(models.QuerySet):
    def editors(self):
        return self.filter(role='E')


    filter(set__iexact=set_code).exclude(frame_effects__overlap=['showcase','extendedart','inverted']).exclude(border_color="borderless")


    def is_colorless(self):
        return self.exclude(type_line__icontains="land").exclude(type_line__icontains="artifact")


class CardManager(models.manager):
