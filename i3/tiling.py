 #!/usr/bin/env python3
 # credit unknown - I did not write this script from scratch but found it somewhere, reddit, stack over flow, etc ...
 # will update it if I can find the original author
import i3ipc

i3          = i3ipc.Connection()
splitv_text = '↕'
splith_text = '↔'
split_none  = '•'
parent      = i3.get_tree().find_focused().parent

if parent.layout   == 'splitv' :
    print( splitv_text )
elif parent.layout == 'splith' :
    print( splith_text )
else                           :
    print( split_none  )
