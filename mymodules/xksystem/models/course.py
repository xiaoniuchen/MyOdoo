# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.modules.module import get_module_resource
from odoo import tools, _
import random
import time


class course(models.Model):
    _name = 'xksystem.course'
    _description = 'xksystem.course'

    name = fields.Char(string=u'课程名')
    code = fields.Char(string=u'课程编号')
    studentlimit = fields.Integer(string=u'学生上限')
    havestudent = fields.Integer(string=u'已选课学生数', compute='_compute_have_student')
    teachers = fields.Many2many('xksystem.teacher', 'xksystem_course_xksystem_teacher_rel',
                                'course_id', 'teacher_id', string='授课教师')
    course_score = fields.Float(string='课程学分')
    remarks = fields.Html()

    @api.constrains('course_score')
    def check_course_score(self):
        for record in self:
            if record.course_score > 2:
                raise ValidationError("The Score is too High: %s" % record.course_score)

    #--重写name_get方法,同时返回课程名称和代码，这样别人在调用的时候就会明确的知道课程名称和课程代码
    @api.multi
    def name_get(self):
        result = []

        for record in self:
            result.append((record.id, "%s(%s)" % (record.name, record.code)))

        return result

    @api.multi
    def _compute_have_student(self):
        for recode in self:
            l_sql = "select course_id,count(*) from xksystem_studentcourseline " \
                    "where course_id = %s group by course_id" % (recode.id)
            self.env.cr.execute(l_sql)
            dicts = self.env.cr.dictfetchall()
            print(dicts)
            if len(dicts) > 0:
                recode.havestudent = dicts[0]['count']
            else:
                recode.havestudent = 0

    @api.multi
    def xk_btn(self):
        # --点击选课按钮,然后创建一笔学生课程资料
        res = self.env['res.users'].search([('id', '=', self.env.uid)])  # 获取当前用户的ID
        print(res.login)
        code = res.login  # 获取当前用户的学号
        res = self.env['xksystem.student'].search([('code', '=', code)])  # 以学号获取当前学生头表信息
        if res.id:
            # 检索是否已经选过此门课程
            res_course = self.env['xksystem.studentcourseline'].search(['&', ('student_id', '=', res.id),
                                                                        ('coursecode', '=', self.id)])
            if res_course:
                print('此门课程已被选过了,不能重复选择！')
                raise UserError(('你已经选过了这门课,不能重复选择！'))
            else:
                # 防止大量并发选课,每位学生随机停止0-1秒
                sleep_time = random.random()
                print(sleep_time)
                time.sleep(sleep_time)

                # 检索课程是否已经被选光
                l_sql = "select course_id,count(*) from xksystem_studentcourseline " \
                        "where course_id = %s group by course_id" % (self.id)
                self.env.cr.execute(l_sql)
                dicts = self.env.cr.dictfetchall()
                if len(dicts)==0:
                    havastudent_count = 0
                else:
                    havastudent_count = dicts[0]['count']
                if havastudent_count >= self.studentlimit:
                    raise UserError(('选课学生人数已经超过上限,请选择其他课程！'))

                # 合规,系统进行选课
                vals = {'linenumber': self.env['ir.sequence'].next_by_code('seq.test'), 'student_id': res.id,
                        'course_id': self.id, 'coursecode': self.code, }
                self.env['xksystem.studentcourseline'].sudo().create(vals)
        else:
            raise UserError(('此账户不是学生账户,不能选课！'))
        return True

    @api.multi
    def qxxk_btn(self):
        # --点击取消选课,则删除对应学生的课程资料
        pass
