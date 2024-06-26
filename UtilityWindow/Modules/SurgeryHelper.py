import PySimpleGUI as sg

class SurgeryHelper:

    def __init__(self):  # Define layout & Setup

        self.surg_rem_key = ""
        self.surg_rep_key = ""

        self.set_layout()

        self.checkMain()

    def set_layout(self):
        ## Surgery Stuff Here

        # TODO: Gonna need something about blood somewhere

        surgery_options = [
            "Headspiders",
            "Implants",
            "Foreign Objects",
            "Limbs",
            "Butt",
            "Eyes",
            "Brain (Humanoid)",
            "Brain (Critters)",
            "Head",
            "Skull",
            "Heart",
            "Lungs",
            "Kidneys",
            "Appendix",
            "Liver",
            "Stomach",
            "Intestines",
            "Pancreas",
            "Spleen",
            "Tail",
            "Chest Cavity",
            "Mask",
        ]

        # TODO: Finish implementing instructions
        # TODO: Work out how to setup dynamic instructions based on Combo, updates in the match I guess?
        # TODO: Try adding in the icons from the SS13 wiki and a "Tools" Section - Resources for images

        surgery_layout = [
            [sg.Combo(surgery_options, default_value=surgery_options[0],enable_events=True, readonly=True,key="-Surgery-")],
            [sg.Text("Removal"),sg.VerticalSeparator(),sg.Text("Replacement")],
            [sg.Text("WIP"),sg.VerticalSeparator(),sg.Text("WIP")],
        ]

        ## Basic Med Stuff Here
        # TODO: Start implementing chems
        # TODO: Maybe a calc built in for recipies?
        # TODO: How to apply each Chem
        # TODO: Maybe Colour code each chem to quickly identify heal type?

        basic_meds = [
            "Stypic Powder",  # BRUTE
            "Silver Sulfadiazine",  # BURN
            "Charcoal",  # TOX - CHEM
            "Potassium Iodide",  # TOX - RAD
            "Mannitol",  # BRAIN
            "Salbutamol",  # OXY
        ]

        basic_med_layout = [
            [sg.Combo(basic_meds, default_value=basic_meds[0], readonly=True,enable_events=True,key="-bMeds-")],
        ]

        ## Advanced Meds
        # TODO: Start implementing chems
        # TODO: Steal new features from Basic Chems

        adv_meds = [
            "Pentetic Acid",  # TOX + BRUTE + BURN
            "Epinephrine",  # OXY - CARDIAC -  HISTA
            "Saline-Glucose",  # BRUTE - BURN - SHOCK
            "Perfluorodecalin",  # OXY - BRUTE - BURN
            "Omnizine",  # BRUTE - BURN - OXY - TOX - ORGAN - BLEED - BLOOD
            "Synthflesh",  # BRUTE - BURN - BLEED
            "Atropine",  # OXY - CARDIAC +- TOX - BRUTE - BURN - BRAIN
            "Mutadone",  # MUTATE
            "Oculine",  # EYE
        ]

        adv_med_layout = [
            [sg.Combo(adv_meds, default_value=adv_meds[0], readonly=True,enable_events=True,key="-advMeds-")]
        ]

        ## Misc
        # TODO: Start implementing misc

        misc = [
            "Penlight",
            "Stethoscope",
        ]

        misc_layout = [
            [sg.Combo(misc, default_value=misc[0], readonly=True,enable_events=True,key="-Misc-")]
        ]

        self.main_layout = [
            [sg.Titlebar("Medical Helper")],
            [sg.Text("Medical Helper v1.1")],
            [sg.TabGroup([[
                sg.Tab("Surgery", surgery_layout),
                sg.Tab("Basic Meds", basic_med_layout),
                sg.Tab("Advanced Meds", adv_med_layout),
                sg.Tab("Misc", misc_layout),
            ]])],
            [sg.Button("Exit", key="-Exit-")]
        ]


    def checkMain(self):
        print("checkMain Started")
        if __name__ == "__main__":  # If run independantly script should have GUI

            print("Running on Main")

            window = sg.Window("Medical Helper", self.main_layout)

            while True:
                event, values = window.read()

                match event:
                    case "-Exit-":
                        break
                    case sg.WINDOW_CLOSED:
                        break
                    case "-Surgery-":
                        pass
                    case "-bMeds-":
                        pass
                    case "-advMeds-":
                        pass
                    case "-Misc-":
                        pass
                    case _:
                        print(event, " | ", values)

    def getResource(self,resource_name):
        return "/Resources/".join(resource_name).join(".png")

    def chemCheck(self,chem):
        match chem:
            # For now recursive recipies are dicts inside of the recipie
            # The LAST part of the dict is ALWAYS the RESULT!!!
            # Will need to check for "Temp" if recipie requires a certain temp!!
            case "Stypic Powder":
                # TODO: Work out how to handle these weird recursive recipies
                return {
                    "Aluminium":1,
                    "Oxygen":1,
                    "Hydrogen":1,
                    "Sulfuric Acid":{"Val":1,"Sulfur":1,"Hydrogen":1,"Oxygen":1,"Sulfuric Acid":2},
                    "Stypic Poweder":4,
                }
            case "Silver Sulfadiazine":
                return {
                    "Silver":1,
                    "Sulfer":1,
                    "Oxygen":1,
                    "Chlorine":1,
                    "Ammonia":{"Val":1,"Hydrogen":3,"Nitrogen":1,"Ammonia":3},
                    "Silver Sulfadiazine":5,
                }
            case "Charcoal":
                # TODO: Make sure to impliment temp!
                return{
                    "Ash":{"Val":1,"Paper":1,"Temp":424,"Ash":1},
                    "Salt":{"Val":1,"Chlorine":1,"Sodium":1,"Water","Salt":2}
                }



_ = SurgeryHelper()