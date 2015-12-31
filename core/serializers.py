from rest_framework import serializers
from core.models import Category, Fighter, Fight


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            )


class FighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fighter
        fields = (
            'name',
            'categories',
            'description',
            'rating',
            'reference',
            )


class FightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fight
        fields = (
            'user',
            'winner',
            'loser',
            'winner_start_rating',
            'loser_start_rating',
            'completed_timestamp',
            )
