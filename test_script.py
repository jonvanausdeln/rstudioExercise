import interface
import time
import sys, argparse

def main(arguments):
    try:
        print("--== STARTING TEST ==--")
        # Start up main page and Log in 
        interface.initialize()
        interface.mainpage.load()
        interface.mainpage.login_button.click()
        interface.loginpage.email.check_existance()
        interface.loginpage.continue_button.check_existance()
        interface.loginpage.email.type_text(arguments.email)
        interface.loginpage.continue_button.click()
        interface.loginpage.password.type_text(arguments.password)
        interface.loginpage.log_in_button.click()

        # Double check previous test was cleaned up
        assert not interface.spacepage.space_name1.check_existance(), "Space exists, can't create new one"
        assert interface.spacepage.new_space_button.check_existance(), "New Space button isn't available"

        # Create a new Space, verify it exists in sidebar
        interface.spacepage.new_space_button.click()
        interface.spacepage.new_space_name.type_text('Test Space 1')
        interface.spacepage.new_space_create_button.click()
        assert interface.spacepage.space_name1.text == "Test Space 1", "New Space wasn't found"

        # Create a new Project
        interface.spacepage.space_name1.click()
        interface.spacepage.new_project_button.click()
        interface.spacepage.new_rstudio_project_selection.click()
        
        # Verify Project IDE loaded
        interface.browser._driver.switch_to.frame(interface.spacepage.project_ide_iframe._get_handle(60)) # switch focus to ide
        assert interface.spacepage.project_console_window.check_existance(timeout=60), "New Project IDE not found"


        print("** Test Passed **")
        
    except AssertionError as e:
        print("!!!! TEST FAILURE !!!!")
        print(e)
    
    finally:
        print(".. Cleaning Up ...")
        interface.browser._driver.switch_to.default_content()
        interface.spacepage.space_name1.click()
        interface.spacepage.space_ellipses_menu_button.click()
        interface.spacepage.space_delete_button.click()
        interface.spacepage.space_delete_confirm_text.type_text("Delete Test Space 1")
        interface.spacepage.space_delete_confirm_button.click()
        interface.cleanup()
        print("--== TEST COMPLETE ==--")


def parse_command_line(args):
    argument_parser = argparse.ArgumentParser(description='Basic RStudio Cloud test')
    argument_parser.add_argument('--email',
                                 type=str,
                                 help='Email address for login',
                                 required=True)
    argument_parser.add_argument('--password',
                                 type=str,
                                 help='Password for login',
                                 required=True)

    arguments = argument_parser.parse_args(args)
    return arguments

if __name__ == "__main__":
    sys.exit(main(parse_command_line(sys.argv[1:])))