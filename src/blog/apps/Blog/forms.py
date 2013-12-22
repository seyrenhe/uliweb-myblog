#coding=utf-8

from uliweb.form import *


class AddForm(Form):

    form_buttons = [Button(value="保存", type='submit', _class="btn btn-primary"),Button(value="重置", type='reset', _class="btn"), ]
    #username = StringField(label="用户名", required=True)
    title = StringField(label="标题", required=True)
    content = TextField(label="内容", required=True, rows=20, cols=100)
    category = StringField(label="分类", required=True)



class AddCForm(Form):
    form_buttons = [Button(value="保存", type='submit', _class="btn btn-primary"),Button(value="重置", type='reset', _class="btn"), ]
    category = StringField(label="分类名", required=True)





