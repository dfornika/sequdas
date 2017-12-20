from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from sequdas.models import SequenceRun, Sample, ReadSummary

class SequenceRunAdmin(GuardedModelAdmin):
    pass

class SampleAdmin(admin.ModelAdmin):
    pass

class ReadSummaryAdmin(admin.ModelAdmin):
    pass

admin.site.register(SequenceRun, SequenceRunAdmin)
admin.site.register(Sample, SampleAdmin)
admin.site.register(ReadSummary, ReadSummaryAdmin)
