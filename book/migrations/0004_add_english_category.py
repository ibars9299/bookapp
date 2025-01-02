from django.db import migrations

def create_english_category(apps, schema_editor):
    Category = apps.get_model('book', 'Category')
    Category.objects.get_or_create(
        name='İngilizce',
        slug='ingilizce',
        icon='fa-language'  # Font Awesome dil ikonu
    )

def remove_english_category(apps, schema_editor):
    Category = apps.get_model('book', 'Category')
    Category.objects.filter(slug='ingilizce').delete()

class Migration(migrations.Migration):
    dependencies = [
        ('book', '0003_wordnote'),
    ]

    operations = [
        migrations.RunPython(create_english_category, remove_english_category),
    ] 