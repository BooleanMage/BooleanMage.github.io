---
layout: default
---

# Color Space

## Mechanism

### visible spectrum
Human eyes have two kinds of light sensitive cells, rod cell and cone cell.  
Cone cell can detect light in the visible spectrum.  
But human only have three types of cone cell, which are red, green, blue.  
Thus, when there are lots of lights combined with different wavelength, human brain will interpolate the color between red and blue.  
However, if a wavelength of a light is combined with red and blue, the problem is that the color should not be green.  
To deal with this problem, human brain create Magenta.

Reference: [这个世界上根本不存在紫色！ ( 眼见为识)](https://www.youtube.com/watch?v=vv79wigS-4I)

Rod cell is sensitive to luminance.  
When there is dark, rod cell can see boundary of objects.

### sensitivity
Green > Red > Blue
<img src="https://qph.cf2.quoracdn.net/main-qimg-de71b9bcbb3a8503ea1b8c968a9f2b29" Height="480" />

## Color Space
Like coordinate systems may be Cartesian coordinate system or Polar coordinate system.  
Color Space also has lots of coordinate systems.

## RGB-CMYK
RGB color model is an additive color model.  

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Barn_grand_tetons_rgb_separation.jpg/320px-Barn_grand_tetons_rgb_separation.jpg" />

CMYK is a subtractive color model,  
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/CMYK_color_swatches.svg/150px-CMYK_color_swatches.svg.png" />
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/CMYK_subtractive_color_mixing.svg/150px-CMYK_subtractive_color_mixing.svg.png" />

## CIE Space
CIE (International Commission on Illumination) is human color vision.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/CIE1931xy_gamut_comparison.svg/800px-CIE1931xy_gamut_comparison.svg.png" Height="480" />
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Colorspace.png/220px-Colorspace.png" Height="480" />


### YUV Space
Due to rod cell, human eye is more sensitive at grayscale.  
Thus, in traditional camera space will try to seprate gray and other color.  
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Barn-yuv.png/200px-Barn-yuv.png" />

RGB and YUV is able to calculate by martix.  
https://en.wikipedia.org/wiki/YUV


### HSL, HSV Space
A little like YUV. HSL and HSV also has an axis is lightness.  
In HSL or HSV, the H is Hue which using 0 to 360 degree to represent all colors.
S is Saturation.   
L is Lightness.  
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Hsl-hsv_models.svg/290px-Hsl-hsv_models.svg.png" />

### CIE-LAB space
A little like YUV, LAB space also has an L-axis is lightness.  
AB is like XY coordination.  
The most important is that it is also CIE, human eye sensitive.

<img src="https://i.imgur.com/sTDteRp.jpg" />
<img src="https://sensing.konicaminolta.asia/wp-content/uploads/2018/09/Apple%20ab%20Chart.jpg" />


---
tags:
  - [[Color]]
  - [[Biology]]
  - [[Physics]]
  - [[眼见为识]]
  
---