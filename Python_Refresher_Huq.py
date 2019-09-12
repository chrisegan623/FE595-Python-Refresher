# Importing numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Setting the X values in the x variable
x = np.arange(0, 2*np.pi, 0.01)

# Setting the values for Sine in the sin_y variable
sin_y = np.sin(x)

# Plotting with x variable for X-axis and sin_y for Y-axis.
# The linewidth argument increases the width of the line,
# making it stand out more. The label argument will allow
# for differentiation of lines on the same axis via a legend
plt.plot(x, sin_y, linewidth=3, label='Sine')

# Setting the values for Cosine in the cos_y variable
cos_y = np.cos(x)

#Setting the values for Sine in the sin_y variable
tan_y = np.tan(x)

# Plotting on same axis with x variable for X-axis and cos_y
# for Y-axis. The linewidth and label arguments do the same
# thing as previously described above the first plt.plot
plt.plot(x, cos_y, linewidth=3, label='Cosine')

plt.plot(x,tan_y, linewidth=3, label='Tangent')

# Adding appropriate title
plt.title('One Period Plot of Sine, Cosine and Tangent')

# Labeling X-axis and Y-axis as appropriate
plt.xlabel('X values from Zero to 2Pi')
plt.ylabel('Sine, Cosine, and Tangent Values')

# Including the legend to differentiate the two lines
plt.legend()

# Adding a grid
plt.grid(True)

# Showing the plot with all relevant information included
plt.show()
