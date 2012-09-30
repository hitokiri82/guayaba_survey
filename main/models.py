from django.db import models


class Visit(models.Model):
    ip_address = models.IPAddressField(max_length=15)
    created_date = models.DateTimeField(auto_now_add=True)
    country = models.TextField()
    city = models.TextField()

    def __unicode__(self):
        return str(self.id) + " " + self.ip_address


class Text(models.Model):
    comp_pk = models.CharField(max_length=8, primary_key=True)
    id = models.CharField(max_length=3)
    locale = models.CharField(max_length=5)
    content = models.TextField()

    def __unicode__(self):
        return str(self.id)


class Question(models.Model):
    QUESTION_TYPES = (
        (u'M', u'Multiple Choice'),
        (u'T', u'Text Area'),
        (u'I', u'Text Input'),
    )
    q_type = models.CharField('Question Type', max_length=1, choices=QUESTION_TYPES)
    order = models.IntegerField()
    textID = models.ForeignKey(Text, verbose_name="Text of the question")

    def __unicode__(self):
        return str(self.id)


class Option(models.Model):
    question = models.ForeignKey(Question)
    textID = models.ForeignKey(Text, verbose_name="Text of the option")
    order = models.IntegerField()

    def __unicode__(self):
        return str(self.id)


class Answer(models.Model):
    visit = models.ForeignKey(Visit)
    question = models.ForeignKey(Question)
    text_area = models.TextField()
    text_field = models.CharField(max_length=3)
    selected = models.CharField(max_length=2)

    def __unicode__(self):
        return str(self.id)
