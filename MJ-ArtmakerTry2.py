""" THis is the computational art miniproject
The old one was tking waaayyy too long.... I am going to split generate art up into different functions and try and make it go faster somehow.
by MJ-McMillen
 """

import random
import math
import colorsys
from PIL import Image
import cmath
from inspect import signature


functions_real = {"cos_pi":(lambda x: math.cos(math.pi*x)),
                  "sin_pi":(lambda x: math.sin(math.pi*x)),
                  "prod":(lambda x,y: x*y),
                  "avg":(lambda x,y: (x+y)/2)
                  , "arctan": (lambda x: math.atan(x*(math.pi/2)))
                  , "geomean":(lambda x,y: math.copysign(math.sqrt(math.fabs(x*y)),(x*y)))}
allfunctions_real = {"x":"x", "y":"y"}
allfunctions_real.update(functions_real)

#functions for the complex number hsv random art.
functions_imaginary = {"sum": (lambda c1,c2:c1+c2),"mult": (lambda c1,c2:c1*c2), "cos" : (lambda c:cmath.cos(c)),"exp" : (lambda c:cmath.exp(c))}
allFunctions_imaginary = {"I": "I"}
allFunctions_imaginary.update(functions_imaginary)

default_real_weights = {"cos_pi":1, "sin_pi":1,"prod":1,"avg":1, "arctan": 1, "geomean":1}
default_imaginary_weights = {"sum": 1,"mult": 1, "cos" : 1,"exp" : 0}

def build_choice(frequ_dict):
    """This function builds a list of functions to chose from. It modifies the
    probability a function can be selected and if it is selected at all.

    """
    final_list = []
    #then we are chosing from real functions.
    for i in frequ_dict:
        for num in range(frequ_dict[i]):
            final_list.append(i)
    return final_list


def build_random_function_real(min_depth,max_depth,f_list):
    """ This function builds a real function that can be used for rgb

    """
    if max_depth == 1:
        return [random.choice(["x","y"])]
    elif min_depth == 1:
        functionDict = allfunctions_real
        choices = f_list+["x"]+["y"]
    else:
        functionDict = functions_real
        choices = f_list
    functionName = random.choice(choices)
    function = functionDict[functionName]
    if function != "x" and function != "y":
        nParams = len(signature(function).parameters)
        params = [build_random_function_real(min_depth-1,max_depth-1,f_list) for _ in range(nParams)]
        return [function] + params
    else:
        return [function]


def evaluate_random_function_real(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

    """
    if f[0] == "x":
        return x
    if f[0] == "y":
        return y
    return f[0](*[evaluate_random_function_real(g,x,y) for g in f[1:]])


def build_random_function_imaginary(min_depth,max_depth,f_list):
    """ This function builds an imaginary function that can be used for HSV

    """
    g = f_list
    if max_depth == 1:
        return ["I"]
    elif min_depth == 1:
        functionDict = allFunctions_imaginary
        choices = f_list+["I"]
    else:
        functionDict = functions_imaginary
        choices = f_list
    functionName = random.choice(choices)
    function = functionDict[functionName]
    if function != "I":
        nParams = len(signature(function).parameters)
        params = [build_random_function_imaginary(min_depth-1,max_depth-1,f_list) for _ in range(nParams)]
        return [function] + params
    else:
        return [function]


def evaluate_random_function_imaginary(f, c):
    """This function evaluates the randomly generated imaginary function.
    It first goes through in a a+bi manner evaluating based on real and imaginary
    components. It outputs the real component and the imaginary one.

    NOT NOWx is a complex number a+bi where a =x and b = y
    y is a complex number a+bi where a = y and b =x
    """
    if f[0] == "I":
        return c
    return f[0](*[evaluate_random_function_imaginary(g,c) for g in f[1:]])


def remap_interval(val,
                   input_interval_start,
                   input_interval_end,
                   output_interval_start,
                   output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    #needs to scale inupt into a different range.
    input_interval = abs(input_interval_end- input_interval_start)
    #the range of numbers input interval is 0 refed
    output_interval = abs(output_interval_end - output_interval_start)
    #the range of numbers the output interval is. 0 refed
    deltoval = val- input_interval_start
    scaled_val = (deltoval/input_interval)* output_interval
    return(output_interval_start + scaled_val)


def color_map(val,colorval=255):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, colorval)
    return int(color_code)



def HSV_to_RGB(c):
    """This function takes the HSV values and converts them to RGB values
    """
    H = math.degrees(cmath.phase(c))
    V = 1
    #+(math.atan(abs(c))/(math.pi/2))
    return colorsys.hsv_to_rgb(H,1,V)


def generate_art_real(filename, c1 =[255,0,0], c2 = [0,255,0],c3 =[0,0,255], mins = [2,2,2], maxes = [10,10,10], frequ_dict_real1 = default_real_weights,frequ_dict_real2 = default_real_weights,frequ_dict_real3 = default_real_weights, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    weighted_choices1 = build_choice(frequ_dict_real1)
    weighted_choices2 = build_choice(frequ_dict_real2)
    weighted_choices3 = build_choice(frequ_dict_real3)
    color_function_one = build_random_function_real(mins[0],maxes[0],weighted_choices1)
    color_function_two = build_random_function_real(mins[1],maxes[1],weighted_choices2)
    color_function_three = build_random_function_real(mins[2],maxes[2],weighted_choices3)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            color_1 =[color_map(evaluate_random_function_real(color_function_one, x, y),c1[0]),color_map(evaluate_random_function_real(color_function_one, x, y),c1[1]),color_map(evaluate_random_function_real(color_function_one, x, y),c1[2])]
            color_2 =[color_map(evaluate_random_function_real(color_function_two, x, y),c2[0]),color_map(evaluate_random_function_real(color_function_two, x, y),c2[1]),color_map(evaluate_random_function_real(color_function_two, x, y),c2[2])]
            color_3 =[color_map(evaluate_random_function_real(color_function_three, x, y),c3[0]),color_map(evaluate_random_function_real(color_function_three, x, y),c3[1]),color_map(evaluate_random_function_real(color_function_three, x, y),c3[2])]
            pixels[i, j] = (
                    color_1[0]+color_2[0]+color_3[0],
                    color_1[1]+color_2[1]+color_3[1],
                    color_1[2]+color_2[2]+color_3[2]
                    )

    im.save(filename)


def generate_art_imaginary(filename, maxes,mins,frequ_dict_imaginary = default_imaginary_weights, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    weighted_choices = build_choice(frequ_dict_imaginary)
    if maxes >8:
        maxes = 8
    if mins > maxes:
            mins = maxes
    HS = build_random_function_imaginary(mins[0],maxes[0],weighted_choices)
    #V = build_random_function_real(2,10)
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            HS_evaled = evaluate_random_function_imaginary(HS,complex(x,y))
            #print(HS_evaled)
            #V_evaled =  evaluate_random_function_real(V,x,y)
            RGB = HSV_to_RGB(HS_evaled)
            pixels[i, j] = (
                color_map(RGB[0]),
                color_map(RGB[1]),
                color_map(RGB[2])
                )
    im.save(filename)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
    # generate_art("myart.png")

    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
    generate_art_real("testing.png", c1 = (27,174,12), c2 = (127,46,242), c3 = (174,87,14))
