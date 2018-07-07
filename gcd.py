from math import gcd
from PIL import Image

def matrix_init():
    # An,m = gcd(n, m) for 100*100 matrix
    for i in range(dim):
        for j in range(dim):
            result = int(255 - (gcd(i+1,j+1)/100)*255)
            intensity_matrix.append((result, result, result))


if __name__=="__main__":
    
    # dimension
    dim = 300
    # Initializing numpy array
    intensity_matrix = []
    matrix_init()
    # create image
    image = Image.new('RGB', (dim, dim))
    image.putdata(intensity_matrix)
    image.save('gcd.png')
    
