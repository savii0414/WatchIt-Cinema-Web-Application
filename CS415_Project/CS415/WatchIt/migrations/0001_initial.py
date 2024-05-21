# Generated by Django 5.0.6 on 2024-05-21 07:59

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinema_type', models.CharField(blank=True, max_length=100, null=True)),
                ('num_rows', models.IntegerField(blank=True, null=True)),
                ('num_cols', models.IntegerField(blank=True, null=True)),
                ('adult_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('child_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Meal', models.CharField(blank=True, max_length=255, null=True)),
                ('Price', models.FloatField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='deals_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.IntegerField(blank=True, help_text='Duration in minutes', null=True)),
                ('starring', models.TextField(blank=True, help_text='Comma-separated list of main actors', null=True)),
                ('director', models.TextField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('ageRating', models.CharField(blank=True, max_length=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='movie_images/')),
                ('trailer', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showtime', models.DateTimeField()),
                ('seats_generated', models.BooleanField(default=False)),
                ('cinema_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='showtimes', to='WatchIt.cinemahall')),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='showtimes', to='WatchIt.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_label', models.CharField(blank=True, max_length=3, null=True)),
                ('availability', models.BooleanField(default=True)),
                ('showtime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='WatchIt.showtime')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=models.ManyToManyField(related_name='movies', to='WatchIt.tag'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_email_verified', models.BooleanField(default=False)),
                ('secret_key', models.CharField(blank=True, max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PasswordResetToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('used', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('payment_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('num_seats', models.PositiveIntegerField(default=1)),
                ('edited', models.BooleanField(default=False)),
                ('charge_id', models.CharField(blank=True, max_length=255, null=True)),
                ('card_last4', models.CharField(blank=True, max_length=4, null=True)),
                ('cinema_hall', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='WatchIt.cinemahall')),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='WatchIt.movie')),
                ('seats', models.ManyToManyField(related_name='bookings', to='WatchIt.seat')),
                ('showtime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='WatchIt.showtime')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
