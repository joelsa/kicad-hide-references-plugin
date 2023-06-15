# A KiCad plugin to hide all reference designators

In most cases, the majority of the silk screen reference designators are unnecessary and take up valuable board space. Hiding all reference designators	and only introducing back select ones (e.g. for I2C-Pull-Ups or Solder Jumpers) to the silk screen is the better approach.

While modern versions of KiCad allow to do this natively (Edit -> Edit Text and Graphic Properties -> Select Footprint references -> Action: Set to specified value -> Untick visible -> Ok) I found that I use this so often that an external plugin is justified.

## Installation

To install, just move the hide_references folder to your KiCad Plugin space, as with any other KiCad Plugin.

## Usage

Just click the icon in the toolbar, if no icon is shown, activate under Preferences in PcbNew.

The plugin will hide all references. If all references are hidden, the will be made visible again, in order to be able to quickly check positioning or correctness.