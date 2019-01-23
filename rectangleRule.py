# Program that uses

# Your program uses the curve to calculate the height of each rectangle,
# multiplies it by its width, and adds the result to get an approximation of the region's area.
# That's the basic algorithm.
# It starts by calculating the width of the rectangles.
# To divide the area into N rectangles,
# the algorithm calculates the maximum x-coordinate minus the smallest x-coordinate
# and divides the result by N. The algorithm initializes the total area variable to 0
# and then makes variable x range over the rectangle's coordinates.
# For each x value, the area of the corresponding rectangle is the value dx times the curve's height at position x.
# The algorithm simply adds those up to get the final estimate

# http://hplgit.github.io/prog4comp/doc/pub/p4c-sphinx-Python/._pylight004.html

#sudo code

# dx = (xmax - xmin) / N
# total_area = 0
# for x = xmin to xmax - dx
#   total_area = total_area + dx * curve(x)


# (O)n runtime

# area of a trapezoid
# area =  w * (h1+h2)/2


# Trapezoid rule algorithm

# dx = (xmax - xmin) / N
# total_area = 0
# for x = xmin to xmax - dx step dx
#   total_area = total_area + dx * curve(x)
#
#  total_area = total_area * 2 - Curve(xmin) - Curbve(max)
#  total_area = total_area +  dx / 2