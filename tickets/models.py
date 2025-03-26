from django.db import models
from django.contrib.auth.models import User




class Ticket(models.Model):

    DEPT_CHOICES = (
                        ("", ""),
                        ("356th District Court", "356th District Court"),
                        ("88th Disctric Court", "88th District Court"),
                        ("Agrilife Extension", "Agrilife Extension"),
                        ("Adult Probation", "Adult Probation"),
                        ("Auditor", "Auditor"),
                        ("Corrections", "Corrections"),
                        ("County Attorney", "County Attorney"),
                        ("County Clerk", "County Clerk"),
                        ("County Commissioner Precinct 1", "County Commissioner Precinct 1"),
                        ("County Commissioner Precinct 2", "County Commissioner Precinct 2"),
                        ("County Commissioner Precinct 3", "County Commissioner Precinct 3"),
                        ("County Commissioner Precinct 4", "County Commissioner Precinct 4"),
                        ("County Judge", "County Judge"),
                        ("Crime Victims Assistance", "Crime Victims Assistance"),
                        ("District Attorney", "District Attorney"),
                        ("District Clerk", "District Clerk"),
                        ("Elections", "Elections"),
                        ("Emergency Management", "Emergency Management"),
                        ("Flood Plain Administration", "Flood Plain Administration"),
                        ("Health Services", "Health Services"),
                        ("Human Resources", "Human Resources"),
                        ("Justice of the Peace Precinct 1", "Justice of the Peace Precinct 1"),
                        ("Justice of the Peace Precinct 2", "Justice of the Peace Precinct 2"),
                        ("Justice of the Peace Precinct 3", "Justice of the Peace Precinct 3"),
                        ("Justice of the Peace Precinct 4", "Justice of the Peace Precinct 4"),
                        ("Justice of the Peace Precinct 5", "Justice of the Peace Precinct 5"),
                        ("Justice of the Peace Precinct 6", "Justice of the Peace Precinct 6"),
                        ("Juvenile Probation", "Juvenile Probation"),
                        ("Maintenance", "Maintenance"),
                        ("Purchasing", "Purchasing"),
                        ("Sheriff's Office", "Sheriff's Office"),
                        ("Tax-Assessor Collector", "Tax-Assessor Collector"),
                        ("Technology", "Technology"),
                        ("Treasurer", "Treasurer"),
                        ("Veterans Services", "Veterans Services"),
    )

    CATEGORY_CHOICES = (
                        ("", ""),
                        ("Audio/Visual Equipment", "Audio/Visual Equipment"),
                        ("Copier", "Copier"),
                        ("Fax", "Fax"),
                        ("Hardware", "Hardware"),
                        ("Move Equipment Request", "Move Equipment Request"),
                        ("New Equipment Request", "New Equipment Request"),
                        ("Other", "Other"),
                        ("Printer", "Printer"),
                        ("Radios", "Radios"),
                        ("Security Cameras", "Security Cameras"),
                        ("Scanner", "Scanner"),
                        ("", ""),
                        ("Connectivity - Network", "Connectivity - Network"),
                        ("Connectivity - Sonic Wall", "Connectivity - Sonic Wall"),
                        ("Connectivity - VPN", "Connectivity - VPN"),
                        ("", ""),
                        ("Cyber Security - Suspicious Email", "Cyber Security - Suspicious Email"),
                        ("Cyber Security - Virus", "Cyber Security - Virus"),
                        ("", ""),
                        ("Phone - Desk Phone", "Desk Phone"),
                        ("Phone - Mobile Phone", "Mobile Phone"),
                        ("", ""),
                        ("Software - CAD", "Software - CAD"),
                        ("Software - DW Spectrum", "Software - DW Spectrum"),
                        ("Software - EDOC", "Software - EDOC"),
                        ("Software - Email", "Software - Email"),
                        ("Software - Internet Browser", "Software - Internet Browser"),
                        ("Software - JMS", "Software - JMS"),
                        ("Software - LGS", "Software - LGS"),
                        ("Software - MDIS", "Software - MDIS"),
                        ("Software - NetData", "Software - NetData"),
                        ("Software - Office", "Software - Office"),
                        ("Software - RMS", "Software - RMS"),
                        ("Software - Watchguard", "Software - Watchguard"),
                        ("Software - Other", "Software - Other"),
                        ("", ""),
                        ("User Access - Controlled Access", "User Access - Controlled Access"),
                        ("User Access - Create New User", "User Access - Create New User"),
                        ("User Access - Network Access", "User Access - Network Access"),
                        ("User Access - Remove User", "User Access - Remove User"),
    )

    created_by = models.ForeignKey(User, default=None, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="NEW")
    assignedto = models.CharField(max_length=50, default="Unassigned")
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=200, choices=DEPT_CHOICES)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    description = models.TextField(max_length=3000)
    ongoing_notes = models.TextField(max_length=3000, blank=True)
    completed_notes = models.TextField(max_length=3000, blank=True)

    def __str__(self):
        return self.name




