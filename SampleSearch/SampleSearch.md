One of the steps in automating an image acquisition routine for a microscope:  find the sample.    
A sample or region of interest (ROI) is not always in the field of view.  An automated routine has to identify that the sample is in the view or incrementally move the stage to the correct location.   

Image fingerprinting or autoencoding are worth examining if training on a fingerprint is faster than training on entire images.  

Number of peaks in the histogram of an image may be a good feature to train on, so we considered it qualitatively.  

Image of a known sample:
![Image description](SampleSearch/8.tif) 

Histogram of the image of known sample:
![Image description](Histogram_of_Image8.tiff) 

Field of view at different locations on the microscope stage:
![Image description](GeneratedEllipticalCurve_1.gif) 

Histogram of each field of view:
![Image description]('SampleSearch/Histogram of divisions of image 9.gif') 



