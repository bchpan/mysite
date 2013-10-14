from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=30)
    p_date = models.DateField(auto_now=True, default=None, blank=True)

    def __unicode__(self):
        return self.book_name

