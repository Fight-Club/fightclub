from rest_framework import serializers
from core.models import Category, Fighter, Fight


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            )


class FighterSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True, read_only=True)

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
    winner = serializers.StringRelatedField(read_only=True)
    loser = serializers.StringRelatedField(read_only=True)

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
