import play # this is the first line in the program
# https://github.com/replit/play
w = 700
h = 400
@play.when_program_starts
def do():
    play.screen.width = w
    play.screen.height = h

box = play.new_box(
    color = (255,255,255), 
    x = 0, 
    y = 0, 
    width = w, 
    height = h,
)



play.start_program() # this is the last line in the program


#mouse_text.go_to(mouse_text.x + mouse_text.width/2 + 10, mouse_text.y)