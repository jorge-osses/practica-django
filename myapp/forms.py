from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Título de tarea", max_length=200)
    description = forms.CharField(
        widget=forms.Textarea, label="Descripción de la tarea", max_length=600)


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyecto", max_length=200)
