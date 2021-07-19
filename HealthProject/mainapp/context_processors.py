
from .models import Department,Doctor,Patient

def menu_links(request):
    links=Department.objects.all()
    return dict(links=links)
def doc_links(request):
    docs=Doctor.objects.all()
    return dict(docs=docs)

