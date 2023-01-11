import numpy as np

image=[]
algo=''
for line in open('input.txt', 'r').readlines():
    if algo=='':
        algo=line
    elif len(line)>1:
        row=[]
        for c in line.strip():
            if c=='#':
                row.append(1)
            else:
                row.append(0)
        image.append(row)
image=np.array(image)
background=0        
for steps in range(50):
    image=np.insert(image, 0, background, axis=1)
    image=np.insert(image, 0, background, axis=1)
    image=np.insert(image, image.shape[1], background, axis=1)
    image=np.insert(image, image.shape[1], background, axis=1)
    image=np.insert(image, 0, background, axis=0)
    image=np.insert(image, 0, background, axis=0)
    image=np.insert(image, image.shape[0], background, axis=0)
    image=np.insert(image, image.shape[0], background, axis=0)
    enh=np.zeros((image.shape[0]-2, image.shape[1]-2), dtype=int)
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            index=0
            if image[i-1,j-1]==1: index+= 100000000
            if image[i-1,j]==1: index+= 10000000 
            if image[i-1,j+1]==1: index+= 1000000 
            if image[i,j-1]==1: index+= 100000 
            if image[i,j]==1: index+= 10000
            if image[i,j+1]==1: index+= 1000 
            if image[i+1,j-1]==1: index+= 100 
            if image[i+1,j]==1: index+= 10 
            if image[i+1,j+1]==1: index+= 1 
            if (algo[int(str(index),2)]=='#'):
                enh[i-1][j-1]=1
    if background==0 and algo[0]=='#':
         background=1
    elif background==1 and algo[int(str("111111111"),2)]=='.':
        background=0
    image=enh 
print(image.sum())