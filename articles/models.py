from django.db import models
from django.contrib.auth.models import User




class Article(models.Model):

    CATEGORY_CHOICES = (
                        ("", ""),
                        ("Audio/Visual Equipment", "Audio/Visual Equipment"),
                        ("Backup", "Backup"),
                        ("Copier", "Copier"),
                        ("Fax", "Fax"),
                        ("Hardware", "Hardware"),
                        ("Other", "Other"),
                        ("Printer", "Printer"),
                        ("Radios", "Radios"),
                        ("Security Cameras", "Security Cameras"),
                        ("Server", "Server"),
                        ("Scanner", "Scanner"),
                        ("", ""),
                        ("Connectivity - Network", "Connectivity - Network"),
                        ("Connectivity - Sonic Wall", "Connectivity - Sonic Wall"),
                        ("Connectivity - VPN", "Connectivity - VPN"),
                        ("", ""),
                        ("Cyber Security", "Cyber Security"),
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
    )
        
    created_by = models.ForeignKey(User, default=None, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    notes = models.TextField(max_length=5000)


    def __str__(self):
        return self.title