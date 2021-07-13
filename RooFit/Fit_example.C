#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooGaussian.h"
#include "TCanvas.h"
#include "RooPlot.h"
#include "TAxis.h"
using namespace RooFit;

void basic_fit()
{
  //Setup Model

  RooRealVar x("x","x", -10, 10);
  RooRealVar mean("mean","mean of gaussian",1,-10,10);
  RooRealVar sigma("sigma","width of gaussian",1,0.1,10);

  //Build gaussian pdf in terms of x, mean and sigma
  RooGaussian gauss("gauss","gaussian PDF",x,mean,sigma);

  //Construct plot frame (i.e. in x)
  RooPlot *xframe = x.frame(Title("Gaussian pdf."));

  /* ----- Plot model and change parameter values ----- */

  //Plot gauss in frame (i.e in x)
  gauss.plotOn(xframe);

  //Change the value of sigma to 3
  sigma.setVal(3);

  //Plot gauss in frame (in x) and draw frame on canvas
  gauss.plotOn(xframe, LineColor(kRed));

  /* ----- Generate events ----- */
  
  //Generate a dataset of 1000 events in x from gauss
  RooDataSet *data = gauss.generate(x,1000);

  //Make a second plot frame in x and draw both the data and pdf in the frame
  RooPlot *xframe2 = x.frame(Title("Gaussian pdf with data"));
  data->plotOn(xframe2);
  gauss.plotOn(xframe2);

  /* ----- Fit model to data ----- */

  //Fit pdf to data
  RooFitResult* fitresult = gauss.fitTo(*data,Save()); //Need to save for getting final fit parameters later

  cout<<"fit result stored"<<endl;

  //Print values of mean and sigma (that now reflect fitted values and errors)
  mean.Print();
  sigma.Print();

  /* ----- Get fit parameters from floatParsFinal() ----- */
  RooRealVar* mean_final = (RooRealVar*)fitresult->floatParsFinal().find("mean");
  RooRealVar* sigma_final = (RooRealVar*)fitresult->floatParsFinal().find("sigma");

  double mean_error = mean_final->getError();
  cout<<"Error is "<<mean_error<<endl;
  sigma_final->Print();

}
