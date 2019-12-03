


class IAAD_UI():
    
    def __init__(self):
        pass

    
    def show_enter_date(self):
        print("\n")
        user_input_date = input("Enter a date: ")
        print("\n")
        IAAD_UI.show_IAAD_menu(self)
        """ This prints out, input date """
        pass
    
    def show_available_employees(self):
        """ This prints out the available employees from a certain date """
        print("this is a list of available employees")
        print("\n")
        print("B Back")
        user_input = IAAD_UI.choose_action(self)
        if user_input == "b":
            IAAD_UI.show_IAAD_menu(self)
        pass
    
    def show_unavailable_employees(self):
        """ This prints out the unavailable employees from a certain date """
        print("this is a list of unavailable employees")
        print("\n")
        print("B Back")
        user_input = IAAD_UI.choose_action(self)
        if user_input == "b":
            IAAD_UI.show_IAAD_menu(self)
        pass
    
    def show_airplane_status(self):
        """ This prints out the status of a airplane from a certain date """
        print("this is a list of airplanes and their status")
        print("\n")
        print("B Back")
        user_input = IAAD_UI.choose_action(self)
        if user_input == "b":
            IAAD_UI.show_IAAD_menu(self)
        pass

    def show_voyages_status(self):
        """ This prints out the status of a voyage from a certain date """
        print("this is a list of voyages and their status")
        print("\n")
        print("B Back")
        user_input = IAAD_UI.choose_action(self)
        if user_input == "b":
            IAAD_UI.show_IAAD_menu(self)
        pass

    
    def show_IAAD_menu(self):
        """ This prints out the information about a date menu """
        print("IAAD")
        print("1 Available Employees","\n2 Unavailable Employees","\n3 Status of voyages","\n4 Status of Airplanes","\nB Back")

        user_input = IAAD_UI.choose_action(self)
        if user_input == "1":
            IAAD_UI.show_available_employees(self)
        elif user_input == "2":
            IAAD_UI.show_unavailable_employees(self)
        elif user_input == "3":
            IAAD_UI.show_voyages_status(self)
        elif user_input == "4":
            IAAD_UI.show_airplane_status(self)
        elif user_input == "b":
            
        pass 

            
      
    def choose_action(self):
        print("\n")
        user_action = input("Choose action: ")
        return user_action


