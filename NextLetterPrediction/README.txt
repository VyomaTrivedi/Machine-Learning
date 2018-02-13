Using 'text_prediction.py' for Text prediction
----------------------------------------------

Required  : 1. Python 3, Keras, Theano 

		      or 

	    2. Access to any EC2 instance

Usage     : python text_prediction.py

The compilation of code gives two options : Test (0) / Train (1)

Test (0)  : 

	Input  : The text to be completed
	Output : Prediction of Neural Network

Train (1) :

	Input  : Training file(.txt) that has text (File can be selected through GUI)
	Output : Checkpoint files(.hdf5) after each epoch that have the parameters of the Neural Network