#coding=utf-8
__author__ = 'seyren'
from uliweb.orm import *



class BlogCategory(Model):
    name = Field(str, max_length=80, verbose_name=_('Name'))

    def __unicode__(self):
        return self.name


class Blog(Model):

    title = Field(TEXT, required=True, verbose_name='标题')
    content = Field(TEXT, required=True, verbose_name='文章内容')
    created_time = Field(datetime.datetime, verbose_name="发布时间", auto_now_add=True, index=True)
    modified_time = Field(datetime.datetime, verbose_name="更新时间", auto_now_add=True)
    #category = Reference('blogscategory', verbose_name=_('Category'), index=True)
    def __unicode__(self):
        return self.title

    class AddForm():
        field = ['title', 'content']

    class EditForm():
        field = ['title', 'content']


# class users(Model):
#     username = Field(CHAR)
#     password = Field(TEXT)

