# -*- coding: utf-8 -*-
import time
import pytest
from credentials import Credentials
from application import Application
from mail import Mail


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_NewMail(app):
    app.login(Credentials(username="slyaquarius", password="Ykolomeicev1990"))
    app.field_and_send_message(Mail(email="slyaquarius@rambler.ru", subject="TEST SUBJECT"))
    time.sleep(1)
    app.logout()


def test_another_subject_Mail(app):
    app.login(Credentials(username="slyaquarius", password="Ykolomeicev1990"))
    app.field_and_send_message(Mail(email="slyaquarius@rambler.ru", subject="ALERT! ALERT!"))
    time.sleep(1)
    app.logout()

