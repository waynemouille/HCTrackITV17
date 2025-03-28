# Generated by Django 5.1.6 on 2025-03-26 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='department',
            field=models.CharField(choices=[('', ''), ('356th District Court', '356th District Court'), ('88th Disctric Court', '88th District Court'), ('Agrilife Extension', 'Agrilife Extension'), ('Adult Probation', 'Adult Probation'), ('Auditor', 'Auditor'), ('Corrections', 'Corrections'), ('County Attorney', 'County Attorney'), ('County Clerk', 'County Clerk'), ('County Commissioner Precinct 1', 'County Commissioner Precinct 1'), ('County Commissioner Precinct 2', 'County Commissioner Precinct 2'), ('County Commissioner Precinct 3', 'County Commissioner Precinct 3'), ('County Commissioner Precinct 4', 'County Commissioner Precinct 4'), ('County Judge', 'County Judge'), ('Crime Victims Assistance', 'Crime Victims Assistance'), ('District Attorney', 'District Attorney'), ('District Clerk', 'District Clerk'), ('Elections', 'Elections'), ('Emergency Management', 'Emergency Management'), ('Flood Plain Administration', 'Flood Plain Administration'), ('Health Services', 'Health Services'), ('Human Resources', 'Human Resources'), ('Justice of the Peace Precinct 1', 'Justice of the Peace Precinct 1'), ('Justice of the Peace Precinct 2', 'Justice of the Peace Precinct 2'), ('Justice of the Peace Precinct 3', 'Justice of the Peace Precinct 3'), ('Justice of the Peace Precinct 4', 'Justice of the Peace Precinct 4'), ('Justice of the Peace Precinct 5', 'Justice of the Peace Precinct 5'), ('Justice of the Peace Precinct 6', 'Justice of the Peace Precinct 6'), ('Juvenile Probation', 'Juvenile Probation'), ('Maintenance', 'Maintenance'), ('Purchasing', 'Purchasing'), ("Sheriff's Office", "Sheriff's Office"), ('Tax-Assessor Collector', 'Tax-Assessor Collector'), ('Technology', 'Technology'), ('Treasurer', 'Treasurer'), ('Veterans Services', 'Veterans Services')], max_length=200),
        ),
    ]
