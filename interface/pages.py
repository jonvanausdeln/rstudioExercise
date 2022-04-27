###########################################
# Page objects representing teh elements of
#   the Rstudio cloud 
###########################################
from . import web_base, elements

class mainPage(web_base.webPageBaseClass):
    # Entry Point of the tool
    def __init__(self, driver, url="https://rstudio.cloud/"):
        super().__init__(driver, url)
        self.login_button = elements.button(driver, "//a[contains(.,'Log In')]", name="Login Button")
        self.sign_up_button = elements.button(driver, "//a[contains(.,'Sign Up')]", name="Sign Up Button")

class loginPage(web_base.webPageBaseClass):
    # User login and signup
    def __init__(self, driver, url = "https://rstudio.cloud/login"):
        super().__init__(driver, url)
        self.email = elements.inputBox(driver, "//input[@name='email']", name="Login Email")
        self.password = elements.inputBox(driver, "//input[@name='password']", name="Login Password")
        self.continue_button = elements.button(driver, "//button[contains(.,'Continue')]", name="Login Continue Button")
        self.log_in_button = elements.button(driver, "//button/span", name="Finish Login Button")

class workspacePage(web_base.webPageBaseClass):
    # Main page of the tool. Contains the Spaces and Projects.  A fully implemented test 
    #   would most likely break these up into several different classes
    def __init__(self, driver, url = "https://rstudio.cloud/content/yours"):
        super().__init__(driver, url)
        self.new_space_button = elements.button(driver, "//button[contains(.,'New Space')]", name="New Space Button")
        self.space_name1 = elements.button(driver, ".spaceNameWithOwner", selector_type='css', name="New Space Sidebar Item")
        self.new_space_name = elements.inputBox(driver, "//input[@id='name']", name="New Space Name input")
        self.new_space_create_button = elements.button(driver, "//button[@type='submit']", name="New Space Create Button")
        self.space_ellipses_menu_button = elements.button(driver, "//div[@id='rStudioHeader']/div/div/div[3]/div/button", name="Spaces ellipses Button")
        self.space_delete_button = elements.button(driver, "//button[contains(.,'Delete Space')]", name="Spaces delete button")
        self.space_delete_confirm_text = elements.inputBox(driver, "//form/div/input", name="Space delete confirm text")
        self.space_delete_confirm_button = elements.button(driver, "//form/div[2]/button", name="Space delete confirm button") # I don't like this selector
        
        self.new_project_button = elements.button(driver, "//span[contains(.,'New Project')]", name="New Project Button")
        self.new_rstudio_project_selection = elements.clickableObject(driver, "//span[contains(.,'New RStudio Project')]", name="New Rstudio Projecct Select button")

        self.project_ide_iframe = elements.clickableObject(driver, "//iframe[@id='contentIFrame']")
        self.project_console_window = elements.button(driver,"//div[@id='rstudio_shell_widget']", name="Project IDE console window")

    