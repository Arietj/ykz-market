from rest_framework import serializers
from apps.product.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id', 'slag')
        
        
    def validate_name(self, value):
        if value[0].isupper():
            return value
        raise serializers.ValidationError("Invalid name")
    
    def create(self, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)
    
    
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ("id","category", "name")
        read_only_fields = ('id', 'slag')
        
    def validate_name(self, value):
        if value[0].isupper():
            return value
        raise serializers.ValidationError("Invalid name")
    
    def create(self, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)

class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('sub_categories',)
        read_only_fields = ('id', 'slag')
        
    def create(self, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)

class ProductSerializer(serializers.ModelSerializer):
    category_detail = CategoryDetailSerializer(read_only=True)
    sub_categories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category_detail', 'sub_categories')
        read_only_fields = ('id', 'slag')
        
    def create(self, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)
    


