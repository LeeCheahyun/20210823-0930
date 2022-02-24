import numpy as np
import cv2
from matplotlib import pyplot as plt

src = cv2.imread('images/candies.png', cv2.IMREAD_COLOR)

b_plane, g_plane, r_plane = cv2.split(src)

src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
b_plane = cv2.cvtColor(b_plane, cv2.COLOR_BGR2RGB)
g_plane = cv2.cvtColor(g_plane, cv2.COLOR_BGR2RGB)
r_plane = cv2.cvtColor(r_plane, cv2.COLOR_BGR2RGB)
plt.subplot(221), plt.axis('off'), plt.imshow(src), plt.title('src')
plt.subplot(222), plt.axis('off'), plt.imshow(b_plane), plt.title('b_plane')
plt.subplot(223), plt.axis('off'), plt.imshow(g_plane), plt.title('g_plane')
plt.subplot(224), plt.axis('off'), plt.imshow(r_plane), plt.title('r_plane')
plt.show()