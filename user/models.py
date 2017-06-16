#coding:utf-8
from __future__ import unicode_literals

from django.db import models

class BaseModel(models.Model):
    delete_flag = models.CharField(max_length=4, verbose_name='删除标志')
    class Meta:
        abstract=True

class User(BaseModel):
    users = models.CharField(max_length=128,verbose_name='登录名')
    passwd = models.CharField(max_length=128,verbose_name='密码')
    name =  models.CharField(max_length=32,verbose_name='用户名')
    city = models.CharField(max_length=32,verbose_name='城市')
    email = models.EmailField(verbose_name='邮箱')
    phone = models.CharField(max_length=32,verbose_name='电话')

class Group(BaseModel):
    name = models.CharField(max_length=128,verbose_name='组名')
    description = models.TextField(verbose_name='组描述')

class Permission(BaseModel):
    name = models.CharField(max_length=128,verbose_name='权限名')
    description = models.TextField(verbose_name='权限描述')

class User_Group(BaseModel):
    userId = models.IntegerField(verbose_name='用户id')
    groupId =  models.IntegerField(verbose_name='组id')

class User_Permission(BaseModel):
    userId = models.IntegerField(verbose_name='用户id')
    permissionId =  models.IntegerField(verbose_name='权限id')


class Permission_Group(BaseModel):
    permissionId = models.IntegerField(verbose_name='权限id')
    groupId =  models.IntegerField(verbose_name='组id')

