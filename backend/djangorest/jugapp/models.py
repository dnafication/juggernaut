from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    "juggernaut: base model for common fields"
    created = models.DateTimeField(
        "created date", auto_now_add=True, 
        # default=timezone.now
        )
    updated = models.DateTimeField(
        "last updated", auto_now=True, 
        # default=timezone.now
        )
    author = models.CharField(max_length=50, default="author name")

    class Meta:
        abstract = True


class Script(BaseModel):
    "model for script list"
    STATUS_CHOICES = (
        (None, 'Unknown'),
        ('uploaded', 'Uploaded'),
        ('pip', 'Parse In Progress'),
        ('parsed', 'Parsed'),
        ('vip', 'Validation In Progress'),
        ('eip', 'Edit in Progress'),
        ('ready', 'Ready'),
    )
    name = models.CharField(
        max_length=25,
        unique=True,
        verbose_name='Script Name',
        error_messages={
            'blank': 'cant be blank',
            'invalid': 'invalid choice',
            'unique': 'it has to be unique, the name entered already exists'
        },
        help_text="Name of the script"
    )
    # file will be uploaded to MEDIA_ROOT/uploads
    script_upload = models.FileField(
        upload_to='uploads/',
        unique=True,
        verbose_name='Script Upload Location'
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=None,
        blank=True, null=True)
    version = models.IntegerField("script's version", blank=True, null=True)

    def __str__(self):
        return "Script: {}".format(self.name)


class Host(BaseModel):
    name = models.CharField(max_length=25, blank=True, null=True)
    ip_address = models.GenericIPAddressField(
        "Host IP Address", protocol="IPv4")
    is_active = models.BooleanField()

    def __str__(self):
        return "Host: {}".format(self.name)


class Test(BaseModel):
    STATUS_CHOICES = (
        (None, 'Unknown'),
        ('created', 'Created'),
        ('eip', 'Edit in Progress'),
        ('ready', 'Ready'),
        ('tip', 'Test In Progress'),
    )
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
        help_text="name of the test")
    scripts = models.ManyToManyField(
        Script, through='Mapping',
        through_fields=('test', 'script'))
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=None,
        blank=True, null=True
    )

    def __str__(self):
        return "Test: {}".format(self.name)


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


class ThreadGroup(BaseModel):
    "thred group details of the script after getting parsed"
    script = models.ForeignKey(Script, on_delete=models.CASCADE)

    # thread level attributes
    enabled = models.BooleanField(null=True)
    tg_name = models.CharField(max_length=30, blank=True, null=True)
    num_threads = models.IntegerField(blank=True, null=True)
    on_sample_error = models.CharField(max_length=10, blank=True, null=True)
    continue_forever = models.BooleanField(null=True)
    loops = models.CharField(max_length=6, blank=True, null=True)
    ramp_time = models.CharField(max_length=7, blank=True, null=True)
    scheduler = models.BooleanField(null=True)
    duration = models.CharField(max_length=7, blank=True, null=True)
    delay = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return "ThreadGroup details for {}: {}".format(self.script, self.tg_name)


class Argument(BaseModel):
    "user defined variables related to script after getting parsed"
    script = models.ForeignKey(Script, on_delete=models.CASCADE)

    argument_name = models.CharField(max_length=30, blank=True, null=True)
    key = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)
    metadata = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "Argument details for {}".format(self.script)


# class ScriptHostMapping(models.Model):
#     script = models.ForeignKey(Script, on_delete=models.CASCADE)
#     host = models.ForeignKey(Host, on_delete=models.CASCADE)
#     test = models.ForeignKey(Test, on_delete=models.CASCADE)

#     def __str__(self):
#         return "Mapping {} {}".format(self.script, self.host)
