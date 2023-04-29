from varname import nameof
import numpy 
from matplotlib.pyplot import *


def showfeature(xclass, ind, img):
    imageslist = []
    atrr = [m.strip() for m in str(xclass.__init__).splitlines()[1:-1]]
    imgg = img[ind]
    l = 0
    for i in atrr:
        imgg.shape
        xxclass = xclass
        ft = i[1:i.find(')')]
        rtt = f"global imggfunc; imggfunc = {nameof(xxclass)}.{ft}"
        exec(rtt)
        if i.find('Linear') > -1:
            imgg = imgg.reshape(1,-1) 
        imgg = imggfunc(imgg)

        if i.find('Conv') > -1:
            imageslist.append(imgg.reshape(-1,imgg.shape[2]).detach())
        if i.find('Pool') > -1:
            pass
            imageslist.append(imgg.reshape(-1,imgg.shape[2]).detach())

    imageslista = [img[ind].reshape(28,28)]
    for k in imageslist:
        imageslista.append(k)
    ini = 1
    for z in imageslista:
        subplot(1, len(imageslista), ini)
        imshow(z, cmap='gray')
        axis('off')
        ini += 1
    