from PIL import Image , ImageOps

raw_img = Image.open("C:\\Users\\dodda\\Downloads\\dinesh 2.jpeg")
print(raw_img.size)
raw_img.show()

gray_img = ImageOps.grayscale(raw_img)
print(gray_img.size)

import numpy as np

img_array = np.asarray(gray_img)
print(img_array.shape)

class Matrices():
    def sharpen_matrix():
        sharpen = [[0,-1,0],[-1,5,-1],[0,-1,0]] 
        sharpen_array=np.array(sharpen).reshape(3,3)
        return sharpen_array
    def outline_matrix():
        outline = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
        outline_array = np.array(outline).reshape(3,3)
        return outline_array
    def emboss_matrix():
        emboss = [[-2,-1,0],[-1,1,1],[0,1,2]]
        emboss_array=np.array(emboss).reshape(3,3)
        return emboss_array
    def sobel_matrix():
        sobel=[[-1,-2,-1],[0,0,0],[1,2,1]]
        sobel_array = np.array(sobel).reshape(3,3)
        return sobel_array

output = [[0 for _ in range(len(img_array[0]))] for _ in range(len(img_array))]

form=int(input('''enter key to select format of prpcessing :
              press 1 to sharpen
                     2 to outline
                     3 to emboss
                     4 to sobel : '''))

def matrix_multiplication(x,y):
    c=0
    for a in range(-1,2):
        for b in range(-1,2):
            if form == 1:
                c=c+((img_array[x+a][y+b])*(Matrices.sharpen_matrix()[a+1][b+1]))
            elif form == 2:
                c=c+((img_array[x+a][y+b])*(Matrices.outline_matrix()[a+1][b+1]))
            elif form == 3:
                c=c+((img_array[x+a][y+b])*(Matrices.emboss_matrix()[a+1][b+1]))
            elif form == 4:
                c=c+((img_array[x+a][y+b])*(Matrices.sobel_matrix()[a+1][b+1]))
            else:
                c = "enter correct format"
            
    return c



for i in range(1,len(img_array)-1):
    for j in range(1,len(img_array[0])-2):
        output[i][j]=matrix_multiplication(i,j)

    
output_matrix=np.array(output)
final_image = Image.fromarray(output_matrix)
final_image.save('final_Image.png')
final_image.show()





