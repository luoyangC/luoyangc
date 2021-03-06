"""
  Created by Amor on 2018-09-22
"""
import random

from django.contrib.auth import get_user_model
from rest_framework import serializers

from articles.models import Category, Article, Sentence
from operation.models import Like, Fav
from users.serializers import UserDetailSerializer
from luoyangc.settings import OSS_URL

__author__ = '骆杨'


User = get_user_model()


class SentenceSerializer(serializers.ModelSerializer):

    lines = serializers.SerializerMethodField()

    def get_lines(self, obj):
        return obj.lines.split(' ')

    class Meta:
        model = Sentence
        fields = ('lines', )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('status', 'create_time')


class ArchiveSerializer(serializers.Serializer):

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    archive = serializers.CharField(read_only=True)


class TagSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
    tag = serializers.CharField()


class ArticleProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'profile', 'update_time', 'tags')


class ArticleSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    is_like = serializers.SerializerMethodField()
    is_fav = serializers.SerializerMethodField()
    is_author = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    def get_image(self, obj):
        random.seed(obj.id)
        return f'{OSS_URL}/media/image/random/{random.randint(200, 600)}.png'

    def get_user(self, obj):
        user = UserDetailSerializer(obj.user, context={'request': self.context['request']})
        return user.data

    def get_is_like(self, obj):
        user = self.context['request'].user
        if not isinstance(user, User):
            return False
        like = Like.objects.filter(user=user, like_id=obj.id, like_type='article').first()
        if not like:
            return False
        return like.id

    def get_is_fav(self, obj):
        user = self.context['request'].user
        if not isinstance(user, User):
            return False
        fav = Fav.objects.filter(user=user, article=obj).first()
        if not fav:
            return False
        return fav.id

    def get_is_author(self, obj):
        user = self.context['request'].user
        return user == obj.user

    def get_category(self, obj):
        return obj.category.title

    class Meta:
        model = Article
        exclude = ('status', )
