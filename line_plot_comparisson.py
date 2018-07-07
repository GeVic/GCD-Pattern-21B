from PIL import Image

def intensities(x,y):
      for a in values:
        for b in values:
          if a*x == b*y:
            return (a, a, a)
      white = 255 
      return (white, white, white)
             

if __name__=='__main__':
  dim = 300
  # let say the range in between 1-5
  values = list(range(1,5)) 
  intensity_matrix = []
  # Equation to be plotted here is ax = by
  for x in range(1, dim+1):
    for y in range(1, dim+1):
      intensity_matrix.append(intensities(x,y))
  
  # create image
  image = Image.new('RGB', (dim, dim))
  image.putdata(intensity_matrix)
  image.save('line.png')
