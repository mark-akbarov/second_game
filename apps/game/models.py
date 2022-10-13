from django.db import models


class Collection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pics/%Y/%m/%d')
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='item')

    def __str__(self) -> str:
        return self.title


class Vote(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='vote')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='vote') 
    vote = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.item__name   