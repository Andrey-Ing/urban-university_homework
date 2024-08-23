from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib.animation as animation
import cv2

cap = cv2.VideoCapture(1)

ws = [1, 1, 1]
hs = [1, 3]
fig = plt.figure(figsize=(10, 15), facecolor="xkcd:eggshell")
gs = GridSpec(2, 3, figure=fig, width_ratios=ws, height_ratios=hs)


def histogram(non):
    ret, frame = cap.read()
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # для matplotlib должен быть RGB
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_r, img_g, img_b = cv2.split(image_rgb)

    # гистограммы
    hist_gray = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
    hist_r = cv2.calcHist([img_r], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([img_g], [0], None, [256], [0, 256])
    hist_b = cv2.calcHist([img_b], [0], None, [256], [0, 256])

    plt.clf()

    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_title("RED channel")
    ax1.grid(True)
    ax1.semilogy(hist_r, color="red")


    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_title("GREEN channel")
    ax2.grid(True)
    ax2.semilogy(hist_g, color="green")

    ax3 = fig.add_subplot(gs[0, 2])
    ax3.set_title("BLUE channel")
    ax3.grid(True)
    ax3.semilogy(hist_b, color="blue")

    ax4 = fig.add_subplot(gs[1, 0:2])
    ax4.set_yticklabels([])
    ax4.set_xticklabels([])
    ax4.set_title("Picture")
    ax4.imshow(image_rgb)

    ax5 = fig.add_subplot(gs[1, 2])
    ax5.set_title("Grayscale Histogram")
    ax5.grid(True)
    ax5.plot(hist_gray, color="black")

    return plt.gcf(),


anim = animation.FuncAnimation(fig, histogram, interval=100, cache_frame_data=False)
plt.show()
cap.release()
