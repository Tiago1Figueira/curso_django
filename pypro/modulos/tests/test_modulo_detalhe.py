from django.urls.base import reverse
import pytest
# from model_mommy import mommy

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo
from model_bakery import baker


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def resp(client, modulo):
    resp = client.get(reverse('base:home'))
    return resp


def test_titulos_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_link_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.get_absolute_url())
