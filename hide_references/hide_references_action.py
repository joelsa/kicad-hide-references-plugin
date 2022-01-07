import pcbnew
import os

class HideReferencesAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Hide References"
        self.category = "Cleanup"
        self.description = "A plugin that hides the reference Designators in PCBNew."

    def Run(self):
        # The entry function of the plugin that is executed on user action
        pcb = pcbnew.GetBoard()       
        
        if hasattr(pcb, 'GetModules'):
            modules = pcb.GetModules()
        else:
            modules = pcb.GetFootprints()

        for module in modules:
            module.Reference().SetVisible(False)
