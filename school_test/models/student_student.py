from odoo import models, fields, api


class StudentStudent(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='age')
    birth_day = fields.Date(string='Birth Day')
    address = fields.Char(string='Address')
    desc = fields.Char(string='Description')
    scores = fields.Integer(string='Scores')


    @staticmethod
    def _get_student_data():
        return [
            {
                'name': 'Student 1',
                'age': 18,
                'scores': 9
            },
            {
                'name': 'Student 2',
                'age': 17,
                'scores': 9
            },
            {
                'name': 'Student 3',
                'age': 17,
                'scores': 10,
                'address': 'Hoang Dong'
            },
            {
                'name': 'Student 4',
                'age': 16,
                'scores': 5,
                'address': 'Hoa Dong'
            }
        ]

    def test(self):
        # name = 'Student 3' or (age = 17 and scores = 9 ) or age = 16
        # |, name = 'Student' 3, & age =17, scores =9, age
        print('test')

# s=[
#     ('id','!=',id), '|',
#         '&', ('mode','=','employee'), ('department_id','=', department_id),
#         '&', ('mode', '=', 'department'), ('company_id','=', company_id)
# ]
# l = ['|', '&', ('id', '=', 1), ('name', '=', 'xx'), ('id', '=', '2')]