def setup(plugin):
    plugin.add_action("SnapTop", "Snap window to top half", "actions/SnapTop")
    plugin.add_action("SnapBottom", "Snap window to bottom half", "actions/SnapBottom")
    plugin.add_action("SnapLeft", "Snap window to left half", "actions/SnapLeft")
    plugin.add_action("SnapRight", "Snap window to right half", "actions/SnapRight")
