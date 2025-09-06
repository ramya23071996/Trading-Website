from django.db import models

class Trade(models.Model):
    symbol = models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    trade_type = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.trade_type.upper()} {self.quantity} {self.symbol} @ {self.price}"
    
class Trade(models.Model):
    symbol = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='logos/')  # This saves to MEDIA_ROOT/logos/
