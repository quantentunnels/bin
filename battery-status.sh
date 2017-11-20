#!/bin/bash
# parse acpi battery status message and shorten w/ unicode chars

#tsv string look-up table
lookup='/home/marius/bin/battery-status.sed'

acpi | sed -f $lookup
