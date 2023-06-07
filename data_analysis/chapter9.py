import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import dlib
import math
import os

#絶対パス指定
os.chdir(r"C:\Users\shira\Desktop\python\data_analysis\sample_100knocks\サンプルコード_20201021\9章")

#画像表示
# img = cv2.imread("img/img01.jpg")
# height, width = img.shape[:2]
# print("画像幅: {} \n画像高さ: {}".format(width, height))
# img2 = cv2.resize(img, (int(width*0.5), int(height*0.5)))
# cv2.imshow("img2", img2)
# cv2.waitKey(0)
#
#動画表示
# cap = cv2.VideoCapture("mov/mov01.avi")
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
# fps = cap.get(cv2.CAP_PROP_FPS)
# print("画像幅: {} \n画像高さ: {} \n総フレーム数: {} \nFPS: {}".format(width, height, count, fps))
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret:
#         frame = cv2.resize(frame, (int(width*0.5), int(height*0.5)))
#         cv2.imshow("frame", frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()
#
# num = 0
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret:
#         cv2.imshow("frame", frame)
#         filepath = "snapshot/snapshot_" + str(num) + ".jpg"
#         cv2.imwrite(filepath, frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
#     num += 1
# cap.release()
# cv2.destroyAllWindows()
#
#画像内のどこに人がいるのか検出
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# hogParams = {'winStride': (8, 8), 'padding': (32, 32), 'scale': 1.05, 'hitThreshold': 0, 'finalThreshold': 5}
# img = cv2.imread("img/img01.jpg")
# height, width = img.shape[:2]
# img2 = cv2.resize(img, (int(width*0.6), int(height*0.6)))
# gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# human, r = hog.detectMultiScale(gray, **hogParams)
# if (len(human)>0):
#     for (x, y, w, h) in human:
#         cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 255, 255), 3)
# cv2.imshow("img2", img2)
# cv2.waitKey(0)
#
#画像内の正面顔検出
# cascade_file = "haarcascade_frontalface_alt.xml"
# cascade = cv2.CascadeClassifier(cascade_file)
#
# img = cv2.imread("img/img02.jpg")
# img2 = cv2.resize(img, (int(width*0.6), int(height*0.5)))
# gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# face_list = cascade.detectMultiScale(gray, minSize=(50, 50))
# for (x, y, w, h) in face_list:
#     color = (0, 0, 225)
#     pen_w = 3
#     cv2.rectangle(img2, (x, y), (x+w, y+h), color, thickness = pen_w)
# cv2.imshow("img2", img2)
# cv2.imwrite("temp.jpg", img2)
# cv2.waitKey(0)

#画像内の顔の向き検出
# predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# detector = dlib.get_frontal_face_detector()
#
# img = cv2.imread("img/img02.jpg")
# height, width = img.shape[:2]
# img2 = cv2.resize(img, (int(width*0.6), int(height*0.5)))
# dets = detector(img2, 1)
#
# for k, d in enumerate(dets):
#     shape = predictor(img2, d)
#     color_f = (0, 0, 225)
#     color_l_out = (255, 0, 0)
#     color_l_in = (0, 255, 0)
#     line_w = 3
#     circle_r = 3
#     fontType = cv2.FONT_HERSHEY_SIMPLEX
#     fontSize = 1
#     cv2.rectangle(img2, (d.left(), d.top()), (d.right(), d.bottom()), color_f, line_w)
#     cv2.putText(img2, str(k), (d.left(), d.top()), fontType, fontSize, color_f, line_w)
#     num_of_points_out = 17
#     num_of_points_in = shape.num_parts - num_of_points_out
#     gx_out, gy_out, gx_in, gy_in = 0, 0, 0, 0
#     for shape_point_count in range(shape.num_parts):
#         shape_point = shape.part(shape_point_count)
#         print("顔器官No.{} 座標位置: ({}, {})".format(shape_point_count, shape_point.x, shape_point.y))
#         if shape_point_count < num_of_points_out:
#             cv2.circle(img2, (shape_point.x, shape_point.y), circle_r, color_l_out, line_w)
#             gx_out += shape_point.x / num_of_points_out
#             gy_out += shape_point.y / num_of_points_out
#         else:
#             cv2.circle(img2, (shape_point.x, shape_point.y), circle_r, color_l_in, line_w)
#             gx_in += shape_point.x / num_of_points_in
#             gy_in += shape_point.y / num_of_points_in
#     cv2.circle(img2, (int(gx_out), int(gy_out)), circle_r, (0, 0, 255), line_w)
#     cv2.circle(img2, (int(gx_in), int(gy_in)), circle_r, (0, 0, 0), line_w)
#     theta = math.asin(2*(gx_in - gx_out) / (d.right() - d.left()))
#     radian = theta*180 / math.pi
#     print("顔方位: {} (角度: {}度)".format(theta, radian))
#     if radian < 0:
#         textPrefix = "  left"
#     else:
#         textPrefix = "  right"
#     textShow = textPrefix + str(round(abs(radian), 1)) + "deg."
#     cv2.putText(img2, textShow, (d.left(), d.top()), fontType, fontsize, color_f, line_w)
# cv2.imshow("img2", img2)
# cv2.imwrite("temp2.jpg", img2)
# cv2.waitKey(0)
