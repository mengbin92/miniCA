from django import forms

class CSRForm(forms.Form):
    common = forms.CharField(label='通用名',max_length=64)
    country = forms.CharField(label='国家',min_length=2,max_length=2)
    locality = forms.CharField(label='地区',max_length=64)
    province = forms.CharField(label='省',max_length=64)
    organization = forms.CharField(label='组织',max_length=64)
    organizationunit = forms.CharField(label='部门',max_length=64)
    email = forms.EmailField(label='邮箱')