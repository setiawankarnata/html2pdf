from django.shortcuts import render
from .models import Participant, Topic, Venue
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile


def home(request):
    return render(request, 'index.html')


def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=MoM.pdf'
    response['Context-Transfer-Encoding'] = 'binary'
    venue = Venue.objects.get(pk=1)
    participants = Participant.objects.all()
    topiks = Topic.objects.all()
    context = {
        'venue': venue,
        'participants': participants,
        'topiks': topiks,
    }
    html_string = render_to_string('mom.html', context)
    html = HTML(string=html_string)
    result = html.write_pdf()
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response
