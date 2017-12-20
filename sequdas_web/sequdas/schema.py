import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django.contrib.auth.models import User

from sequdas.models import SequenceRun, Sample, ReadSummary

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

class Query(graphene.ObjectType):
    current_user = graphene.Field(UserType)
    def resolve_current_user(self, info):
        if not info.context.user.is_authenticated:
            return None
        return info.context.user

    sequence_runs = graphene.List(SequenceRunType)
    def resolve_sequence_runs(self, info, **kwargs):
        return SequenceRun.objects.all()

    samples = graphene.List(SampleType)
    def resolve_samples(self, info, **kwargs):
        return Samples.objects.select_related('sequence_run').all()

    readSummaries = graphene.List(ReadSummaryType)
    def resolve_read_summaries(self, info, **kwargs):
        return ReadSummary.objects.select_related('sequence_run').all()
