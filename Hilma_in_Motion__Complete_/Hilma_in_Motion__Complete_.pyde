# Hilma in Motion
# HaK 165
# Animated arcs with rotation, scaling, and layered composition

# Define colours as RGB values
blue = color(99, 147, 184)
white = color (224, 216, 204)
yellow = color (230, 188, 92)
black = color(43, 43, 43)
pink = color (233, 158, 138)

# define initial arc size
arc_size = 320

# Animation variables
# 'turn' controls rotation
# 'direction' controls arc scaling and speed reversal
# addition to angle
turn = 0
direction = 1

# set up canvas
def setup():
    size(600, 600) #Canvas size
    background(196, 86, 59) #Background colour
    noStroke() #Remove outlines for arcs

# Main animation loop
def draw():
    global turn
    global arc_size
    global direction
    
# Clear the canvas each frame
    background(196, 86, 59)
    
# Update animation variables
    turn = turn + 1 #Increment rotation angle
    arc_size = arc_size + direction #Grow or shrink arc
    
# Reverse direction when reaching limits
    if arc_size >= 600:
        direction*=-1
    if arc_size <= 320:
        direction*=-1
    
# Draw layered arcs
# Each 'fill()' sets colour, followed by 'arc()' to draw it
# Rotation applied via 'turn'
    # draw layers
    fill(blue) #Large blue layer
    arc(width/2, height/2, arc_size, arc_size, radians(270-turn), radians(450-turn))

    fill(white) #Large white layer
    arc(width/2, height/2, arc_size, arc_size, radians(90-turn), radians(270-turn))

    fill(yellow) #Medium yellow layer
    arc(width/2, height/2, arc_size*2/3, arc_size*2/3, radians(270+turn), radians(450+turn))

    fill(black) #Medium black layer
    arc(width/2, height/2, arc_size*2/3, arc_size*2/3, radians(90+turn), radians(270+turn))

    fill(pink) #Small pink layer
    arc(width/2, height/2, arc_size/3, arc_size/3, radians(270+turn), radians(450+turn))

    
    
