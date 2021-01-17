import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [[.1, .2], [.3, .4], [.8,.9], [.15,.16]]



plt.plot(x, y, 'g^')
plt.subplots_adjust(left=0.09, right=0.99, top=0.99, bottom=0.09) #add this after plot to set dimensions.
plt.ylabel('some numbers')
plt.grid(True)
plt.show()
