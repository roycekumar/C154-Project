import matplotlib.pyplot as plt
data=[
     [10,10,10,10,10,10,10,10,10,10,5,10,10,10],
     [10,10,10,10,10,10,10,10,10,9,6,5,10,10],
     [10,10,10,10,10,10,10,10,9,9,9,6,5,10],
     [10,10,10,10,10,10,10,9,9,0,9,9,6,5],
     [10,10,10,10,10,10,9,9,9,9,9,9,6,5],
     [10,10,10,10,10,9,9,9,9,0,9,9,6,5],
     [10,10,10,10,9,9,9,9,9,9,9,6,5,5],
     [10,10,10,9,9,9,9,0,9,9,9,6,5,5],
     [10,10,9,0,9,0,9,9,9,9,6,5,5,10],
     [10,5,6,9,9,9,9,9,9,9,6,5,10,10],
     [10,10,5,6,6,6,6,6,6,6,5,10,10,10],
     [10,10,10,5,5,5,5,5,5,5,10,10,10,10]
     ]
plt.imshow(data,cmap="nipy_spectral")
plt.show()