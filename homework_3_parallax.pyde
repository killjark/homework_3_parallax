
"""
 Inspired by:
      http://1morecastle.com/wp-content/uploads/2013/01/parallax-scrolling-mario.gif

 The images referenced below are available here:
   - http://composingdigitalmedia.org/ccr/week03-mountains.png
   - http://composingdigitalmedia.org/ccr/week03-hills.png
   - http://composingdigitalmedia.org/ccr/week03-foreground.png
 Download these and save them into your sketch folder.
"""

def setup():
    size(800,375)

    global mountainsImage
    global hillsImage
    global foregroundImage

    mountainsImage = loadImage("IMG_2728.jpeg")
    hillsImage = loadImage("Pattern-1-01.png")
    foregroundImage = loadImage("596ce35fed07ad6118f998e8.png")

def draw():

  rg = map(mouseX, 0,width, 155,10)
  b = map(mouseX, 0,width, 255,50)
  background(rg,rg,b)

  mtnX = map(mouseX, 0,width, 0,-1000 );
  image(mountainsImage, mtnX,-700)


  fgX = map(mouseX, 0,width, 200,-2000)
  image(foregroundImage, fgX,225, width/2,height/2)

  darkness = map(mouseX, 0,width, 0,225)
  fill(0,darkness)
  rect(0,0,width,height)
  
  hillsX = map(mouseX, 0,width, -20,-200 )
  rotate(PI/3.0)
  image(hillsImage, hillsX,-1000)
