t = 0
inc = .05
def setup():
    size(600, 600)
    # frameRate(5)

def draw():
    global t
    background(0)
    
    stroke(255)
    noFill()
    beginShape()
    for x in range(width):
        y = random(height/2)
        vertex(x, y)
    endShape()
    
    frameStart = t
    beginShape()
    for x in range(width):
        y = noise(t)
        y = map(y, 0, 1, height/2, height)
        vertex(x, y)
        t += inc
    
    t = frameStart - inc*10
    endShape()
    print(frameRate)
