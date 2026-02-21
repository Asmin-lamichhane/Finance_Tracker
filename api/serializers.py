from rest_framework import serializers
from .models import Category, Transaction

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'is_custom']


class TransactionSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(source='category.name', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Transaction
        fields = ['id','username','category','category_name','amount','description','transaction_type','date']
        read_only_fields = ['date', 'username', 'category_name']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be a positive number.")
        return value

    def validate_transaction_type(self, value):
        valid = ['INCOME', 'EXPENSE']
        if value not in valid:
            raise serializers.ValidationError("transaction_type must be either 'INCOME' or 'EXPENSE'.")
        return value