from django.db import models


LOCALES = ((u'es_ES', u'es_ES'), (u'en_US', u'en_US'))


class Visit(models.Model):
    ip_address = models.IPAddressField(max_length=15)
    created_date = models.DateTimeField(auto_now_add=True)
    country = models.TextField()
    city = models.TextField()

    def __unicode__(self):
        return unicode(self.id) + " " + self.ip_address


class Question(models.Model):
    QUESTION_TYPES = (
        (u'M', u'Multiple Choice'),
        (u'T', u'Text Area'),
        (u'I', u'Text Input'),
    )
    q_type = models.CharField('Question Type', max_length=1, choices=QUESTION_TYPES)
    order = models.IntegerField()
    canonical = models.CharField(max_length=50)

    def __unicode__(self):
        return self.canonical


class Question_Text(models.Model):
    locale = models.CharField(max_length=5, choices=LOCALES)
    content = models.TextField()
    question = models.ForeignKey(Question)

    class Meta:
        verbose_name = "Question Text"
        verbose_name_plural = "Question Texts"

    def __unicode__(self):
        return self.content


class Option_Text(models.Model):
    locale = models.CharField(max_length=5)
    content = models.TextField()

    def __unicode__(self):
        return self.content


class Option(models.Model):
    question = models.ForeignKey(Question)
    order = models.IntegerField()
    canonical = models.CharField(max_length=50)
    texts = models.ManyToManyField(Option_Text)

    def __unicode__(self):
        return self.canonical


class Answer(models.Model):
    visit = models.ForeignKey(Visit)
    question = models.ForeignKey(Question)
    text_area = models.TextField()
    text_field = models.CharField(max_length=3)
    selected = models.ForeignKey(Option)

    def __unicode__(self):
        return unicode(self.id)
