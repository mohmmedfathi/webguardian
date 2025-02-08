import hashlib
import requests
from django.shortcuts import render
from .forms import BreachCheckForm
from django.conf import settings

def check_breaches(request):
    if request.method == 'POST':
        form = BreachCheckForm(request.POST)
        report = {}

        if form.is_valid():
            data = form.cleaned_data
            
            # Check Email via HIBP
            if data['email']:
                headers = {'hibp-api-key': settings.HIBP_API_KEY}
                response = requests.get(
                    f"https://haveibeenpwned.com/api/v3/breachedaccount/{data['email']}",
                    headers=headers
                )
                report['email_breaches'] = [b['Name'] for b in response.json()] if response.status_code == 200 else []

            # Check Password via HIBP
            if data['password']:
                hashed = hashlib.sha1(data['password'].encode()).hexdigest().upper()
                prefix, suffix = hashed[:5], hashed[5:]
                response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
                report['password_breach_count'] = next(
                    (int(line.split(':')[1]) for line in response.text.splitlines() if line.startswith(suffix)),
                    0
                )

            # Check Phone via LeakCheck
            if data['phone']:
                response = requests.get(
                    "https://leakcheck.io/api/public",
                    params={"key": settings.LEAKCHECK_API_KEY, "check": data['phone'], "type": "phone"}
                )
                report['phone_breaches'] = response.json().get('data', []) if response.status_code == 200 else []

            return render(request, 'checker/results.html', {'report': report})

    else:
        form = BreachCheckForm()

    return render(request, 'checker/check.html', {'form': form})