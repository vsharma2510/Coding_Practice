#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooGaussian.h"
#include "RooChebychev.h"
#include "RooAddPdf.h"
#include "TCanvas.h"
#include "TAxis.h"
#include "RooPlot.h"
using namespace RooFit;

void composite_pdf(){
  //Declare observvable x
  RooRealVar x("x","x",0,10);

  //Create two Gaussian PDFs g1(x,mean,sigma) and g2(x,mean2,sigma2) and their parameters
  RooRealVar mean("mean","mean of gaussian",5);
  RooRealVar sigma1("sigma1","width of gaussian", 0.5);
  RooRealVar sigma2("sigma2","width of gaussain",1);

  RooGaussian sig1("sig1","Signal component 1",x,mean,sigma1);
  RooGaussian sig2("sig2","Signal Component 2",x,mean,sigma2);

  //Build Chebychev polynomial pdf
  RooRealVar a0("a0","a0",0.5,0.0,1.0);
  RooRealVar a1("a1","a1",0.2,0.0,1.0);
  RooChebychev bkg("bkg","Background",x,RooArgSet(a0,a1));

  // Method 1 - Two RooAddPdfs
  //Add signal components

  RooRealVar sig1frac("sig1frac","fraction of component 1 in signal",0.8,0.0,1.0);
  RooAddPdf sig("sig","Signal",RooArgList(sig1,sig2),sig1frac);

  //Add signal and background
  RooRealVar bkgfrac("bkgfrac","fraction of background",0.5,0.0,1.0);
  RooAddPdf model("model","g1+g2+a",RooArgList(bkg,sig),bkgfrac);

  //Generate a data sample of 1000 events in x from model
  RooDataSet *data = model.generate(x,1000);

  //Fit model to data
  model.fitTo(*data);

  //Plot data and PDF overlaid
  RooPlot * xframe = x.frame(Title("Example of composite pdf=(sig1+sig2)+bkg)"));
  data->plotOn(xframe);
  model.plotOn(xframe);

  //Overlay the background component of model with a dashed line
  model.plotOn(xframe,Components(bkg),LineStyle(kDashed));

  //Overlay the background+sig2 compnents of model with a dotted line
  model.plotOn(xframe,Components(RooArgSet(bkg,sig2)),LineStyle(kDotted));

  //Print structure of composite pdf
  model.Print("t");
  xframe->Draw();
  double coeff1 = sig1frac.getVal();
  double coeff2 = bkgfrac.getVal();
  double coeff1_err = sig1frac.getError();
  double coeff2_err = bkgfrac.getError();
  cout<<"coeff1: "<<coeff1<<" coeff2: "<<coeff2<<endl;
  cout<<"coeff1_err: "<<coeff1_err<<" coeff2_err: "<<coeff2_err<<endl;
}
