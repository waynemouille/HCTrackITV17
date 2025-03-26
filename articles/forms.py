from django import forms
from .models import Article


class AddKnowledgebaseForm(forms.ModelForm):

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

    created_by = forms.ChoiceField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Created By')
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label='Title')
    category = forms.ChoiceField(required=True, widget=forms.Select(attrs={"placeholder":"", "class":"form-control"}), label='Knowledge Base Category', choices=CATEGORY_CHOICES)
    notes = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"", "class":"form-control"}), label='Notes')

    class Meta:
        model = Article
        fields = ('title', 'category', 'notes')




class UpdateKnowledgebaseForm(forms.ModelForm):


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


    created_by = forms.ChoiceField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Created By')
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label='Title')
    category = forms.ChoiceField(required=True, widget=forms.Select(attrs={"placeholder":"", "class":"form-control"}), label='Knowledge Base Category', choices=CATEGORY_CHOICES)
    notes = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"", "class":"form-control"}), label='Notes')

    

    class Meta:
        model = Article
        fields = fields = ('title', 'category', 'notes')

