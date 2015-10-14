# -*- coding: utf-8 -*-

from django.db import models

# Create your model here.
class Exam(models.Model):
    """Exams Model"""

    class Meta(object):
        verbose_name = u"Екзамен"
        verbose_name_plural = u"Екзамени"

    course = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Предмет")

    lecturer = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Викладач")

    exam_group = models.ForeignKey('Group',
        verbose_name=u"Група",
        blank=False,
        null=True,
        on_delete=models.PROTECT)

    exam_date = models.DateTimeField(
		blank=False,
		verbose_name=u"Дата та час",
		null=True)

    def __unicode__(self):
        return u"предмет: %s, викладач: %s" % (self.course, self.lecturer)
