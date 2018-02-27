import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django.contrib.auth.models import User
#from guardian.shortcuts import get_objects_for_user

from sequdas.models import SequenceRun
from sequdas.models import Sample
from sequdas.models import ReadSummary
from sequdas.models import SampleSheet
from sequdas.models import SampleSheetSample

class UserType(DjangoObjectType):
    class Meta:
        model = User

class SequenceRunType(DjangoObjectType):
    class Meta:
        model = SequenceRun

class ReadSummaryType(DjangoObjectType):
    class Meta:
        model = ReadSummary
        
class SampleType(DjangoObjectType):
    class Meta:
        model = Sample

class SampleSheetType(DjangoObjectType):
    class Meta:
        model = SampleSheet

class SampleSheetSampleType(DjangoObjectType):
    class Meta:
        model = SampleSheetSample

class Query(graphene.ObjectType):
    current_user = graphene.Field(UserType)
    def resolve_current_user(self, info):
        if not info.context.user.is_authenticated:
            return None
        return info.context.user

    sequence_runs = graphene.List(SequenceRunType)
    def resolve_sequence_runs(self, info, **kwargs):
        user = info.context.user
        print(user)
        user_sequence_runs = [x for x in SequenceRun.objects.all() if user.has_perm('sequdas.view_sequence_run', x)]
        return user_sequence_runs

    samples = graphene.List(SampleType)
    def resolve_samples(self, info, **kwargs):
        return Samples.objects.select_related('sequence_run').all()

    read_summaries = graphene.List(ReadSummaryType)
    def resolve_read_summaries(self, info, **kwargs):
        return ReadSummary.objects.select_related('sequence_run').all()

    sample_sheets = graphene.List(SampleSheetType)
    def resolve_sample_sheets(self, info, **kwargs):
        return SampleSheet.objects.all()

    sample_sheet_samples = graphene.List(SampleSheetSampleType)
    def resolve_sample_sheet_samples(self, info, **kwargs):
        return SampleSheet.objects.select_related('sample_sheet').all()
