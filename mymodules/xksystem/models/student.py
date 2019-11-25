# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression

class Student(models.Model):
     _name = 'xksystem.student'
     _description = 'xksystem.student'

     name = fields.Char(string='学生姓名')
     code = fields.Char(string='学生编号')
     student_course_line = fields.One2many('xksystem.studentcourseline','student_id')

class StudentCourseLine(models.Model):
     _name = 'xksystem.studentcourseline'
     _description =  'xksystem.studentcourseline'

     linenumber = fields.Char(string='序号',default = lambda self:self.env['ir.sequence'].next_by_code('seq.test'))
     student_id = fields.Many2one('xksystem.student',ondelete='cascade')
     course_id = fields.Many2one('xksystem.course',string='课程名称')
     coursecode = fields.Text(string='课程代码')
     course_teacher = fields.Many2many(string='授课教师')

     _sql_constraints = [
          ('course_id_uniq', 'unique (student_id,course_id)', "Course already exists !"),
     ]

     @api.multi
     @api.onchange('course_id')
     def onchange_course_id(self):
          result = {}
          if not self.course_id:
               return result
          self.coursecode = self.course_id.code
          print('onchange course_id')

          return result


