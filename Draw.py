from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import base64

class Draw():
    offsetH = 0
    offsetW = 10
    sizeCard = 85,118
    
    def importarImage(self,name):
      return Image.open(str(Path().absolute())+'\\images\\'+name+'.png', 'r')
    
    def draw(self,cardNames,name="out"):
      img = Image.new('RGB', (445, 118), color = (255, 255, 255))
      cards = map(self.importarImage,cardNames)
      i = 0
      for card in cards:
          card.thumbnail(self.sizeCard, Image.ANTIALIAS)
          img.paste(card, [i*(self.offsetW+card.size[0]),self.offsetH])
          i+=1
      path = str(Path().absolute())+"\\out\\"+str(name)+'.png'
      img.save(path)
      return path
