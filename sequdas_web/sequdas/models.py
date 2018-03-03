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

class SampleSheet(models.Model):
    sequence_run = models.ForeignKey(SequenceRun, on_delete=models.CASCADE, related_name='sample_sheet', blank=True, null=True)
    path = models.CharField(max_length=256, blank=True)
    iem_file_version = models.CharField(max_length=8, blank=True)
    investigator_name = models.CharField(max_length=64, blank=True)
    project_name = models.CharField(max_length=64, blank=True)
    experiment_name = models.CharField(max_length=64, blank=True)
    date = models.DateField()
    workflow = models.CharField(max_length=64, blank=True)
    assay = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=64, blank=True)
    chemistry = models.CharField(max_length=64, blank=True)
    application = models.CharField(max_length=54, blank=True)
    read1_length = models.IntegerField()
    read2_length = models.IntegerField()
    reverse_complement = models.NullBooleanField()
    adapter = models.CharField(max_length=128, blank=True)
    adapter_read2 = models.CharField(max_length=128, blank=True)
    def __str__(self):
        return (str(self.date) + ": " + self.investigator_name + "/" + self.project_name)
    
class SampleSheetSample(models.Model):
    sample_sheet = models.ForeignKey(
        'SampleSheet',
        on_delete = models.CASCADE
    )
    sample_id = models.CharField(max_length=64)
    sample_name = models.CharField(max_length=64, blank=True)
    index_1_i7_seq = models.CharField(max_length=16, blank=True)
    index_2_i5_seq = models.CharField(max_length=16, blank=True)
    def __str__(self):
        return (str(self.sample_sheet) + "/" + self.sample_id)
