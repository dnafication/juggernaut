"""
Find out the unused Global variables in a JMX file
"""
import sys, os
import logging
from bzt.jmx import base
from bzt.jmx import http
from bzt.jmx import threadgroups
from bzt.jmx import tools
from bzt import jmx2yaml
import re

class Options:
    "creating an arbitrary class for the bzt options"
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

def understand():
    "doesnt work"
    # Understading the `base` module. Simple workflow
    TEST_PLAN_SEL = base.JMX.TEST_PLAN_SEL
    JMX = base.JMX
    
    # new jmx
    jmx = JMX() # to load add the filename

    # append tg to the tp
    tg = JMX.get_thread_group(concurrency=10, rampup=10, hold=10, testname='BZT TG')
    jmx.append(TEST_PLAN_SEL, tg)

    # append dns cache manager
    jmx.append(TEST_PLAN_SEL, JMX.get_dns_cache_mgr())

    # append kpi listener
    jmx.append(TEST_PLAN_SEL, JMX.new_kpi_listener("kpi.jtl"))
    jmx.append(TEST_PLAN_SEL, JMX.new_xml_listener("xml.jtl", False, user_flags={}))
    jmx.append(TEST_PLAN_SEL, JMX.new_xml_listener("xml.jtl", True, user_flags={}))

    # creat udv
    udv = dict(one="1", two="2")
    jmx.append(TEST_PLAN_SEL, JMX.add_user_def_vars_elements(udv))
    jmx.save("understand.jmx")


def get_all_udv(jmxfile):
    "return a python dictionary containing all jmeter user defined variables in the jmx provided"
    TEST_PLAN_SEL = base.JMX.TEST_PLAN_SEL
    JMX = base.JMX

    # new jmx
    jmx = JMX(jmxfile)
    
    f = open(jmxfile, 'r')
    jmxstring = f.read()

    udv_list = jmx.get('Arguments > collectionProp > elementProp[elementType="Argument"]')
    testplan_element = jmx.get('TestPlan')
    tg_list = jmx.get('ThreadGroup') # list of tg etree elements
    
    for element in udv_list:
        var_name = str(element.attrib)
        
        # count the substring
        print(var_name, jmxstring.count(var_name))





def play_with_j2y():
    options = Options() # command line arguments which are usually passed to `bzt`
    
    # hard defaults below
    options.log = 'logfile' 
    options.option = None
    options.quiet = None
    options.verbose = True
    options.out = 'ymlfile'
    options.dump_jmx = 'jmxfile'

    jmx_file = 'C:\\Users\\dbasumatary\\PycharmProjects\\juggernaut\\backend\\support\\SP_MAIN.jmx'

    tool = jmx2yaml.JMX2YAML(options, jmx_file)
    dialect = jmx2yaml.JMXasDict(tool.log)

    print(dialect.get('TestPlan')[0].items())





if __name__ == "__main__":
    get_all_udv('SP_MAIN.jmx')
    print('hi')


