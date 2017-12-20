from django.contrib import admin
from sequdas.models import SequenceRun, Sample, ReadSummary

admin.site.register(SequenceRun)
admin.site.register(Sample)
admin.site.register(ReadSummary)
