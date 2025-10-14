# Hilma in Motion
# HaK 165

# define colours as RGB 
blue = color(99, 147, 184)
white = color (224, 216, 204)
yellow = color (230, 188, 92)
black = color(43, 43, 43)
pink = color (233, 158, 138)

# define size
arc_size = 320

# addition to angle
turn = 0
direction = 1

# set up variables
def setup():
    size(600, 600)
    background(196, 86, 59)
    noStroke()

# main loop
def draw():
    global turn
    global arc_size
    global direction
    
# draw over old shapes
    background(196, 86, 59)
    
    turn = turn + 1
    arc_size = arc_size + direction
    if arc_size >= 600:
        direction*=-1
    if arc_size <= 320:
        direction*=-1
    
    
    # draw layers
    fill(blue)
    arc(width/2, height/2, arc_size, arc_size, radians(270-turn), radians(450-turn))

    fill(white)
    arc(width/2, height/2, arc_size, arc_size, radians(90-turn), radians(270-turn))

    fill(yellow)
    arc(width/2, height/2, arc_size*2/3, arc_size*2/3, radians(270+turn), radians(450+turn))

    fill(black)
    arc(width/2, height/2, arc_size*2/3, arc_size*2/3, radians(90+turn), radians(270+turn))

    fill(pink)
    arc(width/2, height/2, arc_size/3, arc_size/3, radians(270+turn), radians(450+turn))
