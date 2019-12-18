from psychopy import visual, core

win = visual.Window()
msg = visual.TextStim(win, text=u"\u00A1Esto es una prueba\u00A1")

msg.draw()
win.flip()
core.wait(2)
win.close()