
# Convolutional Neural Networks
 ###### A set of fun programs with applications of Convolutional Neural Networks

## Neural Style Transfer
In this directory, there is an interactive python notebook which walks through the steps of building a neural style transfer script with TensorFlow. The code was based off the code found at the [TensorFlow documentation for neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer). The style model works quite well with the oil painting style and tends to preserve colour in the water color style. The transition of the style output is shown in the gif below, with very minute changes which you can spot if you look closely.

<img src="https://raw.githubusercontent.com/sbalan7/ConvNets/master/Neural%20Style%20Transfer/Images/outputs/rotunda-water-color.gif" width="200" height="200" />

Also given in the module is reusable model from the TensorFlow hub, which produces some rather different images with way more emphasis on the style's colors, as shown below.
### TensorFlow Hub NST Algorithm 
Old Version
<img src="https://raw.githubusercontent.com/sbalan7/ConvNets/master/Neural%20Style%20Transfer/Images/outputs/rotunda-water-color(1).png" width="200" height="200" />
New Version
<img src="https://raw.githubusercontent.com/sbalan7/ConvNets/master/Neural%20Style%20Transfer/Images/outputs/rotunda-water-color(2).png" width="200" height="200" />

The directory also has some style images and some other images to test the program with, though you are free to try your own.

## Visualizing Feature Maps
In this we again take the image of the BITS Pilani Rotunda and pass it through the VGG19 architechture and plot out the feature maps which it generates while running the image through the model. The feature map from the last convolutional layer in the first block is here.

<img src="https://raw.githubusercontent.com/sbalan7/ConvNets/master/Visualizing%20Feature%20Maps/fmap.png" data-canonical-src="https://raw.githubusercontent.com/sbalan7/ConvNets/master/Visualizing%20Feature%20Maps/fmap.png" width="576" height="342" />
