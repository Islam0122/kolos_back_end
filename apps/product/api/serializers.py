from rest_framework import serializers
from product import models as m

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Category
        fields = ['id','title',]


class ProductItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title',queryset=m.Category.objects.all())

    # category_id = serializers.PrimaryKeyRelatedField(source='category', read_only=True)
    sum = serializers.ReadOnlyField()

    class Meta:
        model = m.Product
        fields = [ 'id', 'name','category','identification_number', 'unit', 'quantity', 'price',
                          'sum','state']

class ProductTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Product
        fields = ('id', 'name')

data_json = {
    'name': 'Product',
}

# пользователь вводит строку
# текста я отправлюяь с ф на б запрос и добавлюяю кателгоии и стате
# мы делем поиск по всей базе товаров и смотрим соападения если происх
# совпдажние мы добавляем совпадание если произошло совпадение наименованию то отправлем по наименованию
