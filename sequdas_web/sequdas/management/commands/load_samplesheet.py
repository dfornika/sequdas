#!/usr/bin/env python

import os
import sys
import logging
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
        logger = logging.getLogger(__name__)
        sample_sheet = IlluminaSampleSheet(options['sample_sheet_filename'])
        path = os.path.abspath(sample_sheet.path)
        iem_file_version = sample_sheet.Header.IEMFileVersion
        if sample_sheet.Header.Date:
            try:
                date = datetime.strptime(sample_sheet.Header.Date, "%m/%d/%Y").date()
            except ValueError:
                date = datetime.strptime(sample_sheet.Header.Date, "%d/%m/%Y").date()
        else:
            date = None
        investigator_name = sample_sheet.Header.Investigator_Name
        project_name = sample_sheet.Header.Project_Name
        experiment_name = sample_sheet.Header.Experiment_Name
        workflow = sample_sheet.Header.Workflow
        application = sample_sheet.Header.Application
        assay = sample_sheet.Header.Assay
        description = sample_sheet.Header.Description
        chemistry = sample_sheet.Header.Chemistry
        read1_length = sample_sheet.Reads[0]
        read2_length = sample_sheet.Reads[1]
        reverse_complement = bool(int(sample_sheet.Settings.ReverseComplement))
        adapter = sample_sheet.Settings.Adapter
        adapter_read2 = sample_sheet.Settings.AdapterRead2

        print("path: " + path)
        print("Date: " + date.isoformat() if date else "")
        print("Investigator Name: " + str(investigator_name))
        print("Project Name: " + str(project_name))
        print("Experiment Name: " + str(experiment_name))
        print("Workflow: " + str(workflow))
        print("Application: " + str(application))
        print("Assay: " + str(assay))
        print("Description: " + str(description))
        print("Chemistry: " + str(chemistry))
        print("Read1 Length: " + str(read1_length))
        print("Read2 Length: " + str(read2_length))
        print("Reverse Complement: " + str(reverse_complement))
        print("Adapter: " + str(adapter))
        print("Adapter Read2: " + str(adapter_read2))
        
        db_sample_sheet = SequdasSampleSheet.objects.create(
            path = path,
            iem_file_version = iem_file_version if iem_file_version else "",
            investigator_name = investigator_name if investigator_name else "",
            project_name = project_name if project_name else "",
            experiment_name = experiment_name if experiment_name else "",
            date = date,
            workflow = workflow if workflow else "",
            assay = assay if assay else "",
            description = description if description else "",
            chemistry = chemistry if chemistry else "",
            application = application if application else "",
            read1_length = read1_length,
            read2_length = read2_length,
            reverse_complement = reverse_complement,
            adapter = adapter if adapter else "",
            adapter_read2 = adapter_read2 if adapter_read2 else ""
        )
        
        print(db_sample_sheet.id)
        
        for sample in sample_sheet.samples:
            sample_id = sample.Sample_ID
            sample_name = sample.Sample_Name
#            i7_index = 
            print("Sample ID: " + str(sample_id))
            print("Sample Name: " + str(sample_name))
            print(sample.__dict__)
        
