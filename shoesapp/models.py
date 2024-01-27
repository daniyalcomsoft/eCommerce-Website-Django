from django.db import models

# Create your models here.

class Type(models.Model):
    TypeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, verbose_name='Shoes Type', blank=False)
    Image = models.ImageField(upload_to='media/product', null=True)
    
    def __str__(self) -> str:
        return self.Name
    
class Size(models.Model):
    SizeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, verbose_name='Shoes Size', blank=False)

    def __str__(self) -> str:
        return self.Name

class Condition(models.Model):
    ConditionID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, verbose_name='Shoes Condition', blank=False)
    Image = models.ImageField(upload_to='media/product', null=True)

    def __str__(self) -> str:
        return self.Name

class Brand(models.Model):
    BrandID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, verbose_name='Brand Name', blank=False)

    def __str__(self) -> str:
        return self.Name

    
class Shoes(models.Model):
    ShoesID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, verbose_name='Shoes Name', blank=False)
    CutPrice = models.CharField(max_length=255, verbose_name='Cut Price', blank=False)
    Price = models.CharField(max_length=255, verbose_name='Actual Price', blank=False)
    Image = models.ImageField(upload_to='media/product', null=True)
    Type = models.ForeignKey(Type, verbose_name='Shoes Type', on_delete=models.DO_NOTHING)
    Size = models.ForeignKey(Size, verbose_name='Shoes Size', on_delete=models.DO_NOTHING)
    Condition = models.ForeignKey(Condition, verbose_name='Shoes Condition', on_delete=models.DO_NOTHING)
    Brand = models.ForeignKey(Brand, verbose_name='Shoes Brand', on_delete=models.DO_NOTHING)
    Description = models.TextField(verbose_name='Description')

    def __str__(self) -> str:
        return self.Name


class ShoesImage(models.Model):
    PID = models.AutoField(primary_key=True)
    Shoes = models.ForeignKey(Shoes, verbose_name="Shoes Name", on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='media/product', null=True)

    def __str__(self) -> str:
        return f"Image for Product: {self.Shoes.Name}"

class ShoesReviews(models.Model):
    ShoesReviewsID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, verbose_name='Name', blank=False)
    Image = models.ImageField(upload_to='media/product', null=True)
    Description = models.TextField()

    def __str__(self) -> str:
        return self.Name

class Videos(models.Model):
    VideoID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, verbose_name='Name', blank=True)
    Video = models.FileField(upload_to='videos/')
    Description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.Name
    
class Gallery(models.Model):
    GalleryID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, verbose_name='Name', blank=False)
    Image = models.ImageField(upload_to='media/product', null=True)

    def __str__(self) -> str:
        return self.Name

class ContactUs(models.Model):
    ContactID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, verbose_name='Name', blank=True)
    Telephone = models.CharField(max_length=255, verbose_name='Name', blank=True)
    Email = models.CharField(max_length=255, verbose_name='Name', blank=True)
    Address = models.CharField(max_length=255, verbose_name='Name', blank=True)
    Message = models.TextField(verbose_name='Your Message')

    def __str__(self) -> str:
        return self.Name
    
class Query(models.Model):
    QueryID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, verbose_name='Name', blank=True)
    Telephone = models.CharField(max_length=255, verbose_name='Name', blank=True)
    Email = models.CharField(max_length=255, verbose_name='Name', blank=True)
    Address = models.CharField(max_length=255, verbose_name='Name', blank=True)
    Image = models.ImageField(upload_to='media/product', null=True)
    Message = models.TextField(verbose_name='Your Message')

    def __str__(self) -> str:
        return self.Name
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class BestSelling(models.Model):
    BestSellingID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, verbose_name='Shoes Name', blank=False)
    CutPrice = models.CharField(max_length=255, verbose_name='Cut Price', blank=False)
    Price = models.CharField(max_length=255, verbose_name='Actual Price', blank=False)
    Image = models.ImageField(upload_to='media/product', null=True)
    Type = models.ForeignKey(Type, verbose_name='Shoes Type', on_delete=models.DO_NOTHING)
    Size = models.ForeignKey(Size, verbose_name='Shoes Size', on_delete=models.DO_NOTHING)
    Condition = models.ForeignKey(Condition, verbose_name='Shoes Condition', on_delete=models.DO_NOTHING)
    Brand = models.ForeignKey(Brand, verbose_name='Shoes Brand', on_delete=models.DO_NOTHING)
    Description = models.TextField(verbose_name='Description')

    def __str__(self) -> str:
        return self.Name
    
class BSImage(models.Model):
    BSIID = models.AutoField(primary_key=True)
    BestSelling = models.ForeignKey(BestSelling, verbose_name="Best Selling Name", on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='media/product', null=True)

    def __str__(self) -> str:
        return f"Image for Product: {self.BestSelling.Name}"

class Deals(models.Model):
    DealID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, verbose_name='Shoes Name', blank=False)
    CutPrice = models.CharField(max_length=255, verbose_name='Cut Price', blank=False)
    Price = models.CharField(max_length=255, verbose_name='Actual Price', blank=False)
    Image = models.ImageField(upload_to='media/product', null=True)
    Type = models.ForeignKey(Type, verbose_name='Shoes Type', on_delete=models.DO_NOTHING)
    Size = models.ForeignKey(Size, verbose_name='Shoes Size', on_delete=models.DO_NOTHING)
    Condition = models.ForeignKey(Condition, verbose_name='Shoes Condition', on_delete=models.DO_NOTHING)
    Brand = models.ForeignKey(Brand, verbose_name='Shoes Brand', on_delete=models.DO_NOTHING)
    Description = models.TextField(verbose_name='Description')

    def __str__(self) -> str:
        return self.Name
    
class DealsImage(models.Model):
    DIID = models.AutoField(primary_key=True)
    Deals = models.ForeignKey(Deals, verbose_name="Deals Name", on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='media/product', null=True)

    def __str__(self) -> str:
        return f"Image for Product: {self.Deals.Name}"