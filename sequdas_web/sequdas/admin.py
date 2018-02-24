from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from sequdas.models import SequenceRun
from sequdas.models import Sample
from sequdas.models import ReadSummary
from sequdas.models import SampleSheet
from sequdas.models import SampleSheetSample

class SequenceRunAdmin(GuardedModelAdmin):
    pass

class SampleAdmin(admin.ModelAdmin):
    pass

class ReadSummaryAdmin(admin.ModelAdmin):
    pass

class SampleSheetAdmin(admin.ModelAdmin):
    pass

class SampleSheetSampleAdmin(admin.ModelAdmin):
    pass

admin.site.register(SequenceRun, SequenceRunAdmin)
admin.site.register(Sample, SampleAdmin)
admin.site.register(ReadSummary, ReadSummaryAdmin)
admin.site.register(SampleSheet, SampleSheetAdmin)
admin.site.register(SampleSheetSample, SampleSheetSampleAdmin)
