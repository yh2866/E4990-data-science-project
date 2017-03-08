# Image Style Transfer using Convolutional Neural Networks
Project for E4990 Introduction to Data Science Industry
### Team Members: Yuanqing Hong, Claire Lee, Weiyi Li
#### Role: Leader(Yuanqing Hong), Mathematical Part(Claire Lee), Programming Part(Weiyi Li)
### Tools: Python, Tensor Flow, Jupiterbook, [Flask](http://flask.pocoo.org/)

## Motivation

Inspired by the game ['Machine Learning and Cats'](http://www.atlasobscura.com/articles/cat-computer-program-drawing?utm_source=facebook.com&utm_medium=atlas-page) provided by Dr. Goldman, we were tring to figure out the mechanism behind it.

<p align="center">
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/machine_learning_cats.png?raw=true" width="50%"/>
</p>  
<p align="center">
Fig.1. An example of machine learning for cats
<a href="http://www.atlasobscura.com/articles/cat-computer-program-drawing?utm_source=facebook.com&utm_medium=atlas-page">(Reference)</a>
</p>


After a lot of research, we finally found this is based on an algorithm for combining the content of one image with the style of another image using convolutional neural networks.

Here is the related paper we found:
- [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576)
- [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://arxiv.org/pdf/1603.08155v1.pdf)
- [Combining Markov Random Fields and Convolutional Neural Networks for Image Synthesis](https://arxiv.org/pdf/1601.04589.pdf)
- [Instance Normalization: The Missing Ingredient for Fast Stylization](https://arxiv.org/abs/1607.08022)
- [Image Style Transfer Using Convolutional Neural Networks](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)


<p align="center"> 
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/blending_1.png" width="49%"> 
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/blending_2.png" width="47.5%"> 
</p>
<p align="center">
Fig.2. Blending results from paper
<a href="https://arxiv.org/abs/1508.06576">(Reference)</a>
</p>

In these paper, a kind of deep neural network was provided and successfully blent the object with an artistic sytle. An illustration is provided, in this example, a building is blend with several styles and generated blended images. In this way, we can blend any subject with artistic styles to get a artistic painting.

[](Comment In this paper, a kind of deep neural network was provided and successful blend the object with an artistic sytle.  **Subject** <p align="center"> <img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/subject.jpg?raw=true" width="20%"/> </p> **Styles** <p align="center"> <img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/style_b.png?raw=true" width="18%"/> <img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/style_c.png?raw=true" width="18%"/> <img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/style_d.png?raw=true" width="18%"/> <img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/style_e.png?raw=true" width="18%"/> <img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/style_f.png?raw=true" width="18%"/> </p> **Outputs** <p align="center"> <img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/blending_b.png?raw=true" width="18%"/> <img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/blending_c.png?raw=true" width="18%"/> <img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/blending_d.png?raw=true" width="18%"/> <img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/blending_e.png?raw=true" width="18%"/> <img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/blending_f.png?raw=true" width="18%"/> </p> <p align="center"> Fig.3. The Reuslt for Several Different Sytle <a href="https://arxiv.org/abs/1508.06576">(Reference)</a> </p>)






## Goals

### Project description
#### key words: Deep Learning, Convolutional Neural Networkds, Image Synthesis
<p align="center">
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/description.png" width="80%"/>
</p>
<p align="center">
Fig.3. Content + Style = Result
<a href="http://web.stanford.edu/class/cs20si/lectures/slides_06.pdf">(Reference)</a>
</p>

### Audience
Our intention is to provide a novel artistic painting tool that allows everyone to create their own artistic pictures.
Specifically, it will help painters to inspire their talent and bring a great convenience for illustrators to create illustrations.

### Algorithms

<p align="center">
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/MachineLearningMethodsGraph.jpg" width="80%"/>
</p>
<p align="center">
Fig.4. Methods graph in machine learning
<a href="https://github.com/Columbia-Intro-Data-Science/APMAE4990-/blob/master/pdfs/MachineLearningMethodsGraph.pdf">(Reference)</a>
</p>

In this project, we decide to use Convolutional Neural Networks(CNN) to process images. Convolutional neural network is a type of feed-forward artificial neural network, which are made up of neurons that have learnable weights and biases. Convolutional networks have a bunch of application in the field of image reconization bacause convolutional network architectures make the explicit assumption that the inputs are images, which allows us to encode certain properties into the architecture.




<p align="center">
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/conv_layer.png" width="30%"/>
</p>
<p align="center">
Fig.5. Neurons of a convolutional layer
<a href="https://en.wikipedia.org/wiki/Convolutional_neural_network">(Reference)</a>
</p>

The convolutional layer is the core building block of a CNN. The layer's parameters consist of a set of learnable filters, which have a small receptive field, but extend through the full depth of the input volume.

Here is a regular 3-layer Neural Network. A convolutional network arranges its neurons in three dimensions (width, height, depth), as visualized in one of the layers.
<p align="center">
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/three_layer.png" width="60%"/>
</p>
<p align="center">
Fig.6. A 3-layer neural network
<a href="http://cs231n.github.io/convolutional-networks/#architectures">(Reference)</a>
</p>

Below is a running demo of a CONV layer. The visualization below iterates over the output activations (green), and shows that each element is computed by elementwise multiplying the highlighted input (blue) with the filter (red), summing it up, and then offsetting the result by the bias.
<p align="center">
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/recording.gif" width="60%"/>
</p>
<p align="center">
Fig.7. Convolution demo
<a href="http://cs231n.github.io/convolutional-networks/#architectures">(Reference)</a>
</p>

The above explaination is fouces on 3-layer conventional network, however, in the paper, it presented a 5-layer conventional network to improve performance.
<p align="center">
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/reconstruction_algorithm.png?raw=true" width="60%"/>
</p>
<p align="center">
Fig.8. Five-layers neural network presented in paper
<a href="https://arxiv.org/abs/1508.06576">(Reference)</a>
</p>

### Interface
We decide to finish core algorithms in Python at first. And then we may build a website to let user to upload their pictures to generate the blended pictures if time permitted. But there have some problems. Such as how to build a website, how to run the Python script behind the web. These problems need to be solved. 


## Reference
- [CS231n Convolutional Neural Networks for Visual Recognition](http://cs231n.github.io/convolutional-networks/#architectures)
- [ConvNetJS CIFAR-10 demo](http://cs.stanford.edu/people/karpathy/convnetjs/demo/cifar10.html)
- [Convolutional Neural Networks + Neural Style Transfer](http://web.stanford.edu/class/cs20si/lectures/slides_06.pdf)
