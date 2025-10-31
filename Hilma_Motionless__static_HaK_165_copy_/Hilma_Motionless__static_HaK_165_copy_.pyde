# Hilma Motionless
# HaK 165

# define colours as RGB 
blue = color(99, 147, 184)
white = color (224, 216, 204)
yellow = color (230, 188, 92)
black = color(43, 43, 43)
pink = color (233, 158, 138)


# define size
arc_size = 320

# set up variables
def setup():
   size(600, 600)
   background(196, 86, 59)
   noStroke()

   # draw layers
   fill(blue)
   arc(width/2, height/2, arc_size, arc_size, radians(270), radians(450))

   fill(white)
   arc(width/2, height/2, arc_size, arc_size, radians(90), radians(270))

   fill(yellow)
   arc(width/2, height/2, arc_size*2/3, arc_size*2/3, radians(270), radians(450))

   fill(black)
   arc(width/2, height/2, arc_size*2/3, arc_size*2/3, radians(90), radians(270))

   fill(pink)
   arc(width/2, height/2, arc_size/3, arc_size/3, radians(270), radians(450))
