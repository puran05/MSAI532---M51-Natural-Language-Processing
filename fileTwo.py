# import nltk

# from nltk.book import *


# text7.concordance("stock",)
# text7.dispersion_plot(
#     ["stock","market","gain" ,"bond"]
# )

import nltk
import matplotlib.pyplot as plt
from nltk.draw.dispersion import dispersion_plot
from nltk.book import *

plt.figure()
dispersion_plot(text7, ["stock","market","gain" ,"bond"])
plt.savefig("dispersion_plot3.png")  # Save the plot as an image
print("Plot saved as 'dispersion_plot.png'")
