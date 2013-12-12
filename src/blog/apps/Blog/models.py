#coding=utf-8
__author__ = 'seyren'
from uliweb.orm import *


class blogs(Model):
    username = Field(CHAR)
    title = Field(TEXT)
    content = Field(TEXT)
    datetime = Field(datetime.datetime, auto_now_add=True)

class users(Model):
    username = Field(CHAR)
    password = Field(TEXT)

