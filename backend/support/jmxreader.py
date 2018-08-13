import xml.etree.ElementTree as etree


class JmxHandler():
    """
    A go to class for JMX file interpretation and modification
    Needs file location to initialize
    """
    def __init__(self, filelocation):
        self.filelocation = filelocation
        self.tree = etree.parse(self.filelocation)
        self.root = self.tree.getroot()
        self.tg_list = self.root.iter('ThreadGroup')

    def get_tg(self, name):
        """returns the ThreadGroup element/node based on name in the argument

        Args:
            name: name of the threadgroup

        Returns:
            etree Element

        """
        return self.root.find(".//ThreadGroup[@testname='{}']".format(name))

    @property
    def jmeter_version(self):
        """returns testplan attributes as dict"""
        return self.root.attrib

    @property
    def tgname_list(self):
        """handy property to return a list of names of tgs"""
        return [tg.attrib['testname'] for tg in self.tg_list]

    def get_tg_as_dict(self):
        """return a dict to be displayed on the form"""
        # empty dict
        tg_dict = {}
        for tg in self.tg_list:
            tg_dict[tg.attrib['testname']] = {
                "thread": self.__get_string_prop(tg, 'ThreadGroup.num_threads'),
                "loop": self.__get_string_prop(tg, ''),
                "delay": str(tg)
                }
        

    def __get_string_prop(self, tg, name):
        return str(tg.find(".//stringProp[@name='{}']".format(name)).text)

    def __get_bool_prop(self, tg, name):
        return str(tg.find(".//boolProp[@name='{}']".format(name)).text)


    def set_thread_count(self, name, count=1):
        """set the thread count of a particular tg"""
        tg = self.get_tg(name)
        
        tg_count = tg.find(".//stringProp[@name='ThreadGroup.num_threads']")
        tg_count.text = str(count)

    def set_rampup(self, name, rampup=1):
        """set the rampup of a particular tg"""
        tg = self.get_tg(name)
        tg_rampup = tg.find("./stringProp[@name='ThreadGroup.ramp_time']")
        tg_rampup.text = str(rampup)

    def set_delay(self, name, delay=1):
        """set the test delay of a particular tg"""
        tg = self.get_tg(name)
        scheduler = tg.find("./boolProp[@name='ThreadGroup.scheduler']")
        scheduler.text = str("true")
        tg_delay = tg.find("./stringProp[@name='ThreadGroup.delay']")
        tg_delay.text = str(delay)
    
    def set_duration(self, name, duration=1):
        """set the test duration of a particular tg"""
        tg = self.get_tg(name)
        scheduler = tg.find("./boolProp[@name='ThreadGroup.scheduler']")
        scheduler.text = str("true")
        tg_duration = tg.find("./stringProp[@name='ThreadGroup.duration']")
        tg_duration.text = str(duration)

    def set_pacing(self):
        pass

    def set_loops(self, name, loop):
        """
        set the main iteration of the threadgroup 
        
        Args:
            name: of the threadgroup 
            loop <= 0 : continue forever)
            loop >= 1 : the count of loops)
        """
        tg = self.get_tg(name)
        forever_flag = tg.find(".//boolProp[@name='LoopController.continue_forever']")
        tg_loop = tg.find(".//stringProp[@name='LoopController.loops']")
        if int(loop) <= 0:
            forever_flag.text = str("true")
        else:
            forever_flag.text = str("false")
            tg_loop.text = str(int(loop))

    def save_as(self, new_name):
        """save the current state of tree to new file"""
        self.tree.write(new_name)
    

if __name__ == "__main__":
    j = JmxHandler('B2B_Main_Group_001.jmx')
    print([x.attrib['testname'] for x in j.tg_list])
    j.set_thread_count('B2B060_MAP_AppointmentAvailability', 1030)
    j.set_delay('B2B060_MAP_AppointmentAvailability', 1030)
    j.set_duration('B2B060_MAP_AppointmentAvailability', 1030)
    j.set_loops('B2B060_MAP_AppointmentAvailability', 1300)
    j.save_as('updated.jmx')



'''
If you don’t mind your application blocking on reading XML data but would still 
like to have incremental parsing capabilities, take a look at iterparse(). It can 
be useful when you’re reading a large XML document and don’t want to hold it 
wholly in memory.

ET.iterparse()
ET.parse()
ET.write()
ET.fromstring()

element.text
element.tag
element.attrib
element.set()
element.append()
element.remove()
element.iter() -- iterate recursively over all the sub-tree below it 
element.findall() -- finds only elements with a tag which are direct children of the current element

    # Top-level elements
    root.findall(".")

    # All 'neighbor' grand-children of 'country' children of the top-level
    # elements
    root.findall("./country/neighbor")

    # Nodes with name='Singapore' that have a 'year' child
    root.findall(".//year/..[@name='Singapore']")

    # 'year' nodes that are children of nodes with name='Singapore'
    root.findall(".//*[@name='Singapore']/year")

    # All 'neighbor' nodes that are the second child of their parent
    root.findall(".//neighbor[2]")



'''


