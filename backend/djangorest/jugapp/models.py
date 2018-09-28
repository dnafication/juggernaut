from django.db import models


class Script(models.Model):
    name = models.CharField(
        max_length=25,
        unique=True,
        verbose_name='Script Name',
        error_messages={
            'blank': 'cant be blank',
            'invalid': 'invalid choice',
            'unique': 'it has to be unique, the name entered already exists'
        },
        help_text="name of the script"
    )
    # file will be uploaded to MEDIA_ROOT/uploads
    script_upload = models.FileField(
        upload_to='uploads/',
        unique=True,
        verbose_name='Script Upload Location'
    )
    version = models.IntegerField("Script's version", blank=True, null=True)

    def __str__(self):
        return self.name


class Host(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    ip_address = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(
        max_length=25,
        blank=False, null=False,
        unique=True,
        verbose_name='Test Name',
        error_messages={
            'blank': 'cant be blank',
            'invalid': 'invalid choice',
            'unique': 'the name entered already exists'
        },
        help_text="name of the test"
    )
    scripts = models.ManyToManyField(
        Script, through='Mapping',
        through_fields=('test', 'script'))

    def __str__(self):
        return self.name


class Mapping(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    script = models.ForeignKey(Script, on_delete=models.CASCADE)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    comment = models.CharField(max_length=25)
    settings = models.CharField(max_length=500)

    def __str__(self):
        return "Mapping for {} - {}".format(self.test, self.script)

    @property
    def mapping_name(self):
        "Returns the name given to the mapping "
        return "{} {}".format(self.script, self.host)


# class ScriptHostMapping(models.Model):
#     script = models.ForeignKey(Script, on_delete=models.CASCADE)
#     host = models.ForeignKey(Host, on_delete=models.CASCADE)
#     test = models.ForeignKey(Test, on_delete=models.CASCADE)

#     def __str__(self):
#         return "Mapping {} {}".format(self.script, self.host)
