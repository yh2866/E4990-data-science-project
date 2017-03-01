# Image Style Blending with Convolutional Neural Network
Project for E4990 Introduction to Data Science Industry
### Teamm Members: Yuanqing Hong, Claire Lee, Weiyi Li
#### Role: Leader-  ; Researcher-  ; Writer-
### Tools: Python, Tensor Flow, Jupiterbook

## Previous Work

Inspired by the game ['Machine Learning and Cats'](http://www.atlasobscura.com/articles/cat-computer-program-drawing?utm_source=facebook.com&utm_medium=atlas-page) provided by Prof. Goldman, we were tring to figure out the mechanism behind it.

<p align="center">
<img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/machine_learning_cats.png?raw=true" width="50%"/>
</p>

After a lot of research, we finally found this is based on an algorithm for combining the content of one image with the style of another image using convolutional neural networks.

Here is the related paper we found:
- [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576)
- [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://arxiv.org/pdf/1603.08155v1.pdf)

[](Comment In this paper, a kind of deep neural network was provided and successful blend the object with an artistic sytle.  <p align="center"> <img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/starry_night.jpg" height="223px"> <img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/hoover_tower_night.jpg" height="223px">  <img src="https://github.com/yh2866/E4990-data-science-project/blob/master/images/starry_stanford_bigger.png" width="710px">  </p>)


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
