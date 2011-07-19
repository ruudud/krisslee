from django.db import models

class Picture(models.Model):
    url = models.CharField(max_length=200)
    text = models.CharField(max_length=200, help_text='Used for alt attrib',
                            blank=True, null=True)

    def __unicode__(self):
        return self.text or self.url
