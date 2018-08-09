from django.db import models
from django.forms import ModelForm

class Jmx(models.Model):
    name = models.CharField(max_length=255)
    jmxfile = models.FileField(upload_to='jmxes/uploaded')
    date_added = models.DateTimeField('date added', auto_now=True)
    date_updated = models.DateTimeField('date updated', null=True)
    updated_jmxfile = models.FileField(upload_to='jmxes/uploaded', null=True)

    def __str__(self):
        return "{}: {}".format(self.name, self.jmxfile)

class JmxForm(ModelForm):
    class Meta:
        model = Jmx
        fields = ['name', 'jmxfile']