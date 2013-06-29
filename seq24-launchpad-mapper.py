from mididings import *

# Don't include the rightmost buttons...
forbidden_values = [ 8, 24, 40, 56, 72, 88, 104, 120 ]
midi_toggles_on = {}

for x in range(0, 132):
    midi_toggles_on[x] = False

config(
    client_name = 'seq24-wrapper',
    in_ports = ['input'],
    out_ports = ['output']
)

# Toggle
def toggle_launchpad(event):
    if event.note in forbidden_values:
      event.velocity = 127
      return event
    if event.type == NOTEON and midi_toggles_on[event.note] == False:
        event.velocity = 60
        midi_toggles_on[event.note] = True
    elif event.type == NOTEON and midi_toggles_on[event.note] == True :
        event.velocity = 12
        midi_toggles_on[event.note] = False
        event.type = NOTEOFF
    else:
        return

    return event

run(Filter(NOTE) >> Process(toggle_launchpad))