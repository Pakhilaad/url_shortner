from django.db import models
from hashids import Hashids

class ShortURL(models.Model):
    original_url = models.URLField(max_length=2000)
    short_id = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if the object is new and doesn't have a primary key yet
            super().save(*args, **kwargs)  # Save the object to generate the primary key
            hashids = Hashids(salt="your_salt_here", min_length=7)  # Add a custom salt for security
            self.short_id = hashids.encode(self.pk)
            super().save(*args, **kwargs)  # Save the object again to update the short_id field
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_id}: {self.original_url}"
