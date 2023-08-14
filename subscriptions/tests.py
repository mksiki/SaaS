from django.test import TestCase
from django.urls import reverse
import pytest
from users.models import User
from subscriptions.models import StripeCustomer
# Create your tests here.
def test_homepage_access():
    url = reverse('subscriptions-home')
    assert url == "/"


@pytest.mark.django_db
def test_create_checkout_session(client):
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.force_login(user)
    
    response = client.get(reverse('create-checkout-session'))
    assert response.status_code == 200
    assert 'sessionId' in response.json()
    assert StripeCustomer.objects.filter(user=user).exists()
