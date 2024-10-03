from django.db import models
from django.urls import reverse


class Menu(models.Model):
    """
    Model Menu with unique field name
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Model MenuItem serves as a Menu element linked with a specific Menu.
    Each MenuItem may have an explicit URL or a named URL generated from route.
    Each MenuItem can be nested.
    """
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    # Foreign key to model Menu linking menu items with specific Menu
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    named_url = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    # Foreign key to itself allowing to create tree-like menu structure

    class Meta:
        unique_together = ('menu', 'name')

    def get_url(self):
        """
        Returns URL for Menu element prioritizing named URL
        """
        if self.named_url:
            return reverse(self.named_url)
        return self.url

    def __str__(self):
        return self.name
