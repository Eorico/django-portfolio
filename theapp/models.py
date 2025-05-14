from django.db import models

class Colors(models.Model):
    UI_ID = models.CharField(max_length=255)
    NAME = models.CharField(max_length=255)
    RGB = models.CharField(max_length=255)
    SYMBOL = models.CharField(max_length=255)
    USAGE_FOR_BRANDING = models.CharField(max_length=255)
    CATEGORY = models.CharField(max_length=255)
    MEANING = models.CharField(max_length=255, null=True, blank=True)   
    
    class Meta:
        verbose_name_plural = "Colors"
    
    def __str__(self):
        return f"{self.UI_ID} - {self.NAME} - {self.RGB} - {self.SYMBOL} - {self.USAGE_FOR_BRANDING} - {self.CATEGORY} - {self.MEANING}"