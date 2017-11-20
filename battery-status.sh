#!/bin/bash
# parse acpi battery status message and shorten w/ unicode chars

#tsv string look-up table
lookup='battery-status.sed'

acpi | sed -f battery-status.sed
