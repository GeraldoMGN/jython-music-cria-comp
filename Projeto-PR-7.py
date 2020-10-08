from gui import *
from music import *
from random import *
from math import *

Play.setInstrument(ROCK_ORGAN)

keys = dict([
    (VK_Q, (C4, 0)),
    (VK_2, (CS4, 1)),
    (VK_W, (D4, 2)),
    (VK_3, (DS4, 3)),
    (VK_E, (E4, 4)),
    (VK_R, (F4, 5)),
    (VK_5, (FS4, 6)),
    (VK_T, (G4, 7)),
    (VK_6, (GS4, 8)),
    (VK_Y, (A4, 9)),
    (VK_7, (AS4, 10)),
    (VK_U, (B4, 11)),
    (VK_I, (C5, 12)),
    (VK_9, (CS5, 13)),
    (VK_O, (D5, 14)),
    (VK_0, (DS5, 15)),
    (VK_P, (E5, 16))
])
      
class SynthWaveSynth:
   def __init__(self, width):
      self.width = width
      self.height = width * 2 / 3   
   
      # Graphics
      ## Setup the display
      self.display = Display("SynthWave Synth", self.width, self.height)
      self.display.setColor( Color(27, 16, 46) )
      self.display.onKeyDown( self.beginNote )
      self.display.onKeyUp( self.endNote )
      ## Lines
      self.horizontal_lines = []
      self.polygons = []
      ## Images
      self.background = Icon("background.jpg", self.width, self.height / 2)
      
      self.key_icons = [
         Icon("keys/q.png", 25, 25),
         Icon("keys/2.png", 25, 25),
         Icon("keys/w.png", 25, 25),
         Icon("keys/3.png", 25, 25),
         Icon("keys/e.png", 25, 25),
         Icon("keys/r.png", 25, 25),
         Icon("keys/5.png", 25, 25),
         Icon("keys/t.png", 25, 25),
         Icon("keys/6.png", 25, 25),
         Icon("keys/y.png", 25, 25),
         Icon("keys/7.png", 25, 25),
         Icon("keys/u.png", 25, 25),
         Icon("keys/i.png", 25, 25),
         Icon("keys/9.png", 25, 25),
         Icon("keys/o.png", 25, 25),
         Icon("keys/0.png", 25, 25),
         Icon("keys/p.png", 25, 25),
      ]
      self.add_to_display(self.key_icons)
      
      self.keysPressed = []
      
      self.y_offset = 0.0
      self.timer = Timer(33, self.render)
      self.timer.start()
      
   def render(self):
      self.y_offset -= 1.0
      last_y = self.y_offset
      distance = 0
      ys = []
      for line in self.horizontal_lines:
         y = distance + last_y
         ys.append(self.height - y)
         last_y = y
         distance = (self.height / 2.0 - last_y) / 5.0
      
      for line_index in range(len(self.horizontal_lines)):
         self.display.move(self.horizontal_lines[line_index], 0, int(ys[line_index]) - 5)
      
      if ys[1] >= self.height:
         self.y_offset = 0.0

   def add_to_display(self, key_icons):
      # Lines
      ## Horizontal lines
      line_color = Color(165, 96, 190)
      keys = 17
      for x in range(keys + 1):
         line = Line(self.width / keys * x, self.height, self.width / 2, self.height / 3, line_color, 1)
         self.display.add(line)
      
      for x in range(keys):
         polygonX = []
         polygonX.append(self.width / keys * x)
         polygonX.append(self.width / 2)
         polygonX.append(self.width / keys * (x + 1))
         polygonY = []
         polygonY.append(self.height)
         polygonY.append(self.height / 3)
         polygonY.append(self.height)
         
         polygon = Polygon(polygonX, polygonY, Color(255, 255, 255, 0), True, 0)
         self.polygons.append(polygon)
         self.display.add(polygon)
      
      ## Vertical lines
      y_offset = 0
      distance = self.height / 10.0
      last_y = 0
      while distance > 1:
         y = -y_offset + distance + last_y
         line = Line(0, 0, self.width, 0, line_color, 1)
         self.horizontal_lines.append(line)
         last_y = y
         distance = 2.41/3.0 * distance
         self.display.add(line)
      
      self.display.add(self.background)
      
      for x in range(1, keys + 1):
         self.display.add(
             key_icons[x - 1], 
             (x * (self.width / (keys + 1))) - 12, 
             self.height - 50)
         

   def beginNote(self, key):
      print "Key pressed is " + str(key)
   
      if key in keys:
            Play.noteOn( keys[key][0] )
            self.keysPressed.append( key )
            self.polygons[keys[key][1]].setColor(Color(255, 255, 255, 70))
            self.key_icons[keys[key][1]].setSize(50, 50)
            self.display.move(
                self.key_icons[keys[key][1]], 
                ((keys[key][1] + 1) * (self.width / (len(keys) + 1))) - 25, 
                self.height - 62)
 
   def endNote(self, key):
      if key in keys:
            Play.noteOff( keys[key][0] )
            filter(lambda a: a != key, self.keysPressed)
            self.polygons[keys[key][1]].setColor(Color(255, 255, 255, 0))
            self.key_icons[keys[key][1]].setSize(25, 25)
            self.display.move(
                self.key_icons[keys[key][1]], 
                ((keys[key][1] + 1) * (self.width / (len(keys) + 1))) - 12, 
                self.height - 50)

synthwave = SynthWaveSynth(1000)