#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.DaMall import DaMallSystemSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(Pool,Url,Values,proxies,**kwargs):
    Pool.Append(DaMallSystemSQLInjectionVulnerability.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("DaMall")