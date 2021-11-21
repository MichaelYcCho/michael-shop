from rest_framework import serializers

from accounts.serializers import UserSerializer
from products.models import Product, ProductCategory, ProductCategory, category


class ProductCategorySerializer(serializers.ModelSerializer):
    depth = serializers.SerializerMethodField(read_only=True)
    parent_category = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'depth', 'parent_category')

    def get_depth(self, obj):
        depth = obj.depth
        if depth == 0:
            return '대분류'
        elif depth == 1:
            return '중분류'
        elif depth == 2:
            return '소분류'


class ProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True)
    category = ProductCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = (  'pk',
                    'category',
                    'name',
                    'product_image1',
                    'product_image2',
                    'brand',
                    'description',
                    'weight',
                    'dimensions',
                    'materials',
                    'other_info',
                    'price',
                    'count_in_stock',
                    'recommendation_rank',
                    'product_status',
                    'seller',
                    'is_new',
                    'url_path'
                    )


