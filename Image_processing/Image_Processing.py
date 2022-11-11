from PIL import Image , ImageOps
raw_img = Image.open("C:\\Users\\dodda\\Downloads\\dinesh 2.jpeg")
print(raw_img.format)
print(raw_img.size)
print(raw_img.mode)
raw_img.show()

gray_img = ImageOps.grayscale(raw_img)
print(gray_img.format)
print(gray_img.size)
print(gray_img.mode)

import numpy as np
img_array = np.asarray(gray_img)
print(type(img_array))
print(img_array.shape)
print(img_array.ndim)

sharp = [[0,-1,0],
          [-1,5,-1],
          [0,-1,0]] 
sharpen_array=np.array(sharp)
print(sharpen_array.shape,type(sharpen_array))
print(sharpen_array)

print(img_array)
print(img_array.shape,img_array.ndim)

output = [[0 for _ in range(len(img_array[0]))] for _ in range(len(img_array))]

def matrix_multiplication(x,y):
    c=0
    for a in range(-1,2):
        for b in range(-1,2):
            c=c+((img_array[x+a][y+b])*sharpen_array[a+1][b+1])
    return c

for i in range(1,len(img_array)-1):
    for j in range(1,len(img_array[0])-2):
        output[i][j]=matrix_multiplication(i,j)
    
output_matrix=np.array(output)
print(output_matrix.shape,output_matrix.ndim)
print(output_matrix)
final_image = Image.fromarray(output_matrix)
final_image.save('Final_Img.png')
final_image.show()
