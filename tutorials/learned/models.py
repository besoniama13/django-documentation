from django.utils.translation import gettext_lazy as _
from django.db import models


class Content(models.Model):

    date_learned = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=100)
    subheading = models.TextField()
    footer = models.TextField()

    def __str__(self):
        return self.heading

class Step(models.Model):

    step_number = models.PositiveSmallIntegerField(default=1)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    step_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["step_number"]

    def __str__(self):
        return str(self.step_number) + " " + self.step_name

class Paragraph(models.Model):

    class TextType(models.TextChoices):
        NORMAL = 'NM', _('NORMAL')
        CODE = 'CD', _('CODE')
        BULLET = 'BU', _('BULLET')
        NOTE = 'NT', _('NOTE')

    class Meta:
        ordering = ["order"]
    head = models.CharField(max_length=100)
    order = models.PositiveSmallIntegerField(default=1)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    text = models.TextField()
    text_type = models.CharField(
            max_length=2,
            choices=TextType.choices,
            default=TextType.NORMAL,
            )

    def __str__(self):
        return str(self.order) + " " + self.text
