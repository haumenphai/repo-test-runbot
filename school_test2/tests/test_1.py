from odoo.tests.common import SavepointCase, tagged


@tagged('test_upg')
class Test1(SavepointCase):

    def test_02_example_run_test_tag_failed(self):
        assert 1 + 1 == 3
