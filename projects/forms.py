from django import forms
from .models import Project


class AddProjectForm(forms.ModelForm):


    ASSIGNED_TO = (
        ("", ""),
        ("Aaron Tupper", "Aaron Tupper"),
        ("Ethan Barnett", "Ethan Barnett"),
        ("Michael McConaghy", "Michael McConaghy"),
        ("Wayne Mouille", "Wayne Mouille"),
        ("Unassigned", "Unassigned"),
    )
    
    created_by = forms.ChoiceField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Created By')
    progress = forms.CharField(required=True, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Status', initial="0%")
    assignedto = forms.ChoiceField(required=True, widget=forms.Select(attrs={"placeholder":"", "class":"form-control"}), label='Assigned To', choices=ASSIGNED_TO)
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label='Name')
    description = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"", "class":"form-control"}), label='Description')
    ongoing_notes = forms.CharField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='')
    completed_notes = forms.CharField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Completed Notes')

    class Meta:
        model = Project
        fields = ('progress', 'assignedto', 'name', 'description')




class UpdateProjectForm(forms.ModelForm):
    PROGRESS_CHOICES = (
                        ("", ""),
                        ("0%", "0%"),
                        ("10%", "10%"),
                        ("20%", "20%"),
                        ("30%", "30%"),
                        ("40%", "40%"),
                        ("50%", "50%"),
                        ("60%", "60%"),
                        ("70%", "70%"),
                        ("80%", "80%"),
                        ("90%", "90%"),
                        ("COMPLETED", "COMPLETED"),
    )

    ASSIGNED_TO = (
        ("", ""),
        ("Aaron Tupper", "Aaron Tupper"),
        ("Ethan Barnett", "Ethan Barnett"),
        ("Michael McConaghy", "Michael McConaghy"),
        ("Wayne Mouille", "Wayne Mouille"),
        ("Unassigned", "Unassigned"),
    )


    #created_by = forms.CharField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Created By')
    progress = forms.ChoiceField(required=True, widget=forms.widgets.Select(attrs={"placeholder":"", "class":"form-control"}), label='Status', choices=PROGRESS_CHOICES)
    assignedto = forms.ChoiceField(required=True, widget=forms.Select(attrs={"placeholder":"", "class":"form-control"}), label='Assigned To', choices=ASSIGNED_TO)
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label='Name')
    description = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"", "class":"form-control"}), label='Description')
    ongoing_notes = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={"placeholder":"", "class":"form-control"}), label='Ongoing Notes')
    completed_notes = forms.CharField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Completed Notes')

    class Meta:
        model = Project
        fields = ('progress', 'assignedto', 'name', 'description', 'ongoing_notes')



class CompleteProjectForm(forms.ModelForm):
    PROGRESS_CHOICES = (
        ("100%", "100%"),
        ("CANCELLED", "CANCELLED"),
    )

    ASSIGNED_TO = (
        ("", ""),
        ("Aaron Tupper", "Aaron Tupper"),
        ("Ethan Barnett", "Ethan Barnett"),
        ("Michael McConaghy", "Michael McConaghy"),
        ("Wayne Mouille", "Wayne Mouille"),
        ("Unassigned", "Unassigned"),
    )


    #created_by = forms.CharField(required=False, widget=forms.widgets.HiddenInput(attrs={"placeholder":"", "class":"form-control"}), label='Created By')
    progress = forms.ChoiceField(required=True, widget=forms.widgets.Select(attrs={"placeholder":"", "class":"form-control"}), label='Progress', choices=PROGRESS_CHOICES)
    assignedto = forms.ChoiceField(required=True, widget=forms.Select(attrs={"placeholder":"", "class":"form-control"}), label='Assigned To', choices=ASSIGNED_TO)
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label='Name')
    description = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"", "class":"form-control"}), label='Description')
    ongoing_notes = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={"placeholder":"", "class":"form-control"}), label='Ongoing Notes')
    completed_notes = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"", "class":"form-control"}), label='Completed Notes')

    class Meta:
        model = Project
        fields = ('progress', 'assignedto', 'name', 'description', 'ongoing_notes', 'completed_notes')