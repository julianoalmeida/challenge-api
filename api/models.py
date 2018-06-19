from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from rest_framework.reverse import reverse


class Patient(models.Model):
    """This class represents the patient model."""
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = u'Patient'
        verbose_name_plural = u'Patients'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Procedure(models.Model):
    """This class represents the procedure model."""
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = u'Procedure'
        verbose_name_plural = u'Procedures'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


def validate_date(data):
    if data <= timezone.now().date():
        raise ValidationError('the scheduling can not be created with the date less than today!')


class Scheduling(models.Model):
    """This class represents the scheduling model."""
    date = models.DateField(validators=[validate_date], default=timezone.now)
    initial_time = models.TimeField(default=timezone.now, null=False)
    final_time = models.TimeField(default=timezone.now, null=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False, blank=False)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        unique_together = ('date', 'procedure', 'patient')
        ordering = ['date']
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Schedules'

    def __unicode__(self):
        return '%d: %s' % (self.patient, self.procedure)

    def get_api_url(self, request=None):
        return reverse("scheduling-detail", kwargs={'pk': self.pk}, request=request)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return self.date
