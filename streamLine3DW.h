/*
 * streamLine3D.h
 *
 *  Created on: Dec 30, 2020
 *      Author: gips
 */

#ifndef STREAMLINE3D_H_
#define STREAMLINE3D_H_
#include"point3D.h"
class streamLine3D{
public:
	long unsigned int index;
	point3D *pI,*pE,pH,pL,pU;
	double w;
	streamLine3D();
	streamLine3D(double _w);
	streamLine3D(point3D* _pi);
	streamLine3D(point3D* _pi,double _w);
	streamLine3D(point3D* _pi,point3D _pH0,point3D _pL0,point3D _pU0);
	streamLine3D(point3D* _pi,point3D _pH0,point3D _pL0,point3D _pU0,double _w);
	streamLine3D(point3D* _pi,point3D _pH0);
	streamLine3D(point3D* _pi,point3D _pH0,double _w);
	streamLine3D(point3D* _pi,point3D _pH0,point3D _pL0);
	streamLine3D(point3D* _pi,point3D _pH0,point3D _pL0,double _w);
	streamLine3D(point3D *_pi,point3D *_pe);
	streamLine3D(point3D *_pi,point3D *_pe,double _w);
	streamLine3D(streamLine3D *_s);
	void updateDirRx(double _theta);
	void updateDirRy(double _theta);
	void updateDirRz(double _theta);
	static void childStream(point3D* _pE,streamLine3D* _parentStream,streamLine3D* _child, double dist,double _w);
	void rotateStream(double* _M[3][3]);
	void rotateStreamAndPoints(double* _M[3][3]);
	void setIndex(long unsigned int _index);
	void RotH(const double& theta);
	void RotL(const double& theta);
	void RotU(const double& theta);

};



#endif /* STREAMLINE3D_H_ */
