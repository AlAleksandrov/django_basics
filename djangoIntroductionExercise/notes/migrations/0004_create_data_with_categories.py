from django.db import migrations

def create_data(apps, schema_editor):
    Note = apps.get_model('notes', 'Note')
    Category = apps.get_model('categories', 'Category')

    # Create Categories
    personal = Category.objects.create(name='Personal', description='Personal tasks and notes')
    work = Category.objects.create(name='Work', description='Work related items')
    ideas = Category.objects.create(name='Ideas', description='Creative ideas and thoughts')

    # Create Notes linked to Categories
    Note.objects.create(
        title='Grocery List',
        body='Milk, Eggs, Bread, Cheese, Apples',
        is_published=True,
        priority=1, # Low
        category=personal
    )
    Note.objects.create(
        title='Meeting Notes',
        body='Discuss project timeline, assign tasks, review budget',
        is_published=True,
        priority=3, # High
        category=work
    )
    Note.objects.create(
        title='Project Ideas',
        body='Mobile app for tracking habits, website for sharing recipes',
        is_published=False,
        priority=2, # Medium
        category=ideas
    )
    Note.objects.create(
        title='To-Do List',
        body='Finish report, call mom, schedule dentist appointment',
        is_published=True,
        priority=2, # Medium
        category=personal
    )
    Note.objects.create(
        title='Book Recommendations',
        body='The Great Gatsby, 1984, To Kill a Mockingbird',
        is_published=False,
        priority=1, # Low
        category=ideas
    )

class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_category'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
