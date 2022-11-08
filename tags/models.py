from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    '''
     Class that enable filtering related Food Product instances
    '''
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label


class TaggedItem(models.Model):
    '''
        Class that enable tag relationship between the foodProduct object
    '''
    # Generic relation to other application
    ## Whats needed objectType and ID
    ### Query actual object tag is to be applied to
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

