from django.db import models


class CountryChoice(models.TextChoices):
    BULGARIA = "BG", "Bulgaria"
    UK = "UK", "United Kingdom"
    GERMANY = "DE", "Germany"
    FRANCE = "FR", "France"
    USA = "US", "United States"
    CANADA = "CA", "Canada"
    AUSTRALIA = "AU", "Australia"
    OTHER = "OTHER", "Other"