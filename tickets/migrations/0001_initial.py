# Generated by Django 5.1.6 on 2025-03-05 21:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='NEW', max_length=50)),
                ('assignedto', models.CharField(default='Unassigned', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('completed_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('department', models.CharField(choices=[('', ''), ('356th District Court', '356th District Court'), ('88th Disctric Court', '88th District Court'), ('Agrilife Extension', 'Agrilife Extension'), ('Adult Probation', 'Adult Probation'), ('Auditor', 'Auditor'), ('Corrections', 'Corrections'), ('County Attorney', 'County Attorney'), ('County Clerk', 'County Clerk'), ('County Commissioner Precinct 1', 'County Commissioner Precinct 1'), ('County Commissioner Precinct 2', 'County Commissioner Precinct 2'), ('County Commissioner Precinct 3', 'County Commissioner Precinct 3'), ('County Commissioner Precinct 4', 'County Commissioner Precinct 4'), ('County Judge', 'County Judge'), ('Crime Victims Assistance', 'Crime Victims Assistance'), ('District Attorney', 'District Attorney'), ('District Clerk', 'District Clerk'), ('Elections', 'Elections'), ('Emergency Management', 'Emergency Management'), ('Flood Plain Administration', 'Flood Plain Administration'), ('Health Services', 'Health Services'), ('Human Resources', 'Human Resources'), ('Justice of the Peace Precinct 1', 'Justice of the Peace Precinct 1'), ('Justice of the Peace Precinct 2', 'Justice of the Peace Precinct 2'), ('Justice of the Peace Precinct 3', 'Justice of the Peace Precinct 3'), ('Justice of the Peace Precinct 4', 'Justice of the Peace Precinct 4'), ('Justice of the Peace Precinct 5', 'Justice of the Peace Precinct 5'), ('Justice of the Peace Precinct 6', 'Justice of the Peace Precinct 6'), ('Juvenile Probation', 'Juvenile Probation'), ('Purchasing', 'Purchasing'), ("Sheriff's Office", "Sheriff's Office"), ('Tax-Assessor Collector', 'Tax-Assessor Collector'), ('Technology', 'Technology'), ('Treasurer', 'Treasurer'), ('Veterans Services', 'Veterans Services')], max_length=200)),
                ('category', models.CharField(choices=[('', ''), ('Audio/Visual Equipment', 'Audio/Visual Equipment'), ('Copier', 'Copier'), ('Fax', 'Fax'), ('Hardware', 'Hardware'), ('Move Equipment Request', 'Move Equipment Request'), ('New Equipment Request', 'New Equipment Request'), ('Other', 'Other'), ('Printer', 'Printer'), ('Radios', 'Radios'), ('Security Cameras', 'Security Cameras'), ('Scanner', 'Scanner'), ('', ''), ('Connectivity - Network', 'Connectivity - Network'), ('Connectivity - Sonic Wall', 'Connectivity - Sonic Wall'), ('Connectivity - VPN', 'Connectivity - VPN'), ('', ''), ('Cyber Security - Suspicious Email', 'Cyber Security - Suspicious Email'), ('Cyber Security - Virus', 'Cyber Security - Virus'), ('', ''), ('Phone - Desk Phone', 'Desk Phone'), ('Phone - Mobile Phone', 'Mobile Phone'), ('', ''), ('Software - CAD', 'Software - CAD'), ('Software - DW Spectrum', 'Software - DW Spectrum'), ('Software - EDOC', 'Software - EDOC'), ('Software - Email', 'Software - Email'), ('Software - Internet Browser', 'Software - Internet Browser'), ('Software - JMS', 'Software - JMS'), ('Software - LGS', 'Software - LGS'), ('Software - MDIS', 'Software - MDIS'), ('Software - NetData', 'Software - NetData'), ('Software - Office', 'Software - Office'), ('Software - RMS', 'Software - RMS'), ('Software - Watchguard', 'Software - Watchguard'), ('Software - Other', 'Software - Other'), ('', ''), ('User Access - Controlled Access', 'User Access - Controlled Access'), ('User Access - Create New User', 'User Access - Create New User'), ('User Access - Network Access', 'User Access - Network Access'), ('User Access - Remove User', 'User Access - Remove User')], max_length=200)),
                ('description', models.TextField(max_length=3000)),
                ('ongoing_notes', models.TextField(blank=True, max_length=3000)),
                ('completed_notes', models.TextField(blank=True, max_length=3000)),
                ('created_by', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
