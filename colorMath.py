# Contains functions to convert RGB->LAB and deltaE_1994

import math

def convRGBtoLAB(color):
    r,g,b = color

    #    r, g and b (Standard RGB) input range = 0 ÷ 255
    #    X, Y and Z output refer to a D65/2° standard illuminant.

    R = ( r / 255 )
    G = ( g / 255 )
    B = ( b / 255 )

    if ( R > 0.04045 ):
        R = ( ( R + 0.055 ) / 1.055 ) ** 2.4
    else:
        R = R / 12.92
    if ( G > 0.04045 ):
        G = ( ( G + 0.055 ) / 1.055 ) ** 2.4
    else:
        G = G / 12.92
    if ( B > 0.04045 ):
        B = ( ( B + 0.055 ) / 1.055 ) ** 2.4
    else:
        B = B / 12.92

    R = R * 100
    G = G * 100
    B = B * 100

    x = R * 0.4124 + G * 0.3576 + B * 0.1805
    y = R * 0.2126 + G * 0.7152 + B * 0.0722
    z = R * 0.0193 + G * 0.1192 + B * 0.9505

    #   Reference-X, Y and Z refer to specific illuminants and observers.
    #   Common reference values are available below in this same page.

    X = (x / 100)
    Y = (y / 100)
    Z = (z / 100)

    if ( X > 0.008856 ):
        X = X ** ( 1/3 )
    else:
        X = ( 7.787 * X ) + ( 16 / 116 )
    if ( Y > 0.008856 ):
        Y = Y ** ( 1/3 )
    else:
        Y = ( 7.787 * Y ) + ( 16 / 116 )
    if ( Z > 0.008856 ):
        Z = Z ** ( 1/3 )
    else:
        Z = ( 7.787 * Z ) + ( 16 / 116 )

    L = ( 116 * Y ) - 16
    A = 500 * ( X - Y )
    B = 200 * ( Y - Z )

    pxLAB = (L, A, B)

    return pxLAB


def deltaE_1994(LAB1, LAB2):
    L1 = LAB1[0]
    A1 = LAB1[1]
    B1 = LAB1[2]
    L2 = LAB2[0]
    A2 = LAB2[1]
    B2 = LAB2[2]

    K1 = 0.045  #   0.045 graphic arts, 0.048 textiles
    K2 = 0.015  #   0.015 graphic arts, 0.014 textiles

    KL = 1      #   1 default, 2 textiles
    KC = 1
    KH = 1

    C1 = math.sqrt( math.pow(A1, 2) + math.pow(B1, 2) )
    C2 = math.sqrt( math.pow(A2, 2) + math.pow(B2, 2) )

    SL = 1
    SC = 1 + K1 * C1
    SH = 1 + K2 * C1

    delta_L = L1 - L2
    delta_C = C1 - C2
    delta_a = A1 - A2
    delta_b = B1 - B2

    delta_H = 0;
    deltaHCalc = math.pow(delta_a, 2) + math.pow(delta_b, 2) - math.pow(delta_C, 2)

    #   Can't do a sqrt of a negative num
    if (deltaHCalc < 0):
        delta_H = 0;
    else:
        delta_H = math.sqrt(deltaHCalc)

    #  Make double sure that delta_H is non-negative
    if (math.isnan(delta_H) or delta_H < 0):
        delta_H = 0

    L_group = math.pow(delta_L / (KL * SL), 2)
    C_group = math.pow(delta_C / (KC * SC), 2)
    H_group = math.pow(delta_H / (KH * SH), 2)

    Delta94 = math.sqrt(L_group + C_group + H_group)

    return int(Delta94)
