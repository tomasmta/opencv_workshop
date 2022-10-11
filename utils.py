import cv2 as cv
import numpy as np


def split_colors(img_path):

    colors = list(["blue", "green", "red"])
    img = cv.imread(img_path)
    channels = cv.split(img)
    for channel, color in zip(channels, colors):
        cv.imshow(color, channel)
    cv.waitKey(0)

def transform_colors(img_path):

    img = cv.imread(img_path)
    cv_grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("OpenCV Function", cv_grayscale)
    
    B, G, R = cv.split(img)
    avg_grayscale = (B+G+R)/3
    cv.imshow("Average Weighted", cv_grayscale)
    cv.waitKey(0)
    cv.destroyAllWindows()

def detect_color(img_path):

    img = cv.imread(img_path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    green_lower = np.array([40, 50, 20])
    green_upper = np.array([70, 255, 255])
    green_mask = cv.inRange(hsv_img, green_lower, green_upper)
    green = cv.bitwise_and(img, img, mask = green_mask)

    white_lower = np.array([0,0,200])
    white_upper = np.array([180,20,255])
    white_mask = cv.inRange(hsv_img, white_lower, white_upper)
    white = cv.bitwise_and(img, img, mask=white_mask)

    cv.imshow("green", green)
    cv.imshow("white", white)
    cv.waitKey(0)


def nothing(val):
    pass

def blend(img_path1, img_path2):

    img1 = cv.imread(img_path1)
    img2 = cv.imread(img_path2)
    bar_min, bar_max = 0, 100

    if img1.shape == img2.shape:
        cv.namedWindow("blend_window")
        cv.createTrackbar("test", "blend_window" , bar_min, bar_max, nothing)
        
        while(1):
            k = cv.waitKey(1) & 0xFF
            if k == 27:
                break

            alpha = cv.getTrackbarPos("test", "blend_window") / bar_max
            beta = 1.0 - alpha
            print(f'alpha:{alpha}, beta:{beta}')
            dst = cv.addWeighted(img1, alpha, img2, beta, 0.0) 
            cv.imshow("blend_window", dst)
        cv.destroyAllWindows()

    else: 
        print("Image dimension don't match! Choose other images.")


class Filters():

    def __init__(self, img_path):
        self.img_path = img_path
        self.img = cv.imread(img_path)
        self.bar_min = 0
        self.bar_max = 10

    def nothing(self, val):
        pass

    def gaussian(self):
        cv.namedWindow("Gauss")
        cv.createTrackbar("Magnitude", "Gauss", self.bar_min, self.bar_max, self.nothing)

        while(1):
            key = cv.waitKey(1) & 0xFF
            if key == 27:
                break

            magnitude = int(cv.getTrackbarPos("Magnitude", "Gauss"))
            if magnitude == 0:
                cv.imshow("image", self.img)
            else:
                length = 2*magnitude + 1
                gauss_blur = cv.GaussianBlur(self.img, (length, length), 0)
                cv.imshow("Blur", gauss_blur)

        cv.destroyAllWindows()

    def bilateral(self):
        cv.namedWindow("Bilateral")
        cv.createTrackbar("Magnitude", "Bilateral", self.bar_min, self.bar_max, self.nothing)

        while(1):
            key = cv.waitKey(1) & 0xFF
            if key == 27:
                break

            magnitude = int(cv.getTrackbarPos("Magnitude", "Bilateral"))
            if magnitude == 0:
                cv.imshow("image", self.img)
            else:
                diameter = 2*magnitude + 1
                bilateral_filter = cv.bilateralFilter(self.img, d=diameter, sigmaColor=90, sigmaSpace=90)
                cv.imshow("Bilateral", bilateral_filter)

        cv.destroyAllWindows()
    
    def median(self):
        cv.namedWindow("Median")
        cv.createTrackbar("Magnitude", "Median", self.bar_min, self.bar_max, self.nothing)

        while(1):
            key = cv.waitKey(1) & 0xFF
            if key == 27:
                break

            magnitude = int(cv.getTrackbarPos("Magnitude", "Median"))
            if magnitude == 0:
                cv.imshow("image", self.img)
            else:
                length = 2*magnitude + 1
                median_blur = cv.medianBlur(self.img, length)
                cv.imshow("Median", median_blur)

        cv.destroyAllWindows()




if __name__ == "__main__":
    main()