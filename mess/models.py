import uuid

from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string

# Create your models here.


class Coupons(models.Model):
    couponId = models.AutoField(primary_key=True)
    addTime = models.DateTimeField()
    amount = models.FloatField(max_length=150, null=False)
    valid = models.BooleanField(default=1)
    #code = models.UUIDField(default=uuid.uuid4, editable=False)
    def __str__(self):
        return str(self.amount)

    slug = models.SlugField(max_length=5,
                            blank=True  )  # blank if it needs to be migrated to a model that didn't already have this

    # ...
    def save(self, *args, **kwargs):
        """ Add Slug creating/checking to save method. """
        slug_save(self)  # call slug_save, listed below
        super(Coupons, self).save(*args, **kwargs)


# ...
def slug_save(obj):
    """ A function to generate a 5 character slug and see if it has been used and contains naughty words."""
    if not obj.slug:  # if there isn't a slug
        obj.slug = get_random_string(5)  # create one
        slug_is_wrong = True
        while slug_is_wrong:  # keep checking until we have a valid slug
            slug_is_wrong = False
            other_objs_with_slug = type(obj).objects.filter(slug=obj.slug)
            if len(other_objs_with_slug) > 0:
                # if any other objects have current slug
                slug_is_wrong = True
            if slug_is_wrong:
                # create another slug and check it again
                obj.slug = get_random_string(5)


class Orders(models.Model):
    orderId = models.AutoField(primary_key=True)
    orderName = models.CharField(max_length=150)
    amount = models.FloatField(null=False)
    valid = models.BooleanField(default=1)
    def __str__(self):
        return(self.orderName)

class Posts(models.Model):
    postId = models.AutoField(primary_key=True)
    title = models.CharField(null=False,max_length=150)
    body = models.TextField(null=False)
    addTime = models.DateTimeField(null=False)
    def __str__(self):
        return(self.title)