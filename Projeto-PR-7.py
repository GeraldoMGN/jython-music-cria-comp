from gui import *
from music import *
from random import *
from math import *

Play.setInstrument(ROCK_ORGAN)
      
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
      self.add_to_display()
      
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

   def add_to_display(self):
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

   def beginNote(self, key):
      print "Key pressed is " + str(key)
 
      if key == VK_Q and key not in self.keysPressed:
         Play.noteOn( C4 )
         self.keysPressed.append( VK_Q )
         self.polygons[0].setColor(Color(255, 255, 255, 70))
      elif key == VK_2 and key not in self.keysPressed:
         Play.noteOn( CS4 )
         self.keysPressed.append( VK_2 )
         self.polygons[1].setColor(Color(255, 255, 255, 70))
      elif key == VK_W and key not in self.keysPressed:
         Play.noteOn( D4 )
         self.keysPressed.append( VK_W )
         self.polygons[2].setColor(Color(255, 255, 255, 70))
      elif key == VK_3 and key not in self.keysPressed:
         Play.noteOn( DS4 )
         self.keysPressed.append( VK_3 )
         self.polygons[3].setColor(Color(255, 255, 255, 70))
      elif key == VK_E and key not in self.keysPressed:
         Play.noteOn( E4 )
         self.keysPressed.append( VK_E )
         self.polygons[4].setColor(Color(255, 255, 255, 70))
      elif key == VK_R and key not in self.keysPressed:
         Play.noteOn( F4 )
         self.keysPressed.append( VK_R )
         self.polygons[5].setColor(Color(255, 255, 255, 70))
      elif key == VK_5 and key not in self.keysPressed:
         Play.noteOn( FS4 )
         self.keysPressed.append( VK_5 )
         self.polygons[6].setColor(Color(255, 255, 255, 70))
      elif key == VK_T and key not in self.keysPressed:
         Play.noteOn( G4 )
         self.keysPressed.append( VK_T )
         self.polygons[7].setColor(Color(255, 255, 255, 70))
      elif key == VK_6 and key not in self.keysPressed:
         Play.noteOn( GS4 )
         self.keysPressed.append( VK_6 )
         self.polygons[8].setColor(Color(255, 255, 255, 70))
      elif key == VK_Y and key not in self.keysPressed:
         Play.noteOn( A4 )
         self.keysPressed.append( VK_Y )
         self.polygons[9].setColor(Color(255, 255, 255, 70))
      elif key == VK_7 and key not in self.keysPressed:
         Play.noteOn( AS4 )
         self.keysPressed.append( VK_7 )
         self.polygons[10].setColor(Color(255, 255, 255, 70))
      elif key == VK_U and key not in self.keysPressed:
         Play.noteOn( B4 )
         self.keysPressed.append( VK_U )
         self.polygons[11].setColor(Color(255, 255, 255, 70))
      elif key == VK_I and key not in self.keysPressed:
         Play.noteOn( C5 )
         self.keysPressed.append( VK_I )
         self.polygons[12].setColor(Color(255, 255, 255, 70))
      elif key == VK_9 and key not in self.keysPressed:
         Play.noteOn( CS5 )
         self.keysPressed.append( VK_9 )
         self.polygons[13].setColor(Color(255, 255, 255, 70))
      elif key == VK_O and key not in self.keysPressed:
         Play.noteOn( D5 )
         self.keysPressed.append( VK_O )
         self.polygons[14].setColor(Color(255, 255, 255, 70))
      elif key == VK_0 and key not in self.keysPressed:
         Play.noteOn( DS5 )
         self.keysPressed.append( VK_0 )
         self.polygons[15].setColor(Color(255, 255, 255, 70))
      elif key == VK_P and key not in self.keysPressed:
         Play.noteOn( E5 )
         self.keysPressed.append( VK_P )
         self.polygons[16].setColor(Color(255, 255, 255, 70))  
 
   def endNote(self, key):
      if key == VK_Q:
         Play.noteOff( C4 )
         self.keysPressed.remove( VK_Q )
         self.polygons[0].setColor(Color(255, 255, 255, 0))
      elif key == VK_2:
         Play.noteOff( CS4 )
         self.keysPressed.remove( VK_2 )
         self.polygons[1].setColor(Color(255, 255, 255, 0))
      elif key == VK_W:
         Play.noteOff( D4 )
         self.keysPressed.remove( VK_W )
         self.polygons[2].setColor(Color(255, 255, 255, 0))
      elif key == VK_3:
         Play.noteOff( DS4 )
         self.keysPressed.remove( VK_3 )
         self.polygons[3].setColor(Color(255, 255, 255, 0))
      elif key == VK_E:
         Play.noteOff( E4 )
         self.keysPressed.remove( VK_E )
         self.polygons[4].setColor(Color(255, 255, 255, 0))
      elif key == VK_R:
         Play.noteOff( F4 )
         self.keysPressed.remove( VK_R )
         self.polygons[5].setColor(Color(255, 255, 255, 0))
      elif key == VK_5:
         Play.noteOff( FS4 )
         self.keysPressed.remove( VK_5 )
         self.polygons[6].setColor(Color(255, 255, 255, 0))
      elif key == VK_T:
         Play.noteOff( G4 )
         self.keysPressed.remove( VK_T )
         self.polygons[7].setColor(Color(255, 255, 255, 0))
      if key == VK_6:
         Play.noteOff( GS4 )
         self.keysPressed.remove( VK_6 )
         self.polygons[8].setColor(Color(255, 255, 255, 0))
      elif key == VK_Y:
         Play.noteOff( A4 )
         self.keysPressed.remove( VK_Y )
         self.polygons[9].setColor(Color(255, 255, 255, 0))
      elif key == VK_7:
         Play.noteOff( AS4 )
         self.keysPressed.remove( VK_7 )
         self.polygons[10].setColor(Color(255, 255, 255, 0))
      elif key == VK_U:
         Play.noteOff( B4 )
         self.keysPressed.remove( VK_U )
         self.polygons[11].setColor(Color(255, 255, 255, 0))
      elif key == VK_I:
         Play.noteOff( C5 )
         self.keysPressed.remove( VK_I )
         self.polygons[12].setColor(Color(255, 255, 255, 0))
      elif key == VK_9:
         Play.noteOff( CS5 )
         self.keysPressed.remove( VK_9 )
         self.polygons[13].setColor(Color(255, 255, 255, 0))
      elif key == VK_O:
         Play.noteOff( D5 )
         self.keysPressed.remove( VK_O )
         self.polygons[14].setColor(Color(255, 255, 255, 0))
      elif key == VK_0:
         Play.noteOff( DS5 )
         self.keysPressed.remove( VK_0 )
         self.polygons[15].setColor(Color(255, 255, 255, 0))
      elif key == VK_P:
         Play.noteOff( E5 )
         self.keysPressed.remove( VK_P )
         self.polygons[16].setColor(Color(255, 255, 255, 0))


synthwave = SynthWaveSynth(800)