from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'isbn', 'price',)

    def validate(self, data):
        title = data.get("title", None)
        author = data.get("author", None)
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi xarflardan tashkil topishi kerak"
                }
            )
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi va muallifi bir xil bo'lgan kitobni yuklay olmaymiz!"
                }
            )

        return data

    def validate_price(self, price):
        if price < 0 or price > 99999999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx noto'gri kiritildi"
                }
            )
