from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField(max_length=256, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    in_stock = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Products"
        # ordering = ("-created",)

    def __str__(self):
        return self.name

