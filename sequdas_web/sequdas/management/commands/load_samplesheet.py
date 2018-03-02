#!/usr/bin/env python

import sys
from datetime import datetime
import argparse
from django.core.management.base import BaseCommand, CommandError
from sample_sheet import SampleSheet as IlluminaSampleSheet
from sequdas.models import SampleSheet as SequdasSampleSheet

class Command(BaseCommand):
    help = "Loads an illumina samplesheet into SequDAS"

    def add_arguments(self, parser):
        parser.add_argument('sample_sheet_filename')

    def handle(self, *args, **options):
        sample_sheet = IlluminaSampleSheet(options['sample_sheet_filename'])

        print("Date: " + datetime.strptime(sample_sheet.Header.Date, "%m/%d/%Y").date().isoformat())
        print("Investigator Name: " + str(sample_sheet.Header.InvestigatorName))
        print("Project Name: " + str(sample_sheet.Header.ProjectName))
        print("Experiment Name: " + str(sample_sheet.Header.ExperimentName))

#SequdasSampleSheet.objects.create(
#    iem_file_version = sample_sheet.Header.IEMFileVersion,
#    investigator_name = sample_sheet.Header.InvestigatorName,
#    project_name = sample_sheet.Header.ProjectName,
#    experiment_name = sample_sheet.Header.ExperimentName,
#    )
