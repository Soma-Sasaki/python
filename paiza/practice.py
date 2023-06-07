import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

os.chdir(r"C:\Users\shira\Desktop\python\openCV")
lena_bgr = cv2.imread("lena.png")
lena_rgb = cv2.cvtColor(lena_bgr, cv2.COLOR_BGR2RGB)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(lena_bgr)
axes[0].set_title("BGR")
axes[1].imshow(lena_rgb)
axes[1].set_title("RGB")
plt.show()
