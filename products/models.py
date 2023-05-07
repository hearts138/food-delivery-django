from django.db import models
import uuid

# Concept of DONOT REPEAT YOURSELF is not used.
# uid,created_at,updated_at is being reused many times in different classes.
# use basemodel to define common class(model)fields.

class Product(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    product_name=models.CharField(max_length=100)
    created_at=models.DateField(auto_created=True)
    updated_at=models.DateField(auto_created=True)

class ProductImages(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    product_images=models.ImageField(upload_to="products")
    created_at=models.DateField(auto_created=True)
    updated_at=models.DateField(auto_created=True)
