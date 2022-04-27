from . import web_base

class clickableObject(web_base.objectBaseClass):
    def __init__(self, driver, selector, selector_type='xpath', name='clickableObject'):
        super(clickableObject, self).__init__(driver, selector, selector_type, name)
        
    def click(self):
        print("-- Clicking %s" % self.name)
        this_object = self._get_handle()

        if this_object:
            this_object.click()
            return True
        else:
            return False

class inputBox(clickableObject):
    def __init__(self, driver, selector, selector_type='xpath', name="inputBox"):
        super(clickableObject, self).__init__(driver, selector, selector_type, name)
    
    def type_text(self, text):
        print("-- Entering '%s' into %s" % (text, self.name))
        this_box = self._get_handle()
        this_box.send_keys(text)
        
class button(clickableObject):
    def __init__(self, driver, selector, selector_type='xpath', name="button"):
        super(clickableObject, self).__init__(driver, selector, selector_type, name)
        self.__text = None
    
    @property
    def text(self):
        this_object = self._get_handle()
        return this_object.text
