from ..models import UserCards, Card, Commander

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault



class AddCardsSerializer(serializers.ModelSerializer):
    date_added = serializers.DateTimeField(format="%m-%d-%Y",read_only=True)
    img_url = serializers.CharField(source='card.img_url',read_only=True)
    name = serializers.CharField(source='card.name',read_only=True)
    type_line = serializers.CharField(source='card.type_line',read_only=True)
    class Meta:
        model = UserCards
        fields = ['card','card_count','date_added','img_url','name','type_line']


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card

        fields = ['colors','id','img_url','name','type_line']

class CommanderSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='commander.name',read_only=True)
    img_url = serializers.CharField(source='commander.img_url',read_only=True)

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        # select_related for "to-one" relationships
        queryset = queryset.select_related('commander')
        
        return queryset

    class Meta:
        model = Commander

        fields = ['id','card_list','img_url','name']

class UserCardsSerializer(serializers.ModelSerializer):
    date_added = serializers.DateTimeField(format="%m-%d-%Y")
    img_url = serializers.CharField(source='card.img_url',read_only=True)
    name = serializers.CharField(source='card.name')
    type_line = serializers.CharField(source='card.type_line')
    set = serializers.CharField(source='card.set')

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        # select_related for "to-one" relationships
        queryset = queryset.select_related('card')
        
        return queryset
    
    class Meta:
        model = UserCards
        fields = ['card_count','card_id','date_added','id','img_url','name','type_line','set']

        # read_only_fields = fields