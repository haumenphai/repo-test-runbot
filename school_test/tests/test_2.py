from odoo.tests import standalone


@standalone('test123')
def test_01_standalone(env):
    assert 1 + 1 == 2
