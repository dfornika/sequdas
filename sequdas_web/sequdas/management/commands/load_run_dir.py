#!/usr/bin/env python

import os
import sys
import logging
import numpy
from interop import py_interop_run_metrics, py_interop_run, py_interop_summary
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    help = "Loads an illumina run directory into SequDAS"

    def add_arguments(self, parser):
        parser.add_argument('run_dir')

    def handle(self, *args, **options):
        logger = logging.getLogger(__name__)
        run_folder = os.path.abspath(options['run_dir'])
        print(run_folder)

        run_metrics = py_interop_run_metrics.run_metrics()
        summary = py_interop_summary.run_summary()

        valid_to_load = py_interop_run.uchar_vector(py_interop_run.MetricCount, 0)
        py_interop_run_metrics.list_summary_metrics_to_load(valid_to_load)
        
        try:
            run_metrics.read(run_folder, valid_to_load)
        except Exception as ex:
            logging.warn("Skipping - cannot read RunInfo.xml: %s - %s"%(run_folder, str(ex)))
        
        py_interop_summary.summarize_run_metrics(run_metrics, summary)

        error_rate_read_lane_surface = numpy.zeros((summary.size(), summary.lane_count(), summary.surface_count()))
        for read_index in range(summary.size()):
            for lane_index in range(summary.lane_count()):
                for surface_index in range(summary.surface_count()):
                    error_rate_read_lane_surface[read_index, lane_index, surface_index] = \
                        summary.at(read_index).at(lane_index).at(surface_index).error_rate().mean()
        print("Run Folder: " + run_folder)
        for read_index in range(summary.size()):
            read_summary = summary.at(read_index)
            print("Read " + str(read_summary.read().number()) + " - Top Surface Mean Error: " + \
                  str(error_rate_read_lane_surface[read_index, :, 0].mean()))

