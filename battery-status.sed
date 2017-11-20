#remove battery designation
s/Battery [[:digit:]]: //
s/Full/●/
# or ⚡
s/Charging,/↯/
s/Discharging,/↘/
# or ↓
s/Unknown/❓/
# or ❔ (white ?)

# #set time into parens
# s,\(\([[:digit:]]{2}:\)\{2\}[[:digit:]]\{2\}\),(\2),
s/remaining/⌛/
# or ⌚
s/until charged/↸/
# or ⇥

#reserve/unused
#s/Unavailable/❌/
# or ⌀
