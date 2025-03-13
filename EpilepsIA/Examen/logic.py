

from EpilepsIA.Examen.models import EEG


def get_miRNA():
    pass

def post_miRNA():
    pass

def get_MRI():
    pass

def post_MRI():
    pass

def get_EEG():
    queryset = EEG.objects.all()
    return (queryset)

def post_EEG(form):
    exam = form.save()
    exam.save()
