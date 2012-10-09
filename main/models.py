#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm, TextInput


TIME_MANAGING = (
    (u'01', u'Menos de 1 Hora'),
    (u'02', u'Entre 1 y 2 Horas'),
    (u'03', u'Más de 2 Horas'),
)

BOOLEAN_OP = (
    (u'Y', u'Si'),
    (u'N', u'No'),
)

BOOLEAN_OP2 = (
    (u'Y', u'Si'),
    (u'N', u'No'),
    (u'I', u'Indiferente'),
)

CHARGE_MODES = (
    (u'01', u'Por horas'),
    (u'02', u'Por asunto'),
    (u'03', u'Por trámite'),
    (u'04', u'Por cuota mensual/retainer'),
)

TIME_KEEPER = (
    (u'01', u'Yo mismo'),
    (u'02', u'Mi asistente/secretaria'),
    (u'03', u'Mi jefe/supervisor'),
)

QUESTIONS_TEXTS = {
    "Q01": "Aproximadamente, ¿Cuánto tiempo le dedicas diariamente a organizar tus documentos y tu agenda?",
    "Q02": "¿Quién gestiona principalmente tu agenda?",
    "Q03": "¿Utilizas o has utilizado alguna herramienta informática que te ayude a gestionar tu practica (tiempos, expedientes, etc.)?",
    "Q04": "En caso afirmativo, ¿Cúal(es)?",
    "Q05": "¿Cuál dirías que es la principal deficiencia de estos sistemas?",
    "Q06": "Si pudieras automatizar cualquier aspecto de tu trabajo, ¿cuál sería?",
    "Q07": "¿De qué forma sueles facturar tu trabajo?",
    "Q08": "¿Tienes control efectivo del tiempo/dinero que inviertes en cada cliente?",
    "Q09": "¿Cuántos abogados trabajan en tu despacho?",
    "Q10": "¿Te parecería valioso poder visualizar gráficamente el estado de tus asuntos?",
}


class Visit(models.Model):
    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'

    created_date = models.DateTimeField(auto_now_add=True)
    country = models.TextField()
    city = models.TextField()
    q01 = models.CharField(QUESTIONS_TEXTS['Q01'], max_length=2, choices=TIME_MANAGING, blank=True, null=True)
    q02 = models.CharField(QUESTIONS_TEXTS['Q02'], max_length=2, choices=TIME_KEEPER, blank=True, null=True)
    q03 = models.CharField(QUESTIONS_TEXTS['Q03'], max_length=1, choices=BOOLEAN_OP, blank=True, null=True)
    q04 = models.CharField(QUESTIONS_TEXTS['Q04'], max_length=50, blank=True, null=True)
    q05 = models.TextField(QUESTIONS_TEXTS['Q05'], blank=True, null=True)
    q06 = models.TextField(QUESTIONS_TEXTS['Q06'], blank=True, null=True)
    q07 = models.CharField(QUESTIONS_TEXTS['Q07'], max_length=2, choices=CHARGE_MODES, blank=True, null=True)
    q08 = models.CharField(QUESTIONS_TEXTS['Q08'], max_length=1, choices=BOOLEAN_OP, blank=True, null=True)
    q09 = models.IntegerField(QUESTIONS_TEXTS['Q09'], blank=True, null=True)
    q10 = models.CharField(QUESTIONS_TEXTS['Q10'], max_length=1, choices=BOOLEAN_OP2, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.id)


class VisitForm(ModelForm):
    class Meta:
        model = Visit
        exclude = ('ip_address', 'country', 'city', )


class Contact(models.Model):
    class Meta:
        verbose_name = 'Contacto'
    email = models.EmailField('e-mail')

    def __unicode__(self):
        return unicode(self.email)


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'email': TextInput(attrs={'placeholder': 'E-mail'}),
        }
