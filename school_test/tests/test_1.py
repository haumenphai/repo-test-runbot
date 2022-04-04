from odoo.tests.common import SavepointCase, tagged


@tagged('standalone123')
class Test1(SavepointCase):

    def test_example_run_test_tag_success(self):
        student1 = self.env['student.student'].create({'name': 'Student 1'})
        self.assertEqual(student1.name, 'Student 1')

    def test_example_run_test_tag_failed(self):
        assert 1 + 1 == 3
