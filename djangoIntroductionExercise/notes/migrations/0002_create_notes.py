from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        # Operations removed to avoid creating notes without categories.
        # These will be created in 0004_create_data_with_categories.py
    ]
