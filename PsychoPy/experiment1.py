from psychopy import visual, core
win = visual.Window([600,400])
message = visual.TextStim(win, text='Este es un experimento')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(2.0)
message.text = 'Mi nombre es Luna'  # Change properties of existing stim
win.flip()
core.wait(4.0)

