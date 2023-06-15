#!/usr/bin/env python

import pcbnew
import os

class HideReferencesAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Hide References"
        self.category = "Cleanup"
        self.description = "Hide the reference Designators on the silkscreen"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "./resources/hide-references.png")
        self.show_toolbar_button = True

    def Run(self):
        # The entry function of the plugin that is executed on user action
        pcb = pcbnew.GetBoard()       
        
        if hasattr(pcb, 'GetModules'):
            modules = pcb.GetModules()
        else:
            modules = pcb.GetFootprints()

        for module in modules:
            module.Reference().SetVisible(False)
