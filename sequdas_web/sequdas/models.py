from django.db import models

class SequenceRun(models.Model):
    run_id = models.CharField(max_length=64)
    folder = models.CharField(max_length=256, blank=True)
    run_start_time = models.DateTimeField(auto_now=True, blank=True)
    run_end_time = models.DateTimeField(auto_now=True, blank=True)
    cluster_density = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    clusters_pf = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    def __str__(self):
        return self.run_id

class Sample(models.Model):
    sample_id = models.CharField(max_length=64)
    sequence_run = models.ForeignKey(SequenceRun, on_delete=models.CASCADE, related_name='samples')
    irida_project_id = models.CharField(max_length=64, blank=True)
    def __str__(self):
        return (self.sequence_run.run_id + ": " + self.sample_id)

