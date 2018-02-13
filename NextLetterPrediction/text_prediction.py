import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from random import randint
from Tkinter import Tk
from tkFileDialog import askopenfilename

def train():
	Tk().withdraw() 
	filename = askopenfilename() 
#	print(filename)	
	
	raw = open(filename).read()
	raw = raw.lower()
	
	unique_literals = set(raw)
	sorted_chars = sorted(list(unique_literals))
	#print sorted_chars

	char_to_int = dict((c, i) for i, c in enumerate(sorted_chars))

	n_chars = len(raw)
	n_vocab = len(sorted_chars)
	seq_length = 64
	dataX = []
	dataY = []
	for i in range(0, n_chars - seq_length, 1):
		seq_in = raw[i:i + seq_length]
		seq_out = raw[i + seq_length]
		dataX.append([char_to_int[char] for char in seq_in])
		dataY.append(char_to_int[seq_out])
	no_of_patterns = len(dataX)

	X = numpy.reshape(dataX, (len(dataX), seq_length, 1))

	X = X / float(n_vocab)

	y = np_utils.to_categorical(dataY)

	model = Sequential()
	model.add(LSTM(64, input_shape=(X.shape[1], X.shape[2])))
	model.add(Dense(y.shape[1], activation='softmax'))
#	model.compile(loss='categorical_crossentropy', optimizer='adam')
	model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True))


	filepath="weights-{epoch:02d}-{loss:.4f}.hdf5"
	checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
	callbacks_list = [checkpoint]

	model.fit(X, y, nb_epoch=10, batch_size=64, callbacks=callbacks_list)

def test():
	filename = "sample_cleaned.txt"
	raw = open(filename).read()
	raw = raw.lower()

	unique_literals = set(raw)
	sorted_chars = sorted(list(unique_literals))
	
	char_to_int = dict((c, i) for i, c in enumerate(sorted_chars))
	int_to_char = dict((i, c) for i, c in enumerate(sorted_chars))

	n_chars = len(raw)
	n_vocab = len(sorted_chars)
	seq_length = 64
	dataX = []
	dataY = []
	for i in range(0, n_chars - seq_length, 1):
		seq_in = raw[i:i + seq_length]
		seq_out = raw[i + seq_length]
		dataX.append([char_to_int[char] for char in seq_in])
		dataY.append(char_to_int[seq_out])
	n_patterns = len(dataX)
	X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
	X = X / float(n_vocab)
	
	y = np_utils.to_categorical(dataY)
	
	model = Sequential()
	model.add(LSTM(64, input_shape=(X.shape[1], X.shape[2])))
	model.add(Dense(y.shape[1], activation='softmax'))
	
	filename = "weights-improvement-06-2.2567.hdf5"
	model.load_weights(filename)
	model.compile(loss='categorical_crossentropy', optimizer='adam')
	
	
	start_text = raw_input("Seed:")
	pattern=[]
	pattern1 = []
	temp = 1
	for value in start_text:
		pattern1.insert(len(pattern1),char_to_int[value])
	if len(pattern1)<64:
		for i in range(64-len(pattern1)):
			pattern1.insert(len(pattern1),char_to_int[' '])
	
	pattern = pattern1
	
	out_text = ""
	output_length = randint(1,10)
	for i in range(output_length):
		x = numpy.reshape(pattern, (1, len(pattern), 1))
		print x
		x = x / float(n_vocab)
		prediction = model.predict(x, verbose=0)
		index = numpy.argmax(prediction)
		result = int_to_char[index]
		seq_in = [int_to_char[value] for value in pattern]
		out_text += result
		pattern.append(index)
		pattern = pattern[1:len(pattern)]
	print out_text
	

if(int(raw_input("Test(0) / Train(1) : "))):
	train()
else:
	test()