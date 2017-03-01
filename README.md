# Image Style Blending with Convolutional Neural Network
Project for E4990 Introduction to Data Science Industry
### Team Members: Yuanqing Hong, Claire Lee, Weiyi Li
#### Role: ???
### Tools: Python, Tensor Flow, Jupiterbook

## Motivation

Inspired by the game ['Machine Learning and Cats'](http://www.atlasobscura.com/articles/cat-computer-program-drawing?utm_source=facebook.com&utm_medium=atlas-page) provided by Dr. Goldman, we were tring to figure out the mechanism behind it.

<p align="center">
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/machine_learning_cats.png?raw=true" width="50%"/>
</p>  
<p align="center">
Fig.1. Example of machine learning for cats
<a href="http://www.atlasobscura.com/articles/cat-computer-program-drawing?utm_source=facebook.com&utm_medium=atlas-page">(Reference)</a>
</p>


After a lot of research, we finally found this is based on an algorithm for combining the content of one image with the style of another image using convolutional neural networks.

Here is the related paper we found:
- [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576)
- [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://arxiv.org/pdf/1603.08155v1.pdf)
- [Combining Markov Random Fields and Convolutional Neural Networks for Image Synthesis](https://arxiv.org/pdf/1601.04589.pdf)
- [Instance Normalization: The Missing Ingredient for Fast Stylization](https://arxiv.org/abs/1607.08022)

[](Comment In this paper, a kind of deep neural network was provided and successful blend the object with an artistic sytle.  )

<p align="center"> 
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/starry_night.jpg" height="223px"> 
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/hoover_tower_night.jpg" height="223px">  
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/starry_stanford_bigger.png" width="710px">  
</p>
<p align="center">
Fig.2. Image blending result
<a href="https://arxiv.org/abs/1508.06576">(Reference)</a>
</p>

In these paper, a kind of deep neural network was provided and successfully blent the object with an artistic sytle. An illustration is provided, in this example, a building is blend with several styles and generated blended images. In this way, we can blend any subject with artistic styles to get a artistic painting.

**Subject**

<p align="center">
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/subject.jpg?raw=true" width="20%"/>
</p>


**Styles**
<p align="center">
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/style_b.png?raw=true" width="18%"/>
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/style_c.png?raw=true" width="18%"/>
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/style_d.png?raw=true" width="18%"/>
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/style_e.png?raw=true" width="18%"/>
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/style_f.png?raw=true" width="18%"/>
</p>

**Outputs**
<p align="center">
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/blending_b.png?raw=true" width="18%"/>
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/blending_c.png?raw=true" width="18%"/>
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/blending_d.png?raw=true" width="18%"/>
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/blending_e.png?raw=true" width="18%"/>
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/blending_f.png?raw=true" width="18%"/>
</p>
<p align="center">
Fig.3. The Reuslt for Several Different Sytle
<a href="https://arxiv.org/abs/1508.06576">(Reference)</a>
</p>

## Goals

### Project description

### Audience
Our intention is to provide a novel artistic painting tool that allows everyone to create their own artistic pictures.
Specifically, it will help painters to inspire their talent and bring a great convenience for illustrators to create illustrations.
### Algorithms

<p align="center">
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/reconstruction_algorithm.png?raw=true" width="60%"/>
</p>
<p align="center">
Fig.4. The Reuslt for Several Different Sytle
<a href="https://arxiv.org/abs/1508.06576">(Reference)</a>
</p>

### Interface
We decide to finish core algorithms in Python at first. And then we may build a website to let user to upload their pictures to generate the blended pictures if time permitted. But there have some problems. Such as how to build a website, how to run the Python script behind the web. These problems need to be solved. 


## Reference
- [CS231n Convolutional Neural Networks for Visual Recognition](http://cs231n.github.io/convolutional-networks/#architectures)
- [ConvNetJS CIFAR-10 demo](http://cs.stanford.edu/people/karpathy/convnetjs/demo/cifar10.html)
