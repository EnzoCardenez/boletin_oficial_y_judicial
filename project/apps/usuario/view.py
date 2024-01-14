import requests

from django.http import JsonResponse
from django.conf import settings
from oauth2_provider.views import TokenView
from rest_framework import status


class CustomTokenView(TokenView):
    def post(self, request, *args, **kwargs):
        try:
            captcha_value = request.POST['captcha_value']
        except KeyError:
            return JsonResponse(
                data={'errors': [{"detail": "reCAPTCHA es obligatorio"}]},
                status=status.HTTP_400_BAD_REQUEST
            )

        url = 'https://www.google.com/recaptcha/api/siteverify'
        data = {'secret': settings.SECRET_KEY_CAPTCHA, 'response': captcha_value}

        try:
            response = requests.post(url=url, data=data)
            response.raise_for_status()
            response_json = response.json()
        except requests.RequestException as e:
            return JsonResponse(
                data={'errors': [{"detail": "Error en verificacion de reCAPTCHA"}]},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not response_json.get("success"):
            error_codes = response_json.get("error-codes", ["unknown_error"])
            return JsonResponse(
                data={'errors': [{"detail": f"reCAPTCHA inválido: {error_codes[0]}"}]},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().post(request, *args, **kwargs)
