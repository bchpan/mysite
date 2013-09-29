from django.db import models
form django.contrib import User


class BookCategory(models.Model):
    category = models.CharField(max_length=20)
    p_category = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.category

class Book(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    category = models.ForeignKey(BookCategory)
    
    def __unicode__(self):
        return self.name

"""
class CarShop(models.Model):
    user = models.OneToOneField()
    books = models.ManyToMany(Book)
    
    def add_book(self, book):
        pass

    def remove_book(self, book):
        pass
    def book_sum()
	pass
    def clear_car()

"""
