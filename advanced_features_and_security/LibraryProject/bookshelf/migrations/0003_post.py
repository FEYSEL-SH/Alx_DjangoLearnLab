# Generated by Django 5.1.2 on 2024-11-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'permissions': [('can_view', 'Can view post'), ('can_create', 'Can create post'), ('can_edit', 'Can edit post'), ('can_delete', 'Can delete post')],
            },
        ),
    ]
