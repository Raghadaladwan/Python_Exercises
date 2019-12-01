# Exercise 1 ___________________________________________________

#1. Use List to find following statistics

import statistics as statistics
import random
import math
from PIL import Image , ImageDraw , ImageFilter


x=[3,1.5,4.5,6.75,2.25,5.75,2.25]
print(statistics.mean(x))
print(statistics.harmonic_mean(x))
print(statistics.median(x))
print(statistics.median_high(x))
print(statistics.median_low(x))
print(statistics.median_grouped(x))
print(statistics.mode(x))
print(statistics.pstdev(x))
print(statistics.pvariance(x))
print(statistics.stdev(x))
print(statistics.variance(x))
print()

# Exercise 2 ___________________________________________________
# 2.  Use randomlibrary to generate the following :


print( random.random() )
print ( random.randrange(10) )
print ( random.choice(['Ali', 'Khaleed', 'Hussam']) )
print ( random.sample(range(1000), 10) )
print ( random.choice('OrangeAcademy') )
items = [1,5,8,9,2,4]
random.shuffle(items)
print ( random.randint(20, 30) )
print ( random.randrange(1000,2111,5))
print  ( random.uniform(10000, 11000))
print()


# Exercise 3 ___________________________________________________
# 3. Find the following :

print ('pi: %.40f' % math.pi)
num = 30
print ('arcsine(%.1f)    = %5.2f' % (num, math.sin(num)))
num = 200
print ('arccosine(%.1f)  = %5.2f' % (num, math.cos(num)))
num = 180
print ('arctangent(%.1f) = %5.2f' % (num, math.tan(num)))
num = 10.8
print(math.floor(num))
print(math.ceil(num))
print()


# Exercise 4 ___________________________________________________
# 4. Download two images and one mask from the internet and apply the following into the image and show the results:



# 1 Show image and print format, size , mode
imageTwo = Image.open('cat2.jpg')
image = Image.open('cat.jpg').resize(imageTwo.size)


print(image.format , image.size , image.mode)

image.show()




# 2 Apply image transpose(Image.FLIP_TOP_BOTTOM)

imageFlip = image.transpose(Image.FLIP_TOP_BOTTOM)

imageFlip.show()



# 3 Converts to greyscale_image

greyscaleImage = image.convert('L')

greyscaleImage.show()



# 4 Crop((0,0,50,50)) the image

cropped = image.crop((0,0,50,50))

cropped.show()



# 5 Draw two cross lines and add your name to the image

drawone=ImageDraw.Draw(image)
drawone.line((0,0)+image.size,fill=(255,255,255))
drawone.line((0,image.size[1],image.size[0],0),fill=(255,255,255))
drawone.text((image.size[0]/2- image.size[0]/2,image.size[1]/2+20),"RAGHAD",fill=(255,255,0))

drawTwo=ImageDraw.Draw(imageTwo)
drawTwo.line((0,0)+imageTwo.size,fill=(255,255,255))
drawTwo.line((0,imageTwo.size[1],imageTwo.size[0],0),fill=(255,255,255))
drawTwo.text((imageTwo.size[0]/2- imageTwo.size[0]/2,imageTwo.size[1]/2+20),"RAGHAD",fill=(255,255,0))

image.show()
imageTwo.show()



# 6 Apply the following filters and show result :

newImage = imageTwo.filter(ImageFilter.EDGE_ENHANCE)
newImage.show()

newImage = imageTwo.filter(ImageFilter.FIND_EDGES)
newImage.show()

newImage = image.filter(ImageFilter.SMOOTH)
newImage.show()

newImage = image.filter(ImageFilter.SHARPEN)
newImage.show()



# 7 Apply blend function to the image and show the result

alpha = 0.5
Image.blend(image , imageTwo , alpha).save(
    'New.jpg'.format(alpha))

newOne=Image.open('New.jpg')
newOne.show()




# 8 Apply filter(ImageFilter.BLUR) and show the result

imageBlur = image.filter(ImageFilter.BLUR)
imageBlur.show()




# 9 Apply thumbnail((128,128)) and show the result

image.thumbnail((128,128))

#imageThumbnail.save(imageThumbnail.jpg)
image.show()





# 10 Apply image.rotate(90) and show the result

rotated= image.rotate(90)
rotated.show()




# 11 Composite (image , imageTow , mask)
mask = Image.open('horse_r.png').convert("L").resize(image.size)

imageComposite= Image.composite(image, imageTwo, mask)
imageComposite.show()