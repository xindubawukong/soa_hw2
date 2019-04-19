import cv2


img = cv2.imread('hype_cycle.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
m, n, _ = img.shape
print('m = %d  n = %d' % (m, n))
median = cv2.medianBlur(img, 5)
median = cv2.cvtColor(median, cv2.COLOR_RGB2BGR)
cv2.imwrite('hype_cycle.png', median)
