#!/usr/bin/env python

import os
import sys
import logging
from datetime import datetime
import numpy
import xmltodict
from interop import py_interop_run_metrics, py_interop_run, py_interop_summary
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Loads an illumina run directory into SequDAS"

    def add_arguments(self, parser):
        parser.add_argument('run_dir')

    def handle(self, *args, **options):
        logger = logging.getLogger(__name__)
        run_folder = os.path.abspath(options['run_dir'])
        with open(os.path.abspath(options['run_dir'] + '/RunInfo.xml')) as fd:
            run_info_xml = xmltodict.parse(fd.read())
        
        run_info = py_interop_run.info()
        run_metrics = py_interop_run_metrics.run_metrics()
        run_summary = py_interop_summary.run_summary()

        try:
            run_info.read(run_folder)
            run_metrics.read(run_folder)
            run_summary.initialize(run_info)
            py_interop_summary.summarize_run_metrics(run_metrics, run_summary)
        except Exception as ex:
            logging.warn("Skipping - cannot read RunInfo.xml: %s - %s"%(run_folder, str(ex)))

        date = datetime.strptime(run_info.date(), "%y%m%d").date()
        run_id = run_info.name()
        folder = os.path.abspath(options['run_dir'])
        
        
        print("Date: " + str(date.isoformat()))
        print("Run Name: " + str(run_id))
        print("Lane Count: " + str(run_summary.lane_count()))
        # print("Cluster Density: " + str(cluster_density))
        print("Summary Size: " + str(run_summary.size()))
        print("Summary Lane Count: " + str(run_summary.lane_count()))
        print("Summary Surface Count: " + str(run_summary.surface_count()))

        # db_sequence_run = SequenceRun.objects.create(
        #     run_id = run_id if run_id else "",
        #     folder = folder if folder else "",
        #
        # )
        
