# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request

Dict = {


( 0 , 0 ): [
( 0.344444444 , 1 ),
( 0.262962963 , 5 ),
( 0.406481481 , 6 ),
( 0.271296296 , 7 ),
( 0.314814815 , 9 ),
( 0.332407407 , 10 ),
( 0.387962963 , 13 ),
( 0.446296296 , 14 ),
( 0.237037037 , 17 ),
( 0.361111111 , 18 ),
( 0.271296296 , 19 ),
( 0.327777778 , 20 ),
( 0.010185185 , 22 ),
( 0.446296296 , 23 ),
( 0.413888889 , 24 ),
( 0.324074074 , 25 ),
( 0.17037037 , 26 ),
( 0.262037037 , 28 ),
( 0.291666667 , 30 ),
( 0.375 , 32 ),
( 0.37037037 , 33 ),
( 0.776851852 , 34 )],
( 0 , 1 ): [
( 0.800925926 , 1 ),
( 0.437962963 , 5 ),
( 0.439814815 , 6 ),
( 0.422222222 , 7 ),
( 0.425 , 9 ),
( 0.427777778 , 10 ),
( 0.946296296 , 13 ),
( 1.126851852 , 14 ),
( 0.387962963 , 17 ),
( 0.77037037 , 18 ),
( 0.787037037 , 19 ),
( 0.537037037 , 20 ),
( 0.039814815 , 22 ),
( 0.768518519 , 23 ),
( 0.606481481 , 24 ),
( 0.684259259 , 25 ),
( 0.349074074 , 26 ),
( 0.501851852 , 28 ),
( 0.409259259 , 30 ),
( 0.619444444 , 32 ),
( 0.381481481 , 33 ),
( 0.497222222 , 34 )],
( 0 , 2 ): [
( 1.709259259 , 1 ),
( 1.413888889 , 5 ),
( 0.851851852 , 6 ),
( 0.849074074 , 7 ),
( 0.788888889 , 9 ),
( 0.759259259 , 10 ),
( 1.671296296 , 13 ),
( 2.6 , 14 ),
( 0.815740741 , 17 ),
( 1.75462963 , 18 ),
( 1.337037037 , 19 ),
( 0.928703704 , 20 ),
( 0.023148148 , 22 ),
( 1.473148148 , 23 ),
( 0.892592593 , 24 ),
( 1.085185185 , 25 ),
( 0.548148148 , 26 ),
( 1.037037037 , 28 ),
( 0.67962963 , 30 ),
( 1.10462963 , 32 ),
( 0.862037037 , 33 ),
( 0.973148148 , 34 )],
( 0 , 3 ): [
( 0.739814815 , 1 ),
( 0.394444444 , 5 ),
( 0.52962963 , 6 ),
( 0.448148148 , 7 ),
( 0.712037037 , 9 ),
( 0.42962963 , 10 ),
( 0.95462963 , 13 ),
( 1.669444444 , 14 ),
( 0.515740741 , 17 ),
( 1.331481481 , 18 ),
( 0.916666667 , 19 ),
( 0.461111111 , 20 ),
( 0.060185185 , 22 ),
( 1.275925926 , 23 ),
( 0.648148148 , 24 ),
( 0.875925926 , 25 ),
( 0.353703704 , 26 ),
( 0.869444444 , 28 ),
( 0.636111111 , 30 ),
( 0.927777778 , 32 ),
( 0.663888889 , 33 ),
( 0.833333333 , 34 )],
( 1 , 0 ): [
( 0.324074074 , 1 ),
( 0.297222222 , 5 ),
( 0.243518519 , 6 ),
( 0.175925926 , 7 ),
( 0.384259259 , 9 ),
( 0.25462963 , 10 ),
( 0.391666667 , 13 ),
( 0.465740741 , 14 ),
( 0.264814815 , 17 ),
( 0.327777778 , 18 ),
( 0.268518519 , 19 ),
( 0.314814815 , 20 ),
( 0.001851852 , 22 ),
( 0.510185185 , 23 ),
( 0.378703704 , 24 ),
( 0.364814815 , 25 ),
( 0.208333333 , 26 ),
( 0.326851852 , 28 ),
( 0.327777778 , 30 ),
( 0.431481481 , 32 ),
( 0.503703704 , 33 ),
( 0.825925926 , 34 )],
( 1 , 1 ): [
( 0.802777778 , 1 ),
( 0.440740741 , 5 ),
( 0.4 , 6 ),
( 0.416666667 , 7 ),
( 0.505555556 , 9 ),
( 0.422222222 , 10 ),
( 0.847222222 , 13 ),
( 0.932407407 , 14 ),
( 0.462962963 , 17 ),
( 0.821296296 , 18 ),
( 0.814814815 , 19 ),
( 0.700925926 , 20 ),
( 0.037962963 , 22 ),
( 0.730555556 , 23 ),
( 0.484259259 , 24 ),
( 0.662962963 , 25 ),
( 0.333333333 , 26 ),
( 0.543518519 , 28 ),
( 0.444444444 , 30 ),
( 0.727777778 , 32 ),
( 0.42962963 , 33 ),
( 0.460185185 , 34 )],
( 1 , 2 ): [
( 1.834259259 , 1 ),
( 1.394444444 , 5 ),
( 0.935185185 , 6 ),
( 0.865740741 , 7 ),
( 1.069444444 , 9 ),
( 1.026851852 , 10 ),
( 1.671296296 , 13 ),
( 2.875 , 14 ),
( 0.776851852 , 17 ),
( 1.605555556 , 18 ),
( 1.356481481 , 19 ),
( 0.935185185 , 20 ),
( 0.024074074 , 22 ),
( 1.355555556 , 23 ),
( 1.086111111 , 24 ),
( 1.291666667 , 25 ),
( 0.565740741 , 26 ),
( 1.225925926 , 28 ),
( 0.818518519 , 30 ),
( 1.341666667 , 32 ),
( 0.882407407 , 33 ),
( 0.973148148 , 34 )],
( 1 , 3 ): [
( 0.717592593 , 1 ),
( 0.683333333 , 5 ),
( 0.732407407 , 6 ),
( 0.688888889 , 7 ),
( 0.939814815 , 9 ),
( 0.522222222 , 10 ),
( 0.94537037 , 13 ),
( 1.832407407 , 14 ),
( 0.528703704 , 17 ),
( 1.453703704 , 18 ),
( 1.030555556 , 19 ),
( 0.499074074 , 20 ),
( 0.063888889 , 22 ),
( 1.377777778 , 23 ),
( 0.72962963 , 24 ),
( 1.103703704 , 25 ),
( 0.452777778 , 26 ),
( 0.951851852 , 28 ),
( 0.780555556 , 30 ),
( 1.201851852 , 32 ),
( 0.799074074 , 33 ),
( 0.9 , 34 )],
( 2 , 0 ): [
( 0.314814815 , 1 ),
( 0.293518519 , 5 ),
( 0.425925926 , 6 ),
( 0.294444444 , 7 ),
( 0.552777778 , 9 ),
( 0.416666667 , 10 ),
( 0.405555556 , 13 ),
( 0.536111111 , 14 ),
( 0.211111111 , 17 ),
( 0.446296296 , 18 ),
( 0.337962963 , 19 ),
( 0.259259259 , 20 ),
( 0.000925926 , 22 ),
( 0.54537037 , 23 ),
( 0.513888889 , 24 ),
( 0.375 , 25 ),
( 0.196296296 , 26 ),
( 0.50462963 , 28 ),
( 0.298148148 , 30 ),
( 0.466666667 , 32 ),
( 0.396296296 , 33 ),
( 0.50462963 , 34 )],
( 2 , 1 ): [
( 0.847222222 , 1 ),
( 0.389814815 , 5 ),
( 0.448148148 , 6 ),
( 0.37962963 , 7 ),
( 0.582407407 , 9 ),
( 0.450925926 , 10 ),
( 1.096296296 , 13 ),
( 1.321296296 , 14 ),
( 0.467592593 , 17 ),
( 0.823148148 , 18 ),
( 0.726851852 , 19 ),
( 0.585185185 , 20 ),
( 0.067592593 , 22 ),
( 0.975 , 23 ),
( 0.656481481 , 24 ),
( 0.792592593 , 25 ),
( 0.342592593 , 26 ),
( 0.786111111 , 28 ),
( 0.483333333 , 30 ),
( 0.782407407 , 32 ),
( 0.517592593 , 33 ),
( 0.52962963 , 34 )],
( 2 , 2 ): [
( 1.658333333 , 1 ),
( 1.392592593 , 5 ),
( 0.817592593 , 6 ),
( 0.89537037 , 7 ),
( 1.225 , 9 ),
( 1.041666667 , 10 ),
( 1.744444444 , 13 ),
( 3.092592593 , 14 ),
( 0.72962963 , 17 ),
( 1.821296296 , 18 ),
( 1.662962963 , 19 ),
( 1.137037037 , 20 ),
( 0.049074074 , 22 ),
( 1.490740741 , 23 ),
( 1.14537037 , 24 ),
( 1.671296296 , 25 ),
( 0.730555556 , 26 ),
( 1.248148148 , 28 ),
( 0.97962963 , 30 ),
( 1.289814815 , 32 ),
( 0.914814815 , 33 ),
( 1.060185185 , 34 )],
( 2 , 3 ): [
( 0.969444444 , 1 ),
( 0.711111111 , 5 ),
( 0.777777778 , 6 ),
( 0.776851852 , 7 ),
( 1.130555556 , 9 ),
( 0.578703704 , 10 ),
( 1.083333333 , 13 ),
( 1.934259259 , 14 ),
( 0.585185185 , 17 ),
( 1.474074074 , 18 ),
( 1.001851852 , 19 ),
( 0.566666667 , 20 ),
( 0.038888889 , 22 ),
( 1.366666667 , 23 ),
( 0.849074074 , 24 ),
( 1.385185185 , 25 ),
( 0.659259259 , 26 ),
( 1.008333333 , 28 ),
( 0.963888889 , 30 ),
( 1.436111111 , 32 ),
( 0.824074074 , 33 ),
( 0.962037037 , 34 )],
( 3 , 0 ): [
( 0.463888889 , 1 ),
( 0.230555556 , 5 ),
( 0.414814815 , 6 ),
( 0.365740741 , 7 ),
( 0.475925926 , 9 ),
( 0.474074074 , 10 ),
( 0.488888889 , 13 ),
( 0.630555556 , 14 ),
( 0.284259259 , 17 ),
( 0.641666667 , 18 ),
( 0.452777778 , 19 ),
( 0.333333333 , 20 ),
( 0.025 , 22 ),
( 0.482407407 , 23 ),
( 0.388888889 , 24 ),
( 0.461111111 , 25 ),
( 0.290740741 , 26 ),
( 0.489814815 , 28 ),
( 0.402777778 , 30 ),
( 0.564814815 , 32 ),
( 0.466666667 , 33 ),
( 0.512962963 , 34 )],
( 3 , 1 ): [
( 0.791666667 , 1 ),
( 0.411111111 , 5 ),
( 0.428703704 , 6 ),
( 0.390740741 , 7 ),
( 0.526851852 , 9 ),
( 0.448148148 , 10 ),
( 0.956481481 , 13 ),
( 1.112962963 , 14 ),
( 0.502777778 , 17 ),
( 0.82037037 , 18 ),
( 0.70462963 , 19 ),
( 0.492592593 , 20 ),
( 0.062962963 , 22 ),
( 0.961111111 , 23 ),
( 0.712037037 , 24 ),
( 0.901851852 , 25 ),
( 0.45462963 , 26 ),
( 0.815740741 , 28 ),
( 0.52962963 , 30 ),
( 0.763888889 , 32 ),
( 0.599074074 , 33 ),
( 0.555555556 , 34 )],
( 3 , 2 ): [
( 1.887037037 , 1 ),
( 1.253703704 , 5 ),
( 0.948148148 , 6 ),
( 0.918518519 , 7 ),
( 0.994444444 , 9 ),
( 0.950925926 , 10 ),
( 1.976851852 , 13 ),
( 3.062037037 , 14 ),
( 0.794444444 , 17 ),
( 2.111111111 , 18 ),
( 1.802777778 , 19 ),
( 1.173148148 , 20 ),
( 0.039814815 , 22 ),
( 1.62962963 , 23 ),
( 1.075 , 24 ),
( 1.737962963 , 25 ),
( 0.808333333 , 26 ),
( 1.391666667 , 28 ),
( 1.014814815 , 30 ),
( 1.258333333 , 32 ),
( 1.063888889 , 33 ),
( 1.008333333 , 34 )],
( 3 , 3 ): [
( 0.984259259 , 1 ),
( 0.609259259 , 5 ),
( 0.778703704 , 6 ),
( 0.787962963 , 7 ),
( 1.082407407 , 9 ),
( 0.862962963 , 10 ),
( 1.296296296 , 13 ),
( 2.135185185 , 14 ),
( 0.485185185 , 17 ),
( 1.699074074 , 18 ),
( 1.206481481 , 19 ),
( 0.693518519 , 20 ),
( 0.023148148 , 22 ),
( 1.360185185 , 23 ),
( 0.909259259 , 24 ),
( 1.59537037 , 25 ),
( 0.62962963 , 26 ),
( 1.32037037 , 28 ),
( 0.958333333 , 30 ),
( 1.549074074 , 32 ),
( 0.762037037 , 33 ),
( 0.822222222 , 34 )],
( 4 , 0 ): [
( 0.571296296 , 1 ),
( 0.419444444 , 5 ),
( 0.931481481 , 6 ),
( 0.8 , 7 ),
( 1.131481481 , 9 ),
( 0.712962963 , 10 ),
( 0.836111111 , 13 ),
( 0.962037037 , 14 ),
( 0.412037037 , 17 ),
( 1.131481481 , 18 ),
( 0.637962963 , 19 ),
( 0.303703704 , 20 ),
( 0.012962963 , 22 ),
( 0.70462963 , 23 ),
( 0.5 , 24 ),
( 0.607407407 , 25 ),
( 0.380555556 , 26 ),
( 0.424074074 , 28 ),
( 0.482407407 , 30 ),
( 0.781481481 , 32 ),
( 0.550925926 , 33 ),
( 0.673148148 , 34 )],
( 4 , 1 ): [
( 0.773148148 , 1 ),
( 0.425925926 , 5 ),
( 0.384259259 , 6 ),
( 0.547222222 , 7 ),
( 0.532407407 , 9 ),
( 0.496296296 , 10 ),
( 0.971296296 , 13 ),
( 0.984259259 , 14 ),
( 0.372222222 , 17 ),
( 0.784259259 , 18 ),
( 0.843518519 , 19 ),
( 0.566666667 , 20 ),
( 0.02962963 , 22 ),
( 0.762962963 , 23 ),
( 0.597222222 , 24 ),
( 0.801851852 , 25 ),
( 0.449074074 , 26 ),
( 0.634259259 , 28 ),
( 0.462037037 , 30 ),
( 0.799074074 , 32 ),
( 0.449074074 , 33 ),
( 0.526851852 , 34 )],
( 4 , 2 ): [
( 1.9 , 1 ),
( 1.219444444 , 5 ),
( 0.991666667 , 6 ),
( 0.838888889 , 7 ),
( 1.042592593 , 9 ),
( 0.939814815 , 10 ),
( 1.817592593 , 13 ),
( 2.722222222 , 14 ),
( 0.986111111 , 17 ),
( 1.636111111 , 18 ),
( 1.587962963 , 19 ),
( 1.02037037 , 20 ),
( 0.034259259 , 22 ),
( 1.735185185 , 23 ),
( 0.980555556 , 24 ),
( 1.778703704 , 25 ),
( 0.685185185 , 26 ),
( 1.313888889 , 28 ),
( 0.987962963 , 30 ),
( 1.374074074 , 32 ),
( 0.87037037 , 33 ),
( 0.874074074 , 34 )],
( 4 , 3 ): [
( 0.937037037 , 1 ),
( 0.682407407 , 5 ),
( 0.858333333 , 6 ),
( 0.897222222 , 7 ),
( 1.062037037 , 9 ),
( 0.656481481 , 10 ),
( 1.275925926 , 13 ),
( 2.343518519 , 14 ),
( 0.530555556 , 17 ),
( 1.697222222 , 18 ),
( 1.312037037 , 19 ),
( 0.586111111 , 20 ),
( 0.012037037 , 22 ),
( 1.617592593 , 23 ),
( 0.766666667 , 24 ),
( 2.318518519 , 25 ),
( 0.567592593 , 26 ),
( 1.22962963 , 28 ),
( 0.839814815 , 30 ),
( 1.562962963 , 32 ),
( 0.699074074 , 33 ),
( 0.940740741 , 34 )],
( 5 , 0 ): [
( 0.917592593 , 1 ),
( 0.637962963 , 5 ),
( 1.361111111 , 6 ),
( 1.180555556 , 7 ),
( 1.615740741 , 9 ),
( 0.993518519 , 10 ),
( 0.809259259 , 13 ),
( 0.95462963 , 14 ),
( 0.475925926 , 17 ),
( 1.32037037 , 18 ),
( 0.776851852 , 19 ),
( 0.348148148 , 20 ),
( 0.002777778 , 22 ),
( 0.812962963 , 23 ),
( 0.605555556 , 24 ),
( 0.733333333 , 25 ),
( 0.424074074 , 26 ),
( 0.597222222 , 28 ),
( 0.480555556 , 30 ),
( 0.767592593 , 32 ),
( 0.569444444 , 33 ),
( 1.084259259 , 34 )],
( 5 , 1 ): [
( 0.573148148 , 1 ),
( 0.410185185 , 5 ),
( 0.373148148 , 6 ),
( 0.44537037 , 7 ),
( 0.393518519 , 9 ),
( 0.37962963 , 10 ),
( 0.667592593 , 13 ),
( 0.781481481 , 14 ),
( 0.338888889 , 17 ),
( 0.657407407 , 18 ),
( 0.675 , 19 ),
( 0.408333333 , 20 ),
( 0.000925926 , 22 ),
( 0.625 , 23 ),
( 0.621296296 , 24 ),
( 0.457407407 , 25 ),
( 0.326851852 , 26 ),
( 0.500925926 , 28 ),
( 0.437037037 , 30 ),
( 0.662037037 , 32 ),
( 0.375 , 33 ),
( 0.501851852 , 34 )],
( 5 , 2 ): [
( 1.488888889 , 1 ),
( 0.807407407 , 5 ),
( 0.719444444 , 6 ),
( 0.552777778 , 7 ),
( 0.833333333 , 9 ),
( 0.655555556 , 10 ),
( 1.364814815 , 13 ),
( 2.441666667 , 14 ),
( 0.762037037 , 17 ),
( 1.575 , 18 ),
( 1.513888889 , 19 ),
( 1.028703704 , 20 ),
( 0.026851852 , 22 ),
( 1.156481481 , 23 ),
( 1.012037037 , 24 ),
( 1.263888889 , 25 ),
( 0.459259259 , 26 ),
( 1.142592593 , 28 ),
( 0.860185185 , 30 ),
( 1.128703704 , 32 ),
( 0.765740741 , 33 ),
( 0.825925926 , 34 )],
( 5 , 3 ): [
( 0.837037037 , 1 ),
( 0.651851852 , 5 ),
( 0.813888889 , 6 ),
( 0.753703704 , 7 ),
( 0.976851852 , 9 ),
( 0.598148148 , 10 ),
( 1.052777778 , 13 ),
( 1.952777778 , 14 ),
( 0.517592593 , 17 ),
( 1.573148148 , 18 ),
( 1.112962963 , 19 ),
( 0.530555556 , 20 ),
( 0.02962963 , 22 ),
( 1.381481481 , 23 ),
( 0.92962963 , 24 ),
( 1.281481481 , 25 ),
( 0.515740741 , 26 ),
( 1.094444444 , 28 ),
( 0.703703704 , 30 ),
( 1.435185185 , 32 ),
( 0.734259259 , 33 ),
( 0.888888889 , 34 )],
( 6 , 0 ): [
( 0.596296296 , 1 ),
( 0.562037037 , 5 ),
( 1.237962963 , 6 ),
( 1.028703704 , 7 ),
( 1.426851852 , 9 ),
( 0.907407407 , 10 ),
( 0.801851852 , 13 ),
( 0.883333333 , 14 ),
( 0.399074074 , 17 ),
( 1.407407407 , 18 ),
( 0.550925926 , 19 ),
( 0.344444444 , 20 ),
( 0.000925926 , 22 ),
( 0.750925926 , 23 ),
( 0.399074074 , 24 ),
( 0.642592593 , 25 ),
( 0.414814815 , 26 ),
( 0.431481481 , 28 ),
( 0.386111111 , 30 ),
( 0.831481481 , 32 ),
( 0.477777778 , 33 ),
( 0.990740741 , 34 )],
( 6 , 1 ): [
( 0.387962963 , 1 ),
( 0.287037037 , 5 ),
( 0.271296296 , 6 ),
( 0.278703704 , 7 ),
( 0.336111111 , 9 ),
( 0.310185185 , 10 ),
( 0.510185185 , 13 ),
( 0.719444444 , 14 ),
( 0.306481481 , 17 ),
( 0.57037037 , 18 ),
( 0.509259259 , 19 ),
( 0.389814815 , 20 ),
( 0.0 , 22 ),
( 0.541666667 , 23 ),
( 0.380555556 , 24 ),
( 0.408333333 , 25 ),
( 0.276851852 , 26 ),
( 0.361111111 , 28 ),
( 0.293518519 , 30 ),
( 0.613888889 , 32 ),
( 0.303703704 , 33 ),
( 0.432407407 , 34 )],
( 6 , 2 ): [
( 1.355555556 , 1 ),
( 0.735185185 , 5 ),
( 0.658333333 , 6 ),
( 0.617592593 , 7 ),
( 0.867592593 , 9 ),
( 0.562037037 , 10 ),
( 1.073148148 , 13 ),
( 2.193518519 , 14 ),
( 0.65 , 17 ),
( 1.161111111 , 18 ),
( 1.073148148 , 19 ),
( 0.822222222 , 20 ),
( 0.034259259 , 22 ),
( 1.147222222 , 23 ),
( 0.899074074 , 24 ),
( 0.962037037 , 25 ),
( 0.431481481 , 26 ),
( 0.955555556 , 28 ),
( 0.732407407 , 30 ),
( 0.967592593 , 32 ),
( 0.508333333 , 33 ),
( 0.751851852 , 34 )],
( 6 , 3 ): [
( 0.781481481 , 1 ),
( 0.465740741 , 5 ),
( 0.60462963 , 6 ),
( 0.65 , 7 ),
( 0.84537037 , 9 ),
( 0.480555556 , 10 ),
( 0.946296296 , 13 ),
( 1.608333333 , 14 ),
( 0.467592593 , 17 ),
( 0.919444444 , 18 ),
( 0.652777778 , 19 ),
( 0.536111111 , 20 ),
( 0.010185185 , 22 ),
( 1.164814815 , 23 ),
( 0.690740741 , 24 ),
( 0.937962963 , 25 ),
( 0.451851852 , 26 ),
( 0.949074074 , 28 ),
( 0.562962963 , 30 ),
( 1.062037037 , 32 ),
( 0.541666667 , 33 ),
( 0.902777778 , 34 )],
}

app = Flask(__name__)


@app.route('/report')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 15, type=int)
    b = request.args.get('b', 0, type=int)
    re = ""
    for i in Dict[(a,b)]:
        re += "The precinct No."+ str(i[1]) + " will have "+ str(i[0]) + " cases.<br>"
    return jsonify(result=re)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug=False
    app.run(host='0.0.0.0')

