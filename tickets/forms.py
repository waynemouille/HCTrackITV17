from django import forms
from .models import Ticket


class AddTicketForm(forms.ModelForm):
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

    created_by = forms.ChoiceField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Created By')
    status = forms.CharField(required=True, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Status', initial="NEW")
    assignedto = forms.CharField(required=True, widget=forms.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='', initial="Unassigned")
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label='Name')
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label='Email')
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label='Phone')
    department = forms.ChoiceField(required=True, widget=forms.Select(attrs={"placeholder":"", "class":"form-control"}), label='Department', choices=DEPT_CHOICES)
    category = forms.ChoiceField(required=True, widget=forms.Select(attrs={"placeholder":"", "class":"form-control"}), label='Request Category', choices=CATEGORY_CHOICES)
    description = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"", "class":"form-control"}), label='Description')
    ongoing_notes = forms.CharField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='')
    completed_notes = forms.CharField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Completed Notes')

    class Meta:
        model = Ticket
        fields = ('status', 'assignedto', 'name', 'email', 'phone', 'department', 'category', 'description')




class UpdateTicketForm(forms.ModelForm):
    STATUS = (
        ("ASSIGNED / PENDING", "ASSIGNED / PENDING"),
        ("SCHEDULED", "SCHEDULED"),
        ("IN PROGRESS", "IN PROGRESS"),
        ("ON HOLD - User Unavailable", "ON HOLD - User Unavailable"),
        ("ON HOLD - Waiting on Parts", "ON HOLD - Waiting on Parts"),
        ("ON HOLD - Research", "ON HOLD - Research"),
        ("ON HOLD - Misc", "ON HOLD - Misc"),
    )

    ASSIGNED_TO = (
        ("Aaron Tupper", "Aaron Tupper"),
        ("Ethan Barnett", "Ethan Barnett"),
        ("Michael McConaghy", "Michael McConaghy"),
        ("Wayne Mouille", "Wayne Mouille"),
        ("Unassigned", "Unassigned"),
    )

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
                        ("Technology Project", "Technology Project"),
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
    #created_by = forms.CharField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Created By')
    status = forms.ChoiceField(required=True, widget=forms.widgets.Select(attrs={"placeholder":"", "class":"form-control"}), label='Status', choices=STATUS)
    assignedto = forms.ChoiceField(required=True, widget=forms.Select(attrs={"placeholder":"", "class":"form-control"}), label='Assigned To', choices=ASSIGNED_TO)
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label='Name')
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label='Email')
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label='Phone')
    department = forms.ChoiceField(required=True, widget=forms.Select(attrs={"placeholder":"", "class":"form-control"}), label='Department', choices=DEPT_CHOICES)
    category = forms.ChoiceField(required=True, widget=forms.Select(attrs={"placeholder":"", "class":"form-control"}), label='Request Category', choices=CATEGORY_CHOICES)
    description = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"", "class":"form-control"}), label='Description')
    ongoing_notes = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={"placeholder":"", "class":"form-control"}), label='Ongoing Notes')
    completed_notes = forms.CharField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Completed Notes')

    class Meta:
        model = Ticket
        fields = ('status', 'assignedto', 'name', 'email', 'phone', 'department', 'category', 'description', 'ongoing_notes')



class CompleteTicketForm(forms.ModelForm):
    
    STATUS = (
        ("COMPLETED", "COMPLETED"),
        ("CANCELLED", "CANCELLED"),
    )

    ASSIGNED_TO = (
        ("Aaron Tupper", "Aaron Tupper"),
        ("Ethan Barnett", "Ethan Barnett"),
        ("Michael McConaghy", "Michael McConaghy"),
        ("Wayne Mouille", "Wayne Mouille"),
        ("Unassigned", "Unassigned"),
    )

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
                        ("Technology Project", "Technology Project"),
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

    #created_by = forms.CharField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Created By')
    status = forms.ChoiceField(required=True, widget=forms.widgets.Select(attrs={"placeholder":"", "class":"form-control"}), label='Status', choices=STATUS)
    assignedto = forms.ChoiceField(required=True, widget=forms.Select(attrs={"placeholder":"", "class":"form-control"}), label='Assigned To', choices=ASSIGNED_TO)
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label='Name')
    email = forms.CharField(required=True, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Email')
    phone = forms.CharField(required=True, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Phone')
    department = forms.ChoiceField(required=True, widget=forms.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Department', choices=DEPT_CHOICES)
    category = forms.ChoiceField(required=True, widget=forms.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Request Category', choices=CATEGORY_CHOICES)
    description = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"", "class":"form-control"}), label='Description')
    ongoing_notes = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={"placeholder":"", "class":"form-control"}), label='Ongoing Notes')
    completed_notes = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"", "class":"form-control"}), label='Completed Notes')

    class Meta:
        model = Ticket
        fields = ('status', 'assignedto', 'name', 'email', 'phone', 'department', 'category', 'description', 'ongoing_notes', 'completed_notes')