from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    tel = models.CharField(max_length=50, blank=True)
    add_message = models.TextField(blank=True)

    def __str__(self):
        return self.email

    def get_data(self):
        data = f"""
        name: {self.name}\n
        email: {self.email}\n
        tel: {self.tel}\n
        message: {self.add_message}
        """
        return data
