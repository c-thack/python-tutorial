from Chef import Chef


class ChineseChef(Chef):  # inherits Chef
    def make_special_dish(self):  # overrides the special dish inherited from Chef
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice.")
