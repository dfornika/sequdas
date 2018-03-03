from django.test import TestCase
from sequdas.models import SequenceRun
import datetime

# Create your tests here.
class SequenceRunTestCase(TestCase):
    def setUp(self):
        SequenceRun.objects.create(
            run_id = "Run-0001",
            folder = "/data/miseq/M000001/Run-0001",
            run_start_time = datetime.datetime.now(),
            run_end_time = datetime.datetime.now() + datetime.timedelta(hours = 24),
            cluster_density = 800.0,
            clusters_pf_percent = 95.0,
            reads_total = 5000000,
            reads_pf = 4500000,
            bases_greater_than_q30_percent = 95.0
        )
        
    def test_run_end_time_after_start_time(self):
        """Check that run start time is later than run end time"""
        run_0001 = SequenceRun.objects.get(run_id="Run-0001")
        self.assertTrue(run_0001.run_end_time >  run_0001.run_start_time)

