def argb(alpha, red, green, blue):
    d = alpha * 256 + red
    d = d * 256 + green
    d = d * 256 + blue
    return d

def rgb(red=0, green=0, blue=0):
    return argb(255, red, green, blue)
