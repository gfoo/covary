from django.test import TestCase

from probes.models import Probe


class ProbeTestCase(TestCase):
    def setUp(self):
        self.probe_name = "probe_name"
        self.probe = Probe.objects.create(
            name=self.probe_name,
        )

    def test_create_probe(self):
        self.assertIsInstance(self.probe, Probe)
        assert self.probe.name == self.probe_name
