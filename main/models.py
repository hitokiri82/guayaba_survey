#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm, TextInput


TIMES_OF_DAY = (
    (u'01', u'Mañana'),
    (u'02', u'Tarde'),
)

TIME_MANAGING = (
    (u'01', u'Menos de 1 Hora'),
    (u'02', u'Menos de 3 Horas'),
    (u'03', u'Mas de 3 Horas'),
)

BOOLEAN_OP = (
    (u'Y', u'Si'),
    (u'N', u'No'),
)

CHARGE_MODES = (
    (u'01', u'Por horas'),
    (u'02', u'Por asunto'),
    (u'03', u'Por retainer'),
)

TIME_KEEPER = (
    (u'01', u'Yo mismo'),
    (u'02', u'Mi asistente/secretaria'),
    (u'03', u'Mi jefe/supervisor'),
)

QUESTIONS_TEXTS = {
    "Q01": "Cuáles cree usted que son las horas más productivas de su jornada laboral?",
    "Q02": "Por qué?",
    "Q03": "Qué tiempo aproximado dedica diariamente a organizar documentos, expedientes y su agenda?",
    "Q04": "Quien gestiona su agenda?",
    "Q05": "Utiliza o ha utilizado alguna herramienta informática que le ayude a gestionar su tiempo?",
    "Q06": "Qué aspecto de su trabajo considera que puede mejorar?",
    "Q07": "De qué forma suele facturar su trabajo?",
    "Q08": "Tiene usted control efectivo del tiempo/dinero que invierte en cada cliente?",
    "Q09": "Cuántos abogados trabajan en su despacho?",
}


class Visit(models.Model):
    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'

    ip_address = models.IPAddressField(max_length=15)
    created_date = models.DateTimeField(auto_now_add=True)
    country = models.TextField()
    city = models.TextField()
    q01 = models.CharField(QUESTIONS_TEXTS['Q01'], max_length=2, choices=TIMES_OF_DAY, blank=True, null=True)
    q02 = models.TextField(QUESTIONS_TEXTS['Q02'], blank=True, null=True)
    q03 = models.CharField(QUESTIONS_TEXTS['Q03'], max_length=2, choices=TIME_MANAGING, blank=True, null=True)
    q04 = models.CharField(QUESTIONS_TEXTS['Q04'], max_length=1, choices=TIME_KEEPER, blank=True, null=True)
    q05 = models.CharField(QUESTIONS_TEXTS['Q05'], max_length=1, choices=BOOLEAN_OP, blank=True, null=True)
    q06 = models.TextField(QUESTIONS_TEXTS['Q06'], blank=True, null=True)
    q07 = models.CharField(QUESTIONS_TEXTS['Q07'], max_length=2, choices=CHARGE_MODES, blank=True, null=True)
    q08 = models.CharField(QUESTIONS_TEXTS['Q08'], max_length=1, choices=BOOLEAN_OP, blank=True, null=True)
    q09 = models.IntegerField(QUESTIONS_TEXTS['Q09'], blank=True, null=True)

    def __unicode__(self):
        return unicode(self.id) + " " + self.ip_address


class VisitForm(ModelForm):
    class Meta:
        model = Visit
        exclude = ('ip_address', 'country', 'city', )


class Contact(models.Model):
    class Meta:
        verbose_name = 'Contacto'
    email = models.EmailField('e-mail')

    def __unicode__(self):
        pass


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'email': TextInput(attrs={'placeholder': 'E-mail'}),
        }
