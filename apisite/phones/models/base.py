from django.db import models


class PhonePosition(models.Model):
    article_id = models.BigAutoField(auto_created=True,
                                     primary_key=True)
    phone = models.ForeignKey(to="phones.Phone",
                              on_delete=models.CASCADE)
    color = models.ForeignKey(to="phones.PhoneColor",
                              on_delete=models.CASCADE)
    storage = models.ForeignKey(to="phones.PhoneStorage",
                                on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.phone} for ${self.price}"
