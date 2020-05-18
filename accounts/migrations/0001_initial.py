# Generated by Django 2.2.5 on 2020-04-21 18:38

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.IntegerField(default=0, verbose_name='Telefone')),
                ('birth_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data de Nascimento')),
                ('job_rule', models.CharField(blank=True, max_length=8, verbose_name='Cargo')),
                ('sex', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Nenhuma das opções')], max_length=1, verbose_name='Sexo')),
                ('user_type', models.CharField(choices=[('C', 'Cliente'), ('F', 'Funcionário')], default='C', max_length=1, verbose_name='Tipo de Usuário')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('zipcode', models.IntegerField(blank=True, default=0, null=True, verbose_name='CEP')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rua')),
                ('number', models.IntegerField(blank=True, default=0, null=True, verbose_name='Número')),
                ('complement', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('district', models.CharField(blank=True, max_length=30, null=True, verbose_name='Bairro')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='Cidade')),
                ('state', models.CharField(blank=True, max_length=2, null=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]