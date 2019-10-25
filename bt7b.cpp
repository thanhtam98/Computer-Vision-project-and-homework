
#include "opencv2/core.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/videoio.hpp"
#include "opencv2/features2d.hpp"
#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
using namespace cv;

Mat img, grayImg, cannygrayImg, invGrayImg, hisgrayImg;

int main() {
	img = imread("bt7b.jpg");
	grayImg = imread("bt7b.jpg", IMREAD_GRAYSCALE);
	bitwise_not(grayImg, invGrayImg);

	// Set up the detector with default parameters.
	SimpleBlobDetector::Params params;

	params.filterByArea = true;
	params.maxArea = 5000;

	params.filterByCircularity = true;
	params.minCircularity = 0.815;

	params.filterByConvexity = true;
	params.minConvexity = 0.7;

	params.filterByInertia = true;
	params.minInertiaRatio = 0.001;
	params.maxInertiaRatio = 0.99;

	Ptr<SimpleBlobDetector> detector = SimpleBlobDetector::create(params);

	// Detect blobs.
	std::vector<KeyPoint> keypoints;
	std::vector<KeyPoint> keypoints2;

	detector->detect(grayImg, keypoints);
	detector->detect(invGrayImg, keypoints2);

	keypoints.insert(keypoints.end(), keypoints2.begin(), keypoints2.end());

	// Draw detected blobs as red circles.
	Mat im_with_keypoints;
	drawKeypoints(grayImg, keypoints, im_with_keypoints, Scalar(0, 0, 255), DrawMatchesFlags::DRAW_RICH_KEYPOINTS);

	// Show blobs
	imshow("keypoints", im_with_keypoints);

	// Kmean clustering
	vector<Point2f> points, centers;

	for (int i = 0; i < keypoints.size(); i++)
	{
		Point2f point_f;
		point_f.x = keypoints[i].pt.x;
		point_f.y = keypoints[i].pt.y;
		points.push_back(point_f);
	}

	cout << "Total dot: " << keypoints.size() << endl;

	int clusterCount = 11;
	Mat labels, count;
	int attempts = 5;

	kmeans(points, clusterCount, labels,
		TermCriteria(TermCriteria::EPS + TermCriteria::COUNT, 11, 1),
		attempts, KMEANS_PP_CENTERS, centers);

	count = Mat::zeros(1, clusterCount, CV_16SC2);
	for (size_t i = 0; i < points.size(); i++)
	{
		count.at<int>(labels.at<int>(i))++;
	}

	for (size_t i = 0; i < centers.size(); i++)
	{
		char str[5];
		sprintf_s(str, "%d", count.at<int>(i));
		putText(img, str, centers[i], FONT_HERSHEY_PLAIN, 2, Scalar(0, 255, 0, 0), 2);
	}
	char text[100];
	sprintf_s(text, "Total dot: %d", keypoints.size());
	putText(img, text, Point2f(340, 40), FONT_HERSHEY_PLAIN, 2, Scalar(0, 0, 255, 0), 3);

	imshow("img", img);
	waitKey(0);
	return 0;
}
