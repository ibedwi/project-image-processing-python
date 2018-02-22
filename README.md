# README

## EQUATION USED
### RGB to Grayscale
![eq_rgb2grayscale_1](https://latex.codecogs.com/gif.latex?y%20%3D%200.299R%20&plus;%200.587G%20&plus;%200.144B)

### RGB to Binary
Before using the equation, first convert the RGB image into Grayscale image.

![eq_rgb2bw_1](https://latex.codecogs.com/gif.latex?y%27%20%3D%20%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%201%2C%20%26%20y%20%5Cgeq%20threshold%5C%5C%200%2C%20%26%20otherwise%20%5Cend%7Bmatrix%7D%5Cright.) 

### RGB to CMYK
#### RGB to CMY
![eq1_1](https://latex.codecogs.com/gif.latex?C%20%3D%201%20-%20%5Cleft%20%28%20%5Cfrac%7BR%7D%7B255%7D%20%5Cright%20%29)

![eq1_2](https://latex.codecogs.com/gif.latex?M%20%3D%201%20-%20%5Cleft%20%28%20%5Cfrac%7BG%7D%7B255%7D%20%5Cright%20%29)

![eq1_3](https://latex.codecogs.com/gif.latex?Y%20%3D%201%20-%20%5Cleft%20%28%20%5Cfrac%7BB%7D%7B255%7D%20%5Cright%20%29)

#### RGB to CMYK 

![eq2_1](https://latex.codecogs.com/gif.latex?K%20%3D%201%20-%20%5Cmax%20%5Cleft%20%28%20C%2CM%2CY%20%5Cright%20%29)

![eq2_2](https://latex.codecogs.com/gif.latex?C_%7BCMYK%7D%20%3D%20%5Cfrac%7B%5Cleft%20%28C_%7BCMY%7D%20-%20K%20%5Cright%20%29%7D%7B%5Cleft%20%28%201%20-%20K%20%5Cright%20%29%7D)

![eq2_3](https://latex.codecogs.com/gif.latex?M_%7BCMYK%7D%20%3D%20%5Cfrac%7B%5Cleft%20%28M_%7BCMY%7D%20-%20K%20%5Cright%20%29%7D%7B%5Cleft%20%28%201%20-%20K%20%5Cright%20%29%7D)

![eq2_4](https://latex.codecogs.com/gif.latex?Y_%7BCMYK%7D%20%3D%20%5Cfrac%7B%5Cleft%20%28Y_%7BCMY%7D%20-%20K%20%5Cright%20%29%7D%7B%5Cleft%20%28%201%20-%20K%20%5Cright%20%29%7D)

### RGB to YCrCb

Original Equation :

![eq3_1](https://latex.codecogs.com/gif.latex?Y%20%3D%20%5Cleft%20%28%200.299%20%5Ctimes%20R%20%5Cright%20%29%20&plus;%20%5Cleft%20%28%200.587%20%5Ctimes%20G%20%5Cright%20%29%20&plus;%20%5Cleft%20%28%200.114%20%5Ctimes%20B%20%5Cright%20%29)

![eq3_2](https://latex.codecogs.com/gif.latex?U%20%3D%20B%20-%20Y)

![eq3_3](https://latex.codecogs.com/gif.latex?V%20%3D%20R%20-%20Y)

![eq3_4](https://latex.codecogs.com/gif.latex?Cb%20%3D%20U%20/%20%5Cleft%20%28%201.772%20&plus;%200.5%20%5Cright%20%29)

![eq3_5](https://latex.codecogs.com/gif.latex?Cr%20%3D%20V%20/%20%5Cleft%20%28%201.402%20&plus;%200.5%20%5Cright%20%29)

Equation used to represent YCrCb in 0-255 range :

![eq4_1](https://latex.codecogs.com/gif.latex?Y%20%3D%2016%20&plus;%20%5Cleft%20%28%20%5Cfrac%7B%5Cleft%20%28%2065.481%20%5Ctimes%20R%20%5Cright%20%29%7D%7B256%7D%20&plus;%20%5Cfrac%7B%5Cleft%20%28%20128.553%20%5Ctimes%20G%20%5Cright%20%29%7D%7B256%7D%20&plus;%20%5Cfrac%7B%5Cleft%20%28%2024.966%20%5Ctimes%20B%20%5Cright%20%29%7D%7B256%7D%20%5Cright%20%29)

![eq4_2](https://latex.codecogs.com/gif.latex?Cb%20%3D%20128%20&plus;%20%5Cleft%20%28%20%5Cfrac%7B%5Cleft%20%28%20-37.797%20%5Ctimes%20R%20%5Cright%20%29%7D%7B256%7D%20-%20%5Cfrac%7B%5Cleft%20%28%2074.203%20%5Ctimes%20G%20%5Cright%20%29%7D%7B256%7D%20&plus;%20%5Cfrac%7B%5Cleft%20%28%20112.0%20%5Ctimes%20B%20%5Cright%20%29%7D%7B256%7D%20%5Cright%20%29)

![eq4_3](https://latex.codecogs.com/gif.latex?Cb%20%3D%20128%20&plus;%20%5Cleft%20%28%20%5Cfrac%7B%5Cleft%20%28%20112.0%20%5Ctimes%20R%20%5Cright%20%29%7D%7B256%7D%20-%20%5Cfrac%7B%5Cleft%20%28%2093.786%20%5Ctimes%20G%20%5Cright%20%29%7D%7B256%7D%20-%20%5Cfrac%7B%5Cleft%20%28%2018.214%20%5Ctimes%20B%20%5Cright%20%29%7D%7B256%7D%20%5Cright%20%29)

### RGB to HSV
The R,G,B values are divided by 255 to change the range from 0..255 to 0..1:

![eq5_1](https://latex.codecogs.com/gif.latex?R%27%20%3D%20R/255)

![eq5_2](https://latex.codecogs.com/gif.latex?G%27%20%3D%20G/255)

![eq5_3](https://latex.codecogs.com/gif.latex?B%27%20%3D%20B/255)

![eq5_4](https://latex.codecogs.com/gif.latex?Cmax%20%3D%20%5Cmax%28R%27%2CG%27%2CB%27%29)

![eq5_5](https://latex.codecogs.com/gif.latex?Cmin%20%3D%20%5Cmin%28R%27%2CG%27%2CB%27%29)

![eq5_6](https://latex.codecogs.com/gif.latex?%5CDelta%20%3D%20Cmax%20-%20Cmin)

Hue calculation : 

![eq5_7](https://latex.codecogs.com/gif.latex?H%20%3D%20%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%200%5E%7B%5Ccirc%7D%20%26%20%5CDelta%20%3D%200%5C%5C%2060%5E%7B%5Ccirc%7D%20%5Ctimes%20%5Cleft%20%28%20%5Cfrac%7BG%27-B%27%7D%7B%5CDelta%7D%20%5Cmod%206%5Cright%20%29%26%20%2C%20Cmax%20%3D%20R%27%5C%5C%2060%5E%7B%5Ccirc%7D%20%5Ctimes%20%5Cleft%20%28%20%5Cfrac%7BB%27-R%27%7D%7B%5CDelta%7D%20&plus;2%5Cright%20%29%26%20%2C%20Cmax%20%3D%20G%27%5C%5C%2060%5E%7B%5Ccirc%7D%20%5Ctimes%20%5Cleft%20%28%20%5Cfrac%7BR%27-G%27%7D%7B%5CDelta%7D%20&plus;4%5Cright%20%29%26%20%2C%20Cmax%20%3D%20B%27%5C%5C%20%5Cend%7Bmatrix%7D%5Cright.)

Saturation calculation :

![eq5_8](https://latex.codecogs.com/gif.latex?S%20%3D%20%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%200%20%26%20%2CCmax%20%3D%200%5C%5C%20%5Cfrac%7B%5CDelta%7D%7BC_%7Bmax%7D%7D%20%26%20%2C%20Cmax%20%5Cneq%200%20%5Cend%7Bmatrix%7D%5Cright.)

Value calculation : 

![eq5_9](https://latex.codecogs.com/gif.latex?V%20%3D%20Cmax)
