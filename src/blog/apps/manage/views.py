#coding=utf-8
from uliweb import expose, functions

@expose('/admin/manage')
class ManageAdminView(object):
    def index(self):
        return {}
