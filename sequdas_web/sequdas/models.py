from django.db import models

class SequenceRun(models.Model):
    run_id = models.CharField(max_length=64)
    folder = models.CharField(max_length=256, blank=True)
    run_start_time = models.DateTimeField(auto_now=True, blank=True)
    run_end_time = models.DateTimeField(auto_now=True, blank=True)
    cluster_density = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    clusters_pf_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    reads_total = models.PositiveIntegerField(blank=True)
    reads_pf = models.PositiveIntegerField(blank=True)
    bases_greater_than_q30_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    class Meta:
        permissions = (
            ('view_sequence_run', 'View Sequence Run'),
        )    
    def __str__(self):
        return self.run_id

class ReadSummary(models.Model):
    sequence_run = models.ForeignKey(SequenceRun, on_delete=models.CASCADE, related_name='read_summaries')
    READ_TYPE_CHOICES = (
        ('READ_1', 'Read 1'),
        ('INDEX_1', 'Index 1'),
        ('INDEX_2', 'Index 2'),
        ('READ_2', 'Read 2'),
    )
    read_type = models.CharField(max_length=32, choices=READ_TYPE_CHOICES, blank=True)
    yield_gigabases = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    error_rate = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    bases_greater_than_q30_percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    def __str__(self):
        return (self.sequence_run.run_id + ": " + self.read_type)
    
class Sample(models.Model):
    sample_id = models.CharField(max_length=64)
    sample_name = models.CharField(max_length=64, blank=True)
    sequence_run = models.ForeignKey(SequenceRun, on_delete=models.CASCADE, related_name='samples')
    irida_project_id = models.CharField(max_length=64, blank=True)
    index_1_i7_seq = models.CharField(max_length=16, blank=True)
    index_2_i5_seq = models.CharField(max_length=16, blank=True)
    reads_identified_pf_percent = models.DecimalField(max_digits=6, decimal_places=4, blank=True)
    class Meta:
        permissions = (
            ('view_sample', 'View Sample'),
        )    
    def __str__(self):
        return (self.sequence_run.run_id + ": " + self.sample_id + "/" + self.sample_name)

