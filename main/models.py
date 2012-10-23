#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm, TextInput
from django.utils.translation import ugettext_lazy as _


TIME_MANAGING = (
    (u'01', _(u'Menos de 1 Hora')),
    (u'02', _(u'Entre 1 y 2 Horas')),
    (u'03', _(u'Más de 2 Horas')),
)

BOOLEAN_OP = (
    (u'Y', _(u'Si')),
    (u'N', _(u'No')),
)

BOOLEAN_OP2 = (
    (u'Y', _(u'Si')),
    (u'N', _(u'No')),
    (u'I', _(u'Indiferente')),
)

CHARGE_MODES = (
    (u'01', _(u'Por horas')),
    (u'02', _(u'Por asunto')),
    (u'03', _(u'Por trámite')),
    (u'04', _(u'Por cuota mensual/retainer')),
)

TIME_KEEPER = (
    (u'01', _(u'Yo mismo')),
    (u'02', _(u'Mi asistente/secretaria')),
    (u'03', _(u'Mi jefe/supervisor')),
)

QUESTIONS_TEXTS = {
    "Q01": _(u"Aproximadamente, ¿Cuánto tiempo le dedicas diariamente a organizar tus documentos y tu agenda?"),
    "Q02": _(u"¿Quién gestiona principalmente tu agenda?"),
    "Q03": _(u"¿Utilizas o has utilizado alguna herramienta informática que te ayude a gestionar tu práctica (tiempos, expedientes, etc.)?"),
    "Q04": _(u"En caso afirmativo, ¿Cúal(es)?"),
    "Q05": _(u"¿Cuál dirías que es la principal deficiencia de estos sistemas?"),
    "Q06": _(u"Si pudieras automatizar cualquier aspecto de tu trabajo, ¿cuál sería?"),
    "Q07": _(u"¿De qué forma sueles facturar tu trabajo?"),
    "Q08": _(u"¿Tienes control efectivo del tiempo/dinero que inviertes en cada cliente?"),
    "Q09": _(u"¿Cuántos abogados trabajan en tu despacho?"),
    "Q10": _(u"¿Te parecería valioso poder visualizar gráficamente el estado de tus asuntos?"),
}


class Visit(models.Model):
    class Meta:
        verbose_name = _('Visita')
        verbose_name_plural = _('Visitas')
    referer = models.CharField(max_length=2083, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    #city = models.TextField()
    city = models.CharField(max_length=50, blank=True, null=True)
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
        exclude = ('referer', 'country', 'city', )


class Contact(models.Model):
    class Meta:
        verbose_name = _('Contacto')
        verbose_name_plural = _('Contactos')
    email = models.EmailField('e-mail')

    def __unicode__(self):
        return unicode(self.email)


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'email': TextInput(attrs={'placeholder': 'E-mail'}),
        }
