from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string


def enviar_email(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        destinatario = request.POST.get('email')

        body = render_to_string('core/email.txt', {'nome': nome, 'email': destinatario})

        send_mail(
            nome,
            body,
            'dosimagem.server@gmail.com',
            [destinatario],
        )

        return HttpResponse('E-mail enviado com sucesso!')

    return render(request, "core/index.html")
