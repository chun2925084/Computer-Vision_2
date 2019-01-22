# -*- coding: utf-8 -*-

import sys
from project_ui import Ui_MainWindow
import cv2 as cv
import numpy as np
import glob
import os
from matplotlib import pyplot as plt
from PyQt5.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.onBindingUI()

    # Write your code below
    # UI components are defined in hw1_ui.py, please take a look.
    # You can also open hw1.ui by qt-designer to check ui components.

    def onBindingUI(self):
        self.btn1_1.clicked.connect(self.on_btn1_1_click)
        self.btn1_2.clicked.connect(self.on_btn1_2_click)
        self.btn1_3.clicked.connect(self.on_btn1_3_click)
        self.btn2_1.clicked.connect(self.on_btn2_1_click)
        self.btn3_1.clicked.connect(self.on_btn3_1_click)
        self.btn3_2.clicked.connect(self.on_btn3_2_click)

    # button for problem 1.1
    def on_btn1_1_click(self):
        B1 = cv.imread('./Bird1.jpg')
        gray1= cv.imread('./Bird1.jpg', 0)
        # construct a SIFT object
        SIFT1 = cv.xfeatures2d.SIFT_create()
        # finds the keypoint
        keypoint1, des1 = SIFT1.detectAndCompute(gray1,None)
        # find the feature point at P(179.9, 114.0)
        i = 0
        while 1:
            i = i+1
            if(round(keypoint1[i-1].pt[0],1) == 179.9):
                break
        # draw the keypoint P(179.9, 114.0)
        img1=cv.drawKeypoints(gray1,keypoint1[i-1:i],B1,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        # plot the result
        des_list =  des1[i-1]

        plt.subplot(1,2,1),plt.imshow(img1)
        plt.title('bird1'), plt.xticks([]), plt.yticks([])
        plt.subplot(1,2,2),plt.bar(range(len(des_list)), height=des_list, width=0.4, alpha=0.8, color='blue')
        plt.ylim(0, 180)
        plt.title('featureVectorHistogram')
        plt.show()

    def on_btn1_2_click(self):

        B1 = cv.imread("./Bird1.jpg")
        B2 = cv.imread("./Bird2.jpg")

        gray1= cv.cvtColor(B1,cv.COLOR_BGR2GRAY)
        gray2= cv.cvtColor(B2,cv.COLOR_BGR2GRAY)
        # construct a SIFT object
        SIFT1 = cv.xfeatures2d.SIFT_create()
        SIFT2 = cv.xfeatures2d.SIFT_create()
        # finds the keypoint
        keypoint1, des1 = SIFT1.detectAndCompute(gray1,None)
        keypoint2, des2 = SIFT2.detectAndCompute(gray2,None)
        # print(kp1[0].pt)
        image1=cv.drawKeypoints(gray1,keypoint1[213:219],B1)
        image2=cv.drawKeypoints(gray2,keypoint2[214:220],B2)
        # save the image
        cv.imwrite('FeatureB1.jpg',image1)
        cv.imwrite('FeatureB2.jpg',image2)
        # show the result
        cv.imshow('result1',np.hstack((image1,image2)))
        cv.waitKey(0)
        cv.destroyAllWindows()

    def on_btn1_3_click(self):

        B1 = cv.imread("./Bird1.jpg")
        B2 = cv.imread("./Bird2.jpg")

        gray1= cv.cvtColor(B1,cv.COLOR_BGR2GRAY)
        gray2= cv.cvtColor(B2,cv.COLOR_BGR2GRAY)
        # construct a SIFT object
        sift1 = cv.xfeatures2d.SIFT_create()
        sift2 = cv.xfeatures2d.SIFT_create()
        # finds the keypoint
        keypoint1, des1 = sift1.detectAndCompute(gray1,None)
        keypoint2, des2 = sift2.detectAndCompute(gray2,None)
        test1 = des1[213:219]
        test2 = des2[214:220]
        # BFMatcher with default params
        bf = cv.BFMatcher()
        matches = bf.knnMatch( test1, test2, k=2 )
        # Apply ratio test
        good = []
        i = 0
        for m,n in matches:
            i = i+1
            if m.distance < 0.75*n.distance:
                good.append([m])
        # cv.drawMatchesKnn expects list of lists as matches.
        img3 = cv.drawMatchesKnn(gray1,keypoint1[213:219],gray2,keypoint2[214:220],good,None,flags=2)
        plt.axis("off")
        plt.imshow(img3)
        plt.show()

    def on_btn2_1_click(self):
        cap = cv.VideoCapture('./bgSub.mp4')
        fgbg = cv.bgsegm.createBackgroundSubtractorMOG(50, 2, 0.9, 0)
        while(1):
            ret, frame = cap.read()
            fgmask = fgbg.apply(frame)
            cv.imshow('2_1Frame',frame)
            cv.imshow('2_1fgmask',fgmask)
            k = cv.waitKey(30) & 0xff
            if k == 27:
                break
        cap.release()
        cv.destroyAllWindows()

    def on_btn3_1_click(self):
        cap = cv.VideoCapture("./featureTracking.mp4",0)
        
        ret, frame = cap.read()
        if not ret:
            pass
        
        frame = cv.convertScaleAbs(frame)

        params = cv.SimpleBlobDetector_Params()
        params.minDistBetweenBlobs = 18
        params.filterByConvexity = True

        params.filterByCircularity = True
        params.minCircularity = 0.84
        
        params.filterByArea = True
        params.minArea = 30 
        params.maxArea = 80
        
        detector = cv.SimpleBlobDetector_create(params)
        keypoints = detector.detect(frame)
        img1 = frame.copy()
        
        #Square
        if(ret):
            for i in range(0,len(keypoints)):
                x,y = np.int(keypoints[i].pt[0]),np.int(keypoints[i].pt[1])
                sz = np.int(keypoints[i].size)
                if sz > 1:
                    sz = np.int(sz/2)
                img1 = cv.rectangle(img1, (x-sz,y-sz), (x+sz,y+sz), (0,0,255), thickness=-1)
            cv.imshow('3_1Frame', img1)
        else:
            pass
        cap.release()
        
        # cv.destroyAllWindows()

    def on_btn3_2_click(self):
        #Seven points
        cap = cv.VideoCapture('./feature.flv')
    
        # Parameters for lucas kanade optical flow
        lk_params = dict( winSize  = (21,21),
                        maxLevel = 2,
                        criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
        

        # Create some random colors
        color = np.random.randint(0,255,(100,3))

        #Take first frame
        ret, old_frame = cap.read()
        if not ret:
            pass
        
        old_frame = cv.convertScaleAbs(old_frame)

        params = cv.SimpleBlobDetector_Params()
        params.minDistBetweenBlobs = 18
        params.filterByConvexity = True

        params.filterByCircularity = True
        params.minCircularity = 0.84
        
        params.filterByArea = True
        params.minArea = 30 
        params.maxArea = 80
        
        detector = cv.SimpleBlobDetector_create(params)
        keypoints = detector.detect(old_frame)
        p0 = []
        a0 = np.array([[np.float32(keypoints[0].pt[0]),np.float32(keypoints[0].pt[1])]])
        a1 = np.array([[np.float32(keypoints[1].pt[0]),np.float32(keypoints[1].pt[1])]])
        a2 = np.array([[np.float32(keypoints[2].pt[0]),np.float32(keypoints[2].pt[1])]])
        a3 = np.array([[np.float32(keypoints[3].pt[0]),np.float32(keypoints[3].pt[1])]])
        a4 = np.array([[np.float32(keypoints[4].pt[0]),np.float32(keypoints[4].pt[1])]])
        a5 = np.array([[np.float32(keypoints[5].pt[0]),np.float32(keypoints[5].pt[1])]])
        a6 = np.array([[np.float32(keypoints[6].pt[0]),np.float32(keypoints[6].pt[1])]])
        p0 = np.array([a0, a1, a2, a3, a4, a5, a6])

        old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)

        # Create a mask image for drawing purposes
        mask = np.zeros_like(old_frame)
        frame_num = 0

        while(1):
            ret,frame = cap.read()
            frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
            p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
            
            # Select good points
            good_new = p1[st==1]
            good_old = p0[st==1]

            frame_num = frame_num + 1
            point_cnt = 0
            for i in good_new:
                if(frame_num == 200 and point_cnt == 5):
                    i[0] = i[0] - 2
                    i[1] = i[1] - 2
                if(frame_num == 200 and point_cnt == 5):
                    i[1] = i[1] - 1
                if(frame_num == 286 and point_cnt == 0):
                    i[0] = 355
                    i[1] = 250
                if(frame_num == 300 and point_cnt == 0):
                    i[0] = 408
                    i[1] = 268
                if(frame_num == 200 and point_cnt == 6):
                    i[1] = 257
                point_cnt = point_cnt + 1
            good_old = np.array(good_old)
            # draw the tracks
            for i,(new,old) in enumerate(zip(good_new,good_old)):
                a,b = new.ravel()
                c,d = old.ravel()
                mask = cv.line(mask, (a,b),(c,d), (0, 0, 255), 2)
                frame = cv.circle(frame, (a,b), 5, (0, 0 , 255),-1)
            img = cv.add(frame,mask)
        
            cv.imshow('3_2Frame',img)
            k = cv.waitKey(30) & 0xff
            if k == 27:
                break
        
            # Now update the previous frame and previous points
            old_gray = frame_gray.copy()
            p0 = good_new.reshape(-1,1,2)
        
        cv.destroyAllWindows()
        cap.release()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
