# Deep Learning: question papers in full

62 unique papers · 2018-19 to 2025-26 · Computer Engineering, Electronics and Telecommunication, Artificial Intelligence, Data Science, Information Technology, AI and Data Science, Computer Science and Business Systems, Common (all branches)

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 5 · paper e1026b7cd3fc

- Departments: Artificial Intelligence, Computer Engineering, Data Science, Electronics and Telecommunication, Information Technology
- Programmes: BTech AI 7012, BTech CSE DS 7011, BTech EXTC 7006, BTech IT 7001, MBATech (ELECTRONICS TELECOMMUNICATION, MBATech AI 7051, MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_AI_7012/Deep Learning/QP_Deep Learning(702AI0C008)_2025-2026.pdf` (+6 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech (IT)/MBA Tech (AI)/MBA Tech
(Comp)/MBA Tech (EXTC)
Year: III / IV / VI/Semester V/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Deep Learning
Date: 03 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i. Differentiate between Machine Learning and Deep Learning by   [5]
BL-2   explaining any four key differences between them. Support your answer
with examples relevant to real-world applications.
ii. Choose between machine learning or deep learning for the following
tasks and justify:
1.Sentiment analysis on a dataset of 2,000 product reviews (short text).
2. Detecting fraudulent transactions in a financial dataset with labelled
records.
3. Generating captions for a collection of 100,000 labelled images of
natural scenes.
CO-2;   b. Researchers are developing a deep learning system for automated leaf   [5]
BL-3   Disease classification using images. During model design, they must choose
an appropriate loss function for training and evaluate how it behaves on
specific predictions.
i. Discuss the major factors that influence the selection of a suitable loss
function in machine learning and deep learning applications.
ii. Suppose their classifier predicts the probability distribution for three
Disease classes (Normal, Mild, and Severe). For one validation image the
true one-hot label is Mild Disease (0,1,0). Their model outputs class
probabilities [0.1, 0.8, 0.1]. Compute the categorical cross-entropy for
this sample and interpret it.
CO-2;   c.   i. Which regularization method leads to weight sparsity? Explain why.   [5]
BL-2   ii. You are training a deep convolutional neural network to classify images
of handwritten digits using the MNIST dataset. After several epochs,
you notice that your training accuracy is very high, but your validation
accuracy is much lower. Explain how applying Dropout can help in this
situation. Describe what Dropout does during training and how it affects
the model’s performance and generalization ability.
CO-4;   d. Describe how RNNs process sequential data, how they capture context   [5]
BL-2   between words, and why they are suitable for handling variable-length
********** 1 **********
--- page 2 ---
sentences. Explain how Recurrent Neural Networks (RNNs) are used in
language translation applications like Google Translate.
Q2   a   [10]
CO-2;   .
BL-3
Given a network with the following parameters
𝜃11 (1) = 0.5, 𝜃12 (1) = 0.5, 𝜃21 (1) = 0.5, 𝜃22 (1) = 0.5, 𝜃11 (2) = 0.25, 𝜃21 (2) = 0.25, 𝑏1 =
𝑏2 = 0.
All neurons have a Sigmoid activation function. The actual output at O is 1.
Perform a forward pass and backward pass to update weights of 𝜃11 (1) ,
𝜃11 (2) 𝑎𝑛𝑑 𝑏2 using Gradient Descent algorithm (Assume learning rate = 0.5).
Q2   b   i. Discuss how skip connections in ResNet influence gradient flow, feature [10]
CO-3;   .   reuse, and help in addressing the vanishing gradient problem during
BL-2   backpropagation.
ii. Explain how the learning approach and feature extraction strategy of
InceptionNet differ from the AlexNet.
Q3   a   i. Determine the weights required to perform the classification as per the [10]
CO-2;   .   table using single layer perceptron network. Assume learning rate is 1
BL-3   and initial weights are 0. Consider threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   0
-1   1   1   1
1   -1   1   1
-1   1   1   1
ii. Illustrate the correspondence between components of a biological
neuron and an artificial neuron.
Q3   b A system is being designed for marking the attendance of students using face [10]
CO-3;   .   recognition. This task is given to you. You and your team are planning to use
BL-2   convolutional neural network for this task, but the dataset provided to you is
very small. Suggest and discuss different approaches to handle this issue.
How transfer learning can be applied to improve the model’s performance in
this situation.
Q4   a.   i. A neural network uses a dataset with 1000 samples and batch size of [10]
CO-2;   100. If the learning rate and other parameters remain constant, explain
BL-3   how many weight updates occur in:
(i)   Batch Gradient Descent
(ii)   Stochastic Gradient Descent (SGD)
(iii)   Mini-Batch Gradient Descent
ii.   Consider the cost function J(θ)=0.5𝜃2. Perform two iterations of SGD
with Momentum, where learning rate (η or α) is 0.1, momentum is 0.9,
initial velocity 𝑣0=0, initial parameter 𝜃0=1. Write the update rule and
compute the velocity & parameter after each iteration.
********** 2 **********
--- page 3 ---
iii.   List the number of hyperparameters required in training a model using
Stochastic Gradient Descent with Momentum.
Q4   b.   i.   Define the vanishing gradient problem in RNNs. Why does it   [10]
CO-4;   occur?
BL-2   ii.   In a sentence like “The dogs barked at the thief and … were
appreciated”, why does a simple RNN fail to predict the correct
verb form?
iii.   Justify how the forget gate in LSTM helps preserve long-term
dependencies.
iv.   Assuming that the forget gate output is ft=[0.1,0.9] and the
previous cell state Ct−1=[2,1], compute the updated cell memory
contribution from the forget gate.
Q5   a. With respect to LSTM, answer the following questions:   [10]
CO-4;   i.   Identify the purpose of each gate (input, forget, output) in an LSTM
BL-2   unit.
ii.   Consider the sentence “Artificial Intelligence has revolutionized
every domain. The work force will have to update themselves to
remain relevant.” Explain how the input and forget gates update
memory as context changes.
Given: it=0.7,  ft=0.4,  ot=0.8,  𝐶𝑡̃=0.9,  Ct−1=0.5. Compute the new
cell state Ct and hidden state ht. Assume ht=ot × tanh(Ct)
iii. Why are LSTM models more effective for language modelling than
simple RNNs?
Q5   b. Explain the working principle of the AdaGrad optimizer. Write the update [10]
CO-2;   rule of AdaGrad. List advantages and disadvantages of using AdaGrad
BL-2   compared to standard Stochastic Gradient Descent (SGD).
Q6   a.   i. Consider input image of size 128 X 128 X 3.   [10]
CO-3;   1) It is passed through convolution layer 1 with filter size 3x3, no. of
BL-3   filters = 16, no padding and stride = 1.
2) It is followed by pooling layer of mask size 2X2 with stride=2.
3) Then it is passed through convolution layer 2 with filter size 3X3,
no. of filters = 32, no padding and stride = 1.
4) It is followed by pooling layer of mask size 2X2 with stride=2.
5) Further it is passed through fully connected layer 1 consisting of 240
neurons and then FC2 with 120 neurons.
6) Finally, SoftMax layer of 5 neurons is used. Calculate the size of
activation and trainable parameters at the end of each layer.
ii. Determine the output of the given 5x5 image after convoluting with the
3x3 kernel. Given padding=valid and stride=2
3   1   2   2   1   1   0   -1
2   1   2   1   0   2   0   -2
3   2   1   0   1   1   0   -1
0   3   0   1   2
1   1   0   2   3
Q6   b.   i. Explain the concept of activation functions in deep neural networks. Discuss [10]
CO-2;   the role of non-linearity.
BL-3   ii. Compare the following activation functions: Sigmoid, Tanh, ReLU, and
Leaky ReLU. Include their advantages, disadvantages.
Q7   a.   Explain how information flows through a feedforward network during the [10]
CO-2;   forward propagation process, describing the role of weights, biases, and
BL-3   activation functions in transforming inputs to outputs. Then, compute the
output of the following FNN:
********** 3 **********
--- page 4 ---
• Network structure: 2 input neurons → 2 hidden neurons (ReLU
activation) → 1 output neuron (ReLU activation).
•   Input: X=[1,0]
• Weights and biases:
𝑊1 = [0.2 0.4 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.5 0.6] 𝑏2 = 0.1
0.3
b.   i. Explain how Convolutional Neural Networks (CNNs) extract hierarchical [10]
Q7   features from an input image. Include the roles of convolutional, pooling,
CO-3   and fully connected layers in this process.
BL-2   ii. Discuss why CNNs are preferred over traditional fully connected
Artificial Neural Networks (ANNs) for image processing tasks.
iii. Describe how CNNs can be applied in Medical Image Analysis and
Autonomous Vehicles. Provide an example for each application and
highlight the advantages of using CNNs in these scenarios.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper 41d5bd68f6d2

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIDS_7056/Deep Learning/QP_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA
SCIENCE)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Deep Learning
Date: 11 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Attempt any 4 questions from the remaining questions.
6. Attempt five (5) questions in total.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1. (a)   A company is working on a face recognition system. Provide five reasons why would deep 5
CO1;   learning be more suitable than traditional machine learning for this task?
SO1;BL2
Q1. (b)   Mention five differences between single layer perceptron (SLP) and multilayer perceptron 5
CO2;   (MLP) in terms of model architecture, decision boundary, application, computational cost,
SO1;BL3   and learning algorithm.
Q1. (c)   A 6 × 6 image uses a 3 × 3 kernel with stride = 1. Compare the output sizes for:   5
CO3;   i.   No padding (P = 0)
SO1;BL3   ii.   With padding (P = 1).
iii.   Also state why padding helps for border pixels.
Q1. (d)   5
CO4;   Why does LSTM handle long dependencies better than vanilla RNN?
SO1;BL3
Q2 (a)   A company is building a system that takes an image as input, detects objects and generates 5
CO2;   a caption. Which deep learning models are required in this pipeline. Also, mention
SO1;BL1,   challenges in building such a system.
2
Q2 (b)   Identify suitable loss functions and calculate it’s value for the following cases:   5
CO2;   i.   You are building a model to classify emails as Spam (1) or Not Spam (0). The
SO1;BL4   output of the model is a probability between 0 and 1. For a given email, the
model outputs a probability of 0.8, and the actual label is 1.
ii. A regression model is used to predict house prices based on features like area,
location, and number of rooms. The output is a continuous value. For a given
house, the predicted price is ₹52 lakh, while the actual price is ₹50 lakh.
Q2 (c)   A retailer needs on-device detection of missing items from shelf images. Compare AlexNet 10
CO3;   vs Inception vs ResNet in terms of their characteristics, network depth, accuracy, and
SO1;BL4   compute memory. Recommend any one architecture with reasons.
Q3 (a)   An input grayscale image of size 28 × 28 × 1is passed through the following architecture: 10
CO3;
SO1;BL5   • Conv Layer 1: 32 filters of size 3 × 3, stride = 1, padding = valid
• Max Pooling 1: 2 × 2, stride = 2
• Conv Layer 2: 64 filters of size 3 × 3, stride = 1, padding = valid
• Max Pooling 2: 2 × 2, stride = 2
• Conv Layer 3: 128 filters of size 3 × 3, stride = 1, padding = valid
•   Flatten Layer
• Dense Layer 1: 128 neurons
********** 1 **********
--- page 2 ---
•   Output Layer: 10 neurons
Compute the output shape at each layer, calculate the number of parameters for each
trainable layer and find the total number of trainable parameters. Note: Consider floor
wherever required
Q3 (b)   For a wearable device that recognizes daily activities (e.g., walking, running) with limited 10
CO4;   battery. Answer the following:
SO1;BL4
i.   Compare LSTM and GRU models.
ii.   Which model has fewer parameters and is faster?
iii.   Which model may give slightly better accuracy for complex patterns?
iv.   Which model would you recommend for this scenario and why?
Q4 (a)   i.   Apply perceptron training algorithm for single epoch to determine the weights and 10
CO2;   bias for AND function using bipolar inputs and targets. Use learning rate 𝜂=1,
SO1;BL3   initial weights 𝑤1=0, 𝑤2=0,and bias 𝑏=0. Use activation function:
𝑦𝑜𝑢𝑡 = 1, if 𝑦𝑖𝑛>=0
𝑦𝑜𝑢𝑡 = −1, otherwise
Show the complete training table for each sample.
ii.   Identify the equation of decision boundary
Q4 (b)   Explain why early CNN layers transfer well across domains and later layers are task-   10
CO3;   specific. Use an example (e.g., cats vs X-rays).
SO1;BL1,
2
Q5 (a)   i.   Explain the network architecture of gated recurrent neural network with   10
CO4;   formulas.
SO1;BL3   ii.   You train an RNN on sequences of length 200 but use truncated BPTT with
window 25. How many timesteps does each gradient flow through?
Q5 (b)   i.   While training a model, you observe: highly fluctuating loss curve and faster   10
CO2;   initial convergence. Which gradient descent variant is being used? With the
SO1;BL4   help of an algorithm explain why this behaviour occurs.
ii.   Compare L1 and L2 regularization technique. You are working on a model
with many irrelevant features. Which regularization would you use and why?
Q6 (a)   Consider the following neural network with inputs [x1,x2]=[0.5,0.1] and targets=[0.6,0.3]. 10
CO2;   Consider bias on all nodes at hidden layer b1=0.1 and bias on all nodes at output layer b2
SO1;BL5   = 0.1, learning rate η =0.5 and sigmoid activation function. The weights are: w13=0.45,
w14=0.32, w23=0.45, w24=0.67, w35=0.56, w36=0.50, w45=0.23, w46=0.12.
i.   Compute output of node 3, 4, 5, and 6.
ii.   Calculate mean square error at output layer.
iii.   Update weights w46 and w24.
Q6 (b)   i.   While training a model using AdaGrad, you observe that the learning rate 10
CO2;   becomes extremely small after several iterations. Explain why this happens.
SO1;BL3
********** 2 **********
--- page 3 ---
Show how RMSProp modifies the learning rate calculation to resolve this
problem with an algorithm.
ii.   A neural network is overfitting the training data. Explain any three techniques
to reduce overfitting.
Q7 (a)   i.   Compare sigmoid, relu, and tanh activation functions in terms of output range   10
CO2;   and their respective drawbacks. Apply these activation functions for input x=−2.
SO1;BL3   ii.   Identify whether the learning rate and bias are a parameter or a hyperparameter.
Explain the role of learning rate in neural network training. What happens when
the learning rate is too small or too large.
Q7 (b)   Explain Backpropagation Through Time in recurrent neural networks with diagram.   10
CO4;   Discuss vanishing and exploding gradients problem with solution.
SO1;BL4
********** 3 **********
````

## 2025-26 · Final-Exam · Sem 7 · paper 13283dc8714d

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_Computer_7002/Deep Learning/QP_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech (IT)/MBA Tech (AI)/MBA Tech
(Comp)/MBA Tech (EXTC)
Year: III / IV / VI/Semester V/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Deep Learning
Date: 03 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i. Differentiate between Machine Learning and Deep Learning by   [5]
BL-2   explaining any four key differences between them. Support your answer
with examples relevant to real-world applications.
ii. Choose between machine learning or deep learning for the following
tasks and justify:
1.Sentiment analysis on a dataset of 2,000 product reviews (short text).
2. Detecting fraudulent transactions in a financial dataset with labelled
records.
3. Generating captions for a collection of 100,000 labelled images of
natural scenes.
CO-2;   b. Researchers are developing a deep learning system for automated leaf   [5]
BL-3   Disease classification using images. During model design, they must choose
an appropriate loss function for training and evaluate how it behaves on
specific predictions.
i. Discuss the major factors that influence the selection of a suitable loss
function in machine learning and deep learning applications.
ii. Suppose their classifier predicts the probability distribution for three
Disease classes (Normal, Mild, and Severe). For one validation image the
true one-hot label is Mild Disease (0,1,0). Their model outputs class
probabilities [0.1, 0.8, 0.1]. Compute the categorical cross-entropy for
this sample and interpret it.
CO-2;   c.   i. Which regularization method leads to weight sparsity? Explain why.   [5]
BL-2   ii. You are training a deep convolutional neural network to classify images
of handwritten digits using the MNIST dataset. After several epochs,
you notice that your training accuracy is very high, but your validation
accuracy is much lower. Explain how applying Dropout can help in this
situation. Describe what Dropout does during training and how it affects
the model’s performance and generalization ability.
CO-4;   d. Describe how RNNs process sequential data, how they capture context   [5]
BL-2   between words, and why they are suitable for handling variable-length
********** 1 **********
--- page 2 ---
sentences. Explain how Recurrent Neural Networks (RNNs) are used in
language translation applications like Google Translate.
Q2   a   [10]
CO-2;   .
BL-3
Given a network with the following parameters
𝜃11 (1) = 0.5, 𝜃12 (1) = 0.5, 𝜃21 (1) = 0.5, 𝜃22 (1) = 0.5, 𝜃11 (2) = 0.25, 𝜃21 (2) = 0.25, 𝑏1 =
𝑏2 = 0.
All neurons have a Sigmoid activation function. The actual output at O is 1.
Perform a forward pass and backward pass to update weights of 𝜃11 (1) ,
𝜃11 (2) 𝑎𝑛𝑑 𝑏2 using Gradient Descent algorithm (Assume learning rate = 0.5).
Q2   b   i. Discuss how skip connections in ResNet influence gradient flow, feature [10]
CO-3;   .   reuse, and help in addressing the vanishing gradient problem during
BL-2   backpropagation.
ii. Explain how the learning approach and feature extraction strategy of
InceptionNet differ from the AlexNet.
Q3   a   i. Determine the weights required to perform the classification as per the [10]
CO-2;   .   table using single layer perceptron network. Assume learning rate is 1
BL-3   and initial weights are 0. Consider threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   0
-1   1   1   1
1   -1   1   1
-1   1   1   1
ii. Illustrate the correspondence between components of a biological
neuron and an artificial neuron.
Q3   b A system is being designed for marking the attendance of students using face [10]
CO-3;   .   recognition. This task is given to you. You and your team are planning to use
BL-2   convolutional neural network for this task, but the dataset provided to you is
very small. Suggest and discuss different approaches to handle this issue.
How transfer learning can be applied to improve the model’s performance in
this situation.
Q4   a.   i. A neural network uses a dataset with 1000 samples and batch size of [10]
CO-2;   100. If the learning rate and other parameters remain constant, explain
BL-3   how many weight updates occur in:
(i)   Batch Gradient Descent
(ii)   Stochastic Gradient Descent (SGD)
(iii)   Mini-Batch Gradient Descent
ii.   Consider the cost function J(θ)=0.5𝜃2. Perform two iterations of SGD
with Momentum, where learning rate (η or α) is 0.1, momentum is 0.9,
initial velocity 𝑣0=0, initial parameter 𝜃0=1. Write the update rule and
compute the velocity & parameter after each iteration.
********** 2 **********
--- page 3 ---
iii.   List the number of hyperparameters required in training a model using
Stochastic Gradient Descent with Momentum.
Q4   b.   i.   Define the vanishing gradient problem in RNNs. Why does it   [10]
CO-4;   occur?
BL-2   ii.   In a sentence like “The dogs barked at the thief and … were
appreciated”, why does a simple RNN fail to predict the correct
verb form?
iii.   Justify how the forget gate in LSTM helps preserve long-term
dependencies.
iv.   Assuming that the forget gate output is ft=[0.1,0.9] and the
previous cell state Ct−1=[2,1], compute the updated cell memory
contribution from the forget gate.
Q5   a. With respect to LSTM, answer the following questions:   [10]
CO-4;   i.   Identify the purpose of each gate (input, forget, output) in an LSTM
BL-2   unit.
ii.   Consider the sentence “Artificial Intelligence has revolutionized
every domain. The work force will have to update themselves to
remain relevant.” Explain how the input and forget gates update
memory as context changes.
Given: it=0.7,  ft=0.4,  ot=0.8,  𝐶𝑡̃=0.9,  Ct−1=0.5. Compute the new
cell state Ct and hidden state ht. Assume ht=ot × tanh(Ct)
iii. Why are LSTM models more effective for language modelling than
simple RNNs?
Q5   b. Explain the working principle of the AdaGrad optimizer. Write the update [10]
CO-2;   rule of AdaGrad. List advantages and disadvantages of using AdaGrad
BL-2   compared to standard Stochastic Gradient Descent (SGD).
Q6   a.   i. Consider input image of size 128 X 128 X 3.   [10]
CO-3;   1) It is passed through convolution layer 1 with filter size 3x3, no. of
BL-3   filters = 16, no padding and stride = 1.
2) It is followed by pooling layer of mask size 2X2 with stride=2.
3) Then it is passed through convolution layer 2 with filter size 3X3,
no. of filters = 32, no padding and stride = 1.
4) It is followed by pooling layer of mask size 2X2 with stride=2.
5) Further it is passed through fully connected layer 1 consisting of 240
neurons and then FC2 with 120 neurons.
6) Finally, SoftMax layer of 5 neurons is used. Calculate the size of
activation and trainable parameters at the end of each layer.
ii. Determine the output of the given 5x5 image after convoluting with the
3x3 kernel. Given padding=valid and stride=2
3   1   2   2   1   1   0   -1
2   1   2   1   0   2   0   -2
3   2   1   0   1   1   0   -1
0   3   0   1   2
1   1   0   2   3
Q6   b.   i. Explain the concept of activation functions in deep neural networks. Discuss [10]
CO-2;   the role of non-linearity.
BL-3   ii. Compare the following activation functions: Sigmoid, Tanh, ReLU, and
Leaky ReLU. Include their advantages, disadvantages.
Q7   a.   Explain how information flows through a feedforward network during the [10]
CO-2;   forward propagation process, describing the role of weights, biases, and
BL-3   activation functions in transforming inputs to outputs. Then, compute the
output of the following FNN:
********** 3 **********
--- page 4 ---
• Network structure: 2 input neurons → 2 hidden neurons (ReLU
activation) → 1 output neuron (ReLU activation).
•   Input: X=[1,0]
• Weights and biases:
𝑊1 = [0.2 0.4 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.5 0.6] 𝑏2 = 0.1
0.3
b.   i. Explain how Convolutional Neural Networks (CNNs) extract hierarchical [10]
Q7   features from an input image. Include the roles of convolutional, pooling,
CO-3   and fully connected layers in this process.
BL-2   ii. Discuss why CNNs are preferred over traditional fully connected
Artificial Neural Networks (ANNs) for image processing tasks.
iii. Describe how CNNs can be applied in Medical Image Analysis and
Autonomous Vehicles. Provide an example for each application and
highlight the advantages of using CNNs in these scenarios.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 7 · paper 53de151930a7

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_EXTC_7006/Deep Learning/QP_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech (IT)/MBA Tech (AI)/MBA Tech
(Comp)/MBA Tech (EXTC)
Year: III / IV / VI/Semester V/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Deep Learning
Date: 03 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i. Differentiate between Machine Learning and Deep Learning by   [5]
BL-2   explaining any four key differences between them. Support your answer
with examples relevant to real-world applications.
ii. Choose between machine learning or deep learning for the following
tasks and justify:
1.Sentiment analysis on a dataset of 2,000 product reviews (short text).
2. Detecting fraudulent transactions in a financial dataset with labelled
records.
3. Generating captions for a collection of 100,000 labelled images of
natural scenes.
CO-2;   b. Researchers are developing a deep learning system for automated leaf   [5]
BL-3   Disease classification using images. During model design, they must choose
an appropriate loss function for training and evaluate how it behaves on
specific predictions.
i. Discuss the major factors that influence the selection of a suitable loss
function in machine learning and deep learning applications.
ii. Suppose their classifier predicts the probability distribution for three
Disease classes (Normal, Mild, and Severe). For one validation image the
true one-hot label is Mild Disease (0,1,0). Their model outputs class
probabilities [0.1, 0.8, 0.1]. Compute the categorical cross-entropy for
this sample and interpret it.
CO-2;   c.   i. Which regularization method leads to weight sparsity? Explain why.   [5]
BL-2   ii. You are training a deep convolutional neural network to classify images
of handwritten digits using the MNIST dataset. After several epochs,
you notice that your training accuracy is very high, but your validation
accuracy is much lower. Explain how applying Dropout can help in this
situation. Describe what Dropout does during training and how it affects
the model’s performance and generalization ability.
CO-4;   d. Describe how RNNs process sequential data, how they capture context   [5]
BL-2   between words, and why they are suitable for handling variable-length
********** 1 **********
--- page 2 ---
sentences. Explain how Recurrent Neural Networks (RNNs) are used in
language translation applications like Google Translate.
Q2   a   [10]
CO-2;   .
BL-3
Given a network with the following parameters
𝜃11 (1) = 0.5, 𝜃12 (1) = 0.5, 𝜃21 (1) = 0.5, 𝜃22 (1) = 0.5, 𝜃11 (2) = 0.25, 𝜃21 (2) = 0.25, 𝑏1 =
𝑏2 = 0.
All neurons have a Sigmoid activation function. The actual output at O is 1.
Perform a forward pass and backward pass to update weights of 𝜃11 (1) ,
𝜃11 (2) 𝑎𝑛𝑑 𝑏2 using Gradient Descent algorithm (Assume learning rate = 0.5).
Q2   b   i. Discuss how skip connections in ResNet influence gradient flow, feature [10]
CO-3;   .   reuse, and help in addressing the vanishing gradient problem during
BL-2   backpropagation.
ii. Explain how the learning approach and feature extraction strategy of
InceptionNet differ from the AlexNet.
Q3   a   i. Determine the weights required to perform the classification as per the [10]
CO-2;   .   table using single layer perceptron network. Assume learning rate is 1
BL-3   and initial weights are 0. Consider threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   0
-1   1   1   1
1   -1   1   1
-1   1   1   1
ii. Illustrate the correspondence between components of a biological
neuron and an artificial neuron.
Q3   b A system is being designed for marking the attendance of students using face [10]
CO-3;   .   recognition. This task is given to you. You and your team are planning to use
BL-2   convolutional neural network for this task, but the dataset provided to you is
very small. Suggest and discuss different approaches to handle this issue.
How transfer learning can be applied to improve the model’s performance in
this situation.
Q4   a.   i. A neural network uses a dataset with 1000 samples and batch size of [10]
CO-2;   100. If the learning rate and other parameters remain constant, explain
BL-3   how many weight updates occur in:
(i)   Batch Gradient Descent
(ii)   Stochastic Gradient Descent (SGD)
(iii)   Mini-Batch Gradient Descent
ii.   Consider the cost function J(θ)=0.5𝜃2. Perform two iterations of SGD
with Momentum, where learning rate (η or α) is 0.1, momentum is 0.9,
initial velocity 𝑣0=0, initial parameter 𝜃0=1. Write the update rule and
compute the velocity & parameter after each iteration.
********** 2 **********
--- page 3 ---
iii.   List the number of hyperparameters required in training a model using
Stochastic Gradient Descent with Momentum.
Q4   b.   i.   Define the vanishing gradient problem in RNNs. Why does it   [10]
CO-4;   occur?
BL-2   ii.   In a sentence like “The dogs barked at the thief and … were
appreciated”, why does a simple RNN fail to predict the correct
verb form?
iii.   Justify how the forget gate in LSTM helps preserve long-term
dependencies.
iv.   Assuming that the forget gate output is ft=[0.1,0.9] and the
previous cell state Ct−1=[2,1], compute the updated cell memory
contribution from the forget gate.
Q5   a. With respect to LSTM, answer the following questions:   [10]
CO-4;   i.   Identify the purpose of each gate (input, forget, output) in an LSTM
BL-2   unit.
ii.   Consider the sentence “Artificial Intelligence has revolutionized
every domain. The work force will have to update themselves to
remain relevant.” Explain how the input and forget gates update
memory as context changes.
Given: it=0.7,  ft=0.4,  ot=0.8,  𝐶𝑡̃=0.9,  Ct−1=0.5. Compute the new
cell state Ct and hidden state ht. Assume ht=ot × tanh(Ct)
iii. Why are LSTM models more effective for language modelling than
simple RNNs?
Q5   b. Explain the working principle of the AdaGrad optimizer. Write the update [10]
CO-2;   rule of AdaGrad. List advantages and disadvantages of using AdaGrad
BL-2   compared to standard Stochastic Gradient Descent (SGD).
Q6   a.   i. Consider input image of size 128 X 128 X 3.   [10]
CO-3;   1) It is passed through convolution layer 1 with filter size 3x3, no. of
BL-3   filters = 16, no padding and stride = 1.
2) It is followed by pooling layer of mask size 2X2 with stride=2.
3) Then it is passed through convolution layer 2 with filter size 3X3,
no. of filters = 32, no padding and stride = 1.
4) It is followed by pooling layer of mask size 2X2 with stride=2.
5) Further it is passed through fully connected layer 1 consisting of 240
neurons and then FC2 with 120 neurons.
6) Finally, SoftMax layer of 5 neurons is used. Calculate the size of
activation and trainable parameters at the end of each layer.
ii. Determine the output of the given 5x5 image after convoluting with the
3x3 kernel. Given padding=valid and stride=2
3   1   2   2   1   1   0   -1
2   1   2   1   0   2   0   -2
3   2   1   0   1   1   0   -1
0   3   0   1   2
1   1   0   2   3
Q6   b.   i. Explain the concept of activation functions in deep neural networks. Discuss [10]
CO-2;   the role of non-linearity.
BL-3   ii. Compare the following activation functions: Sigmoid, Tanh, ReLU, and
Leaky ReLU. Include their advantages, disadvantages.
Q7   a.   Explain how information flows through a feedforward network during the [10]
CO-2;   forward propagation process, describing the role of weights, biases, and
BL-3   activation functions in transforming inputs to outputs. Then, compute the
output of the following FNN:
********** 3 **********
--- page 4 ---
• Network structure: 2 input neurons → 2 hidden neurons (ReLU
activation) → 1 output neuron (ReLU activation).
•   Input: X=[1,0]
• Weights and biases:
𝑊1 = [0.2 0.4 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.5 0.6] 𝑏2 = 0.1
0.3
b.   i. Explain how Convolutional Neural Networks (CNNs) extract hierarchical [10]
Q7   features from an input image. Include the roles of convolutional, pooling,
CO-3   and fully connected layers in this process.
BL-2   ii. Discuss why CNNs are preferred over traditional fully connected
Artificial Neural Networks (ANNs) for image processing tasks.
iii. Describe how CNNs can be applied in Medical Image Analysis and
Autonomous Vehicles. Provide an example for each application and
highlight the advantages of using CNNs in these scenarios.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 7 · paper 8ca75a03c82b

- Departments: Electronics and Telecommunication
- Programmes: MBATech (ELECTRONICS & TELECOMMUNICATIO
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/MBATech (ELECTRONICS & TELECOMMUNICATIO_ba3ceaa3/Deep Learning/QP_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech (IT)/MBA Tech (AI)/MBA Tech
(Comp)/MBA Tech (EXTC)
Year: III / IV / VI/Semester V/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Deep Learning
Date: 03 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i. Differentiate between Machine Learning and Deep Learning by   [5]
BL-2   explaining any four key differences between them. Support your answer
with examples relevant to real-world applications.
ii. Choose between machine learning or deep learning for the following
tasks and justify:
1.Sentiment analysis on a dataset of 2,000 product reviews (short text).
2. Detecting fraudulent transactions in a financial dataset with labelled
records.
3. Generating captions for a collection of 100,000 labelled images of
natural scenes.
CO-2;   b. Researchers are developing a deep learning system for automated leaf   [5]
BL-3   Disease classification using images. During model design, they must choose
an appropriate loss function for training and evaluate how it behaves on
specific predictions.
i. Discuss the major factors that influence the selection of a suitable loss
function in machine learning and deep learning applications.
ii. Suppose their classifier predicts the probability distribution for three
Disease classes (Normal, Mild, and Severe). For one validation image the
true one-hot label is Mild Disease (0,1,0). Their model outputs class
probabilities [0.1, 0.8, 0.1]. Compute the categorical cross-entropy for
this sample and interpret it.
CO-2;   c.   i. Which regularization method leads to weight sparsity? Explain why.   [5]
BL-2   ii. You are training a deep convolutional neural network to classify images
of handwritten digits using the MNIST dataset. After several epochs,
you notice that your training accuracy is very high, but your validation
accuracy is much lower. Explain how applying Dropout can help in this
situation. Describe what Dropout does during training and how it affects
the model’s performance and generalization ability.
CO-4;   d. Describe how RNNs process sequential data, how they capture context   [5]
BL-2   between words, and why they are suitable for handling variable-length
********** 1 **********
--- page 2 ---
sentences. Explain how Recurrent Neural Networks (RNNs) are used in
language translation applications like Google Translate.
Q2   a   [10]
CO-2;   .
BL-3
Given a network with the following parameters
𝜃11 (1) = 0.5, 𝜃12 (1) = 0.5, 𝜃21 (1) = 0.5, 𝜃22 (1) = 0.5, 𝜃11 (2) = 0.25, 𝜃21 (2) = 0.25, 𝑏1 =
𝑏2 = 0.
All neurons have a Sigmoid activation function. The actual output at O is 1.
Perform a forward pass and backward pass to update weights of 𝜃11 (1) ,
𝜃11 (2) 𝑎𝑛𝑑 𝑏2 using Gradient Descent algorithm (Assume learning rate = 0.5).
Q2   b   i. Discuss how skip connections in ResNet influence gradient flow, feature [10]
CO-3;   .   reuse, and help in addressing the vanishing gradient problem during
BL-2   backpropagation.
ii. Explain how the learning approach and feature extraction strategy of
InceptionNet differ from the AlexNet.
Q3   a   i. Determine the weights required to perform the classification as per the [10]
CO-2;   .   table using single layer perceptron network. Assume learning rate is 1
BL-3   and initial weights are 0. Consider threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   0
-1   1   1   1
1   -1   1   1
-1   1   1   1
ii. Illustrate the correspondence between components of a biological
neuron and an artificial neuron.
Q3   b A system is being designed for marking the attendance of students using face [10]
CO-3;   .   recognition. This task is given to you. You and your team are planning to use
BL-2   convolutional neural network for this task, but the dataset provided to you is
very small. Suggest and discuss different approaches to handle this issue.
How transfer learning can be applied to improve the model’s performance in
this situation.
Q4   a.   i. A neural network uses a dataset with 1000 samples and batch size of [10]
CO-2;   100. If the learning rate and other parameters remain constant, explain
BL-3   how many weight updates occur in:
(i)   Batch Gradient Descent
(ii)   Stochastic Gradient Descent (SGD)
(iii)   Mini-Batch Gradient Descent
ii.   Consider the cost function J(θ)=0.5𝜃2. Perform two iterations of SGD
with Momentum, where learning rate (η or α) is 0.1, momentum is 0.9,
initial velocity 𝑣0=0, initial parameter 𝜃0=1. Write the update rule and
compute the velocity & parameter after each iteration.
********** 2 **********
--- page 3 ---
iii.   List the number of hyperparameters required in training a model using
Stochastic Gradient Descent with Momentum.
Q4   b.   i.   Define the vanishing gradient problem in RNNs. Why does it   [10]
CO-4;   occur?
BL-2   ii.   In a sentence like “The dogs barked at the thief and … were
appreciated”, why does a simple RNN fail to predict the correct
verb form?
iii.   Justify how the forget gate in LSTM helps preserve long-term
dependencies.
iv.   Assuming that the forget gate output is ft=[0.1,0.9] and the
previous cell state Ct−1=[2,1], compute the updated cell memory
contribution from the forget gate.
Q5   a. With respect to LSTM, answer the following questions:   [10]
CO-4;   i.   Identify the purpose of each gate (input, forget, output) in an LSTM
BL-2   unit.
ii.   Consider the sentence “Artificial Intelligence has revolutionized
every domain. The work force will have to update themselves to
remain relevant.” Explain how the input and forget gates update
memory as context changes.
Given: it=0.7,  ft=0.4,  ot=0.8,  𝐶𝑡̃=0.9,  Ct−1=0.5. Compute the new
cell state Ct and hidden state ht. Assume ht=ot × tanh(Ct)
iii. Why are LSTM models more effective for language modelling than
simple RNNs?
Q5   b. Explain the working principle of the AdaGrad optimizer. Write the update [10]
CO-2;   rule of AdaGrad. List advantages and disadvantages of using AdaGrad
BL-2   compared to standard Stochastic Gradient Descent (SGD).
Q6   a.   i. Consider input image of size 128 X 128 X 3.   [10]
CO-3;   1) It is passed through convolution layer 1 with filter size 3x3, no. of
BL-3   filters = 16, no padding and stride = 1.
2) It is followed by pooling layer of mask size 2X2 with stride=2.
3) Then it is passed through convolution layer 2 with filter size 3X3,
no. of filters = 32, no padding and stride = 1.
4) It is followed by pooling layer of mask size 2X2 with stride=2.
5) Further it is passed through fully connected layer 1 consisting of 240
neurons and then FC2 with 120 neurons.
6) Finally, SoftMax layer of 5 neurons is used. Calculate the size of
activation and trainable parameters at the end of each layer.
ii. Determine the output of the given 5x5 image after convoluting with the
3x3 kernel. Given padding=valid and stride=2
3   1   2   2   1   1   0   -1
2   1   2   1   0   2   0   -2
3   2   1   0   1   1   0   -1
0   3   0   1   2
1   1   0   2   3
Q6   b.   i. Explain the concept of activation functions in deep neural networks. Discuss [10]
CO-2;   the role of non-linearity.
BL-3   ii. Compare the following activation functions: Sigmoid, Tanh, ReLU, and
Leaky ReLU. Include their advantages, disadvantages.
Q7   a.   Explain how information flows through a feedforward network during the [10]
CO-2;   forward propagation process, describing the role of weights, biases, and
BL-3   activation functions in transforming inputs to outputs. Then, compute the
output of the following FNN:
********** 3 **********
--- page 4 ---
• Network structure: 2 input neurons → 2 hidden neurons (ReLU
activation) → 1 output neuron (ReLU activation).
•   Input: X=[1,0]
• Weights and biases:
𝑊1 = [0.2 0.4 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.5 0.6] 𝑏2 = 0.1
0.3
b.   i. Explain how Convolutional Neural Networks (CNNs) extract hierarchical [10]
Q7   features from an input image. Include the roles of convolutional, pooling,
CO-3   and fully connected layers in this process.
BL-2   ii. Discuss why CNNs are preferred over traditional fully connected
Artificial Neural Networks (ANNs) for image processing tasks.
iii. Describe how CNNs can be applied in Medical Image Analysis and
Autonomous Vehicles. Provide an example for each application and
highlight the advantages of using CNNs in these scenarios.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 5 · paper ba5e45671bd1

- Departments: Artificial Intelligence, Computer Engineering, Electronics and Telecommunication, Information Technology
- Programmes: B TECH / ARTIFICAL INTELLIGENCE, B TECH / COMPUTER, B TECH / EXTC, B TECH / IT, B.TECH INTEGRATED / COMPUTER, MBA TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-V/DEEP LEARNING/B Tech, Deep Learning, 2025-26 Final Exam.pdf` (+6 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: ocr (4 pages), mean OCR confidence 89.9
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

(CSE - DS) G1)/B, Tech (EXTO)B. Tech Intg. (CE)B. Tech (I1T)/MBA Tech (AD/MBA fech
(Comp)/MBA Tech (EXTC)
Year: III / IV/ VI/Semester V/Semester VII/Semester XI(Exam Year: 2025- 2026)
Subject: Deep Learning

Date: 03 Dec 2025 Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100

FINAL EXAMINATION (Acad. Year:2025-2026)

Instructions:

1. This question paper contains 4 pages.

2. Answer to each new question to be started on a fresh page.

3. Figure in right hand side indicates full marks

4. Question No. 1 is compulsory.

5. Out of remaining questions, attempt any 4 questions.

6. All questions carry equal marks.

7. Assume Suitable data if necessary.

Ql Answer briefly: [20]
CO-1; | a.| i. Differentiate between Machine Learning and Deep Learning by | [5]
BL-2 explaining any four key differences between them. Support your answer

with examples relevant to real-world applications.
ii. Choose between machine learning or deep learning for the following
tasks and justify:
1.Sentiment analysis on a dataset of 2,000 product reviews (short text).
2. Detecting fraudulent transactions in a financial dataset with labelled
records.
3. Generating captions for a collection of 100,000 labelled images of
natural scenes.

CO-2; | b.| Researchers are developing a deep learning system for automated leaf | [5]
BL-3 Disease classification using images. During model design, they must choose
an appropriate loss function for training and evaluate how it behaves on
specific predictions.
i. Discuss the major factors that influence the selection of a suitable loss
function in machine learning and deep learning applications.
ii. Suppose their classifier predicts the probability distribution for three
Disease classes (Normal, Mild, and Severe). For one validation image the
true one-hot label is Mild Disease (0,1,0). Their model outputs class
probabilities [0.1, 0.8, 0.1]. Compute the categorical cross-entropy for
this sample and interpret it.

CO=2; } °c. i. Which regularization method leads to weight sparsity? Explain why. [5]
BL-2 ii. You are training a deep convolutional neural network to classify images

of handwritten digits using the MNIST dataset. After several epochs,

you notice that your training accuracy is very high, but your validation
accuracy is much lower. Explain how applying Dropout can help in this
situation. Describe what Dropout does during training and how it affects

the model’s performance and generaljzation ability.

«

CO-4; | d.| Describe how RNNs process sequential data, how they capture context | [5]
BL-2 between words, and why they are suitable for handling variable-length

FOI 7 FCG ak
--- page 2 ---
sentences. Explain how Recurrent Neural Networks (RNNs) are used in
language translation applications like Google Translate.

Q2 a [10]
BL-3
Given a network with the following parameters
ay, = 0.5, 4) = 05,0? = 05,0) = 05,62 = 0.25,a = 0.25,b1 =
b2=0.
All neurons have a Sigmoid activation function. The actual output at O is 1.
Perform a forward pass and backward pass to update weights of a) ,
a and b2 using Gradient Descent algorithm (Assume learning rate = 0.5).
Q2 b | i. Discuss how skip connections in ResNet influence gradient flow, feature | [10]
CO-3; reuse, and help in addressing the vanishing gradient problem during
BL-2 backpropagation.
ii. Explain how the learning approach and feature extraction strategy of
InceptionNet differ from the AlexNet.
Q3 a | i. Determine the weights required to perform the classification as per the | [10]
CO-2; table using single layer perceptron network. Assume learning rate is 1
BL-3 and initial weights are 0. Consider threshold=0 and solve for 1 epoch.
Xi X2 X3 target
-1 1 -1 0
-1 1 1 1
1 -1 1 1
-1 1 1 1
ii. Illustrate the correspondence between components of a biological
‘ neuron and an artificial neuron. ‘
Q3 b | A system is being designed for marking the attendance of students using face [10]
CO-3; recognition. This task is given to you. You and your team are planning to use
BL-2 convolutional neural network for this task, but the dataset provided to you is
very small. Suggest and discuss different approaches to handle this issue.
How transfer learning can be applied to improve the model’s performance in
this situation.
Q4 i. A neural network uses a dataset with 1000 samples and batch size of | [10]
CO-2; 100. If the learning rate and other parameters remain constant, explain
BL-3

how many weight updates occur in:
(i) Batch Gradient Descent
3 (ii) Stochastic Gradient Descent (SGD)
(iii) Mini-Batch Gradient Degcent
ii. Consider the cost function J(@)=0.50?. Perform two iterations of SGD
with Momentum, where learning rate (q or a) is 0.1, momentum is.0.9,
initial velocity vo=0, initial parameter 8=1. Write the update rule and
compute the velocity & parameter after each iteration.

FRR Rk

&
--- page 3 ---
z

————————"™.

iii. List the number of hyperparameters required in training a model using
Stochastic Gradient Descent with Momentum.

Q4
CO-4;
BL-2

b.

i. Define the vanishing gradient problem in RNNs. Why does it

occur? .

ii, Ina sentence like “The dogs barked at the thief and ... were
appreciated”, why does a simple RNN fail to predict the correct
verb form?

iii. Justify how the forget gate in LSTM helps preserve long-term
dependencies.
iv. Assuming that the forget gate output is ft=[0.1,0.9] and the

previous cell state C,-1=[2,1], compute the updated cell memory
contribution from the forget gate.

[10

»

Q5
CO-4;
BL-2

a

With respect to LSTM, answer the following questions:

i. Identify the purpose of each gate (input, forget, output) in an LSTM
unit.

ii. Consider the sentence “Artificial Intelligence has revolutionized
every domain. The work force will have to update themselves to
remain relevant.” Explain how the input and forget gates update
memory as context changes.

Given: i=0.7, f=0.4, 00.8, C.=0.9, Ci-1=0.5. Compute the new
cell state C; and hidden state hy. Assume h,=o, x tanh(C;)

iii. | Why are LSTM models more effective for language modelling than
simple RNNs?

[10]

Q5
CO-2;
BL-2

b.

Explain the working principle of the AdaGrad optimizer. Write the update
rule of AdaGrad. List advantages and disadvantages of using AdaGrad
compared to standard Stochastic Gradient Descent (SGD).

[10]

Q6
CO-3;
BL-3

a.

i. Consider input image of size 128 X 128 X 3.
1) It is passed through convolution layer 1 with filter size 3x3, no. of
filters = 16, no padding and stride = 1.
2) It is followed by pooling layer of mask size 2X2 with stride=2.
3) Then it is passed through convolution layer 2 with filter size 3X3,
no. of filters = 32, no padding and stride = 1.
4) It is followed by pooling layer of mask size 2X2 with stride=2.
5) Further it is passed through fully connected layer 1 consisting of 240
neurons and then FC2 with 120 neurons.
6) Finally, SoftMax layer of 5 neurons is used. Calculate the size of
activation and trainable parameters at the end of each layer.
ii. Determine the output of the given 5x5 image after convoluting with the
3x3 kernel. Given padding=valid and stride=2

3 1 2 2 1 1 0 -1
2 1 2 1 0 2 0 -2
3 2 1 0 1 1 0 -1
0 3 0 1 2
1 1 0 2 3

[10] -

b.

i. Explain the concept of activation functions in deep neural networks. Discuss
_the role of non-linearity.

ii. ‘Compare the following activation functions: Sigmoid, Tanh, ReLU, and
Leaky ReLU. Include their advantages, disadvantages.

[10]

Explain how information flows through a feedforward network during the
forward propagation process, describing the role of weights, biases, and
activation functions in transforming inputs to outputs. Then, compute the
output of the following FNN:

[10]

dhadieledlaiiaiiateleie: Wadetadalaietateiele’
.

4
--- page 4 ---
¢ Network structure: 2 input neurons > 2 hidden neurons (ReLU
activation) > 1 output neuron (ReLU activation).

e Input: X=[1,0] <

¢ Weights and biases:

70.2 04 701) _

b. | i. Explain how Convolutional Neural Networks (CNNs) extract hierarchical | [10]

Q7 features from an input image. Include the roles of convolutional, pooling,
Co-3 and fully connected layers in this process.
BL-2 ii. Discuss why CNNs are preferred over traditional fully connected

Artificial Neural Networks (ANNs) for image processing tasks.

iii. Describe how CNNs can be applied in Medical Image Analysis and
Autonomous Vehicles. Provide an example for each application and
highlight the advantages of using CNNs in these scenarios.

- FAI OA OR RK
````

## 2025-26 · Re-Exam · Sem 8 · paper 8e4765e78b76

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2024/Sem_08/Re-Exam/BTech_CSBS_7036/Deep Learning/QP_Deep Learning(702AI0C008)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: IV/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Deep Learning
Date: 11 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 3 pages.
2. Question No. 1 is compulsory
3. Out of the remianing questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
CO-3   a.
Discuss CNN based two convolution.   [5]
BL-1,2
b.
What will the convolution operation's output be over the following feature map?
Where the following kernel is applied with a stride of 2.
Input Feature map   Kernel
1 2 3
3   5   8   2   3
CO-3   4 5 6
3 2   3   2   5   [5]
BL-2,4
1 2 3
1   2   3   8   3
6   4   5   1   4
3   4   7   4
3
CO-4   c.   What are the computational challenges of BPTT? Suggest optimization   [5]
BL-3   techniques to improve efficiency
CO-2   d.
In autonomous driving systems, deep learning models sometimes fail in unusual
BL-3   [5]
conditions. Explain two limitations responsible for this issue.
a.   Compare RNN, LSTM, and GRU based on:   [10]
1) Architecture
Q2   2) Computational complexity
CO-   3) Ability to capture long-term dependencies
4,BL-4   4) Training efficiency
b
CO-3,   Design an LSTM-based model for:
BL-3   1) Time-series prediction   [5+5]
2) Explain input representation, architecture, and training process.
********** 1 **********
--- page 2 ---
Q3
a.
Explain the architecture of Gated Recurrent Unit (GRU) networks using a   [10]
CO-4
diagram. Then, use formulas to discuss the critical components of a GRU unit
BL-4
(All gates).
CO-2   b.
Write and explain the algorithm for ADAM and SGD with Nesterov momentum.   [10]
BL-2
a.   Consider the neural network as shown in the figure.
The inputs x1, x2, and the initial weights and two biases are given. The actual
output is [0.9, 0.1] for the two output neurons. The activation used is sigmoid.
{w3 is between x1-h2, w6 is between h1-o2}, Learning rate is 0.55.
Calculate the following: (4 significants)   [10]
Q4.
1. Predicted output after forward propagation.
2. Mean square error after the first forward pass
CO-2
3. Calculate the updated weights w4 and w8 after the first iteration of
BL-3
backpropagation.
CO-2
b.
BL-3
A fully connected Neural Network with 8 layers is being trained using the sigmoid
activation function.   [10]
i   What is the activation output f / (12.9)?
ii   What is the first derivative of the gradient f (x) at x=8?
iii   Explain how this affects backpropagation in deeper layers.
iv   Solve the SoftMax values for y = [3.5, 5.8, 4.4]
a.
Q5   Discuss common problems in Gradient Descent:
[10]
1. Local minima
CO-3   2. Saddle points
BL-1,2   3. Vanishing gradients
b.
Explain the application of deep learning in speech recognition systems:
[10]
CO-4   1. Feature extraction
BL-2   2. Model architecture
3. Training challenges
********** 2 **********
--- page 3 ---
Q6   a.   You are training a deep learning model on limited GPU memory.
CO-4   How would you choose the batch size? Justify your answer.   [10]
BL-4   Explain the architecture of the Inception Model and why you use 1x1
CO-3   convolution in it?
BL-   b.
2,1,5   Design an AlexNet-inspired architecture for a new image classification task.
Specify how you would adapt the architecture to work with a dataset that
contains smaller images (e.g., 64 × 64 64×64 pixels) and fewer classes than
ImageNet. What modifications would you make to the original AlexNet
architecture to suit this task.
Modified AlexNet-Inspired Architecture for 64×64 Images:
•   Input Layer: 64×64×3
•   Conv1: 5×5 kernel, 32 filters, stride 1, padding 2 → Max Pooling (2×2,
stride 2) → Output size: 32×32×32
•   Conv2: 3×3 kernel, 64 filters, stride 1, padding 1 → Max Pooling (2×2,
[10]
stride 2) → Output size: 16×16×64
•   Conv3: 3×3 kernel, 128 filters, stride 1, padding 1 → Output size:
16×16×128
•   Conv4: 3×3 kernel, 128 filters, stride 1, padding 1 → Output size:
8×8×128
•   Conv5: 3×3 kernel, 256 filters, stride 1, padding 1 → Max Pooling (2×2,
stride 2) → Output size: 4×4×256
•   Flatten: Flatten the output to 4096 features.
•   FC1: Fully connected, 512 neurons → ReLU
•   FC2: Fully connected, 256 neurons → ReLU
•   Output Layer (FC3): Fully connected, number of neurons = number of
classes (e.g., 10 for 10 classes) → Softmax activation.
a.   1) Interpret the trade-off between bias and variance over deep learning models
by taking relevant examples.
2) Implement EXNOR gates using perceptron models.   [5+5]
Q7.
CO-3   Explain how the learning rate affects:
BL-2   b.   1. Speed of convergence
2.   Stability of training
3. Risk of divergence
CO-3   1) Consider a feature map as shown below[
BL-4   [5+5]
********** 3 **********
````

## 2025-26 · Re-Exam · Sem 5 · paper 6f31f697f004

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_AI_7012/Deep Learning/QP_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech (IT)/MASTER OF BUSINESS
ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (EXTC)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Deep Learning
Date: 10 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i.   Explain any two situations where deep learning models outperform   [5]
BL-2   traditional machine learning algorithms.
ii. You are given the following applications. Choose between machine
learning and deep learning, and justify your choice:
•   Predicting house prices using a dataset of 1,000 entries containing
numerical features such as area, location rating, and number of
bedrooms.
•   Detecting emotions from facial expressions in real-time video
streams.
•   Translating text from one language to another using millions of text
sentence pairs.
CO-2;   b.   i.   Explain how different activation functions influence gradient   [5]
BL-3   propagation, convergence behavior, and the overall performance of a
deep neural network.
ii.   Discuss the scenarios or types of problems where specific activation
functions such as Sigmoid, Tanh, ReLU, and Leaky ReLU are preferred.
CO-2;   c.   i.   Explain the role of L1 and L2 regularization in deep neural networks,   [5]
BL-2   and discuss how these techniques help prevent overfitting and improve
the model’s generalization to unseen data.
ii. You are training a fully connected neural network layer with 4 neurons
during training. The outputs of the neurons before applying dropout are:
[0.8, −0.4, 0.6, 0.2]. A dropout rate of 50% is applied to this layer.
Randomly determine which neurons are dropped (assume a possible
dropout mask) and compute the output after applying dropout.
CO-4;   d. An e-commerce platform wants to automatically determine whether customer   [5]
BL-2   reviews are positive, negative, or neutral. Explain how an RNN model
processes customer review text to perform sentiment classification. Why is
RNN suitable for this task, and what role does word order play in determining
sentiment?
********** 1 **********
--- page 2 ---
Q2   a.   [10]
CO-2;
BL-3
The given network with the following parameters:
i1= 0.25, i2= 0.7, w1= 0.2, w2=0.15, w3= 0.28, w4=0.3, w5= 0.1, w6= 0.24,
w7 = 0.12, w8= 0.21, b1= 1 and b2=1.
All neurons have a Sigmoid activation function. The actual output at O1 is
0.7 and at O2 is 0.3. Perform a forward pass and backward pass to update
weights of w1, w5 and w7 using Gradient Descent algorithm (Assume
learning rate = 1).
Q2   b.   i. Explain how AlexNet’s design improved upon earlier traditional CNNs [10]
CO-3;   in terms of regularization, and training methodology.
BL-2   ii. Discuss how the Inception Network captures features at multiple scales
efficiently and the role of 1×1 convolutions in enhancing both
computational efficiency and feature representation in deep CNNs.
iii. Based on your analysis, which architecture would you recommend for
classification of large-scale image dataset and why?
Q3   a.   i. Determine the weights required to perform the classification as per the [10]
CO-2;   table using single layer perceptron network. Assume learning rate is 1 and
BL-3   initial weights are 0. Consider threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   -1
1   1   1   1
-1   -1   1   -1
-1   1   1   -1
ii. Discuss its limitations and provide suitable examples to illustrate these
limitations.
Q3   b. How to decide number of filters in CNN? How it will influence the following [10]
CO-3;   1) feature extraction capability, 2) dimensionality, 3) computational and
BL-2   memory cost, 4) risk of overfitting, 5) hierarchical feature learning.
Q4   a.   i. Illustrate how batch gradient descent and Stochastic Gradient Descent [10]
CO-2;   (SGD) differ in terms of 1) oscillations in the loss function (with
BL-3   diagram/graph), 2) memory usage, and 3) suitability for large datasets.
ii. Discuss the impact of the learning rate being too high or too low during
training.
iii. Consider the cost function J(θ)=0.7𝜃3. Perform two iterations of SGD,
where learning rate (η or α) is 0.1, initial parameter 𝜃0=1. Write the
update rule and compute the updated parameter after each iteration.
Q4   b.   With reference to Gated Recurrent Unit (GRU) answer the following [10]
CO-4;   questions:
********** 2 **********
--- page 3 ---
BL-2   i.   State the difference between LSTM and GRU in terms of architecture
and number of gates.
ii. Why is GRU computationally more efficient for smaller datasets?
iii.   Explain how GRUs “decide” to skip irrelevant tokens in a text
sequence.
iv.   Justify the advantage of bidirectional RNNs.
Q5   a.   i. Explain why a feedforward neural network fails to capture sequential [10]
CO-4;   context in language modelling.
BL-2   ii. Describe how a recurrent connection in an RNN overcomes this
limitation.
iii. Consider a RNN with a single hidden layer. Calculate the output of the
hidden layer ht given the following values: (use tanh as activation
function)
Wxh= [0.6 0.4   , Whh= [0.5 0.3 ht-1=[0 xt=[0
0.3 0.7]   0.2   0.4],   1],   1]
iv. Explain how RNN-based language models predict the next word
probability distribution in a sentence.
Q5   b.   Explain the working principle of the RMSProp optimizer. Write the update [10]
CO-2;   rule and explain the role of the accumulated squared gradients. List
BL-2   advantages and disadvantages of RMSProp compared to standard SGD.
Q6   a.   Consider the CNN for binary classification as below. Compute the shape of   [10]
CO-3;   the output volume dimension and trainable parameters at each layer.
BL-3
Layer   Volume   No of
Dimension   parameters
Input   256 X 256 X 3
Conv2D
Filter = 32, stride = 1, Kernel
Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 64, stride = 1, Kernel
Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 128, stride = 1,
Kernel Size = 5x5, padding=1
Pool2D Kernel Size = 2,
stride = 2
Flatten
Fully connected dense units =
84
Fully connected dense units =
32
Output
********** 3 **********
--- page 4 ---
Q6   b.   Fully connected Neural Network with 10-layer is training using the sigmoid [10]
CO-2;   activation function.
BL-3   i. What is the activation output f (6)?
ii. What is the first derivative of gradient f 1(x) at x=6?
iii. Explain how this affects backpropagation in deeper layers.
iv. Solve the SoftMax values for y= [2.3, 4.5, 3.2]
Q7   a.   Differentiate between single-layer and multi-layer feedforward neural [10]
CO-2;   networks. Explain the importance of non-linearity in hidden layers. Illustrate
BL-3   your answer by computing the output of a feedforward neural network with
the following configuration:
•   Structure: 3 input neurons → 2 hidden neurons (sigmoid activation)
→ 1 output neuron (sigmoid activation)
•   Input: X=[0.5,0.2,0.1]
• Weights and biases:
𝑊1 = [0.1 0.4 0.2 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.6 0.9], 𝑏2 = 0.5
0.3 0.5
b.   Explain the concept of Transfer Learning using CNNs. Describe how pre- [10]
Q7   trained models can be adapted for a new image classification task. Explain
CO-3   with any example model.
BL-2
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 5 · paper 3e564cf0e9c7

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_AI_7051/Deep Learning/QP_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech (IT)/MASTER OF BUSINESS
ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (EXTC)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Deep Learning
Date: 10 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i.   Explain any two situations where deep learning models outperform   [5]
BL-2   traditional machine learning algorithms.
ii. You are given the following applications. Choose between machine
learning and deep learning, and justify your choice:
•   Predicting house prices using a dataset of 1,000 entries containing
numerical features such as area, location rating, and number of
bedrooms.
•   Detecting emotions from facial expressions in real-time video
streams.
•   Translating text from one language to another using millions of text
sentence pairs.
CO-2;   b.   i.   Explain how different activation functions influence gradient   [5]
BL-3   propagation, convergence behavior, and the overall performance of a
deep neural network.
ii.   Discuss the scenarios or types of problems where specific activation
functions such as Sigmoid, Tanh, ReLU, and Leaky ReLU are preferred.
CO-2;   c.   i.   Explain the role of L1 and L2 regularization in deep neural networks,   [5]
BL-2   and discuss how these techniques help prevent overfitting and improve
the model’s generalization to unseen data.
ii. You are training a fully connected neural network layer with 4 neurons
during training. The outputs of the neurons before applying dropout are:
[0.8, −0.4, 0.6, 0.2]. A dropout rate of 50% is applied to this layer.
Randomly determine which neurons are dropped (assume a possible
dropout mask) and compute the output after applying dropout.
CO-4;   d. An e-commerce platform wants to automatically determine whether customer   [5]
BL-2   reviews are positive, negative, or neutral. Explain how an RNN model
processes customer review text to perform sentiment classification. Why is
RNN suitable for this task, and what role does word order play in determining
sentiment?
********** 1 **********
--- page 2 ---
Q2   a.   [10]
CO-2;
BL-3
The given network with the following parameters:
i1= 0.25, i2= 0.7, w1= 0.2, w2=0.15, w3= 0.28, w4=0.3, w5= 0.1, w6= 0.24,
w7 = 0.12, w8= 0.21, b1= 1 and b2=1.
All neurons have a Sigmoid activation function. The actual output at O1 is
0.7 and at O2 is 0.3. Perform a forward pass and backward pass to update
weights of w1, w5 and w7 using Gradient Descent algorithm (Assume
learning rate = 1).
Q2   b.   i. Explain how AlexNet’s design improved upon earlier traditional CNNs [10]
CO-3;   in terms of regularization, and training methodology.
BL-2   ii. Discuss how the Inception Network captures features at multiple scales
efficiently and the role of 1×1 convolutions in enhancing both
computational efficiency and feature representation in deep CNNs.
iii. Based on your analysis, which architecture would you recommend for
classification of large-scale image dataset and why?
Q3   a.   i. Determine the weights required to perform the classification as per the [10]
CO-2;   table using single layer perceptron network. Assume learning rate is 1 and
BL-3   initial weights are 0. Consider threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   -1
1   1   1   1
-1   -1   1   -1
-1   1   1   -1
ii. Discuss its limitations and provide suitable examples to illustrate these
limitations.
Q3   b. How to decide number of filters in CNN? How it will influence the following [10]
CO-3;   1) feature extraction capability, 2) dimensionality, 3) computational and
BL-2   memory cost, 4) risk of overfitting, 5) hierarchical feature learning.
Q4   a.   i. Illustrate how batch gradient descent and Stochastic Gradient Descent [10]
CO-2;   (SGD) differ in terms of 1) oscillations in the loss function (with
BL-3   diagram/graph), 2) memory usage, and 3) suitability for large datasets.
ii. Discuss the impact of the learning rate being too high or too low during
training.
iii. Consider the cost function J(θ)=0.7𝜃3. Perform two iterations of SGD,
where learning rate (η or α) is 0.1, initial parameter 𝜃0=1. Write the
update rule and compute the updated parameter after each iteration.
Q4   b.   With reference to Gated Recurrent Unit (GRU) answer the following [10]
CO-4;   questions:
********** 2 **********
--- page 3 ---
BL-2   i.   State the difference between LSTM and GRU in terms of architecture
and number of gates.
ii. Why is GRU computationally more efficient for smaller datasets?
iii.   Explain how GRUs “decide” to skip irrelevant tokens in a text
sequence.
iv.   Justify the advantage of bidirectional RNNs.
Q5   a.   i. Explain why a feedforward neural network fails to capture sequential [10]
CO-4;   context in language modelling.
BL-2   ii. Describe how a recurrent connection in an RNN overcomes this
limitation.
iii. Consider a RNN with a single hidden layer. Calculate the output of the
hidden layer ht given the following values: (use tanh as activation
function)
Wxh= [0.6 0.4   , Whh= [0.5 0.3 ht-1=[0 xt=[0
0.3 0.7]   0.2   0.4],   1],   1]
iv. Explain how RNN-based language models predict the next word
probability distribution in a sentence.
Q5   b.   Explain the working principle of the RMSProp optimizer. Write the update [10]
CO-2;   rule and explain the role of the accumulated squared gradients. List
BL-2   advantages and disadvantages of RMSProp compared to standard SGD.
Q6   a.   Consider the CNN for binary classification as below. Compute the shape of   [10]
CO-3;   the output volume dimension and trainable parameters at each layer.
BL-3
Layer   Volume   No of
Dimension   parameters
Input   256 X 256 X 3
Conv2D
Filter = 32, stride = 1, Kernel
Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 64, stride = 1, Kernel
Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 128, stride = 1,
Kernel Size = 5x5, padding=1
Pool2D Kernel Size = 2,
stride = 2
Flatten
Fully connected dense units =
84
Fully connected dense units =
32
Output
********** 3 **********
--- page 4 ---
Q6   b.   Fully connected Neural Network with 10-layer is training using the sigmoid [10]
CO-2;   activation function.
BL-3   i. What is the activation output f (6)?
ii. What is the first derivative of gradient f 1(x) at x=6?
iii. Explain how this affects backpropagation in deeper layers.
iv. Solve the SoftMax values for y= [2.3, 4.5, 3.2]
Q7   a.   Differentiate between single-layer and multi-layer feedforward neural [10]
CO-2;   networks. Explain the importance of non-linearity in hidden layers. Illustrate
BL-3   your answer by computing the output of a feedforward neural network with
the following configuration:
•   Structure: 3 input neurons → 2 hidden neurons (sigmoid activation)
→ 1 output neuron (sigmoid activation)
•   Input: X=[0.5,0.2,0.1]
• Weights and biases:
𝑊1 = [0.1 0.4 0.2 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.6 0.9], 𝑏2 = 0.5
0.3 0.5
b.   Explain the concept of Transfer Learning using CNNs. Describe how pre- [10]
Q7   trained models can be adapted for a new image classification task. Explain
CO-3   with any example model.
BL-2
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper 18ed3b880b25

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_AIDS_7056/Deep Learning/QP_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 Jul 2026
- Text: mixed (4 pages), mean OCR confidence 52.0
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA
SCIENCE)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Deep Learning
Date: 14 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Attempt any 4 questions from the remaining questions.
6. Attempt five (5) questions in total.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1. (a)   Justify why deep learning is preferred over traditional image processing techniques 5
CO1;SO1; with atleast five reasons.
BL2
Q1. (b)   A neural network model is designed using a 3-layer architecture (Input Layer - 5
CO2;   Hidden Layer - Output Layer).
SO1;BL3   i.   Compute the total number of trainable parameters (weights and biases), if
the input layer has 𝑛=4 neurons, the hidden layer has ℎ=5 neurons, and the
output layer has 𝑜=2 neurons.
ii.   Differentiate between parameters and hyperparameters in neural networks.
Q1. (c)   Calculate the output size and compute the output feature map with stride =1 and 5
CO3;   padding = 0 with input image (4×4):
SO1;BL3   2   4   6   8
1   3   5   7
2   4   6   8
1   3   5   7
Kernel:
1   0   1
0   2   0
1   0   1
Q1. (d)   Explain how a vanilla RNN models sequence data and give one reason it may fail 5
CO4;   on long call transcripts.
SO1;BL3
Q2 (a)   For each of the following scenarios, identify whether machine learning or deep   5
CO2;   learning is more appropriate. If deep learning is used, specify the suitable
SO1;BL1,   architecture: CNN, RNN, or both. Justify
2   i. A system predicts house prices based on features such as location, size, and
number of rooms.
ii. A model analyzes medical images (X-rays) to detect signs of pneumonia.
iii. A chatbot processes user queries and generates meaningful responses in
natural language.
iv. A model generates captions automatically for images uploaded on a social
media platform.
v. A system predicts stock prices using historical time-series data.
********** 1 **********
--- page 2 ---
Q2 (b)   Justify why the XOR problem is not linearly separable (with graph) and cannot   5
CO2;   be solved using a single-layer perceptron. Suggest a suitable solution to address
SO1;BL4   this issue.
Q2 (c)   Identify key design choices that made AlexNet successful (at least five) and   10
CO3;   explain how each affects training/performance.
SO1;BL4
Q3 (a)   An RGB image of size 64 × 64 × 3is given as input to a convolutional neural 10
CO3;   network. The architecture consist of:
SO1;BL5   1. Conv Layer 1:
o 8 filters of size 3 × 3, stride = 1, padding = valid
2. Max Pooling 1:
o Pool size 2 × 2, stride = 2
3. Conv Layer 2:
o 16 filters of size 3 × 3, stride = 1, padding = valid
4. Max Pooling 2:
o Pool size 2 × 2, stride = 2
5. Fully Connected Layers:
o Dense layer with 64 neurons
o Output layer with 10 neurons
Compute the output size after each layer and calculate the total number of
trainable parameters. Note: Consider floor wherever required.
Q3 (b)   Design a simple LSTM-based model to predict the next day’s product demand for 10
CO4;   a retail store. Clearly specify:
SO1;BL4   i. What will be the input features and output of the model?
ii. What window size (number of past days) will you use and why?
iii. Which loss function will you choose?
iv. Which evaluation metric(s) will you use to assess performance?
Q4 (a)   Implement OR function with bipolar inputs and bipolar targets using perceptron 10
CO2;   training algorithm for 2 epochs. Assume initial weights 𝑤1=0, 𝑤2=0, bias (b)=0,
SO1;BL3   learning rate (η)=1. Consider the following activation function:
𝑦𝑜𝑢𝑡 = −1 if 𝑦𝑖𝑛≤0,
𝑦𝑜𝑢𝑡 = 1 if 𝑦𝑖𝑛>0
Show the complete training table for each sample in both epochs.
Q4 (b)   i.   Explain why a fully connected (FC) neural network is inefficient for 10
CO3;   processing raw images. How does the design of a Convolutional Neural
SO1;BL1,   Network (CNN)—specifically local receptive fields and weight sharing—
2   address these limitations?
ii.   Consider the following: An input image of size 64 × 64 × 3is fed to:
Case 1: A fully connected layer with 100 neurons
Case 2: A convolutional layer with 10 filters of size 3 × 3 (stride = 1,
padding = valid, bias included).
• Compute the number of parameters in both cases
• Compare the results and justify why CNN is more efficient
Q5 (a)   i.   Explain the architecture of LSTM network architecture with formulas.   10
CO4;   ii.   An LSTM network has input size = 3 and hidden size = 2.
SO1;BL3   Calculate the total number of trainable parameters in the LSTM cell
(consider all 4 gates and include biases).
Q5 (b)   i.   Explain Momentum based Stochastic Gradient Descent Algorithm.   10
CO2;   ii. A machine learning model is trained using Momentum based Stochastic
SO1;BL4   Gradient Descent to minimize the function:
𝐿(𝜃) = 𝜃3
Consider initial parameter 𝜃0=1, momentum coefficient α=0.8, learning
rate η=0.5, initial velocity 𝑣0 = 2. Calculate parameter update for single
iteration.
********** 2 **********
--- page 3 ---
iii. How Nesterov Accelerated Gradient Descent improves convergence as
compared to Momentum based Stochastic Gradient Descent.
Q6 (a)   Apply back-propagation algorithm on the neural network shown below with input 10
CO2;   𝑥1=4, 𝑥2=3 and target = [0.4, 0.2]. Consider w13=0.25, w14=0.45, w15=0.32,
SO1;BL5   w23=0.55, w24=0.45, w25=0.67, w36=0.23, w37=0.36, w46=0.56, w47=0.50,
w56=0.23, w57=0.12, bias on all nodes at hidden layer b1=0.6 and bias on all
nodes at output layer b2 = 0.5. Use learning rate η=0.5, and sigmoid activation
function.
i.   Compute output of node 3, 4, 5, 6 and node 7.
ii.   Calculate mean square error at output layer.
iii.   Update weights w25 and w57.
Q6 (b)   10
CO2;   Consider a dataset with 5,000 samples trained for 20 epochs.
SO1;BL3   Answer the following:
i.   Calculate number of weight updates for batch gradient descent and
stochastic gradient descent algorithms.
ii.   Compare batch gradient descent, mini batch gradient descent and
stochastic gradient descent algorithms in terms of memory cost and
convergence behaviour.
iii.   Compare the number of weight updates when Batch size = 500 and 1000
in mini-batch gradient descent.
iv. A student claims that increasing batch size always improves learning. Is
this correct? Justify.
Q7 (a)   A neural network is designed to classify plant diseases into three mutually 10
CO2;   exclusive classes: Healthy, Disease A, and Disease B. The network has an output
SO1;BL3   layer with 3 neurons. The weighted sum (logits) at the output layer is given as: 𝑧
= [2.1, 0.5, 1.2]. The model achieves training accuracy = 96% and testing accuracy
= 58%.
i.   List any four hyperparameters used in training this network.
ii.   State whether the model is overfitting or underfitting. Identify whether the
model suffers from:
• High Bias or Low Bias
• High Variance or Low Variance
iii.   Which activation function should be applied at the output layer to obtain a
probabilistic distribution?   Calculate the output after applying this
activation function.
iv.   Identify the most appropriate loss function for this classification problem.
Assume the one-hot-encoded target outputs as [0,1,0] and calculate the
loss.
Q7 (b)   Explain why repeated multiplication in BPTT causes vanishing gradients, and   10
give two mitigations (one architectural, one training trick) to resolve this issue.
********** 3 **********
--- page 4 ---
C04;
SO1;BL4

FIC 7) IC HOH
````

## 2025-26 · Re-Exam · Sem 7 · paper 259911d3fec2

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CSE_DS_7011/Deep Learning/QP_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech (IT)/MASTER OF BUSINESS
ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (EXTC)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Deep Learning
Date: 10 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i.   Explain any two situations where deep learning models outperform   [5]
BL-2   traditional machine learning algorithms.
ii. You are given the following applications. Choose between machine
learning and deep learning, and justify your choice:
•   Predicting house prices using a dataset of 1,000 entries containing
numerical features such as area, location rating, and number of
bedrooms.
•   Detecting emotions from facial expressions in real-time video
streams.
•   Translating text from one language to another using millions of text
sentence pairs.
CO-2;   b.   i.   Explain how different activation functions influence gradient   [5]
BL-3   propagation, convergence behavior, and the overall performance of a
deep neural network.
ii.   Discuss the scenarios or types of problems where specific activation
functions such as Sigmoid, Tanh, ReLU, and Leaky ReLU are preferred.
CO-2;   c.   i.   Explain the role of L1 and L2 regularization in deep neural networks,   [5]
BL-2   and discuss how these techniques help prevent overfitting and improve
the model’s generalization to unseen data.
ii. You are training a fully connected neural network layer with 4 neurons
during training. The outputs of the neurons before applying dropout are:
[0.8, −0.4, 0.6, 0.2]. A dropout rate of 50% is applied to this layer.
Randomly determine which neurons are dropped (assume a possible
dropout mask) and compute the output after applying dropout.
CO-4;   d. An e-commerce platform wants to automatically determine whether customer   [5]
BL-2   reviews are positive, negative, or neutral. Explain how an RNN model
processes customer review text to perform sentiment classification. Why is
RNN suitable for this task, and what role does word order play in determining
sentiment?
********** 1 **********
--- page 2 ---
Q2   a.   [10]
CO-2;
BL-3
The given network with the following parameters:
i1= 0.25, i2= 0.7, w1= 0.2, w2=0.15, w3= 0.28, w4=0.3, w5= 0.1, w6= 0.24,
w7 = 0.12, w8= 0.21, b1= 1 and b2=1.
All neurons have a Sigmoid activation function. The actual output at O1 is
0.7 and at O2 is 0.3. Perform a forward pass and backward pass to update
weights of w1, w5 and w7 using Gradient Descent algorithm (Assume
learning rate = 1).
Q2   b.   i. Explain how AlexNet’s design improved upon earlier traditional CNNs [10]
CO-3;   in terms of regularization, and training methodology.
BL-2   ii. Discuss how the Inception Network captures features at multiple scales
efficiently and the role of 1×1 convolutions in enhancing both
computational efficiency and feature representation in deep CNNs.
iii. Based on your analysis, which architecture would you recommend for
classification of large-scale image dataset and why?
Q3   a.   i. Determine the weights required to perform the classification as per the [10]
CO-2;   table using single layer perceptron network. Assume learning rate is 1 and
BL-3   initial weights are 0. Consider threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   -1
1   1   1   1
-1   -1   1   -1
-1   1   1   -1
ii. Discuss its limitations and provide suitable examples to illustrate these
limitations.
Q3   b. How to decide number of filters in CNN? How it will influence the following [10]
CO-3;   1) feature extraction capability, 2) dimensionality, 3) computational and
BL-2   memory cost, 4) risk of overfitting, 5) hierarchical feature learning.
Q4   a.   i. Illustrate how batch gradient descent and Stochastic Gradient Descent [10]
CO-2;   (SGD) differ in terms of 1) oscillations in the loss function (with
BL-3   diagram/graph), 2) memory usage, and 3) suitability for large datasets.
ii. Discuss the impact of the learning rate being too high or too low during
training.
iii. Consider the cost function J(θ)=0.7𝜃3. Perform two iterations of SGD,
where learning rate (η or α) is 0.1, initial parameter 𝜃0=1. Write the
update rule and compute the updated parameter after each iteration.
Q4   b.   With reference to Gated Recurrent Unit (GRU) answer the following [10]
CO-4;   questions:
********** 2 **********
--- page 3 ---
BL-2   i.   State the difference between LSTM and GRU in terms of architecture
and number of gates.
ii. Why is GRU computationally more efficient for smaller datasets?
iii.   Explain how GRUs “decide” to skip irrelevant tokens in a text
sequence.
iv.   Justify the advantage of bidirectional RNNs.
Q5   a.   i. Explain why a feedforward neural network fails to capture sequential [10]
CO-4;   context in language modelling.
BL-2   ii. Describe how a recurrent connection in an RNN overcomes this
limitation.
iii. Consider a RNN with a single hidden layer. Calculate the output of the
hidden layer ht given the following values: (use tanh as activation
function)
Wxh= [0.6 0.4   , Whh= [0.5 0.3 ht-1=[0 xt=[0
0.3 0.7]   0.2   0.4],   1],   1]
iv. Explain how RNN-based language models predict the next word
probability distribution in a sentence.
Q5   b.   Explain the working principle of the RMSProp optimizer. Write the update [10]
CO-2;   rule and explain the role of the accumulated squared gradients. List
BL-2   advantages and disadvantages of RMSProp compared to standard SGD.
Q6   a.   Consider the CNN for binary classification as below. Compute the shape of   [10]
CO-3;   the output volume dimension and trainable parameters at each layer.
BL-3
Layer   Volume   No of
Dimension   parameters
Input   256 X 256 X 3
Conv2D
Filter = 32, stride = 1, Kernel
Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 64, stride = 1, Kernel
Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 128, stride = 1,
Kernel Size = 5x5, padding=1
Pool2D Kernel Size = 2,
stride = 2
Flatten
Fully connected dense units =
84
Fully connected dense units =
32
Output
********** 3 **********
--- page 4 ---
Q6   b.   Fully connected Neural Network with 10-layer is training using the sigmoid [10]
CO-2;   activation function.
BL-3   i. What is the activation output f (6)?
ii. What is the first derivative of gradient f 1(x) at x=6?
iii. Explain how this affects backpropagation in deeper layers.
iv. Solve the SoftMax values for y= [2.3, 4.5, 3.2]
Q7   a.   Differentiate between single-layer and multi-layer feedforward neural [10]
CO-2;   networks. Explain the importance of non-linearity in hidden layers. Illustrate
BL-3   your answer by computing the output of a feedforward neural network with
the following configuration:
•   Structure: 3 input neurons → 2 hidden neurons (sigmoid activation)
→ 1 output neuron (sigmoid activation)
•   Input: X=[0.5,0.2,0.1]
• Weights and biases:
𝑊1 = [0.1 0.4 0.2 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.6 0.9], 𝑏2 = 0.5
0.3 0.5
b.   Explain the concept of Transfer Learning using CNNs. Describe how pre- [10]
Q7   trained models can be adapted for a new image classification task. Explain
CO-3   with any example model.
BL-2
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 7 · paper 6356703b5e8c

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_Computer_7002/Deep Learning/QP_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech (IT)/MASTER OF BUSINESS
ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (EXTC)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Deep Learning
Date: 10 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i.   Explain any two situations where deep learning models outperform   [5]
BL-2   traditional machine learning algorithms.
ii. You are given the following applications. Choose between machine
learning and deep learning, and justify your choice:
•   Predicting house prices using a dataset of 1,000 entries containing
numerical features such as area, location rating, and number of
bedrooms.
•   Detecting emotions from facial expressions in real-time video
streams.
•   Translating text from one language to another using millions of text
sentence pairs.
CO-2;   b.   i.   Explain how different activation functions influence gradient   [5]
BL-3   propagation, convergence behavior, and the overall performance of a
deep neural network.
ii.   Discuss the scenarios or types of problems where specific activation
functions such as Sigmoid, Tanh, ReLU, and Leaky ReLU are preferred.
CO-2;   c.   i.   Explain the role of L1 and L2 regularization in deep neural networks,   [5]
BL-2   and discuss how these techniques help prevent overfitting and improve
the model’s generalization to unseen data.
ii. You are training a fully connected neural network layer with 4 neurons
during training. The outputs of the neurons before applying dropout are:
[0.8, −0.4, 0.6, 0.2]. A dropout rate of 50% is applied to this layer.
Randomly determine which neurons are dropped (assume a possible
dropout mask) and compute the output after applying dropout.
CO-4;   d. An e-commerce platform wants to automatically determine whether customer   [5]
BL-2   reviews are positive, negative, or neutral. Explain how an RNN model
processes customer review text to perform sentiment classification. Why is
RNN suitable for this task, and what role does word order play in determining
sentiment?
********** 1 **********
--- page 2 ---
Q2   a.   [10]
CO-2;
BL-3
The given network with the following parameters:
i1= 0.25, i2= 0.7, w1= 0.2, w2=0.15, w3= 0.28, w4=0.3, w5= 0.1, w6= 0.24,
w7 = 0.12, w8= 0.21, b1= 1 and b2=1.
All neurons have a Sigmoid activation function. The actual output at O1 is
0.7 and at O2 is 0.3. Perform a forward pass and backward pass to update
weights of w1, w5 and w7 using Gradient Descent algorithm (Assume
learning rate = 1).
Q2   b.   i. Explain how AlexNet’s design improved upon earlier traditional CNNs [10]
CO-3;   in terms of regularization, and training methodology.
BL-2   ii. Discuss how the Inception Network captures features at multiple scales
efficiently and the role of 1×1 convolutions in enhancing both
computational efficiency and feature representation in deep CNNs.
iii. Based on your analysis, which architecture would you recommend for
classification of large-scale image dataset and why?
Q3   a.   i. Determine the weights required to perform the classification as per the [10]
CO-2;   table using single layer perceptron network. Assume learning rate is 1 and
BL-3   initial weights are 0. Consider threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   -1
1   1   1   1
-1   -1   1   -1
-1   1   1   -1
ii. Discuss its limitations and provide suitable examples to illustrate these
limitations.
Q3   b. How to decide number of filters in CNN? How it will influence the following [10]
CO-3;   1) feature extraction capability, 2) dimensionality, 3) computational and
BL-2   memory cost, 4) risk of overfitting, 5) hierarchical feature learning.
Q4   a.   i. Illustrate how batch gradient descent and Stochastic Gradient Descent [10]
CO-2;   (SGD) differ in terms of 1) oscillations in the loss function (with
BL-3   diagram/graph), 2) memory usage, and 3) suitability for large datasets.
ii. Discuss the impact of the learning rate being too high or too low during
training.
iii. Consider the cost function J(θ)=0.7𝜃3. Perform two iterations of SGD,
where learning rate (η or α) is 0.1, initial parameter 𝜃0=1. Write the
update rule and compute the updated parameter after each iteration.
Q4   b.   With reference to Gated Recurrent Unit (GRU) answer the following [10]
CO-4;   questions:
********** 2 **********
--- page 3 ---
BL-2   i.   State the difference between LSTM and GRU in terms of architecture
and number of gates.
ii. Why is GRU computationally more efficient for smaller datasets?
iii.   Explain how GRUs “decide” to skip irrelevant tokens in a text
sequence.
iv.   Justify the advantage of bidirectional RNNs.
Q5   a.   i. Explain why a feedforward neural network fails to capture sequential [10]
CO-4;   context in language modelling.
BL-2   ii. Describe how a recurrent connection in an RNN overcomes this
limitation.
iii. Consider a RNN with a single hidden layer. Calculate the output of the
hidden layer ht given the following values: (use tanh as activation
function)
Wxh= [0.6 0.4   , Whh= [0.5 0.3 ht-1=[0 xt=[0
0.3 0.7]   0.2   0.4],   1],   1]
iv. Explain how RNN-based language models predict the next word
probability distribution in a sentence.
Q5   b.   Explain the working principle of the RMSProp optimizer. Write the update [10]
CO-2;   rule and explain the role of the accumulated squared gradients. List
BL-2   advantages and disadvantages of RMSProp compared to standard SGD.
Q6   a.   Consider the CNN for binary classification as below. Compute the shape of   [10]
CO-3;   the output volume dimension and trainable parameters at each layer.
BL-3
Layer   Volume   No of
Dimension   parameters
Input   256 X 256 X 3
Conv2D
Filter = 32, stride = 1, Kernel
Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 64, stride = 1, Kernel
Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 128, stride = 1,
Kernel Size = 5x5, padding=1
Pool2D Kernel Size = 2,
stride = 2
Flatten
Fully connected dense units =
84
Fully connected dense units =
32
Output
********** 3 **********
--- page 4 ---
Q6   b.   Fully connected Neural Network with 10-layer is training using the sigmoid [10]
CO-2;   activation function.
BL-3   i. What is the activation output f (6)?
ii. What is the first derivative of gradient f 1(x) at x=6?
iii. Explain how this affects backpropagation in deeper layers.
iv. Solve the SoftMax values for y= [2.3, 4.5, 3.2]
Q7   a.   Differentiate between single-layer and multi-layer feedforward neural [10]
CO-2;   networks. Explain the importance of non-linearity in hidden layers. Illustrate
BL-3   your answer by computing the output of a feedforward neural network with
the following configuration:
•   Structure: 3 input neurons → 2 hidden neurons (sigmoid activation)
→ 1 output neuron (sigmoid activation)
•   Input: X=[0.5,0.2,0.1]
• Weights and biases:
𝑊1 = [0.1 0.4 0.2 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.6 0.9], 𝑏2 = 0.5
0.3 0.5
b.   Explain the concept of Transfer Learning using CNNs. Describe how pre- [10]
Q7   trained models can be adapted for a new image classification task. Explain
CO-3   with any example model.
BL-2
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 7 · paper df60190e12d9

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/MBATech_Computer_7047/Deep Learning/QP_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech (IT)/MASTER OF BUSINESS
ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (EXTC)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Deep Learning
Date: 10 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i.   Explain any two situations where deep learning models outperform   [5]
BL-2   traditional machine learning algorithms.
ii. You are given the following applications. Choose between machine
learning and deep learning, and justify your choice:
•   Predicting house prices using a dataset of 1,000 entries containing
numerical features such as area, location rating, and number of
bedrooms.
•   Detecting emotions from facial expressions in real-time video
streams.
•   Translating text from one language to another using millions of text
sentence pairs.
CO-2;   b.   i.   Explain how different activation functions influence gradient   [5]
BL-3   propagation, convergence behavior, and the overall performance of a
deep neural network.
ii.   Discuss the scenarios or types of problems where specific activation
functions such as Sigmoid, Tanh, ReLU, and Leaky ReLU are preferred.
CO-2;   c.   i.   Explain the role of L1 and L2 regularization in deep neural networks,   [5]
BL-2   and discuss how these techniques help prevent overfitting and improve
the model’s generalization to unseen data.
ii. You are training a fully connected neural network layer with 4 neurons
during training. The outputs of the neurons before applying dropout are:
[0.8, −0.4, 0.6, 0.2]. A dropout rate of 50% is applied to this layer.
Randomly determine which neurons are dropped (assume a possible
dropout mask) and compute the output after applying dropout.
CO-4;   d. An e-commerce platform wants to automatically determine whether customer   [5]
BL-2   reviews are positive, negative, or neutral. Explain how an RNN model
processes customer review text to perform sentiment classification. Why is
RNN suitable for this task, and what role does word order play in determining
sentiment?
********** 1 **********
--- page 2 ---
Q2   a.   [10]
CO-2;
BL-3
The given network with the following parameters:
i1= 0.25, i2= 0.7, w1= 0.2, w2=0.15, w3= 0.28, w4=0.3, w5= 0.1, w6= 0.24,
w7 = 0.12, w8= 0.21, b1= 1 and b2=1.
All neurons have a Sigmoid activation function. The actual output at O1 is
0.7 and at O2 is 0.3. Perform a forward pass and backward pass to update
weights of w1, w5 and w7 using Gradient Descent algorithm (Assume
learning rate = 1).
Q2   b.   i. Explain how AlexNet’s design improved upon earlier traditional CNNs [10]
CO-3;   in terms of regularization, and training methodology.
BL-2   ii. Discuss how the Inception Network captures features at multiple scales
efficiently and the role of 1×1 convolutions in enhancing both
computational efficiency and feature representation in deep CNNs.
iii. Based on your analysis, which architecture would you recommend for
classification of large-scale image dataset and why?
Q3   a.   i. Determine the weights required to perform the classification as per the [10]
CO-2;   table using single layer perceptron network. Assume learning rate is 1 and
BL-3   initial weights are 0. Consider threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   -1
1   1   1   1
-1   -1   1   -1
-1   1   1   -1
ii. Discuss its limitations and provide suitable examples to illustrate these
limitations.
Q3   b. How to decide number of filters in CNN? How it will influence the following [10]
CO-3;   1) feature extraction capability, 2) dimensionality, 3) computational and
BL-2   memory cost, 4) risk of overfitting, 5) hierarchical feature learning.
Q4   a.   i. Illustrate how batch gradient descent and Stochastic Gradient Descent [10]
CO-2;   (SGD) differ in terms of 1) oscillations in the loss function (with
BL-3   diagram/graph), 2) memory usage, and 3) suitability for large datasets.
ii. Discuss the impact of the learning rate being too high or too low during
training.
iii. Consider the cost function J(θ)=0.7𝜃3. Perform two iterations of SGD,
where learning rate (η or α) is 0.1, initial parameter 𝜃0=1. Write the
update rule and compute the updated parameter after each iteration.
Q4   b.   With reference to Gated Recurrent Unit (GRU) answer the following [10]
CO-4;   questions:
********** 2 **********
--- page 3 ---
BL-2   i.   State the difference between LSTM and GRU in terms of architecture
and number of gates.
ii. Why is GRU computationally more efficient for smaller datasets?
iii.   Explain how GRUs “decide” to skip irrelevant tokens in a text
sequence.
iv.   Justify the advantage of bidirectional RNNs.
Q5   a.   i. Explain why a feedforward neural network fails to capture sequential [10]
CO-4;   context in language modelling.
BL-2   ii. Describe how a recurrent connection in an RNN overcomes this
limitation.
iii. Consider a RNN with a single hidden layer. Calculate the output of the
hidden layer ht given the following values: (use tanh as activation
function)
Wxh= [0.6 0.4   , Whh= [0.5 0.3 ht-1=[0 xt=[0
0.3 0.7]   0.2   0.4],   1],   1]
iv. Explain how RNN-based language models predict the next word
probability distribution in a sentence.
Q5   b.   Explain the working principle of the RMSProp optimizer. Write the update [10]
CO-2;   rule and explain the role of the accumulated squared gradients. List
BL-2   advantages and disadvantages of RMSProp compared to standard SGD.
Q6   a.   Consider the CNN for binary classification as below. Compute the shape of   [10]
CO-3;   the output volume dimension and trainable parameters at each layer.
BL-3
Layer   Volume   No of
Dimension   parameters
Input   256 X 256 X 3
Conv2D
Filter = 32, stride = 1, Kernel
Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 64, stride = 1, Kernel
Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 128, stride = 1,
Kernel Size = 5x5, padding=1
Pool2D Kernel Size = 2,
stride = 2
Flatten
Fully connected dense units =
84
Fully connected dense units =
32
Output
********** 3 **********
--- page 4 ---
Q6   b.   Fully connected Neural Network with 10-layer is training using the sigmoid [10]
CO-2;   activation function.
BL-3   i. What is the activation output f (6)?
ii. What is the first derivative of gradient f 1(x) at x=6?
iii. Explain how this affects backpropagation in deeper layers.
iv. Solve the SoftMax values for y= [2.3, 4.5, 3.2]
Q7   a.   Differentiate between single-layer and multi-layer feedforward neural [10]
CO-2;   networks. Explain the importance of non-linearity in hidden layers. Illustrate
BL-3   your answer by computing the output of a feedforward neural network with
the following configuration:
•   Structure: 3 input neurons → 2 hidden neurons (sigmoid activation)
→ 1 output neuron (sigmoid activation)
•   Input: X=[0.5,0.2,0.1]
• Weights and biases:
𝑊1 = [0.1 0.4 0.2 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.6 0.9], 𝑏2 = 0.5
0.3 0.5
b.   Explain the concept of Transfer Learning using CNNs. Describe how pre- [10]
Q7   trained models can be adapted for a new image classification task. Explain
CO-3   with any example model.
BL-2
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 11 · paper cdab709ffb80

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_11/Re-Exam/Integrated_Computer_7032/Deep Learning/QP_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech (IT)/MASTER OF BUSINESS
ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (EXTC)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Deep Learning
Date: 10 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i.   Explain any two situations where deep learning models outperform   [5]
BL-2   traditional machine learning algorithms.
ii. You are given the following applications. Choose between machine
learning and deep learning, and justify your choice:
•   Predicting house prices using a dataset of 1,000 entries containing
numerical features such as area, location rating, and number of
bedrooms.
•   Detecting emotions from facial expressions in real-time video
streams.
•   Translating text from one language to another using millions of text
sentence pairs.
CO-2;   b.   i.   Explain how different activation functions influence gradient   [5]
BL-3   propagation, convergence behavior, and the overall performance of a
deep neural network.
ii.   Discuss the scenarios or types of problems where specific activation
functions such as Sigmoid, Tanh, ReLU, and Leaky ReLU are preferred.
CO-2;   c.   i.   Explain the role of L1 and L2 regularization in deep neural networks,   [5]
BL-2   and discuss how these techniques help prevent overfitting and improve
the model’s generalization to unseen data.
ii. You are training a fully connected neural network layer with 4 neurons
during training. The outputs of the neurons before applying dropout are:
[0.8, −0.4, 0.6, 0.2]. A dropout rate of 50% is applied to this layer.
Randomly determine which neurons are dropped (assume a possible
dropout mask) and compute the output after applying dropout.
CO-4;   d. An e-commerce platform wants to automatically determine whether customer   [5]
BL-2   reviews are positive, negative, or neutral. Explain how an RNN model
processes customer review text to perform sentiment classification. Why is
RNN suitable for this task, and what role does word order play in determining
sentiment?
********** 1 **********
--- page 2 ---
Q2   a.   [10]
CO-2;
BL-3
The given network with the following parameters:
i1= 0.25, i2= 0.7, w1= 0.2, w2=0.15, w3= 0.28, w4=0.3, w5= 0.1, w6= 0.24,
w7 = 0.12, w8= 0.21, b1= 1 and b2=1.
All neurons have a Sigmoid activation function. The actual output at O1 is
0.7 and at O2 is 0.3. Perform a forward pass and backward pass to update
weights of w1, w5 and w7 using Gradient Descent algorithm (Assume
learning rate = 1).
Q2   b.   i. Explain how AlexNet’s design improved upon earlier traditional CNNs [10]
CO-3;   in terms of regularization, and training methodology.
BL-2   ii. Discuss how the Inception Network captures features at multiple scales
efficiently and the role of 1×1 convolutions in enhancing both
computational efficiency and feature representation in deep CNNs.
iii. Based on your analysis, which architecture would you recommend for
classification of large-scale image dataset and why?
Q3   a.   i. Determine the weights required to perform the classification as per the [10]
CO-2;   table using single layer perceptron network. Assume learning rate is 1 and
BL-3   initial weights are 0. Consider threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   -1
1   1   1   1
-1   -1   1   -1
-1   1   1   -1
ii. Discuss its limitations and provide suitable examples to illustrate these
limitations.
Q3   b. How to decide number of filters in CNN? How it will influence the following [10]
CO-3;   1) feature extraction capability, 2) dimensionality, 3) computational and
BL-2   memory cost, 4) risk of overfitting, 5) hierarchical feature learning.
Q4   a.   i. Illustrate how batch gradient descent and Stochastic Gradient Descent [10]
CO-2;   (SGD) differ in terms of 1) oscillations in the loss function (with
BL-3   diagram/graph), 2) memory usage, and 3) suitability for large datasets.
ii. Discuss the impact of the learning rate being too high or too low during
training.
iii. Consider the cost function J(θ)=0.7𝜃3. Perform two iterations of SGD,
where learning rate (η or α) is 0.1, initial parameter 𝜃0=1. Write the
update rule and compute the updated parameter after each iteration.
Q4   b.   With reference to Gated Recurrent Unit (GRU) answer the following [10]
CO-4;   questions:
********** 2 **********
--- page 3 ---
BL-2   i.   State the difference between LSTM and GRU in terms of architecture
and number of gates.
ii. Why is GRU computationally more efficient for smaller datasets?
iii.   Explain how GRUs “decide” to skip irrelevant tokens in a text
sequence.
iv.   Justify the advantage of bidirectional RNNs.
Q5   a.   i. Explain why a feedforward neural network fails to capture sequential [10]
CO-4;   context in language modelling.
BL-2   ii. Describe how a recurrent connection in an RNN overcomes this
limitation.
iii. Consider a RNN with a single hidden layer. Calculate the output of the
hidden layer ht given the following values: (use tanh as activation
function)
Wxh= [0.6 0.4   , Whh= [0.5 0.3 ht-1=[0 xt=[0
0.3 0.7]   0.2   0.4],   1],   1]
iv. Explain how RNN-based language models predict the next word
probability distribution in a sentence.
Q5   b.   Explain the working principle of the RMSProp optimizer. Write the update [10]
CO-2;   rule and explain the role of the accumulated squared gradients. List
BL-2   advantages and disadvantages of RMSProp compared to standard SGD.
Q6   a.   Consider the CNN for binary classification as below. Compute the shape of   [10]
CO-3;   the output volume dimension and trainable parameters at each layer.
BL-3
Layer   Volume   No of
Dimension   parameters
Input   256 X 256 X 3
Conv2D
Filter = 32, stride = 1, Kernel
Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 64, stride = 1, Kernel
Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 128, stride = 1,
Kernel Size = 5x5, padding=1
Pool2D Kernel Size = 2,
stride = 2
Flatten
Fully connected dense units =
84
Fully connected dense units =
32
Output
********** 3 **********
--- page 4 ---
Q6   b.   Fully connected Neural Network with 10-layer is training using the sigmoid [10]
CO-2;   activation function.
BL-3   i. What is the activation output f (6)?
ii. What is the first derivative of gradient f 1(x) at x=6?
iii. Explain how this affects backpropagation in deeper layers.
iv. Solve the SoftMax values for y= [2.3, 4.5, 3.2]
Q7   a.   Differentiate between single-layer and multi-layer feedforward neural [10]
CO-2;   networks. Explain the importance of non-linearity in hidden layers. Illustrate
BL-3   your answer by computing the output of a feedforward neural network with
the following configuration:
•   Structure: 3 input neurons → 2 hidden neurons (sigmoid activation)
→ 1 output neuron (sigmoid activation)
•   Input: X=[0.5,0.2,0.1]
• Weights and biases:
𝑊1 = [0.1 0.4 0.2 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.6 0.9], 𝑏2 = 0.5
0.3 0.5
b.   Explain the concept of Transfer Learning using CNNs. Describe how pre- [10]
Q7   trained models can be adapted for a new image classification task. Explain
CO-3   with any example model.
BL-2
********** 4 **********
````

## 2024-25 · Final + Re-Exam · Sem 5 · paper e0c00de51ee7

- Departments: Computer Engineering, Data Science, Electronics and Telecommunication, Information Technology
- Programmes: B TECH / COMPUTER, B TECH / CSE DATA SCIENCE, B TECH / EXTC, B TECH / I T
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/DEEP LEARNING/Deep Learning, Sem-V, Final Exam 2024-25 & Re Exam 2023-24.pdf` (+3 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (5 pages), mean OCR confidence 90.3

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS& E
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

¥’

Program/s: BTech / MBATech a Year: III/IV Semester: V/VII
Stream/s : IT / COM / EXTC/ CSE-DS /AI /AIML
Subject: Deep Learning ° Time: 3 hrs (2:0gpmto 5+00pm)

Date:_A /| 2/2024 No. of Pages: 5

Marks: 100

Final Examination/Re-Examination (23-24)
(024-25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory. A

2) Out of remaining questions, attempt any__4 _ questions.

3) Inall___5_ questions to be attempted. _

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: : [20]
a. Consider a feature map as shown below:
1 {2 |3 |4 ‘
5 |6 |7 {8
€O3 ; 2 4 1 3
SO2 ; 9 |7 [5 |6 [5]
BL3 i. Perform 2x2 max pooling with a stride of 2 on this feature map
ii. Perform 2x2 average pooling with a stride of 1 (no padding)
iii. | Mention the significance of pooling in CNN architecture
b. Under what circumstances a model can suffer overfitting and how does
CO2 ; .
S06: dropout help in prevent overfitting. , ; [5]
BL3 ® Describe the potential challenges of using too high or too low dropout rates.
CO4-: c. Discuss any three applications of recurrent neural networks (RNNs) in real-
on 2 world scenarios. ; ; ; ; ; 5]
BI2. To mitigate the exploding gradient problem which technique can be applied
to gradient updates during training? >
Col; d.
SO1; i. State the benefits of deep learning over machine learning. [5]
BL3
--- page 2 ---
HT

ii. You are working on below applications, and you need to decide whether to
use traditional machine learning or deep learning for each. Justify your
choice based on the nature of the problem and the data.

i. You have a small dataset of structured tabular data containing details
about various products (e.g., weight, price, category) and you need to
predict whether a‘product will be profitable or not.

ii. | Develop a system to automatically classify different species of
animals in wildlife photographs. The dataset consists of thousands of
high-resolution images.

iii. Build an automatic speech recognition (ASR) system to convert spoken
language into text. The dataset consists of thousands of hours of
recorded audio data in various accents and languages?

Consider a three-layer neural network as shown below. The inputs and initial
weights are as given below. The sigmoid activation function is used for all
the neurons in all layers. uy

Qa
CO2; [10]
S06;
BL4
Based on the network, inputs, and initial weights, calculate the following:
a. Predicted output after forward pass
b. Calculate the error
c. Assume the learning rate is 0.5, and update weights ws and we
Wi W2_ | W3 Ww4 Ws Wo W7 ws
0.15 | 0.2 | 0.25 | 0.30 | 0.40 | 0.45 | 0.50 | 6.55
bl b2 b3 b4 iy in Tl T2
0.35 0.35 0.60 0.60 0.05 0.10 0.01 0.99
You are working for a company that is developing a smart email client with an
autocomplete feature. Your task is to design a language model that can predict
Q2b the next word in a sentence using historical email data. The model should be
trained on a large dataset of emails. Which deep learning architecture can be
CO4; used for this application? Describe the architecture*in detail. [10]
SO6;
BLS

Cie
--- page 3 ---
i. Implement ANDNOT function using perceptron network for bipolar
inputs and targets when all inputs are presented only one time.

Q3a Xl xK2 t
C02; ! ! “I
1 -1 1 [10]
SO2; -1 1 -1
BL4 zl sl sl
ii. Can perceptron network solve non-linearly seperable problem?
Explain with an example.
Consider the following Convolutional Neural Network (CNN) architecture
designed for image classification. Calculate the number of parameters
(weights and biases) and the size of the feature maps for each layer.
Layer No‘of | Kern | Padd | Strides
‘filters | el ing
Size
Image - -
Q3b (128 x 128x3)
Convolution 1 64 Tx7 | 1 1
CO3; Max Pooling 1(2x2) 0 2 [10]
S06;
BLS Convolution 2 128 5x5 | 2+ 1
Max Pooling 2(2x2) 0 2
Convolution 3 256 3x3_| 1 1
Max Pooling 3 0 2s.
(2x2)
FC 1 512
FC2 256
Output(softmax) 10
You are working as a machine learning engineer at a tech company.
Currently you are using stochastic gradient descent to optimize the
performance an autonomous driving system. However, during training, your
Q.4a team observes that the training process is slow
. i. To address the challenges faced, your team suggests using
CO2; Momentum-Based Gradient Descent. Explain Momentum-based [10]
SO1; gradient descent
BL4 ii. Explain how Adam optimizer works for updating the model's

parameters.
--- page 4 ---
HT

i. Consider a deep neural network where the input X is 10,dimensional.
The network has 2 hidden layers containing 4 neurons each. This is
followed by an output layer gontaining 4 neurons each. Each of the
neurons in the hidden layer has a bias associated with it. Calculate the
total number of parameters in this network

Q4b ii. State the problems associated with the Sigmoid activation function
iii. | Describe how the ReLU (Rectified Linear Unit) activation function
CO2-; overcomes these issues. [10]
SO2; iv. You are building a neural network to classify images of fruits into
BL4 three categories: Apple, Banana, and Orange. After processing an

input image, the network outputs the following logits (pre-softmax
values) for the three classes. Apply the softmax function to the given
logits and calculate the probability distribution across the three fruit

categories
z= [3.5,1.2,0.9]
we

Qa You are designing a project involves summarizing lengthy legal documents
C04: into concise summaries. _.
S02 i. Highlight the challenges RNN architecture will face in this task [10]
BL 4 ii. Describe the gates of GRU architecture

Consider you are tasked with building an image classification model for a
Q5b application that contains only 500 labeled images.

i. How would you apply transfer learning using a pre-trained model like
CO3; ResNet or VGG? . [10]
S02; ii. | Describe the steps involved and explain how transfer learning would
BL4 help improve the performance of your model compared to training a
CNN from scratch. ‘

You are working on a team developing a recommendation system for a large-

scale online retail platform. The dataset contains millions of user

interactions, making model training computationally intensive. To train the

model efficiently without sacrificing accuracy, you are considering different

optimization strategies.
Q6a (a) Explain how Mini-Batch Gradient Descent strikes a balance between
CO3-: Batch Gradient Descent and Stochastic Gradient Descent in terms of
SOl; > convergence speed, and loss curve smoothness. [10]
BL4

(b) Suppose you have a dataset with 1500 samples, and you are using a
batch size of 50 for training. Calculate the number of samples processed in
one iteration and the total number of parameter updates for Gradient Descent
(GD), Stochastic Gradient Descent (SGD), and Mini-Batch Stochastic
Gradient Descent. ,
--- page 5 ---
Hy

Optimizer Number of samples Total number of
processed in one iteration | updates’-~

Gradient Descent (GD)

Stochastic GD

Mini Batch GD

i. | Why does the Inception architecture utilize multiple filter sizes in a

Q6b single module?
ii. | How do the various branches in an Inception module contribute to
CO3; feature diversity? [10]
SOl; iii, | Explain the role of 1x1 convolutions in the Inception architecture.
BLS How is computational cost reduced in the Inception network?

iv. _ Illustrate the structure of.a’single Inception V1 block.

i. Explain the different types of RNN.
ii. | Suggest which type of RNN should be used for the given two scenario

Qa with proper architecture diagram and working.
co4; a) You are building an AI system to provide caption to an input image. [10]
SOl; b) Imagine you are developing a text generation application for a creative
BLS writing platform. The goal is to assist writers by generating the next
few sentences or paragraphs based on a given prompt or the current
context of their story. .
Q7b Describe an application of CNNs in any real-world domain. Explain how
CNNs are applied in that domain, and highlight the key advantages of using [5]
CO3-; CNNs over traditional machine learning techniques for this task.
SO1; BL3
i. State different types of loss function used in deep learning.
ii. You are building a neural network model for the task given below
Q7c identify the most appropriate loss function to use and explain why that
loss function is suitable for the respective task.
Col; a) Predict whether a tumor is malignant or benign based on patient data [5]
SO1; (features include age, tumor size, etc.).
BL3 b) Classify handwritten digits (0-9) from images.
c) Predict the price of a car based on features such as mileage, age, and
condition.
````

## 2024-25 · Final-Exam · Sem 6 · paper 4a8ea75baf3f

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSBS/SEM-VI/DEEP LEARNING/Deep Learning, Sem VI, Final Exam 2024-25.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 88.0

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
| SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2024-2025
Program/s: BTech ,

Stream/s : CSBS/AIDS

Year: III/IV Semester: VI/VIII

Subject: Deep Learning
Date:_05/05/2025
Marks: 100

Time: 3hrs (24 00pm to 52 00pm)

No. of Pages:4

Final Examination Q.4-25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover

of the Answer Book, which: is provided for their use. .
1) Question No. _1°__ is compulsory. .

~~, 2) Out of remaining questions, attempt any4 “questions.
3) In all__5_ questions to be attempted.
4) All questions carry equal marks. .
5). Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: [20]
08802 a. Calculate the Softmax function for [ 1.5, 0.58, 0.75]. [5]
b. Consider an RNN model used for predicting the next word. Given an input
C04,SO02 sequence [“I”, “love”, “machine”], describe how an RNN would process [5]
,BL4 this sequence step by step. Include the concept of hidden states and output
generation. .
c. Imagine training a deep neural network to predict stock prices. The
dataset is large, and the loss function has a complex landscape with steep
slopes and flat regions. You decide to use momentum-based
optimization to speed up convergerice.
CO2.S02 However, using standard momentum-based gradient descent (GD) can
B 12 sometimes lead to overshooting the optimal solution, especially in cases

where the gradient updates are significant due to accumulated momentum. :
This results in oscillations around the minimum, slowing down
convergence. To overcome this, you apply Nesterov Accelerated
Gradient Descent (NAG).

Explain the weight update rule for NAG using a stepwise algorithm.
--- page 2 ---
Discuss the bias-variance tradeoff applicable to deep learning models.

, d.
eae Determine the effect on bias and variance by regularizing the weights and
> ; adding dropout layers.
a A government agency wants to use a CNN for analysing satellite images to
Q2 detect deforestation patterns. However, satellite images are extremely large, [10]
CO3,SO2 making CNN training computationally expensive. How can you modify the
»BL3 CNN pipeline to make it feasible for the large-scale processing of satellite
images? .
Consider the neural network with input values [1, 0], a target value of 1, and
b a sigmoid activation function. Calculate the following [10]
CO2,SO2 | ~. 1. Predicted Output after forward propagation :
> 2. Error after the first forward pass
BL4 .
Q3 a Justify how the noise can contribute to data augmentation and
02,802 Regularization. _ [3]
»BL3 Consider the following 7 * 7 image and 3*3 filter ;
(7)
2130246
corsor| [578312
,BL4

Filter

0 1.0

1 -1 1

010 ;

Consider padding = 1 and stride= 2

Compute the output after applying the convolution operation.
--- page 3 ---
Explain the key differences between Gradient Descent (GD), Stochastic
CO3,SO2 Gradient Descent (SGD) in terms of the following criteria.

,BL4 [10]
; e Computational Efficiency

e Reaches the optimal solution the fastest

e Most stable weight updates

e Handling massive datasets. -

c.

Clearly mention which method performs the best or worst for each
category. Show graphs.

Q4 a A neural network is trained using Gradient Descent with a learning rate of
C02.S02 0.01. The current weight is.w = 0.5, and-the loss gradient with respect to the [4]
° weight is dL/dw = -4..Calculate the updated weight after one iteration. What

BLS _- - | will happen if the learning rate is too > large or too small? _ -

How would you design a simple Multi- Layer Perceptron (MLP) architecture
CO2,S02 | b to classify handwritten digits from the MNIST dataset, and what would be | [6]
BL4 the role and functionality of each layer in the network?

A tech company is developing an intelligent email assistant that helps

C0402 users by auto-completing sentences as they type. The system-should +
> ° predict the most likely following words based on the context of the (4+6]
»BLS previous words in the email.

@ Which type of deep learning model would be most suitable for
this task if we want to use fewer gates?
(ii) | Using a diagram, describe the architecture of the selected

model.
a. Discuss the advantages of parameter sharing. [2+6+
Q5
. . . . . 2]
C03,S02 Consider a scenario where you are designing a convolutional neural ;

network (CNN) for image classification. Your dataset consists of high-
-BL2 resolution grayscale medical images (1024 x 1024). Given the large image
size, you are concerned about the number of trainable parameters and the -
CO3,SO2
computational cost.
,BL4 To optimize your model, you decide to use a convolutional layet with 32
filters of size 5x5 and a stride of 1, followed by a fully connected (FC)
layer.
How many parameters are learned i in the convolutional layer, considering
CO03.S02 parameter sharing?
, . How does parameter sharing help in reducing the total number of trainable
,BL3 parameters compared to a fully connected layer?

d. A machine learning engineer is developing a deep learning model to
classify medical images into different disease categories. The dataset
--- page 4 ---
C03,S02 contains 50,000 high-resolution images. The model initially achieves high .
[2]

BL4~ accuracy on the training set but fails to generalize well on new test images.
(i) Does. the model suffer from underfitting or overfitting? [8]
(ii) | What is early stopping? Explain how it can be applied to
address this issue with the help of an algorithm.
: a. A bank is building an AI system to recognize handwritten digits from
Q6 : scanned checks. The team is debating the.use of a Fully Connected Network [10]
C0O3,SO2 (FCN) versus a Convolutional Neural Network (CNN). Discuss which
model would be more. effective and why. How does the handling of spatial
»BL3 features differ between FCNs and CNNs in this scenario?
A speech-to-text application is being developed to transcribe spoken.
commands into text for a smart home device. : [24+
+-€04;S802.}°- _ -.| @) Which neural network model (Feedforward, RNN, or hybrid).would be ee
. most effective in this context? Why? : 4]
»BL2 (b) Explain how backpropagation through time (BPTT) would be used in
this model. . .
(c) How can’ you utilize activation functions such as ReLU or tanh
effectively within this network? ;
Q7 fa. A deep learning engineer finds that AdaGrad reduces the learning rate too
C03.S02 aggressively, leading to slow convergence. They decide to use RMSProp
_ to maintain an adaptive learning rate without excessive decay. . | [10]
,BL4 Explain the working of RMSProp using an algorithm.
. Explain the role of Gated Recurrent Unit (GRU) in handling. long-term [10]
C04,S02 | . dependencies in sequential data. Discuss the gates used in GRU by
BL2 b. providing mathematical equations for each gate, accompanied by a

diagram.
````

## 2024-25 · Final-Exam · Sem 3 · paper 7db88b2d12c5

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCES FALL BACH
- Source: `02_Question_Papers/Legacy/M TECH/2ND YEAR/DATA SCIENCES FALL BACH/SEM III/DEEP LEARNING/Deep Learning Batch 2024-25 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 88.3

````text
SVKM’S NMIMS J
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS EN! ppewnnc! , ARY
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2024-2025

Program/s: M Tech. Year: II Semester? IIT

Stream/s :DS

Subject: Deep Learning . Time: 3 hrs (2:00pm tos. 00 pm)
Date:_26 /Nov/ 2024 No. of Pages:2

Marks: 100

Final Examination @ooy- 28)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks. .

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

-

Ql
Answer briefly: [20]
CO-; SO-; | a. What is role of activation functions in neural network?
BL- 7
CO- ; SO-; | b. What is a learning rate and why is it important? :
BL- .
CO-; SO-; | c. What is the purpose of a loss function in neural network?
BL-
CO- ; SO-; | d. Why is data normalization important in training?
BL-
Q2 Explain the concept of backpropagation and its significance in training 120]
CO-; SO-; neural networks.
BL-
Q3
CO-: SO-: What is overfitting in neural networks and techniques to prevent it? [20]
BL-
Q4
CO-; SO-; What are CNNs and why are they effective for image processing task? [20]
BL- *
--- page 2 ---
Q5
CO-; SO-; What are GANs and how do they work? [20]
BL-

Q6
CO-; SO-; How do LSTM networks improve upon traditional RNNs? [20]
BL-

Q7
CO-; SO-; Explain any four activation functions. [20]
BL-

Cad
````

## 2024-25 · Re-Exam · Sem 5 · paper 5fc62eebec69

- Departments: Artificial Intelligence, Computer Engineering, Data Science, Electronics and Telecommunication, Information Technology
- Programmes: B TECH / COMPUTER, B TECH / CSE DATA SCIENCE, B TECH / EXTC, B TECH / I T, MBA TECH / ARTIFICIAL INTELLIGENCE, MBA TECH / COMPUTER, MBA TECH / EXTC, MBA TECH / I T
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/DEEP LEARNING/Deep Learning, Sem-V, Batch 2023-24 & 2024-25 Re Exam.pdf` (+7 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (6 pages), mean OCR confidence 87.0
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025
Program/s: BTech / MBATech Year: III/IV Semester: V/VII
Stream/s : IT / COM/EXTC /CSE-DS /AI /AIML

Subject: Deep Learning Time: 3 hrs (2-00. to § Dopn)

Date: 22]02] 2025 No. of Pages: 6
Marks: 100

Re-Examination ( 23-24) | (24- 25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any __4 questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q1 [Answer briefly: [20]

ja. |What distinguishes deep learning from traditional machine learning?
Identify the suitable neural network architecture for the given applications. Justify your reasons.

col: i. Detection of diabetic retinopathy from high-resolution retina images and classification
Sol : into five different stages of disease (no retinopathy, mild, moderate, severe, orl[5]
BL2. proliferative diabetic retinopathy

ii. | Recognizing an alphabet (in upper case or lower case) of English language in an image
iii. Forecasting the weather for the next N days based on historical weather data

lb. |We have trained four different neural network models on the same dataset using various hyper
parameters. The training and validation errors for each model are provided below. Based on
this information, which model is likely to perform worst and best on the test dataset? Justify
your reasons. State the possible solution to improve the performance of the worst model.

CO2 ; Model Training Error Validation Error
S06 ; n 0.9 12 5]
laa D 03 0.6

3 1.5 0.5

4 12 i
--- page 2 ---
c. |Why are multiple convolution layers important in CNNs?
What will the convolution output over the following feature map with the following kernel

with a stride 2?

Kernel
1 0 1
C03 ; ee
S06; 6 4 2 [5]
IBL3
Input Feature Map

2 3 8 2 3
2 2 4 4 6
1 2 1 2 9
7 5 3 3 2
2 4 3 5 4

C04; |d. |How is backpropagation different in a Recurrent Neural Network (RNN) compared to al
SOL; traditional feedforward neural network? [5]
BL3 Describe strengths of RNNs for processing sequential data.

i. What is the significance of an activation function in a neural network, and how does it
impact the learning process. Explain Relu activation function with the help of diagram

ii. | Suppose you are given a dataset with various attributes about houses (such as size,
number of rooms, age, location, etc.), and you want to predict the selling price of a
house. Is it appropriate to use sigmoid function to model the relationship between the

Qra house attributes and the selling price? Justify
CO2-; [10]
ee iii. Consider the vector u = [1.2, 3.4, 0.9]. Find the corresponding softmax values.

iv. You are using the sigmoid activation function in a neural network. If the network's

weighted input is 2.5, what is the output of the sigmoid activation function?
i. Describe the problem of vanishing and exploding gradients. How do these problems

Q2b affect the training of deep neural networks, particularly RNNs?

ii. Explain the role of the different gates in the GRU architecture. How do these gates
mec(y help mitigate the vanishing gradient problem? [10]
BL4
--- page 3 ---
For the fully connected feed forward neural network given below find
i. Total error at the output layer after first forward pass
ii. Total error with dropout of Hi2 neuron from hidden layer after first forward pass.
iii. | Compare the error of part a and b.

Q3 a
CO2-; [10]
S06;
BL4
0.10 0.15 [0.20 [0.25 |0.30 |0.35 |0.40 (0.45 [0.50
0.55 0.60 |0.65 {0.70 |0.75 |0.80 |0.85 |0.90 0.95
Xi X2 X3 Xs T1 T2
0.10 | 0.20 0.30 0.40 0.01 0.99
\Assume bias at hidden layer neurons b;=0.60, and bias at output layers neurons b2=0.60
i. | Why does CNN use parameter sharing and sparse connections compared to fully
connected networks?
ii. Explain the computational trade-offs between using larger convolution kernels (e.g.,
Q3 b
5x5) versus smaller ones (e.g., 3x3).
CO2-; iii. Justify the choice of activation functions, such as ReLU, affects the learning process in
S06: CNNs a
Lae iv. Can aCNN perform well without pooling layers?
--- page 4 ---
Consider the following Convolutional Neural Network (CNN) architecture designed for
image classification. Calculate the number of parameters (weights and biases) and the size of
ithe feature maps for each layer.

\Layer Feature Number of |Kernel |Padding (Strides |Parameters
Map Size|Filters/Units |Size
Image 64 x 64x3 - -
Q4a Convolution 1 32 3x3 1 1
O32: Max Pooling 1 0 2 [10]
SOl; (2x2)
BL5 ‘Convolution 2 64 3x3 1 1
Max Pooling 2 0 2
(2x2)
Convolution 3 128 3x3 1 1
IMax Pooling 3 0 2
(2x2)
FC1 256
Output(softmax) 43
Q4b
co2, Implement AND logic gate using perceptron neural network considering bipolar inputs, [10]
S02,6, bipolar targets and learning rate =1.
BL4
Q5a
CO3; i. Describe concept of a skip connection used in the ResNet architecture. What
sol: advantage does it provide for training deep neural networks? [10]
2 ii. In the Inception architecture, describe the role of a 1x1 convolution with an example
BL4
Considering a recurrent neural network with one hidden layer
i. Sketch and state the hidden layer output (hr) at time step t.
Assume the following notations.
xt = the input to be at time step t,
Wxn = weights of input-to-hidden weight,
Wnn = the weight of the hidden-to-hidden layer
bn = the bias of the hidden layer,
ale hut = the hidden state from the previous time st [10]
; tl len state from the previous time step.
CO4-; ii. Given the following weight matrices for the network in part A
| Wn = [O2 O] Wan = [P30] by = [0.102] x= [10] ena = [01]

Compute the hidden state hi assuming a ReLU activation function.
--- page 5 ---
Consider a three-layer neural network as shown below. The inputs and initial weights are as
given below. Sigmoid activation function is used for all the neurons in all layers. The actual
output of the network is 1.

Q6a
CO2, . 7 5 :
S026, Weight |wi w2 lw3 lw lws Wo Ww lws [10]
BL4 Value 0.2 -0.3 0.4 0.1 -0.5 10.2 -0.3   |-0.2

Input = fii in is

‘Value {1 0 1

Bias [by bz b3

Value [+04 (0.2 0.1

Based on the network, inputs, and initial weights, calculate the following:

i. Predicted output after forward pass
ii. Calculate the error
iii. | Assume the learning rate is 0.9, and update weights w7 and wg

Q6b 'You are developing a model for a healthcare startup that predicts patient outcomes based on

medical data. While experimenting with different optimization algorithms, you initially try
co2: \AdaGrad but after training for several epochs, you notice that the model's performance is
S01 2 stagnant. After consulting with your team, you consider switching to RMSProp to address this
BL A issue.

[Discuss both the optimizer in detail and the fundamental differences between them.
Q7a Imagine you are working for a social media analytics company that provides insights into
co4: customer sentiment about products and services. The company collects large volumes of long
Sol e sequence of text data from platforms like Twitter, Facebook, and customer reviews. Your task |L10]
BL 5 is to build a deep learning model to analyze the sentiment of these texts as positive, negative,

lor neutral.
--- page 6 ---
i. | Which deep learning architecture would you suggest for analysing the sentiments from
the text?
ii. Describe the working of the suggested architecture with required equations.

Q7b

CO3; Discuss the concept of “Transfer Learning” and its benefits. Explain by taking suitable [5]
SO]; examples.

BL4

eave i. | What is the importance of learning rate in the context of training a neural network.

CO1,2 ii. Provide one example of a commonly used loss function for classification tasks and (5)
$02,6 one for regression tasks and explain them

BL3
````

## 2023-24 · Exam not stated · Sem 8 · paper 128ce27edbc3

- Departments: Electronics and Telecommunication
- Programmes: MBA TECH / EXTC
- Source: `02_Question_Papers/Legacy/MBA TECH/4TH YEAR/EXTC/VIII SEMESTER/DEEP LEARNING/Deep Learning.pdf`
- Printed on paper: max marks: 100
- Text: ocr (3 pages), mean OCR confidence 87.4

````text
SVKM’S NMIMS

SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024

Program/s: MBA.Tech /B.Tech Year: 4 Semester: VIII _
Stream/s; EXTC_

Subject: Deep Learning Time: 3_ hrs (Zioopmto Stoop)
Date:_2.3 / 04 / 2024- No. of Pages:-3___

Marks: 100.

Re-Examination (2021-22, 22-23)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the
cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.
3)Inall___5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi , _ ra cnny
Answer briefly: [4x5=20]
ary SO-1; | a. Compare machine learning and deep learning. [4]
oa Q SO-1; | b. Define what a perceptron is and describe its basic structure. [4]
c. For the given scenario,
ng 1} Number of Filters = 5
10 *
\
Convolution
CO- 2; SO-1; 10 Filter size=(3,3) [4]
BL-3
filters = 5,kernel_size=(3,3), input_shape=(10,10,1), stride=1, padding=0
(i) Determine the number of parameters in the convolution layer.
Q Determine the output shape.
ne SO-l; | d. Explain a simple RNN cell and explain how it processes sequential data. [4]
tee SO-1; |e Compare Relu and Tanh activation function. [4]
--- page 2 ---
Q2 CO-2; a. Describe the architecture of AlexNet, including the number of layers, their 7
SO-1; BL-2 . “he [10]
types, and the number of neurons in each layer. ‘

b. (i) What is the role of optimizers in training neural networks, and why [05]
are they necessary
CO-1; SO-1; rr ng «
BL-4 (ii) Compare and contrast different variants of gradient descent, such
as batch gradient descent, stochastic gradient descent, and mini- [05]
batch gradient descent
Q3 a. Explain Feed forward algorithm and back propagation algorithm in neural
CO-1; SO“; network with i i
BL2 with an example.
CO-1;S0-1; | b. (a) Explain L1 and L2 regularization. [5]
BL-2 (b) Explain the various hyperparameters used in training a neural network.. [5]
Q4 a. Explain any one image classification application using convolutional neural
CO-3; SO-1; [10]
BL-6 network. *
CO-3;$0-1; | b. Explain the architecture of an LSTM cell and how it addresses the vanishing 110]
BL-2 gradient probiem in traditional RNNs.
Q5 a. Explain the steps for calculating the number of parameters, feature map size in
p Pi [10]
CO-2; SO-1; ° c
BL-5 Sor a given convolutional neural network by taking an example. .
CO-3;$0-1; | b. Discuss machine translation application with a suitable deep learning [10]
BL-6 architecture.
Q6 a. Explain the structure of an Encoder-Decoder model and how it differs from rt]
CO-3; SO-1;
BL-6 ales traditional feedforward neural networks.
CO-2; $0-1; | b. Describe the components of a typical CNN architecture, including (10)
BL-2 convolutional layers, pooling layers, and fully connected layers.
Q7 “ya, (i) Explain why simple perceptron can’t be used for non-linearly separable [05]
CO-1; SO-1;
BL-2 dataset.
Poe SO (ii) Explain Bias and variance tradeoff. [05]
--- page 3 ---
i

CO-1; SO-1;
BL-2
CO-1; SO-1;
BL-2

F ny

(i) Explain the various methods to solve overfitting problems in neural
network.
(ii) Compute the output of the given neural network using sigmoid activation

function.

[5]

[5]
````

## 2023-24 · Final-Exam · Sem 5 · paper 017671e0097f

- Departments: Artificial Intelligence, Computer Engineering, Electronics and Telecommunication, Information Technology
- Programmes: B TECH / ARTIFICAL INTELLIGENCE, B TECH / COMPUTER, B TECH / EXTC, B TECH / I T, B TECH / IT, MBA TECH / ARTIFICIAL INTELLIGENCE, MBA TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-V/DEEP LEARNING/Deep Learning, Final exam,2023-24.pdf` (+7 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (5 pages), mean OCR confidence 84.4
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS q
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINE
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2023-2024

Program/s: B Tech /MBA.Tech ; Year: 34/4" Semester: V/ VII
Stream/s ;AI/AIML/IT/EXTC/Comp Engg

Subject: Deep Learning Time: 03 hrs (10:90 to [200 py,
Date: 02. /|2. / 2023 No. of Pages: 4 5 _

Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) Inall__5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi ;
Answer briefly: (20]
COo- 1; (a)
SO- 1; State features and limitations of deep learning. [05]
BL-2
on (b) A ANN network is being trained. Identify and state the significance of the (05]
BL-3 different hyper parameters which will have to be tuned.
CO-5 (c) A recurrent neural network (RNN) is to be trained using back propagation
SO-] ; through time (BPTT). Show the architecture and explain in brief how it can be [05]
BL-2 implemented.
(d) “ Determine the output of the given 4x4 image after convoluting with the given
3x3 kernel. Given padding=0 and stride =1.
CO-3 ; io l9 [5 |6 1]1]1 |
05)
SO-1 ; 4 5
° 5 |7 6 Z 1 }2 ]1
BL-3 : .
3 3 2 8 1 1 |1

3 2 6 7
--- page 2 ---
Q2

CO-2;
SO-1;
BL-3

(a)

x
The following diagram represents a feed-forward neural network with one

hidden layer:

(4-8)

A weight on connection between nodes i and j is denoted by wij, such as w13

is the weight on the connection between nodes | and 3. The following table

lists all the weights in the network:

Ww13 = —2 W35 = 1
we3 = 3 | wa5 = —1
wi =4 w3g = —1
wea = —1 | wag = 1

Each of the nodes 3, 4, 5 and 6 uses the following activation function:

eto 1 ifv>0
? ~ ) 0. otherwise *

where v denotes the weighted sum of a node. Assume bias to be zero. Each
of the input nodes (1 and 2) can only receive binary values (either 0 or 1).

Calculate the output of the network (y5 and y6) for each of the input patterns:

Pattern: | P, Py, P; P,
Node 1: 0 1 0 i
Node 2: 0 0 1 tH

[10]
--- page 3 ---
PA AANTIIIS Sie be

CO-2; (b)
SO-1; (i) “The activation functions are essential in Neural Networks” Justify. 05
BL-5 Explain any two activation functions. [03]
CO-1; (ii) An application for facial recognition is to be designed. The training [05]
SO-1; dataset consists of images of resolution 227x227x1. Infer whether a
BL-2 machine learning model or a deep learning model should be used. State
the advantages of your choice of the model.
(a) For the neural network shown in fig, wg bias) W) a b}a3)
“Woe
a O
Ar

Q3 X2, Wa
CO-2; 35 Wos Lbias)
SO-1; [10]
BL-3 . _

First training example, x = [1 0 1] whose class label is t= 1. The sigmoid

activation function is applied to hidden layer and output layer. Assume that

the learning rate y is 0.9. The weights are given by

Initial input and weight values 1
0.2 -03 04 01 05 02 -03 -02 040201 —

Woa and Wos are bias applied at hidden neurons and Woe is the bias applied at

output layer. Using Backpropagation, update the value of Wa6 and Wse.
CO-2; (b)
SO-l; What are the key advantages of using the Adam optimizer in Artificial Neural
BL-l Networks (ANNs), and how does it differ from Stochastic Gradient Descent [10]

(SGD).
--- page 4 ---
i

(a) Determine the number of parameters and the feature map size at each layer

Clo]

for the vow CNN srenteau as post» in the figure. 256 koyn els
ax Poo 2
P pan sy | a WAGs P max book
22+ Sz
o4 Ab Kein 3,
22+ Con
CO-3; at
SO-1; 2x3, P=]
BL-5 . ag Eevrel
Ba 4
< | {Max a,
FC Se pool = :
€ < a 2x3 L 7 iv g : kemeb:
a Kevnes . an
5 HUIe FOIE
[00 (6) | You have to design an application for autocomplete using LSTM. The input to
CO-4; the network is “Maharashtra is a state in the western part of India. The capital
SO-1; of Maharashtra is , [10]
BL-2 Show the network architecture for this language modelling task. Determine the
equations of the conditional probabilities for each time step.
Q5 (a) | With reference to inception network, answer the following:
1. The need of using filters of different kernel sizes in a single inception
CO-3;
in block (module). [10]
BL-S 2. Justify the significance of 1x1 convolution used in this network.
3. Sketch the architecture of a single block of inception V1 architecture,
CO-2; (b) (i) Justify why single/simple perceptron cannot be used for non- [05]
SO-1; linearly separable data. [054
BL-5 (ii) Implement XOR and XNOR gate using perceptron. =
ys t>
(a) Consider the single time step of LSTM as shown in the figurd. Soft
' act
<t-] <b>
Qo C > cD
CO-4; 10
SO-1; {10}
BL-3,5

ie. L>
--- page 5 ---
1. Identify the significance of the forget, update gate and output gate.
2. Develop the equations for the update gate and reset gate. p
3. Justify whether this model will be able to handle long sequence lengths.

(o)/ With respect to Resnet (residual network) answer the following:

CO-3; ‘
SO-1: 1. Discuss how vanishing gradient problem is solved in this network. [10]
BL-6,4 2. Considering a single block of ResNet with skip (residual) connections,
compare the output with and without these connections.
ar (a) Consider that you are designing the application of sentiment analysis, where
CO-4; the input is a sequence of words in the form of a small paragraph. Suggest and [10]
SO-1; sketch a model which can be used for this application. Determine and explain ,
BL-5S how the output will be generated. :
(b) ; ; ; ; ; , [05]
(i) Discuss bias and variance trade off applicable to deep learning .
models. [05]
(ii) Determine the effect of the following operations on the bias and
variance of your model. Fill in one of ‘increases’, ‘decreases’ or
‘no change’ in each of the cells:
CO-2, Bias Variance
SO-1; Regularizing the weights
BL-6,5 Increasing the size of layers(more hidden units

per layer)

Using dropout to train a deep neural network
Getting more training data (from the same
distribution as before)
````

## 2023-24 · Final-Exam · Sem 2 · paper 74053399e184

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENT
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ARTIFICIAL INTELLIGENT/SEM II/DEEP LEARNING/Deep Learning Batch 2023-24 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (1 page), mean OCR confidence 87.9

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING

Academic Year: 2023-2024 .
Program/s: M-Tech Year: I Semester: Il
Stream/s : Artificial Intelligence
Subject: Deep Learning ; . Time: _03 hrs @pm toSpm)

Date:_03 /05 / 2024 No. of Pages:01_
Marks: 100
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use. :

( 1) QI is compulsory

2) Attempt any one dataset from Q2.

3) Use of internet is allowed.

4) Figures in brackets on the right hand side indicate full marks.
5) Assume Suitable data if necessary.

Qi.

A. Explain LSTM (10M)
B. Explain CNN (10M)

Q2. Apply the deep learning concept and train any one of the following model (80M)
Dataset 1-AtoZ
Dataset 2 — Mnist

;» Dataset 3 - Bean

tfds.load('beans')

Page o|
````

## 2023-24 · Final-Exam · Sem 3 · paper 27ea3c94d6f5

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCES FALL BACH
- Source: `02_Question_Papers/Legacy/M TECH/2ND YEAR/DATA SCIENCES FALL BACH/SEM III/DEEP LEARNING/Deep Learning Batch 2023-24 Final.pdf`
- Printed on paper: max marks: 100
- Text: ocr (2 pages), mean OCR confidence 92.8

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING

Academic Year: 2023-2024
Program/s: M Tech

Stream/s : Data Science
Subject: Deep Learning
Datere 25/5 11/2023,
Marks: 100

No. of Pages:-<087

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Attempt any ONE Dataset out of 3.

2) All questions carry equal marks.

3) Answer to each new question to be started on a fresh page.

4) Figures in brackets on the right hand side indicate full marks.
5) Assume Suitable data if necessary.

Q1 . Apply the deep learning concept and train any one of the following model [100]

Dataset 1— MNIST
from keras.datsets import mnist

data = mnist.load_data()
Dataset 2—-AtoZ

Dataset 3 — Fasion mnist

tf.keras.datasets.fashion_mnist.load_data()

Each training and test example is assigned to one of the following labels:
0 T-shirt/top

1 Trouser

2 Pullover

3 Dress

4 Coat
--- page 2 ---
5 Sandal
6 Shirt

7 Sneaker
8 Bag

9 Ankle boot

Each row is a separate image
Column 1 is the class label.
Remaining columns are pixel num!

Each value is the darkness of the pixel (1 to 255)

bers (784 total}.

PORa-
````

## 2023-24 · Re-Exam · Sem 5 · paper 3df2c1997c77

- Departments: Artificial Intelligence, Common (all branches), Computer Engineering, Electronics and Telecommunication, Information Technology
- Programmes: B TECH, B TECH / ARTIFICAL INTELLIGENCE, B TECH / COMPUTER, B TECH / EXTC, B TECH / IT, MBA TECH / ARTIFICIAL INTELLIGENCE, MBA TECH / COMPUTER, MBA TECH / EXTC, MBA TECH / I T
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ALL STREAM/SEM-V/DEEP LEARNING/Deep Learning , Re-exam 2023-24.pdf` (+8 identical copies)
- Printed on paper: max marks: 100; exam date: 13/02/2024
- Text: ocr (5 pages), mean OCR confidence 89.6

````text
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2023-2024
Program: B Tech /MBA.Tech Year: 3'4/4" Semester: V / VII
Stream/s : AI/AIML/IT/EXTC/Comp Engg

Subject: Deep Learning Time: 99 _ hrs (Loopreto 5260p")
= t

Date: 13/02/2024 No. of Pages:__ 4 &

Marks: 100

ReExamination

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No._1___is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3)Inall__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary.

Ql .
Answer briefly: [20]
© cor; (a) ica) ot
SO-1- What factors drive the widespread adoption and utilization .of deep learning [05]
BL-1 techniques in various applications?
(b) Consider a deep neural network for designing animal species classification
with 10 features and 4 classes. The network has 3 hidden layers containing 5
CO-2; neurons each. Each of the neurons in the hidden layer and output layer has a
SO- 1; . afi, : 105]
BL2.5 bias associated with it. Show the neural network architecture and determine
; the total number of parameters in this network?
CO-2: (c) You are using a deep neural network for a prediction task. After training your
SO-1 2 model, you notice that it is strongly overfitting the training set and that the [05]
BL-l performance on the test is not good. What can you do to reduce overfitting?
--- page 2 ---
(d) For the given 4x4 feature map, Determine the output of max pooling and

average pooling keeping pooling size as 2x2 and stride as 2. a
CO-3: 21 11 15 10
SO-1; [05]
BL-5 12 |9 10 11

11 13 18 12

7 (4 [is [12

(a) Consider a three layer neural network with the initial weights shown below.
W| represents weights between input layer and hidden layer, W2 represents
weight between hidden layer and output layer. Consider sigmoid activation
function. = ;

Q2

CO-2;
SO-1;
BL-5

[10]
--- page 3 ---
O11 P12 813 14 08 02 03 Of

W= 62, 022 O23 O24}   |-0.5 04 03 0.2
1 165; 032 O33 934{ | 0.1 0.2 -0.1 0.2
641 O42 643 O44 -0.2 05 0.5 0.8
We = [0.5 0.7 —0.6 0.2] X =(04 0.3 05 -0.4]
b= [0.6 0.2]

a. Compute the mean square error loss after the forward pass
b. Update the weight between first neuron of hidden layer and output
neuron (weight between hj and y:). Consider target =0.9 and learning

rate = 0.5
CO-2; (b)
SO-1; i) Compare standard momentum and Nesterov accelerated gradient differ.
BL-5 How does their performance (convergence as a function of time T) differ [05]
CO-2: on convex optimization problems? [05]
2 ii) What might happen if you set the momentum hyperparameter too close to
SO-1; : rr
BL-1 1 (e.g., 0.9999) when using an SGD optimizer?
Q3 (a) .
i) Differentiate between Sigmoid and Relu activation functions [04]
CO-2; ii) Why Sigmoid or Tanh is not preferred to be used as the activation function [03]
SO-1; in the hidden layer of the neural network?
BL-2,3 iii)Consider v = [2.1, 4.8, 3.5], find the corresponding softmax. [03]
CO-2; (b) Explain importance of regularization of ANN during training processes?
SO-1; State various techniques of regularizations of network and elaborate any one [10]
BL-2 of the same in detail?
@) Determine the weights required to perform the classification as per the table
using perceptron network. Assume learning rate as | and initial weights as
04 0. Consider threshold = 0 and solve for 2 epochs.
Inputs
CO-2; -
SO-1: Xi X2 X3 X4_| Bias |_ Target [10]
BL-5 1 1 1 1 1 1
-l 1 -1 -1 1 1
1 1 1 -1 1 -l
1 -1 -1 1 1 -1
--- page 4 ---
(b) Consider a Convolution Neural Network (CNN) classifier. For each layer,
solve for the number of parameters (weights), number of biases and the size of
the associated feature maps. POOL-K indicates a K x K pooling layer with
stride K and padding 0. FC stands for a fully connected layer with N neurons.
FC3 has 120 neurons and FC4 has 84 neurons and there are a total of 10 output

classes
-) layer Feature map Size No. of parameters
INPUT (227 x 227 x 3)
CONV 9x9 kernels , 32 filters (P=0, Stride
=1)
CO-3;
SO-1: POOL (2x2 pool size, stride=2, P=0) . [10]
BL-5 CONV : 5x5 kernel size, 64 filters (P=0,
Stride =1)
POOL 2 (2x2 pool size,stride=2,P=0)
CONV 5x5 kernal   size,64filters(P=0,
Stride =1)
POOL 2 (2x2 pool size,stride=2,P=0)
FC-3
FC-4
SOFTMAX
Total Parameters
(a) | Youare using GoogleNet for a classification task. The network is taking a long
Q5 . é : : Tae .
time to train. You identify that the problem may be due to vanishing gradients
CO-3; and you need to change the architecture. Suggest and explain a better [10]
SO-1; architecture which can be used to solve this problem. Highlight the important
BL-5 features of the revised architecture.
(b) (i) A system is designed to diagnose chest cancer through X-ray images using [05]
deep learning. Justify why deep learning is the suitable approach?
(ii) List down the advantages and disadvantages of Recurrent Neural Network. [95]
Q6 (a)
CO-4; Consider a single time step in GRU as shown in the figure, [10]
SO1-;
BL-3
--- page 5 ---
AOE

a. Identify the significance of the update gate and reset gate.
b. Develop the equations for the update gate and reset gate.

CO-3; (b) A machine learning expert wants to design an application for classification of
SO-1; vegetables in a supermarket. There are 10 classes but the number of samples
BL-3 per class are less. Since he does not have sufficient samples and resources to [10]

train a complex network, he decides to-use a pre-trained model. Identify and
explain the different ways in which he can use it.

Q7 (a)
ie Show and Explain the architecture of Long Short Term Memory (LSTM). [10]
BL-2

CO-4; (b) Explain different types of recurrent neural network with architecture.
SO-1; [10]
BL-2
````

## 2023-24 · Re-Exam · Sem 6 · paper 1725979869ef

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSBS/SEM-VI/DEEP LEARNING/Deep Learning, Sem-VIII, A Y 2023-24, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 86.5

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEME
Academic Year: 2023-24

2
Program: BTech Year: [V/IH’Semester: VIII/VI
Streams: CSBS/Aas) AT DS

Subject: Deep Learnin Time:3 hrs (220Q~to 5700
g

Date:_27/ 6 / 2024 ; No. of Pages: 3
Marks: 100
Re Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and the cover of
the Answer Book provided for their use.

>» 1) Question No. _1___ is compulsory.
2) Out of the remaining questions, attempt any __4 _ questions.
3) In all___5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: (20]
CO-1 a. : . F ’
S0-1.6.7 Discuss the need for Deep Learning. Explain two popular Deep Learning [5]
BL-1.2 Frameworks.
CO-2 b. : : a .
SO-1.6.7 Draw and describe the components and mathematical principles underlying the model [5]
~ of an artificial neuron.
BL-2
CO-2 G Interpret the trade-off between bias and variance over deep learning models by taking [5]
SO-1,6,7 relevant examples.
©) | BL-3
CO-2 d. . F head F .
SO-1.6.7 What will the convolution operation's output be over the following feature map?
BL-3 Where the following kernel is applied with stride 2.
Input Feature map Kernel
2 |4 }9 Ji fa |! ]? }3
2/1 14 Ja Jo [4]? }4 [5]
1 fr f2 fo fa f% Jey
7 3 5 1 3
--- page 2 ---
i

a. Illustrate two vision and text-based applications of deep learning in real-world | [10]
scenarios. Additionally, specify the names of deep learning models or

oy 234 architectures suitable for implementing these applications (Include input, pre-
S0-1.6.7 processing, model and output in the diagram).
BL-3,2 b ‘i ‘ ; : Sy crit Sy. yi
: Explain the working of the:-basic RNN architecture. Discuss its limitations, types, and | [10]
use cases.
2 Compare binary cross-entropy loss and categorical cross-entropy loss with the help of [5]
co.2 examples.
ira Ms Discuss the role of LI and L2 regularization in training deep learning models. (5]
Consider that you are designing an application to predict international airline
CO-2 c. : : .
SO-1.6.7 passengers. Given a year and a month, the task is to predict the number of [10]
BL-2 , international airline passengers in units of 1000. The data ranges from January 2009 (>
to December 2020, or 12 years, with 144 observations. Suggest and sketch a model
CO-4 that can be used for this application. Determine and explain how the output will be
SO-1,6,7 generated.
BL-3,2
a. Given a three-layer artificial neural network with a learning rate of 0.55 and target [10]
outputs of [0.2, 0.8], calculate the updated weights w8 and w4 after applying the
sigmoid activation function.
Ge
EF nt
N
Q4.
CO-2 -
SO-1,6,7 b, Given below is the CNN classifier information. For each layer, solve the feature map
BL-3 size and the number of parameters (weights). FC stands for a fully connected layer [10]
with N neurons. F is the filter size, K is the number of filters, s is the stride, and p is
CO-3 the padding.
SO-1,6,7
BL-3 5 7
Layer Specifications
Input Layer 240 x240x3
Conv Layer k=50, f=8, s=4
Max Pooling 3x3, s=2
Conv Layer k=128, f=5, p=2
Max Pooling 3x3, s=2
Conv Layer k=256, f=3, p=1
Conv Layer k=128, f=3, p=1
Max Pooling 2x2, s=2
--- page 3 ---
FC 1024

FC 512 o2
Softmax 10
Qs a. What are hyperparameters? List four hyperparameters of CNN. [1+4]
CO-3 b. Imagine you are designing a,simple RNN for a text generation task. The goal is to
SO-1.6,7 predict the next character in a sequence given the previous characters. The network
BL-1.2 architecture consists of an input layer, one hidden recurrent layer, and an output layer
CO-4 that uses a softmax activation function for prediction. You use Back-propagation [3+2]
SO-1.6,7 Through Time (BPTT) to train your network.
BL-2 (i) Use a diagram to Illustrate the role of the RNN's unfolded computation
CO-2 graph in the BPTT process.
aes (ii) Discuss one potential issue when using BPTT for long sequences.
CO-3 C. Derive the Gradient Descent derivation for a neural network with 1 hidden layer, 2 (7]
SO-1,6,7 inputs, and 2 outputs.
BL-2 d. Discuss the different data formats that can be used with convolution neural networks. [3]
Q6 a. Explain the architecture of Long-Short-Term Memory (LSTM) networks using a [10]
g ry
Co-4 diagram. Then, use formulas to discuss the critical components of an LSTM unit
SO-1,6,7 (input gate, forget gate, output gate, and cell state).
BL-4
CO-2 b. Write an algorithm for SGD with a moment. List its advantages and disadvantages. [5]
SO-1,6,7
BL-2,1,5 : What role does data augmentation play in enhancing deep learning models? Justify how the
noise injection can contribute to data augmentation. [5]
a. Discuss the advantages and potential challenges of fine-tuning a pre-trained [5]
' p g
Q7 convolutional neural network (CNN) for a new computer vision task, considering
C03 domain adaptation, dataset size, and model complexity.
a Analyze the challenge of exploding and vanishing gradients in Recurrent Neural [5]
CO-4 b. Networks (RNNs) that may arise during their application in language translation
SO-1.6.7 tasks. Identify which network architecture could be leveraged to mitigate this
BL-4_ > problem.
CO-2 : ; —_— :
SO-1.6.7 Cc. Differentiate between Relu and Leaky Relu activation functions. [2]
boo d. Calculate the corresponding softmax values for v=[2.3, 4.5, 3.2] [3]
SO-1,6,7 . . wo. .
BL-3.2 e. Discuss the concept of parameter tying and parameter sharing in a convolution neural
> network. [5]
````

## 2023-24 · Re-Exam · Sem 7 · paper 431e2c24b83f

- Departments: Computer Engineering
- Programmes: MBA TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/MBA TECH/4TH YEAR/COMPUTER/VII SEMESTER/DEEP LEARNING/Deep Learning , Re-exam 2022-23.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 88.4

````text
SVKM’S NMIMS aS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/ an
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024
Program/s: MBA Tech Year: IV Semester: VII

¥

Stream/s: Computer Engineering

Subject: Deep Learning Time: 3 hrs ( © ao m™)
Date:_O2 / [2/2023 No. of Pages:2

Marks: 100 RE- Exim CQ02 a8)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book provided for their use.

1) Question No. _1___ is compulsory.

2) Out of the remaining questions, attempt any 4 __ questions.

3) In all___5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql

Answer briefly:
CO-1;SO- | a, Why deep learning is preferred over machine learning? 5
1,6; BL-4
CO-2; SO- | b. Discuss tiled and stride convolution. 5
1,6 ; BL-3
CO-3;SO- | c. Explain the working of Multilayer Perceptron 5
1; BL-2
0-3; S0- d. Compare batch Gradient descent, Stochastic Gradient Descent, and Mini- 5
1,6; BL-2 batch Gradient Descent.

a. . . . . 1 0

Q Enlist names of the optimizer that uses an adaptive learning rate. Explain
CO-3; SO- the RMS prop with its weight updating process.
1,6;BL-2 ,

Explain the working of the basic RNN architecture. Discuss its limitations,
CO-3;SO- | b. types, and use cases. 10
1,6; BL-3
Q3 a. . ce .. | 10

Discuss the need for Regularization in the deep neural network. Explain in
CO-2; SO- detail the L1 and L2 regularization. {Required mathematical equation}
1,6; BL-1
eae bs Calculate the actual shape, actual size, and the number of training

parameters per layer-wise for the following CNN architecture. 10
--- page 2 ---
Input Layer 240x240x3

Conv Layer k=50, f=8, S=4 oe
Max Pooling 3x3, S=2
Conv Layer k=128, f=5, p=2
Max Pooling 3x3, S=2
Conv Layer k=256, f=3, p=1
Conv Layer k=128, f=3, p=1
Max Pooling 2x2, s=2
FCL 512
FCL 512
Softmax so
4 Write the algorithm for EARY STOPPING / 10
Q -to determine the best amount of time to train
CO-3; SO- -to determine how long it takes to train and retrain all data
1,6; BL-3 -to determine at what object value we start to overfit, then continue till the
CO-1: S0- value is reached.
1,6; BL-2 Explain various challenges in neural network optimization. 10
; : 10
Q5 Explain the architecture of the Inception Model and why you use 1x1
CO-3; SO- convolution in it.
1; BL-4
Apply Standard and Transposed convolution separately to produce
standard and transposed output for the given image and filter size with 10
CO-2; SO- stride=1 and padding =0.
1,6; BL-2 IMAGE
3 4 1 2
| 4 1 2 3 Filter/Kernel
i} i 0
1 2 3 4 zi i 7
2 3 4 1 0 1 o
Q6 Derive the expression for Gradient descent with 2 nodes in input, 1 hidden
CO-2; SO- layer and | output layer. 10
2; BL-4 ; - ;
CO-2; SO- Write the algorithm for Backpropagation in the Deep learning model.
, 10
2; BL-2
Q7 Explain the architecture and working of the Autoencoder model. Give a =
CO-2,3; brief note on its use cases.
SO-1,6;
BL-2 Suppose you are applying a deep learning model on the dataset, but it has
. been observed that the model overfits on training data. Identify the 0
CO-3; SO- . . 1
techniques that can be used to reduce overfitting on training data and
1,6; BL-3

explain them.
````

## 2022-23 · Exam not stated · Sem 7 · paper d08033b7789d

- Departments: Computer Engineering
- Programmes: MBA TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/MBA TECH/4TH YEAR/COMPUTER/VII SEMESTER/DEEP LEARNING/Deep Learning.pdf`
- Printed on paper: max marks: 100
- Text: ocr (2 pages), mean OCR confidence 87.2

````text
i.

MFP STME
LiSRARY

SVKM’S NMIMS m ;
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGIN } ;
Academic Year: 2022-2023
Program: MBATech Year: IV Senter! VII

Stream: Computer Engineering

Subject: Deep Learning Time: _08 hrs @4iooamto 2:00pm)
Date: 14 ]06]2028 No. of Pages: 2

Marks: 100

Special Ret Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: [20]
Lt. * Compare AI, ML and DL. 5
reon b Explain the working of Auto Encoder. 5
SOA) | ¢, | Discuss 3 Activation functions in detail 5
[CO-1,BL- How the noise injection can be considered as data augmentation. Can we 5
2,SO-1] d. add noise at the output layer? {Required Mathematical equations}

C an LBL a Derive the Gradient Descent derivation for a neural network with 1 hidden [10]

4 [ SO-1] ~ layer, 2 inputs, and 2 outputs.

[CO-1,BL- | b. , ; ae [10]
2,S0-1] Explain various challenges in neural network optimization.
Q3 a. .
[CO-3,BL- Explain the working of the basic RNN architecture. Discuss its limitations, [10]
2,SO-1] types, and use cases.
[CO-1,BL- | b. Explain the architecture of the Inception Model and why do you use 1x1 [10]
2,S0-1] convolution in it?
--- page 2 ---
Q4 a.

[CO-1,BL- Discuss the need for Regularization in the deep neural network. Explain in | [10]
2,SO-1] detail the L1 and L2 regularization. {Required mathematical equation}
[CO-1,BL-
2,SO-1] b. What is the effect of ADAM optimizer over RMS Prop {Algorithm} [10]
a Calculate the actual shape, actual size, and the number of training [10]:
parameters per layer-wise for the following CNN architecture.
input Layer 240x240x3
Q5 Conv Layer k=50, f=8, S=4
[CO-2,BL- Max Pooling 3x3, S=2
6,SO-1] Conv Layer k=128, f=5, p=2
Max Pooling 3x3, S=2
Conv Layer k=256, f=3, p=1
Conv Layer k=128, f=3, p=1
[CO-1,BL- Max Pooling 2x2, s=2Z
5 SO-1] FOL 512
> FCL 512
Softmax 50 [10]
b. Explain the architecture of the UNet model and discuss its applications.
6 a. Apply Standard and Transposed convolution separately to produce
[CO-2,BL- standard and transposed output for the given image and filter size with
3,80- 1] stride=2 and padding =1. [10]
IMAGE
4 3 2 1 Filter/Kernel
1 4 3 2 0 1 0
2 1 4 3 1 2 a
3 2 1 4 0 1 0
b. Write the algorithm for EARY STOPPING
a -to determine the best amount of time to train [10]
BOT] -to determine how long to train and retrain all data
-to determine at what object value we start to overfit, then continue till the
value is reached.
Q7 “ . . . .
[CO-1,BL- Discuss the variants of the Convolution operation [10]
2,SO-1]
[CO-1,BL- Li Explain the architecture and working of the GAN model. Discuss the loss _| [10]
2,SO0-1] incurred in the generator and discriminator. Give a brief note on its use

cases
````

## 2022-23 · Exam not stated · Sem 8 · paper 83c59453fffe

- Departments: Electronics and Telecommunication
- Programmes: MBA TECH / EXTC
- Source: `02_Question_Papers/Legacy/MBA TECH/4TH YEAR/EXTC/VIII SEMESTER/DEEP LEARNING/Deep Learning (DE-IV).pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 85.0

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2022-2023 ;
Program/s: MBA.Tech Year: 4th ~~ Semester: VIII

Stream/s ; EXTC

Subject: Deep Learning (DE-IV) Time: 3 hrs (LO0(Odamto 1:00 pr
Date:_0% Muley 2023 No. of Pages: 3

Marks: 100

Re+Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1__ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) Inall___5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

os Answer briefly: [4x5=20]
o ri SO-1; | a. Compare leave one out cross validation and k-fold cross validation. [4]
7 hy SO-1; | b. Analyze XOR and XNOR gate using a simple perceptron. [4]
oa The feature map after applying 3 x 3 kernel/mask is given below.
342/515
Cc 1}i1 yi 41
7 3/3 }1 {2
CO-2; 80-1; 2/2]3 1/3 [4]
Solve for
(i) Max pooling with 2x 2
(ii) Min pooling with 2x2
(iii) | Average Pooling with 2 x 2
(iv) Sum pooling 2x2
a! SO-1; | d. Explain Bidirectional RNN in brief. [4]
ar SO-1; |e Explain various types of activation functions in neural network. {4]
--- page 2 ---
Q2 CO-2; a.

SO-1; BL-2 Explain the architecture of ALEXNET in detail. [10]
b. Differentiate between the following optimizers.
CO-1; SO-1: (i) Gradient and Stochastic Gradient Descent
Bit (ii) Mini Batch GD and AdaGrad HO]
Q3 a. Explain Feed forward algorithm and back propagation algorithm in neural
ao 80-1; . network with an example. ia
C0-1;$0-1; | b. (#) Explain why there is a need of regularization in deep neura! network. [5]
BL-2 Wy Explain parameter norm penalties in regularization of neural network. [5]
oes sok a. (i) Discuss image classification application using deep learning. [5]
BL-6 (ii) Discuss recurrent neural network in brief. What can be the limitations of (5)
CO-3; SO-1; RNN?
BL-6
CO-3; SO-1; | b, P se 3 . : 5
ar Explain Bi-Directional Long Short Term Memory with suitable neat diagram. [10]
a. You have designed a convolutional neural network (CNN). The specifications
of each layer are represented in the following table. The notation is as follows:
CNN (s, n): denotes a CNN layer with n filters of size s
Pooling (s): denotes a pooling layer with size s
FC (n): denotes a fully-connected layer with n output neurons
Given padding=0 and stride=1 wherever applicable.
The input image is a color image with shape of 256 x 256 x 3. Determine the
— shape for the output of each layer, the number of weights and biases for each
0-2: $O-1: layer and the total number of parameters required to train the network. [10]
BL-5
Layer Activation map | Number of Number of
size weights biases
Input 256 X 256 X 3 0 0
Conv(7, 16)
Conv(11,32)
Pooling(2)

Conv(21,64)
--- page 3 ---
Pooling(2)

Conv(5,64)
Pooling(2)
FC(120)
FC(4)
CO-3; SO-1; ' a . : se : ‘
_ b. Discuss the application of time series prediction using deep learning. [10]
Q6 a. Discuss Encoder decoder sequence to sequence architecture.
CO-3; SO-1; [10]
BL-6 .
vo b. Explain the following with respect to Convolutional neural network.
(i) Receptive field
CO-2; SO-1; (ii) Pooling “Valid” and Pooling “Same” [10]
BL-2 (iii) Stride
(iv) Flattening
(v) Fully connected layer
a. (i) Explain why RELU activation is used in the hidden layers of neural network [5]
Q7
CO-1; SO-1; in comparison to other activation function.
BL-2 a x . co P 7
CO-2; $O-1; (ii) Explain parameter estimation in convolutional neural network with [5]
Ble example.
0-1: $0-1: b. (i) Explain overfitting and under fitting in neural networks and how it can be [5]
BL-2 removed.
CO-1; SO-1;
pe (ii)Explain the significance of early stopping and dropout. [5]
````

## 2022-23 · Exam not stated · Sem 8 · paper ff7f17bfbed6

- Departments: Electronics and Telecommunication
- Programmes: MBA TECH / EXTC
- Source: `02_Question_Papers/Legacy/MBA TECH/4TH YEAR/EXTC/VIII SEMESTER/DEEP LEARNING/Deep Learning (DE-IV)_ff7f17bfbe.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 84.9

````text
SVKM’S NMIMS NG WN

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERIN(
Academic Year: 2022-2023

Program/s: MBA.Tech Year: 4 — Semester: VIII
Stream/s ; EXTC

Subject: Deep Learning (DE-IV) Time: 3 hrs (L0:00amto 1:00pm)
Date: 28 /Ap4! 2023 No. of Pages: 3 _

Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

(> 2) Out of remaining questions, attempt any__4 _ questions.
3) In all__5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
Ql -
Answer briefly: : [4x5=20]
Pe SO-1; | a. Compare Lasso and Ridge Regularization. (4]
oy SO-1; | b. Explain early stopping and dropout in neural networks. [4]
c. The feature map after applying 3 x 3 kernel/mask is given below.
3. }2|)5 1/5
oO 4|[2/2/4
3/3 |1 42
CO- 2; SO-1; 2 {2 13 3 [4]
BL-3
Solve for
(i) Max pooling with 2x 2
(ii) Min pooling with 2x2
(iii) Average Pooling with 2 x 2
(iv) Sum pooling 2x2
a > SO-1; | d. Explain Recurrent Neural Network with example. [4]

i]s
--- page 2 ---
Explain the problem of vanishing and exploding gradients. How it can be

CO-1; SO-1; [4]
BL-2 avoided?
Q2 a.
CO-1; SO-1: (i) Explain Bias and Variance trade-off. [5]
_ _ $0-1: (ii) Explain capacity, under fitting, and overfitting in machine learning. [5]
BL- 2 :
ae SO-1; | b. Explain five types of optimizers with advantages and limitations. [10]
a. For the given neural network, solve for the updated weights and biases for the
hidden layer and the output layer using back propagation algorithm.
0.05
0.01
Q3 ~
CO-2; SO-1; . [14]
BL-3
0-10
0.99
1 =. oO: a 5
b 2c 0: 6 0)
CO-1; SO-1; | b. : 2 , <4
BLD Explain various techniques for regularization in deep learning. [6]
Q4 a.
CO-3; SO-1; (i) Discuss Machine translation application using deep learning. (5]
BL-6
00-3: $0-1: (ii) Discuss the advantage of using bidirectional RNN over simple RNN. (5]
BL6
CO-3;SO-1; | b. é : : .
BES Explain Long Short Term Memory with suitable neat diagram. [10] ~~
Qs a. Explain VGG-16 CNN architecture. Also determine the number of trainable
CO-2; SO-1; parameters at each convolutional layer, the feature map shape and size and the [10]
Bless total number of parameters for the given network
CO-3;SO-1; | b. : er : : or . .
BLS Discuss the application of time series prediction using deep learning. [10]
Q6 a. Discuss Encoder decoder sequence to sequence architecture.
CO-3; SO-1; {10]
BL-6
CO-2; SO-1; ' ,
-— i Compare LENET,ALEXNET andgoadlenetnn architectures. [10]
in kon | (i) Explain the role of activation functions in neural networks. {5]

s)3
--- page 3 ---
— (ii) What do you mean by hyperparameters? List a few common [5]
-1; SO-1;

BL-1 hyperparameters which are used in deep neural networks.

oe SO-1; | b. (i) Explain maximum likelihood estimation in machine learning. [5]
CO-1; SO-1; (ii) Explain semi supervised learning and multitask learning. [5]
BL-2

3/2
````

## 2022-23 · Final-Exam · Sem 5 · paper 39d3f520183f

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-V/DEEP LEARNING/Deep Learning, 3rd Year, Sem-V, Year 2022-23, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 19 November 2022
- Text: ocr (5 pages), mean OCR confidence 89.7
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’s NMIMS
H PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /

SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING
Academic Year: 2022-23

Programme: B. Tech (Artificial Intelligence) Year: III Semester: V |
Subject: Deep Learning

Marks: 100
Date: 19 November 2022 Time: 10.00 am - 1.00 pm

Durations: 3 (Hrs)
No. of Pages: _0@5
Final Examination — —
Instructions: Candidates should read carefully the instructions printed on the question paper and
ae on the cover of the Answer Book, which is provided for their use.

1) Question No.1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted. *

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly:

CO-3; | a. | Consider normalized image matrix shown in figure. It is convolved with a 3x3 filter shown | [4]

_ with a stride of 2. Compute the normalized output of convolution. Which features obtained
: from this output?
l~ 0.5 | 0.5 | 0.3 | 0.3 | 0.3
0.5 | 0.5 | 0.3 | 0.3 | 0.3 1 0 7
0.5 | 0.5 | 0.3 | 0.3 | 0.3 1 ar 7
05105 [03 103/03 X fen
0.5 | 0.5 | 0.3 | 0.3 | 0.3
CO-1; | b. | The weights of the two neurons hj and hp of the hidden layer after a particular epoch are 0.55 | [4]
rh and 0.65 respectively. You are implementing gradient descent and observe that the gradients

are gi and gz are +0.3 and -0.25 respectively. Assuming a learning rate of 0.1, determine the
updates in the weights of hi and ho.

fage sm
--- page 2 ---
anh c. | Compare machine learning and deep learning algorithms. [4]
SO-1;
BL-4
CO-2; | d. | Compare Sigmoid and Tanh activation functions. Clearly bring out the advantage of Tanh [4]
80-2; over Sigmoid.
BL-4
CO-4; | e, | A machine learning expert is designing a network for image captioning application. Suggest | [4]
ie a RNN network architecture and sketch the same.
Q2
eH a. | Justify the advantage of Gated Recurrent Unit (GRU) over a normal Recurrent Neural | [10]
ro Network.

—_ Consider that you are designing an application for sequence modelling using (GRU). The

sentence given as input to the network is:

‘The student who did not submit the assignment was bound to loose marks.’ If the highlighted Fan

word ‘was’ is to be predicted, show how the sequence will be handled by showing the output

of memory state and update gate ‘at each time step.
CO-1; | b. | Consider a three-layer neural network with the initial wei ghts as shown in the figure. Sigmoid | [10]
nan activation is used for the neuron in all the layers.

Feature 1
Feature 2
Feature 3

The following data is given to the network:

A
| Input samples | Feature 1 Feature 2 | Feature 3 | Class

1 0.3 0.2 0.4 0

2 0.5 0.6 0.8 1

Based on the network and the data samples, calculate the following:
I. Predicted output for each input samples.
2. Average mean square error.

3. Assuming a learning rate of 0.2, compute the updates in the 2 weights of hidden layer
se to output layer after first backward pass.
--- page 3 ---
Q3

CO-2; | a. | Discuss the concept of bias-variance trade off. Under what conditions is model said to be | [10]
SO-2; under-fitting and overfitting?
BL-4 An application of classifying the products manufactured in an industry into four grades (grade
1, grade 2, grade 3 and reject) based on the four different texture features. A deep neural
network is to be used for the same.
1. Select and justify the use of an appropriate loss function and output activation for
this network.
2. After training, the network has an error of 15% on the training data and 18% on the
validation data. Identify the issue and suggest a solution for the same.
CO-3; | b. | Compute the total number of trainable parameters for the LeNet-5 network shown in the | [10]
ie figure below. The network is used to classify the ten hand written digits from 0 to 9 using a
Softmax classifier at the output layer.
Layer o
Digit image
Pail
vO-3; | a. | For the part of the inception block shown below, the input feature map is of size 28x28x192. | [10]
Pair It is first convolved using 16 filters of size 1x1, which is further convolved using 32 filters of

size 5x5. Compute the number of computations required. Justify the significance of the 1x1
convolution in inception networks.

(age 3]

Ss
--- page 4 ---
oo oo

TONY CONV,
lek Sw 4,
i, meme <=
Pein di 24 ENE Sy ag

iia tn ee

CO-2; Consider a 4-layer deep neural network architecture having five neurons in the hidden layer | [101
a 1, five neurons in the hidden layer 2 which is being trained using back propagation using )
° Adagrad optimizer. The input samples to this network are 6 dimensional vectors and the
dataset is a classification dataset having four different classes. Assume that there are no
weights or biases to the input layer. Sketch the neural network architecture and answer the
following:
1. Identify and explain the different parameters which will have to updated and trained
during the training process.
2. What are the hyper parameters for this network which need to be optimized during
the training process?
Q5
CO-4; Develop a model for Recurrent neural network (RNN) with hidden states and show how back | [10]
. propagation is used for updating the gradients of RNN.
CO-2; Identify and explain the different optimization challenges in deep learning. Justify the | [10]
i advantage of momentum based gradient descent optimizer over mini batch gradient descent
| optimizer.
Q6 “\
You have designed an application for image classification using Convolutional Neural | [10]
CO-3; Networks (CNN). The performance of the network is not good and you identify the reason to
a be vanishing gradients. Indicate and explain how you can solve the vanishing gradient
problem in CNN.
CO-2; An application for the task of classifying the clothes in a Pantaloons’ outlet is to be [10]
nae developed. Consider the dataset and the parameters as given below:

Sr. No. | Parameter Values

1 No. of available data samples | 250000

2 Dimension of data samples | 6
3 Number of output classes 6 (types of women’s apparel)
4 Number of hidden layers 2
--- page 5 ---
Design and draw the Deep neural network. Answer the following:

1. How would you split the data set? (train, validate and test).

2. What can be the activation function of each hidden layer and the output layer?

3. Which loss function is best suited for this application?

4. Initially your training error is 15% and your validation error is 20%. What would you
do?

5. After you correct the errors in training error is now 1% and validation error is 1.5%.

6. Next when you test it on test data, you observe that the test error is 15%. What can be
the possible solution?

Q7

A C03: a. | Show with the help of an example how LSTM can handle long sequences for a language | [10]
: i. modelling application.

CO-1; | b. | Justify the statement, ‘Single-Layer Percpetrons cannot classify non-linearly separable data | [10]

rd : points’, with the help of an example. Suggest a solution for this.

x
Om
() ane S | g
````

## 2022-23 · Final-Exam · Sem 8 · paper bdcafc4e00d8

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/COMPUTER/Sem_08/DEEP LEARNING/Deep Learning, Sem-VIII, Year 2022-23, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 90.2
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS oN
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT®&*
Academic Year: 2022-2023

Program: BTech Year: [V Semester: VIII

Stream: Computer Engineering

Subject: Deep Learning Time: 03 hrs Gotooamto4!oo pm )
Date: 25]04 | 2023 No. of Pages: 3

Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

>
2) Out of remaining questions, attempt any __4 _ questions.
3) Inall___5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
Qi Answer briefly: [20]
Ico acrid a Why do we need Deep Learning and explain its three limitations? 5
, SO-
b.
yy )
a
- | (CO-2,BL- 5
4,SO-1]
Consider the above 2 hidden layers neural network
a. What is the shape of W"]
b. What is the shape of W?!
c. What is the shape of W°!
d. If we add biases to hidden layer neurons what is the shape of b!!]
e. If we add biases to hidden layer neurons what is the shape of b?!
[CO-2,BL- | c. How the noise injection can be considered as data augmentation. Can we add noise at the 5
2,SO-1] output layer? {Required Mathematical equations}
[CO-1,BL- | d. ; ; ; : ;
Discuss the variants of basic convolution functions. 5
2,SO-1]
Q2. a. ; [10]
Apply Standard and Transposed convolution separately to produce standard and
3,SO-1] transposed output for the given image and filter size with stride=2 and padding =1.
.SO-
--- page 2 ---
3 4 1 2
4 1 2 3 Filter/Kernel
0 1 0
1 2 3 4 "4 5 "a
2 3 4 1 0 1 0
. . yom ‘ p [10]
[CO2,BL- b. What is the importance of regularization in deep learning? Explain L1 and L2 :
2 SO-1] regularization. Give the advantage of L1 regularization over L2 regularization. {Required
? Mathematical equations}
a. _ | Below is a diagram of a small convolutional neural network that converts a 13x13 image
into 4 output values. The network has the following layers/operations from input to
Q3 output: convolution with 3 filters, max pooling, ReLu, and finally a fully-connected layer.
en For this network, we will not be using any bias/offset parameters [10] ,
i :
13x13 3@10x10 >
Convolution Max Pooling Fuilly-
3 Filters 4x4 2x2 Connected
Stride 1 Stride 2
How many weights in the convolutional layer do we need to learn?
How many ReLu operations are performed on the forward pass?
How many weights do we need to learn for the entire network?
In the above diagram if we change the filter size of the convolutional layer to 3x3 what
will be the output shape after the convolutional layer?
[CO2,BL- Suppose you are applying a deep learning model on the dataset, but it has been observed [10]
3,S0-1] b. that the model overfits on training data. Identify the techniques which can be used to
reduce overfitting on training data and explain them.
Q4 a. A machine learning engineer has to design an application for medical image analysis. The [10] _
[CO-3,BL- dataset includes MRI images of brain tumors and wants to classify them into Metastatic,
4,SO-1] Meningioma, Glioblastoma, and Astrocytoma.
i)Which Deep learning model is best suited for this task? Why this model?
ii)Design and draw the suitable deep learning model diagram
iii) What can be the activation function of each layer?
iv)Which loss function is best suited for this application?
v)If our dataset is having less number of images then what would you do?
vi)If your model is giving less error on training data and high error on testing data what
[CO-1,BL- are the possible solutions?
2,SO-1]
b. How do you differentiate Adam from RMSProp optimizer?.{Agorithm} [10]
Q5 a. Consider neural network as shown in the figure. [10]
[CO2,BL- The input x1=1,x2=4,x3=5 and the initial weights and biases are shown in the figure, The
5,SO-1] actual output are [0.1, 0.05] for the two output neurons. The activation used is sigmoid.

Calculate the following:
1. Predicted output after forward propagation.
2. Mean square error after the first forward pass

3. Assume learning rate of 0.01 and update the weight w7 by performing backward pass
--- page 3 ---
bi=0.S b2=0.5

[CO-3,BL- | b. Explain the architecture and working of the GAN model. Discuss the loss incurred in the [10]
2,SO-1] generator and discriminator. Give a brief note on its use cases.
Q6 a. Explain the working of the basic RNN architecture. Discuss its limitations, types, and use | [10]
[CO-3,BL- cases.
2,SO-1]
Calculate the actual shape, actual size, and the number of training parameters per layer-
b. wise for the following CNN architecture.

Input Layer 240x240x3

Conv Layer k=50, f=8, S=4

Max Pooling 3x3, S=2

Conv Layer k=128, f=5, p=2

Max Pooling 3x3, S=2
[CO-2,BL- Conv Layer k=256, f=3, p=1 [10]
6,SO-1 Conv Layer k=128, f=3, p=1

Max Pooling 2x2, s=2

FCL 512

FECL 512

Softmax 50
igen BL- a: Describe in detail Tanh, Sigmoid, Relu, Leaky Relu activation function with its [10]
1,S0-1] properties, equations and suitable graphs also give its advantages and disadvantages.
ye a Dp: Explain the different preprocessing steps in NL. Give one application where NLP can be

used. [10]
````

## 2022-23 · Final-Exam · Sem 8 · paper 32dbc484cda0

- Departments: Information Technology
- Programmes: B TECH / IT, MBA TECH / I T
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/IT/VIII SEMESTER/DEEP LEARNING/Deep Learning, Sem-VIII, Year 2022-23, Final Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 86.6

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT&
Academic Year: 2022-2023

Program: Btech / Mbatech; Information Technology Year: [V Semester: VII
Subject: Deep Learning Time: 03 hrs

(lo:ooamto 1:00 pm)
Date:_02 /05/2023 . No. of Pages:02
Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper
and on the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) Inall___5_ questions to be attempted.

4) All questions carry equal marks. ‘
5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary.

Qi “hy [20=
Answer briefly:
5M*4]
a. Draw neural networks for Boolean XOR Gate with number of input neurons,
CO-1 ; SO- output neuron and their weights. Do we need bias and activation function to [1+1+2+1]
2; BL-3
design them? Justify.
CO-3;SO- | b. Discuss GloVe embeddings. [5]
2; BL- 1
c.
1
fw,2) = eT
CO-2 ; SO- (5]
2; BL-3 Wo =2, Xo = -1, Wi = -3,W2= 5, x1 = -2. Draw DAG for above equation and find
upstream and downstream gradient.
d. Suppose you have an input image of size 256x256x1 and a filter of size 7x7x1
CO-3 ; SO- with stride 1 and no padding. If average pooling is applied with a window size of | [5]
2;BL-2
3x3 and stride 2, what is the size of the output volume?
a.
NZ
Q2
CO-1; SO- [5]
2; BL-3

O=W@O@xeYezZz

Design a minimal neural network for above Boolean expression. How many

total perceptrons you need for the network and justify.
--- page 2 ---
\

. b. What is transfer learning; How it is used in deep learning. Discuss architecture
CO- 3; SO- [4+8+3]
2; BL-2 of VGG16 and how the architecture can be used in transfer learning.
a.
2/}1/7/1)2|5
5}0;3/4/1)2
1|/7/8|3)/3)0
Qs 0;3;2/0;1/1
6/2)5/3|0)3
CO-1; SO- [8]
stad 3/6|0/2\/1]\0
a) What will be output of above matrix, if Max pooling layer is applied given
stride is 2X2
b) What will be output of of above matrix, if Mean/Average pooling layer is
applied given stride is 2X2
- b. What are Generative Adversarial Networks (GANs). Discuss any one type of
CO-3 ; SO- [10]
2; BL-2 GAN architecture applied to solving a problem.
Q4 a.
CO-2 ; SO- Explain Back propagation with its algorithm. . [10]
; BL-2
CO-3 ; SO- | b. What are attention models and how they are used in computer vision tasks. (10)
; BL-2
5
Q e What is the exploding and vanishing gradient problem in RNNs and how can it
CO-3 ; $O2- b (10]
-BL3 e addressed.
CO-2;S0-2 | b. What are bidirectional RNNs and how they can be used in implementing a
(5+5]
; BL-3 question answer chatbot.
Q6 a. Explain the concept of convolution and its role in RESNETSO architecture. How
CO- 3; SO-2 it can be used in Image captioning. What kind of Image pre processing is [10]
; BL-3 required for training images using CNN.
b. You are selling laptops through online web sites. How will you implement an
CO- 1; SO-2
ar opinion Mining application. Discuss the steps and propose an architecture for {10]
: the application.
[20= 5M
Q7 Answer Any four al
CO-3 ;SO-2 | a.
-BL2 Lenet-5 architecture and drawback of the architecture
CO-3 ; SO-2 | b. . . a
BLD Gradient Descent, stochastic GD and minibatch GD
CO-2 ; SO-2 | ¢.
Autoencoder Architecture
; BL-2
CO-1;SO- [| d. ;
Continuous Bag-of words model (CBOW)
2; BL-2
CO-2 ; SO- e A
5e8t-2 Challenges with CNN deep neural network

Wd
````

## 2022-23 · Final-Exam · Sem 2 · paper 34f8817101d9

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENT
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ARTIFICIAL INTELLIGENT/SEM II/DEEP LEARNING/Deep Learning Batch 2022-23 Final0001.pdf`
- Printed on paper: max marks: 100
- Text: ocr (1 page), mean OCR confidence 93.2

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2022-2023

Program/s: M Tech
Stream/s : Artificial Intelligence
Subject: Deep Learning
Date:_28 / 04 / 2023
Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Assume Suitabie data if necessary.

Q1. Apply the deep learning concept and train any one of the following model

Dataset 1 —- MNIST
from keras.datsets import mnist

data = mnist.load_data()

Dataset 2 — Pima Indians Diabetes

Dataset 3 — Fasion mnist

tf.keras.datasets.fashion_mnist.load_data()

Each training and test example is assigned to one of the following labels:
0 T-shirt/top

1 Trouser

2 Pullover

3 Dress

4 Coat

5 Sandal

6 Shirt
````

## 2022-23 · Final-Exam · Sem 3 · paper 2438318cee35

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCES FALL BACH
- Source: `02_Question_Papers/Legacy/M TECH/2ND YEAR/DATA SCIENCES FALL BACH/SEM III/DEEP LEARNING/Deep Learning Batch 2022 Final0001.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 22 November 2022
- Text: ocr (4 pages), mean OCR confidence 90.8

````text
T ; SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT &

SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINE!

Academic Year: 2022-23
Programme: M. Tech (Data Science) “ : Year: II Semester: III

! Subject: Deep Learning -
Marks: 100 -
Date: 22 November 2022 ~- Time: 2.00 pm - 5.00 pm |
Durations: 3 (Hrs)

No. of Pages: _o¥
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. | is compulsory.

> 2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page. °
6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Q.1 a. Suppose you are training deep learning model for handwritten digit images and notice underfitting, 5
hence you decide to add data augmentation as part of your preprocessing pipeline. For each below
augmentation techniques, state whether the technique is appropriate or not for the model. If not,
explain why not?

i. Scaling
ii. Flipping (vertically or horizontally)
iii. Rotating 90 or 180 degree
iv. Shearing
v. Zooming 50%

b. Why transfer learning is important? Explain any four advantages of transfer learning. 5
>
¢. Convert the following comma separated sentences into post padded sequences based on the longest 5
sentence,
Sentiment Sentences

This is an excellent movie, It was a wonderful movie, You should

Bopitive Reviews watch this brilliant movie, Exceptionally good movie

Horrible acting, I did not like the movie, I will not recommend you this

Negative Review . : : :
gm ews movie, Pathetic and boring movie

Assuming embedding dimension as 4 how values will be allocated to each vocabulary keeping the
sentiment column into consideration? Explain with an example.

d. With the help of the diagram and mathematical function, explain the working of single-layer neural 5
network.

Page | of 4
--- page 2 ---
Q.2 a. Derive Adam optimizer with proper notations.
b. Compute the value of Y1 and Y2 for the following neural network,
Wwo=l
Weight
Weight Mat zs 2 Z7
Matrix 7! 72 23 24 tax?
Zi 1 1 0
xt I o +l 0
22 1 1 1
X2 1 1 1 0
Zz 1 0 1
x3 0 o - ©
“a 1 1 0
Weight
Matrix 3 YI Y2
Zs ( 1 1
- 2) 1 0
ReLU ReLU Softmax
Zz 1 0

Q.3 a. Consider the following CNN for binary classification, compute the shape of the output volume
dimension and number of parameters at each layer. Activation shape format (H, W, C) for height,
width, and channel respectively, no padding applied,

Layer Volume Dimension Number of parameters
Input 256 x 256 x 3 0
CONV2D
filters = 64, stride = 1,
kernel size = 3x3
POOL2D
kernel size = 2, stride = 2
CONV2D
filters = 32, stride = 1,
kernel size = 3x3

POOL2D

kernel size = 2, stride = 2
CONV2D

filters = 16, stride = 1, 4624
kernel size = 3x3

POOL2D

kernel size = 2, stride = 2
FLATTEN

Fully Connected Dense

units = 24

Output Dense, 1

b. Explain the concept of convolution and pooling with an example. Convolution neural network
model consume less memory than fully connected dense neural network for image classification
problem, justify the statement with an example.

Page 2 of 4

10

10

10

10

>
--- page 3 ---
Q.4 a. Draw single unit LSTM highlighting important information such as gates, hidden state, cell state, 10
and activation functions. Define and write down the formula with proper notation for,
i. Forget gate
ii. Input gate
iii. | Output gate

Why sigmoid and hyperbolic tangent activation functions are used in LSTM?

b. Calculate the total parameters of the following sequence modeling networks, 10
Network 1 — NLP model Network 2 - Forecasting Model
Layer j Layer
Embedding (Input) Input
@ . vocab size = 6150 time window = 30 days
embedding dimension = 4 n features = 5
input length = 15
Simple RNN pes ie

: its = =T
units = 100, return = True units = 64, return rue

Simple RNN Batch Normalization
units = 50 LSTM

Dense units = 32

units = 24 Dense

Output Dense units = 1 ‘| units = 16

Output Dense units = 1

Q.5 a. What is mini-batch gradient descent? How it is different from gradient descent? Write an algorithm 10
for gradient descent.

b. Draw and simplify single unit of RNN of time steps t = 4, with proper notation indicating forward 10
and backward pass. Write down the formula to update the information of hidden state and output

state.

Estimate the value of yhat for 2 RNN units where,

X=[1 2 3] Wx=[3 -4] Wa=[4, 3] wy=[5') by=0 by=11 ho=0
—3 2 2
Q.6 a. Youare training the CNN model to classify five different cat breeds, 10
i. | What loss function you will use? Write down the formula of the loss function.

ii. | What will be the output activation function? Write down the formula of the function, use
proper notation.

ili. | You found pre-trained model on dog vs cat data, and it performs very well thus you want
to use transfer learning to build your own model. Explain what additional hyperparameters
you will need to tune.

b. Elaborate five applications of deep learning with recent development. 10

Page 3 of 4
--- page 4 ---
Q.7

a. LSTM model outperforms RNN model, justify the statement with the help of the gradient issues.

b. Apply convolution on Matrix B with Filter F,

Matrix B Stride: 1
1 1 1 0 0 1 Filter F
1 1 0 0 0 1 0 1 0
1 1 1 0 0 1 1 -4 ]
1 1 0 0 0 1 0 1 0

e. Write a short note on variational autoencoder.
d. Explain the concept of bounding boxes in object detection with an example.

e. Why backpropagation is required in neural network? Explain how it works with an example.

Page 4 of 4

4
````

## 2022-23 · Re-Exam · Sem 5 · paper 6879e8b34cc8

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-V/DEEP LEARNING/Deep Learning, 3rd Year, Sem-V, Year 2022-23, Re-Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 January 2023
- Text: ocr (4 pages), mean OCR confidence 89.9

````text
/

vo 1) Question No.1 is compulsory.

SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING /
SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING
Program: B. Tech (Artificial Intelligence) . Year: II]. | Semester : V
AcademicY ear: 2022-2023

Subject: Deep Learning -
Marks: 100

Time: 10.00 am - 1.00 pm

Durations: 3 (Hrs)

No. of Pages: 4
Re-Examination (2022-23)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

Date : 28 January 2023

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

/

Ql Answer briefly:

CO-4; | a. A music enthusiast is trying to create a network for synthesizing a tune. Suggest a RNN network | [4]
80-1; architecture for him and sketch the architecture.

BL-4
CO-3; | b. | Consider the output of convolution as shown in figure, [4]
SO-1;
BL-3 1 |2 3 215
5 |3 4 6 13
L 7/4 [8 [5 [9
8 | 5 10 |4 42
9 }10 |3 4 |3
A 3X3 average pooling with a stride of 2 is applied to this feature map.
1. Determine the output of the pooling layer.
2. Justify the purpose of the pooling layer ina CNN.
CO-1; | c. | Bring out the advantages and limitations of deep learning. [4]
SO-1;
BL-2

CO-2; | d. | A machine learning expert is using mini batch gradient descent for training the network. Evaluate | [4]

an the effect of batch size on the optimization and the use of parallel processing.

fa)
faqge ‘WG
~~
--- page 2 ---
CO-1; | e, | For the following input output sequence, design a perceptron network. You may use layers, | [4]
SO-2; perceptrons in each layer and weights of your choice.

Blea X1 |X2 | Output
0 0 0
i 0 0
0 1 0
1 i 1
Q2

CO-3; | a. | Consider a convolutional network architecture having convolutional, pooling, fully connected and [10]
eh output layers, which is being trained using back propagation using Adam optimizer. The input a
: samples to this network are images of size 127x127 and the dataset is a classification dataset
having five different classes.
1. Identify and explain the different parameters which will have to updated and trained
during the training process.
2. What are the hyper parameters for this network which need to be optimized during the
training process?

CO-2; | b. | Justify the use of Relu activation for deep neural networks as against Sigmoid or Tanh for a deep | [10]
SO-2; neural network.

BEY An application of predicting the rating of different brands on a scale of 10, based on the features
extracted through a survey uses a deep neural network.
1. Select and justify the use of an appropriate loss function and output activation for this
network.
2. After training, the network has an error of 2% on the training data and 18% on the
validation data. Identify the issue and suggest a solution for the same.
Q3
CO-4; | a, | A recurrent neural network is being used for language modelling application. Identify and write | [1>
Ae the steps for the same for building and training the model. The input to the network is “Mumbai

is the financial capital of Maharashtra.”

Draw the network architecture and show the conditional probabilities that will be predicted at
each time step.

Page 7/4
--- page 3 ---
CO-1;

b. [10]
SO-1;
BL-3
The input vector of [0.5, 0.7, 0.8] is applied to a neural network, which has been initialized by the
€ initial weights as depicted on the arrows. The actual output for the inputs are [0, 1] for the two
output neurons. The activation used is relu for the first and second layer, whereas sigmoid for the
output layer. Determine the following:
1. Predicted output after forward propagation.
2. Mean square error after the first forward pass :
3. Assuming a learning rate of 0.1, the updates in the four weights of the hidden layer to the
output layer first backward pass.
Q4
CO-3; | a. | You have been given the task of designing an application of recording employee attendance based | [10]
oi on face recognition. You are planning to use convolution neural network for the application but
° the dataset you have is very small and will not be sufficient for training a convolutional neural
network. And explain different solutions for this purpose.
— b. | For the CNN architecture shown in the figure, estimate the number of number of parameters [10]
BL-3
AlexNet
an MAX-POOL, MAX-POOL

— — —> —
xi ~ 3x3 5x5 3x3
Bos=d4 s=2 same s=2

PSS Re 55x55 x 96 27x27 x96 27x27 X256 13x13 x256
227x227 x3 QC
MAX-POOL ee Fe
— — — — = —+| | }./-0
ae 3x3 3x3 axe Softmax
= ° O 1000
13x13 x384 13x13 x384 13x13 x256 6x6 x256 9216 4096 4096

Page 3y
--- page 4 ---
Q5

CO-4; | a. | You are using a Recurrent Neural Network (RNN) for sequence modelling application and | [10]
7 observe that the network performance does not improve after training. You identify that the reason
: for this is that the parameters are not updated due to vanishing gradients.
1. Suggest a solution to solve this problem.
2. What are the changes required in the architecture to improve the performance?

CO-2; | b. | Justify the need for adding multiple layers in an artificial neural network. [10]

ie An application for classification of transactions into fraudulent and non-fraudulent is desired. The
: dataset has 10,000 samples and each sample is 4-dimesnional.
1. Design a deep neural network. Assume suitable number of layers and number of neurons.
2. Calculate the number of parameters for this network.
Q6

CO-2; | a. | Suggest and justify a solution for the following scenarios during the process of optimization of | [10]
ie the hyper parameters of a neural network. iv"
1. In spite of training for a number of epochs, the loss function does not minimize.

2. You observe that the gradients are very noisy and thus the loss oscillates.
3. You observe that the loss decreases to a certain extent and then increases., i.e. you miss

the minima.

CO-3; |b. | For the convolution block shown in the figure below, calculate the number of computations | [10]

pie required. What would be the effective computations if the 5x5 convolution is preceded by a 1x1
. convolution block?
v
ee
CONV
5x 5,
Same,
32 28 x 28 x 32
28 x 28 x 192
Q7
CO-4; | a. | ‘XYZ was very brave soldier. He was a part of the Kargil war and laid down his life fighting | [10]
wD li against the enemy. The president of India honored patriotic... >

_Considering an LSTM network, show how this sequence can be processed. Justify the need for
the different gates in LSTM.

CO-2; | b. | Youare training a deep neural network and the performance of the network is good on the training | [10]
ee data but degrades when you test it on the unseen data. Identify the reason for this. Suggest and
: explain different techniques which can be used for improving the performance on the unseen data.

fag e 4]
````

## 2022-23 · Re-Exam · Sem 8 · paper 873392690773

- Departments: Electronics and Telecommunication
- Programmes: B TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/EXTC/Sem_08/DEEP LEARNING/Deep Learning, Sem-VIII, Batch 2021-22, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 fia 23
- Text: ocr (3 pages), mean OCR confidence 91.2

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2022-2023

Program: B Tech Stream :EXTC Year: IV Semester: VIII
Subject: Deep Learning Time: 3 hrs @0:00amto 1:00pm)
Date: 01 fia 23. No. of Pages: 3

Marks: 100

Re Examination (2021-22)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
_-», of the Answer Book, which is provided for their use.

1) Question No.1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly:
CO-1; SO- a.| State the significance of learning rate in a neural network. What are the | [4]
2; consequences of a very small and very large learning rate?
BL-2
CO-1; SO- b. [4]
2; XI X2 =| Y
| BL-3
C 0 0
7 1 0
0 1
1 1

Consider the simple neural network shown in the figure. If the threshold is 2.

Determine the output Y for the input sequences, x1 and x2 as shown in the table.

Page 3
--- page 2 ---
?

CO-2; SO- c.| Compare artificial neural networks and recurrent neural networks. Give one | [4]
1; j

BL-3 example application of each of the two networks.

CO-3; SO- d.| What are the advantages of convolutional neural network over artificial neural | [4]
_ networks for computer vision applications?
CO-3; SO- e. | Consider the output of convolution as shown in figure, [4]
2;
BL-3 1);2/3}4
5|4/7|8
1);3,5|4
8|9/17}7
A 2x2 average pooling with a stride of 2 is applied to this feature map. Determine
the output of the pooling layer.
Q2
CO-3; SO- a.| With the help of an architecture, explain the working of Variational auto-encoder. | [10]
23 What are the applications of this type of auto-encoder?
BL-2
CO-3; SO- b.| Bring out the need of Generative adversarial networks (GANs). Explain in brief | [10]
1; the work of such networks.
BL-2
Q3
| CO-2; SO- a.| An application for image captioning is to be designed. Sketch the architecture of | [10]
>: BL-A the network. State and explain the various parameters of this network.
CO-1; SO- b.| You are trying to optimize the neural network. What are the possible challenges | [10]
23 you may face? Bring out the advantage of momentum based gradient descent
BL-3 over stochastic gradient descent optimization technique.
Q4
CO-1; SO- a. | Explain how error is propagated backwards in the gradient descent algorithm. [10]
oe | TLE Use a three-layer artificial neural network for depicting the process.

Page aE
--- page 3 ---
?

CO-3; SO- b.| Consider the following block from a CNN network. Calculate the number of

2; parameters for the layers shown below:
BL-3
Layer Name Tensor Size
Input Image 227x227x3
Conv-1 55xS55x96
MaxPool-1 27X27x96
Conv-2 27x27x256
MaxPoo!-2 13x13x256
aes Conv-3 13x13x384
Conv-4 13x13x384
Conv-5 13x13x256
Q5
CO-1; SO- a.| Bring out the significance of activation function. What are the different types of | [10]
23 activation functions commonly used in dep learning? State their advantages and
BL-2 disadvantages.
CO-3; SO- b.| Justify the advantage of adding skip connections in a residual network. Compare | [10]
2; the output of a single block of residual network, with and without residual
BL-4 connections.
Q6
a. | What are the different types of recurrent neural networks? Show the sketch of the | [10]
|CO-3; SO- architecture and state the applications of each type.
BL-2
CO-3; SO- b.| With the help of an architecture explain the working of Gated recurrent unit | [10]
1; (GRU). Compare the performance with recurrent neural network.
BL-3
````

## 2022-23 · Re-Exam · Sem 8 · paper 2653c288be9e

- Departments: Electronics and Telecommunication
- Programmes: B TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/EXTC/Sem_08/DEEP LEARNING/Deep Learning, Sem-VIII, Year 2022-23, Batch 2021-22, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 90.3

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2022-2024

Program: B Tech Stream :EXTC Year: IV Semester: VIII
Subject: Deep Learning Time: 3 hrs (49!00amto 4ioopm)
Date:_25 /04/23 . No. of Pages: 3

Marks: 100

Re Examination — Bata 2021-22

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

_
1) Question No.1 is compulsory.
2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
Q1 Answer briefly:
CO-3; SO-1; a.| The weights of the two neurons h; and hz of the hidden layer after a particular | [4]
BL-3 epoch are 0.35 and 0.60 respectively. You are implementing gradient descent and
observe that the gradients are gi and g2 are +0.3 and -0.55 respectively. Assuming
a learning rate of 0.05, determine the updates in the weights of hy and ho.
CO-3; SO-1, b.| For the following input output sequence, design a perceptron network. You may | [4]
BL-3 use a layers, perceptrons in each layer and weights of your choice.
Al A2 Output
0 0 0
1 0 1
0 1 1
1 1 0
_ = SO-1; c.| Compare Sigmoid and Relu activation functions. Clearly bring out the advantage | [4]
BL-3

of Relu over Sigmoid.
--- page 2 ---
ma SO-2; _] A software engineer is working on a project where there are noisy images. Select | [4]
and draw a suitable network architecture to de-noise the images.
wo SO-2; A machine learning expert is designing a network for image captioning application. | [4]
Suggest a RNN network architecture and sketch the same.
Q2
ae SO-2; i. Justify the significance of inception networks. {10]
ii. State the different operations to be performed in a single inception block.
iii. Consider the input to the inception block as an image of size
256x256x128. Draw the architecture of the inception block and show the
image matrix size for each operation.
Pe SO-1, .| With the help of architecture, explain Generative Adversarial Network (GAN) is | [10]
able to generate data samples.
Q3
CO-1; SO-2, An application for person identification based on fingerprint is to be designed. The | [10]
Blea dataset includes the ten print fingerprint images captured from the employees of
the organization, which is small in number to be used for a deep learning model.
Propose a suitable model which can be used for this application.
CO-3; SO-1, With the help of examples explain the concept of underfitting and overfitting. [10]
BLS Explain the significance of the term bias variance trade off in machine learning.
Q4
es SO-2; Justify the need of LSTM for handling long sequences for a language modelling | [10]
application. Compare the performance with RNN.
CO-3; SO-2; .| An application for the task of classifying the grains in a superstore is to be [10]
Bled developed. Consider the dataset and the parameters as given below:
Sr. No. | Parameter Values
1 No. of available data samples | 300000
2 Features considered _ for | 5
~H grains
aa 3 Number of output classes 6 (types of grains)
4 Number of hidden layers 2
--- page 3 ---
Design and draw the Deep neural network. Answer the following:
1. How would you split the data set? (train, validate and test).
2. What can be the activation function of each hidden layer and the output
layer?
3. Which loss function is best suited for this application?

Q5
Ce SO-2; a. | Justify the need for regularization in deep neural networks. What are the different | [10]
-4
types of regularization techniques?
ey SO-2; b.| A deep learning model designed for classifying the types of fruits based on their | [10]
features is to be trained. Identify and explain the algorithm which can be used for
training this model. (forward and back propagation)
roe
a. | For the CNN architecture shown in the figure, estimate the total number of [10]
CO-2; SO-2; parameters:
BL-2
fe_3 fc_4
Fully-Connected Fully-Connected
Neural Network Neural Network
C 1 Conv_2 ivati
Convatition Conecliston = “s Nation ——s
(5x S) kernel Heol (5x 5) kernel 5 i "
valid padding areca valid padding Sa ad dropout
INPUT ni channels ni channels n2 channels n2 channels + : ‘@ 9
i (28 x 28 x1) (24x 24xn1) (12x12 xn) (8x8xn2) (4x4xn2) e” ourpur
3 units
CO-2; SO-1; b. | Consider a convolutional network architecture having convolutional, pooling, fully | [10]
BL-3

connected and output layers, which is being trained using back propagation using
Adam optimizer. The input samples to this network are images of size 127x127
and the dataset is a classification dataset having five different classes.
1. Identify and explain the different parameters which will have to updated
and trained during the training process.
2. What are the hyper parameters for this network which need to be optimized
during the training process?

Page 2] 3
````

## 2022-23 · Re-Exam · Sem 8 · paper 5cab63b7e3bc

- Departments: Information Technology
- Programmes: B TECH / IT, MBA TECH / I T
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/IT/VIII SEMESTER/DEEP LEARNING/Deep Learning, Sem-VIII, Year 2022-23, Re Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 87.1

````text
SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINE
Academic Year: 2022-2023

Program: Btech / Mbatech; Information Technology Year: lV Semester:VIII
Subject: Deep Learning Time: 03 hrs

(do:o0amto_4+o0pro)
Date:_03 /07 /2023 . No. of Pages;02 3
Marks: 100

Re+Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and
on the cover of the Answer Book, which is provided for their use.

1) Question No._1__ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.

3) Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

qi
Answer briefly: [20= 5M*4]
a. Draw neural networks for Boolean OR Gate, AND Gate and NOT
gate with required number of input neurons, output neuron and
CO-1 ; SO-2 [2+2+1+1]
;BL-3 their weights. Do we need bias and activation function to design
them? Justify.
CO-3;SO- | b. Differentiate between LSTM and GRU. [5]
2; BL-1
com
f(z,y,2) =(e+y)2
CO-2 ; SO-2 [5]
; BL-3 x = -2, y = 5, z= -4. Draw DAG for above equation and find
upstream and downstream gradient.
d. Consider an input image of size 32x32x3 and a filter of size 5x5x3
0-3: S0-2 with stride 1 and no padding. if max pooling is applied with a [5]
; BL-2 window size of 2x2 and stride 2, what is the size of the output

volume?

le
--- page 2 ---
x2 -2 -1 -1

+ (3,6) 1
a tn a
yw Si
(2.4)¢ ™ (5,4)
-1 | +a +1
| “1
“1 +1
Q2 - = +1 “1
CO-1; SO-2 (1,0) wa G.0) [10]
; BL-3 . . . .
Design a minimal neural network architecture with hard/step
threshold
Output = -1 if input W1*X1+W2*X2 < T
=1 if input >=T
Also, X1, X2 >= 0
Discuss the architecture of LSTM cell and construct a Deep
CO- 3; SO-2 neural network using LSTM cells. Explain the working for (6+2+2]
; BL-2
predicting the next word for any given part of sentence.
Q3
What are Generative Adversarial Networks (GANs). Discuss any
CO-1; SO-2; (5+2+2+2]
one type of GAN architecture applied to solving a problem.
BL-3
2);1/;7/);1;)2)5
5;0/;3/4;)1)2
1/|7/;8|3);31]0
o;3;2;);0;1)1
CO-3 ; $O-2 6/2/5| 3/9) 3 [3]
;BL-2 3/6}0)/2;1]0
a)What will be output of if Min pooling layer is applied given
stride is 2X2
b) What will be output of if Mean/Average pooling layer is
applied given stride is 2X2
Q4 List and explain the various activation functions used in
CO-2 ; SO- ; modeling of artificial neuron. Also explain their suitability with [10]
BL-2 respect to applications.
CO-3 ; SO-; What are auto encoders and how they are different from
BL-3 Principal components analysis (PCA). Which of these two is [10]

faster.

ee)
--- page 3 ---
Qs

Give an example of learning XOR function to explain a fully

CO-3 ; SO2- [10]
functioning feed forward network.
+ BL-4 i
CO-2 ; SO-2
Discuss GloVe algorithm and how it is used in NLP applications. {10]
; BL-3
Q6
CO- 3; SO-2 Explain in detail about the concept of gradient based learning. [10]
; BL-3
CO- 1; SO-2 Discuss different Types of Sequence Modeling Tasks with their [10]
10
; BL- examples.
[20= 5M
a Answer Any four
*4]
CO-3 ; SO-2
- BL-2 Lenet-5 architecture and drawback of the architecture
CO-3 ; SO-2
Face Recognition Application
; BL-2
CO-2 ; SO-2
Limitations of autoencoders
; BL-2
CO-1 ; SO-
Continuous Skip-Gram Model
2; BL-2
CO-2 ; SO-
Challenges with RNN deep neural network
2; BL-2

313
````

## 2022-23 · Re-Exam · Sem 7 · paper 50a77864e17f

- Departments: Computer Engineering
- Programmes: MBA TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/MBA TECH/4TH YEAR/COMPUTER/VII SEMESTER/DEEP LEARNING/Deep Learning,Re-eam 2022-23.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 February 2023
- Text: ocr (2 pages), mean OCR confidence 86.7

````text
SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING /
SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING
Program: MBA Tech (Computer) Year: IV Semester : VII

AcademicY ear: 2022-2023
Subject: Deep Learning Marks: 100
arks:

Time: 2.00 pm - 5.00 pm
Durations: 3 (Hrs)
No. of Pages: 2

Date : 03 February 2023

Re-Examination (2022-23)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

antennae,

MEO i =,
1) Question No. _1___ is compulsory. Liew . S
2) Out of remaining questions, attempt any __4 __questions. Hx \
3) In all__5_ questions to be attempted. hed ]
4) All questions carry equal marks: \ : }
5) Answer to each new question to be started on a fresh page. \ wo

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: {20}
CO- 1; SO-1 | a.
; Justify the need to add randomness in the weight initialization process. [05]
BL-5
CO- 3;SO- | b. .
6; What Is the Role of Activation Functions in a Neural Network? [05]
BL- 2
CO- 2; SO-1 | c. <
; Explain, why convolution operation is important in CNN. [05]
BL-5
CO- 3;SO- | d.
6; Describe Softmax and ReLU Functions? [05]
BL- 2 :
Q2 Explain working principle of perceptron and its structure. List advantages and 110)
a.
CO-2; SO-1; disadvantages.
BL- 2
CO-3: SO-6: Describe architecture of Inception Network with its advantages and f10]
, "Tb.
BL-2 disadvantages.
Q3 a. Describe what is a ResNet and where would you use it? Why it is efficient as
CO-3:S0-6: compared to normal deep neural networks? [10]
BL- 2
CO-2; SO-1; | b. Illustrate with necessary diagrams, Dropout and Batch Normalization? [10]
BL-2 ry

Page 1 of 2
--- page 2 ---
Q4 a. .
Illustrate what is transfer learning with some real-life examples. Further explain it
CO- 3; SO- in detail with its types. (12]
6;
BL-3
CO-2: SO-1: 7 Write and explain the derivation of the backpropagation training algorithm. (08)
’ , a 08
BL- 3 Explain the role of the learning rate coefficient in its convergence
Q5 = Justify why we have gates in neural networks. Explain the Foregate Gate, Input
CO-4; SO-6; Gate, and Output Gate. [10]
BL- 4
CO-2; SO-1; | b. Illustrate working principle of Auto encoder with its architecture
gP Pp:
BL-3 [10]
a. Consider an ANN with four layers. One input layer, one output layer and two
hidden layers in between. Input layer consists of 6 neurons, hidden layer1
Qs consists of 8 neurons, hidden layer2 consists of 6 neurons and output layer
CO-2; SO-1; ; . . ; . . [10]
BL- 5 consists of 3 neurons. Draw suitable diagram with proper notations,
representing this ANN and calculate the number of trainable parameters at each
layer.
CO-4: 50-6; | - Differentiate between object classification and object detection in computer {10}
; H 1
BL- 4 vision
Q7 a.
CO-4; SO-6; Explain Long Short Term Memory (LSTM) with its architecture [12]
BL- 2
C0-2: 0-1: b. Compare and contrast between Al, Machine Learning, and Deep Learning?
BL- 2 ‘ [08]
Page 2 of 2
````

## 2021-22 · Final-Exam · Sem 6 · paper 1a51bc63944d

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM VI/DEEP LEARNING/B Tech, Data Science, Deep Learning, 3rd Year, Sem-VI, Final Exam, Year 2021-22.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 April 2022
- Text: ocr (1 page), mean OCR confidence 91.1

````text
SVKM’s NMIMS i : ”
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING L J

SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINERTING,

Academic Year: 2021-22

Programme: B.Tech (Data Science) Year: III Semester: VI
Subject: Deep Learning

, ; » Marks: 100
Date: 08 April 2022 Time: 10.00 am to 1.00 pm

Durations: 3 (hrs)

s No. of Pages: 4
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper

1) All code is to be deployed using Kaggle/Google Colab

2) Internet is allowed.

3) Models are to be trained for not more than 50 epochs.

4) EDA is recommended and expected. Additional marks for solid feature engineering.

Qi. Any one: (30 Marks)

a. Pick any starter dataset of your choice (mnist/fashion mnist) and build a classification model
on that. The uniqueness of the dataset will matter.

b. Pick any starter dataset of your choice (boston housing/ etc) and build a regression model
on that. The uniqueness of the dataset will matter.

Q2. Any one: (30 Marks)

a. Build a classification model to solve the following problem
https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv

b. Build a classification model to solve the following problem
https://www.kaggle.com/rdizzl3/jpeg-happywhale-128x128

Q3. Any one: (40 Marks)

a. Build a sequence model to classify IMDB movie reviews. You are required to build one
baseline model and beat the performance of that model. Marks will be given for approach/
pre trained model/ etc.

b. Build a classification model for CIFAR 100 (imbalanced) data using a custom model. Then
benchmark your model versus any 4 pre trained models of your choice and display the
results in the form of a graph
https://www.tensorflow.org/datasets/catalog/cifar100
````

## 2021-22 · Final-Exam · Sem 8 · paper 085b35c93341

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/COMPUTER/Sem_08/DEEP LEARNING/B Tech, Computer, Deep Learning, 4th Year, Sem-VIII, Year 2021-22, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 April 2022
- Text: ocr (3 pages), mean OCR confidence 90.1

````text
SVKM’s NMIMS Aer
‘MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING T-

SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING ie
Academic Year: 2021-22
Programme: B.Tech (Computer) ; Year: IV

Subject: Deep Learning
Marks: 100
Date: 14 April 2022 Time: 2.00 pm to 5.00 pm
Durations: 3 (hrs)
No. of Pages: __3
Final Examination

Instructions: Candidates should read ‘carefully the instructions printed « on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1____ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.

3) in aii___5__ questions to be attempied.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

a Answer briefly: [20]
a SO-1; | a. Explain what is the need of Deep learning? x [04]
ae ;S0-1; |b. Elaborate different challenges in neural network gradient descent algorithm. [04]
CO-3;SO-6; | c. | List and Justify the limitations of convolutional neural network for sequence to 04]
BL-5 sequence mapping tasks with example.
- 4; SO-1; | d.
Far sa0- ih Differentiate between RNN and LSTM. [04]
-2-SO-1: | e&
nl paO= 1; Explain what is dropout in neural networks and the advantages of using it [04]
a. | Explain why introducing nonlinearity is required in neural network. Which are
Q2 different activation functions used to introduce nonlinearity? Describe in detail
CO-1; SO-1; significance of sigmoid activation function in neural networks with its properties, | [10]
BL-2 derivative and suitable graph.
b. | Describe how weights are updated using back propagation in deep neural network in
CO-2; SO-1; detail with required diagram and derivation equations. Write generalized equations.
. - a oa ; [10]
BL-2 Consider minimum two layers in diagram for deriving equations.
a. | A CNN classifier is used with filters and pooling layers. It is denoted by following
notation.
e CONV-K-N denotes a convolutional layer with N filters, each them of size KxK,
Q3 ; ; ‘A
CO-3: SO-6: Padding and stride parameters are always 0 and | respectively. [10]
BL- 4 , e POOL-K indicates a K x K pooling layer with stride K and padding 0.

e FC-N stands for a fully-connected layer with N neurons. °
Filters and pooling layers are applied in the sarne order as mentioned below table.
Calculate number of weights, no of biases and size of feature maps for each layer.

Page 1 of 3
--- page 2 ---
Prepare your answer in same tabular form as given. Show one sample calculation for

each case with formula used to calculate it. i
layer Feature map | No. of weights No of Biases j
dimension ,
Input 256x256x3_ | ----- =
Conv-9-32
Pool-2
Conv-5-64
Pool-2
Conv-5-64
Pool-2
FC-3
a S0-1; | >. | py olain LSTM architecture in detail stating its advantages. [10]
a. | Recommend when transfer learning can be used while training deep neural networks.
Q4 Explain feature extraction and fine tuning in transfer learning. If a model is trained on
CO-3; SO-1,2; dataset with 100 training examples and then pre-trained model is used on dataset with [08]
BL-5 1 million training examples for classification, what will be the result?

€O-2;SO-1; | >. | Explain how adam optimizer speeds up learning as compared to standard gradient [07]
BL-4 descent.
c. | Explain working of autoencoder. What is overcomplete and undercomplete
autoencoder? In an autoencoder with one input layer, one hidden layer and one output

0-2; SO-1,2; - ; . : . :
aes BOT a layer, if input xR" and no bias parameter is considered, if total number of weights is | [05]

BL-2
160, what kind of autoencoder it is?
5 a. | Explain, how do gradients affect the performance of deep neural networks if there are
Q too many layers? Can pre trained model help in this case and to what extent? How
CO-2; SO-1; ; : a’ ae : a : [10]
BL-4 decrease in gradient can be prevented using identity function? Explain in detail.
b. | Consider following deep neural network. Identify parameters and hyperparameters of
given network and list them. What will be weight matrix size for each layer? Assume
that all weights in layer 1 are 0.05, all weights in layer 2 are 0.025, All weights in
layer 3 are 1. Bias vectors are as below: b1=[0.1, 0.2, 0.3, 0.4]; b2=[5.2, 3.2, 4.3];
b3=[0.2, 0.45, 0.75, 0.55, 0.95] and input x is x=[1.5, 2.5, 3]. Calculate value of
output at the four nodes in first hidden layer and at the output of second hidden layer?
O; Or Os Os Os
CO-2; SO-1;
BL-5 ha

Page 2 of 3
--- page 3 ---
Q6 a.
CO-4; SO-6; Discuss different types of RNNs with probable application of each case. [10]

BL-2

CO-2;SO-1; |b. | Illustrate the effect of L2 regularization on weights during training with suitable [10]
BL-3 mathematical equations.

Page 3 of 3
````

## 2021-22 · Final-Exam · Sem 8 · paper 9947e1d99c1a

- Departments: Electronics and Telecommunication, Information Technology
- Programmes: B TECH / EXTC, B TECH / IT
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/EXTC/Sem_08/DEEP LEARNING/B Tech, IT & EXTC, Deep Learning, 4th Year, Sem-VIII, Year 2021-22, Final Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 April 2022
- Text: ocr (4 pages), mean OCR confidence 89.2

````text
i ; Wh
SVKM’s NMIMS i oa.
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /

SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

SZ 03 we
Academic Year: 2021-22 : .
Programme: B. Tech (IT/EXTC) Year: IV Semester: VIII ‘,
Subject: Deep Learning
: ; . Marks: 100
Date: 14 April 2022 Time: 2.00 pm to 5.00 pm

Durations: 3 (hrs)

No. of Pages: __4

Final Examination

oo Se eee See ne - —

—— = = -_
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover

of the Answer Book, which is provided for their use.

1) Question No.1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

A) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly:
CO-3; SO-1; a. | Consider the output of convolution as shown in figure, [4]
BL-3

1/2 13 14
5/6 17 |8
1/3 /2 |4
8 16 |7 |5

A 2x2 average pooling with a stride of 2 is applied to this feature map. Determine
the output of the pooling layer.
CO-1; SO-1; b.| Assume a simple MLP model as shown in the figure with 3 neurons and inputs= | [4]
BL-3 1,2,3. The weights to the input neurons are 4,5 and 6 respectively. Assume the
activation function is a linear constant value of 3. Determine whether the neuron
will fire and what is the output of the model.

0.4
1
J output
> 05 p
0.6
3 a

fage 1/4
--- page 2 ---
The input sample and the initial weights are shown in the figure. The actual output
for the inputs is 1. The activation used is sigmoid. Calculate the following:

1. Predicted output after forward propagation.

2. Mean square error after the first forward pass .

3. Assuming a learning rate of 0.5, the updates in the weights after first

backward pass.

CO-3; SO-1; Consider the operations below for a CNN: [4]
_ 1. A convolution layer with a filter of size 5x5 with a stride of 2 and no
padding.
2. A 2x2 max pooling with stride = 2 is applied.
Ifthe input is 15x15 and both the operations are applied sequentially one after the
other. Calculate the size of the output after the second operation.
CO-2; SO-2; .| A software engineer is working on a project where there are noisy images. Select | [4]
Bs and draw a suitable network architecture to de-noise the images.
CO-1; SO-2; .| A deep learning model has been trained on a dataset, but the model seems to over- | [4]
ue fit the training data. Identify the techniques which can be used to reduce overfitting
on the training data.
Q ;
CO-3; SO-2; Choose an appropriate architecture for developing an application for machine | [10]
ue translation. With the help of an example, show the translation is achieved.
wr SO-1; .| Consider a three-layer neural network as shown in the figure. [10]
--- page 3 ---
Q3

CO-1; SO-2; a. | Discuss the concept of bias-variance off. Under what conditions is model said to

BL-2 be underfitting and overfitting?

CO-35 SO-1; b.| For'the CNN architecture shown below Estimate the number of number of [10]
a parameters

1. After 1st convolutional layer C1

2. After 1st subsampling (pooling) layer S2.
3. After 2nd convolutional layer C3

4. After 2nd subsampling (pooling) layer S4

cia C3:f, maps 16@ 10x10, xs
: feature maps ef 1
6a28 maps 16@!

‘$2: f. maps C5: k 7
CS: layer Bj layer QUTPUT

| "Full condection

i | | eaten connections
Convolutions Subsampling Convolutions | Subsampling Full connection
Cl c2 C3 $4
Q4
CO-3; SO-2; a. |. Compare artificial neural networks (ANN) and Convolutional neural networks [10]
i (CNN) when used for image classification task where the resolution of the
images is 28x28x3 on the following parameters:
1. Number of neurons in the input layer
2. Parameter sharing
3. Pre-processing required
ie SO-2; b.| Sketch the architecture of a Generative Adversarial Network (GAN) and describe | [10]
the function of each block.
Q5
pie SO-2; a. | Consider the application of predicting the next word (autocomplete), knowing the | [10]

first few words. Select a suitable architecture for the application and explain in

brief the steps involved.

Page 3/4
--- page 4 ---
)

CO-1; SO-2; b. Identify and state the different optimization challenges in deep learning. Justify the [10]
me advantage of momentum based gradient descent optimizer over mini batch gradient
descent optimizer.
Q6
: a. | You have designed an application for image classification using Convolutional [10]
ri ae Neural Networks (CNN). The performance of the network is not good and you
identify the reason to be vanishing gradients. Indicate and explain how you can
solve the vanishing gradient problem in CNN.
ir SO-1; b.| An application for the task of classifying the clothes in a Pantaloons’ outlet is to | [10]

be developed. Consider the dataset and the parameters as given below:

Sr. No. | Parameter Values

1 No. of available data samples | 100000

2 Dimension of datasamples | 5

3 Number of output classes 5 (types of clothes)
4 Number of hidden layers 2

Design and draw the Deep neural network. Answer the following:
1. How would you split the data set? (train, validate and test).
2. What can be the activation function of each hidden layer and the output
layer?
3. Which loss function is best suited for this application?
4. Initially your training error is 15% and your validation error is 20%. What
would you do?
5. After you correct the errors in training error is now 1% and validation error
is 1.5%.
6. Next when you test it on test data, you observe that the test error is 15%.

What can be the possible solution?

fage 414
````

## 2021-22 · Final-Exam · Sem 2 · paper 3a35ad31ca40

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENT
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ARTIFICIAL INTELLIGENT/SEM II/DEEP LEARNING/Deep Learning 2021-22 Final0001.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 April 2022
- Text: ocr (1 page), mean OCR confidence 94.4

````text
4

SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT

SCHOOL OF TECHNOLOGY MANAGEMENT & ENG)

Academic Year: 2021-22

Programme: M.Tech (Artificial Intelligence) Year: I Semester: II

Subject: Deep Learning
. Marks: 100

Time: 2.00 pm to 5.00 pm
Durations: 3 (hrs)

No. of Pages: _@ |

Date: 13 April 2022
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper

1) All code is to be deployed using Kaggle/Google Colab

2) Internet is allowed.

3) Models are to be trained for not more than 50 epochs.

4) EDA is recommended and expected. Additional marks for solid feature engineering

Qi. Pick any starter dataset of your choice (mnist/fashion mnist) and build a classification model on
that. The uniqueness of the dataset will matter. [30 Marks]

Qz2. Any one: (30 Marks)

a. Build a classification model to solve the following problem
https://www.tensorflow.org/datasets/catalog/horses_or humans

b. Build a classification model to solve the following problem
https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv

Q3. Any one: (40 Marks)

a. Build a sequence model to classify IMDB movie reviews. You are required to build one baseline
model and beat the performance of that model. Marks will be given for approach/ pre trained
model/ etc.

b. Build a classification model for the data using a custom model. Then benchmark your model
versus any 4 pre trained models of your choice and display the results in the form of a graph
https://www.kaggle.com/hasinisadunikasilva/skincancerdetectiondcnn
````

## 2021-22 · Re-Exam · Sem 6 · paper 64f852e54b42

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM VI/DEEP LEARNING/Deep Learning, Sem-VI, Re-Exam, Year 2021-22.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 June 2022
- Text: ocr (1 page), mean OCR confidence 93.9

````text
. SVKM’s NMIMS

SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEE!

Academic Year: 2021-22

Programme: B.Tech (Data Science) Year: III Semester: VI
Subject: Deep Learning

Marks: 100
Date: 07 June 2022 Time: 2.00 pm to 5.00 pm

Durations: 3 (Hrs)

No. of Pages: © |
Re-Examination (2021-22)

Instructions: Candidates should read carefully the instructions printed on the question paper

1) All code is to be deployed using Kaggle/Google Colab

2) Internet is allowed.

3) Models are to be trained for not more than 50 epochs.

4) EDA is recommended and expected. Additional marks for solid feature engineering.

Q1. (30 Marks)

a. Pick any starter dataset of your choice (mnist/fashion mnist) and build a classification model
on that. The uniqueness of the dataset will matter.

Q2. Any one: (30 Marks)

a. Build a classification model to solve the following problem
https://www.kaggle.com/mkoklu42/rice-msc-dataset

b. Build a classification model to solve the following problem
https://www.tensorflow.org/datasets/catalog/horses or humans

Q3. Any one: (40 Marks)

a. Build a sequence model to classify reuters newswire. You are required to build one baseline
model and beat the performance of that model. Marks will be given for approach/ pre
trained model/ etc.

b. Build a classification model for the data using a custom model. Then benchmark your model
versus any 4 pre trained models of your choice and display the results in the form of a graph
https://www.kaggle.com/hasinisadunikasilva/skincancerdetectiondcnn

i/j
````

## 2021-22 · Re-Exam · Sem 8 · paper b0842fb22eed

- Departments: Electronics and Telecommunication, Information Technology
- Programmes: B TECH / EXTC, B TECH / IT
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/EXTC/Sem_08/DEEP LEARNING/Deep Learning, Sem-VIII, Re-Exam, Year 2021-22.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 June 2022
- Text: ocr (5 pages), mean OCR confidence 87.8

````text
/ . SVKM’s NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /
SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING
ee INSTITGSS
£

WEE

4

Academic Year: 2021-22 S,
/ Programme: B. Tech (IT/EXTC) Year: IV Semester: VII
Subject: Deep Learning i
v Marks: 100
Date: 06 June 2022 Time: 10.00 am to 1.00 pm
af Durations: 3 (Hrs)

No. of Pages: Ss
Re-Examination (2021-22)

v

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover

5 of the Answer Book, which is provided for their use.
2 1) Question No.1 is compulsory.
2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
Ql Answer briefly:
CO-1; SO-1; a. | Assume a three-layer neural network. Consider the inputs and the weights to the | [4]
BL-3 neurons as shown in the figure. Assume the activation function used is RELU.
Determine whether the output neuron will fire.
2 2
1
2
-2
CO-3; SO-1; b. | Consider the output of convolution as shown in figure, [4]
BL-3
1<}2 [3 |4 75
5 |6)7 /8 19
1 43 {2 |}4 75
8 |}6 17 15 19
on | 1 |/4]5 1/7 18

A 3X3 max pooling with a stride of 2 is applied to this feature map. Determine

the output of the pooling layer.

fage |S
--- page 2 ---
CO-3; SO-1, c. | A 35x35 image is filtered by a filter of size 5x5. Padding is not used and number | [4]

a of strides = 2. A 2x2 max pooling with stride = 2 is applied to the filtered image.
Calculate the number of trainable parameters after the training layer.
CO-2; SO-2; d.| A software engineer is working on a project where he wants to detect anomalies | [4]
i from.the data set. Select and draw a suitable network architecture to achieve the
task of anomaly detection.
CO-1; SO-2; e.| You have built a deep learning model but the model seems to perform poorly on | [4]
7 BL-2 "| the training data. Identify the techniques you can use to improve the
' performance of the model. ;
: Q2z
ae SO-1; a. | For the given image matrix and filter determine filtered image matrix with [10]
stride = 2. Also compute the output of 2x2 max pooling layer with stride = 1.
Which elements of the filtered image are high? justify.
0 1 0 2 1 2 5
0 1 1 2 2 5 2
1 1 2 0 5 2 1
0 1 1 5 0 0 1
1 1 5 0 2 1 2
1 PS] 1 1 1 1 1
P) 2 1 2 2 1 1
Image
-1 -1 2
-1 2 -1
2 -1 -1
ie
aa le SO-2; b. | Identify an appropriate architecture for developing an application for sentiment [10]

analysis. With the help of an example, show it is achieved.
--- page 3 ---
Q3

- SO-2; a. | Compare the architecture and performance of LSTM and GRU for sequence [10]
BL-
modeling applications.
- m4 SO-1; b. | Consider a three-layer neural network as shown in the figure. [10]
BL-
$
Fs
The input sample and the initial weights are shown in the figure. The actual
output for the inputs are [1,2] for the two output neurons. The activation used is
sigmoid. Calculate the following:
1. Predicted output after forward propagation.
2. Mean square error after the first forward pass
3. Assuming a learning rate of 0.5, the updates in the weights after first
backward pass.
Q4
— ; SO-2; a. | Justify the use of regularization in Deep Neural Networks (DNN). Explain the
BL-

commonly used types of regularization techniques in DNNs.
--- page 4 ---
CO-3; SO-2; b. | For the CNN architecture shown in the figure, estimate the number of number [10]
BL-3 of parameters

Ag uaxt 3x3 5x5 3x3
ie s=4 #22 same s=2

55 x 55x 96 27x27 96 2727x256 1313x256

y tc 1

= = | |} ]} |—o

Y Pe
é ad lo

9216 4096, 4096

227x227 x3,

$ 13x 13 x 384 1313 x 364 13x13 x 256 6x6 x 256

60M parameters

. 1. After lst convolutional layer C1
2. After Ist subsampling (pooling) layer S2.
3. After 2nd convolutional layer C3
4. After 2nd subsampling (pooling) layer S4
Q5
CO-1; SO-1; a. | Explain the concept of backpropagation as used in gradient descent. Compare . _ | (10)
_ batch gradient descent and stochastic gradient descent algorithms.
CO-2; SO-2; b.| A machine learning engineer is given the task of designing an application of | [10]
oe classifying transactions into fraudulent and authentic. The number of sample
transactions available to be used are 2 lakhs. Design and draw a deep learning
model by considering the parameters (number of layers and number of neurons
in each layer) of your choice. Answer the following:
1. How would you split the data set? (train, test and validate).
2. What can be the activation function of each hidden layer and the output layer?
3. Which loss function is best suited for this application?
4. Initially your training error is 15% and your validation error is 20%. What
would you do?
5. After you correct the errors in training error is now 1% and validation error is
=

1.5%. The vendor tells you to test the application on the unseen dataset (which

has a different distribution), you observe that the test error is 15%. What can

be the possible solution?
--- page 5 ---
Q6

CO-2; SO-2; a.| A machine learning expert has to design an application for biometric | [10]
BL-6

authentication using face recognition. The dataset includes the face images
captured from the employees of the organization, which is small in number to be
used for a deep learning model. Propose a suitable model which can be used for

this application.

‘ CO-3; SO-2; b. a. Justify the significance of inception networks.
BL-3
i b. Consider the inception block shown in the figure. If the input to the
* inception block is an image of size 64x64x128. Compute the final output

of the inception block after filter concatenation.

SO

3x3 convolstions | | SxS convolutions | 1x1 convolutions
1 | i |
| |

128

—
} -

[vant
J |

a 64 | 1x1 convolutions | | 3x3 max pooling
32 oe —— +
32 128
Previous layer |
64x64x128
````

## 2019-20 · Final-Exam · Sem 3 · paper 508d1be2be06

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCES FALL BACH
- Source: `02_Question_Papers/Legacy/M TECH/2ND YEAR/DATA SCIENCES FALL BACH/SEM III/DEEP LEARNING/Deep Learning 2019-20 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 November 2019
- Text: ocr (5 pages), mean OCR confidence 91.3

````text
,

SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT

Programme: M.Tech Data Science (Business Analytics) Year: II Fall Semeste 3

Academic Year: 2019-20
Subject: Deep Learning
Marks: 100
Date: 20 November 2019 Time: 2.00 pm - 5.00 pm
Durations: 3 (Hrs)
No. of Pages: _@ 9
Final Examination (2019-20)

Instructions: Candidates should read carefully the instructions printed on the question paper
and on the cover of the Answer Book, which may be provided for their use.

1) Answer any 5 questions

2) Assume suitable data if necessary.

Answer any one from below three questions:
“Question 1: [20 marks]

a. Pick/Download your images of two types (Dogs, Cats). Do some pre-processing of data if
required and explain your steps

b. Write a CNN model to predict unseen images from above types.

c. White all the mathematics equation that you are using explaining various layers that you are
using in the mode!

d. Explain lose function and your optimization algorithm that you are using and why.

e. Explain the accuracy with respect to parameters and hyper parameters that you are using

Question 2: {20 marks]

a. Pick/Download some stock market or time series data. Do some pre-processing of data if
required and explain your steps

b. Write a RNN/LSTM/GRU model to predict future.

c. White all the mathematics equation that you are using explaining various layers that you are
using in the model

d. Explain lose function and your optimization algorithm that you are using and why.

e. Explain the accuracy with respect to parameters and hyper parameters that you are using

Question 3: {20 marks]

a. Pick/Download MNIST. Do some pre-processing of data if required and explain your steps

b. Write a RNN model to predict unseen images from above types.

c. White all the mathematics equation that you are using explaining various layers that you are
using in the model. ; ;

d. Explain lose function and your optimization algorithm that you are using and why.

e. Explain the accuracy with respect to parameters and hyper parameters that you are using

1/5
--- page 2 ---
4
Question 4:

What can be achieved with “Convolution” operation on Images?

a. Noise Filtering

b. Image Smoothing
c. Image Blurring

d. Edge Detection
e. Allofthe above

For convolution, it is better to store Images in TensorFlow Graph as:

a. Placeholder

b. CSV file
-c. Numpy array
d. Variable

e. None of the above
Which of the following statements is TRUE about Convolution Neural Networks (CNN)?

a. CNN can be applied Only on Image and Text data.
b. CNN can be applied on ANY 2D and 3D array of data.
c. CNN can be applied Only on Text and speech data.
d. CNN can be applied Only on Image data.

e. Allofthe above

Which of the following Layers can be part of Convolution Neural Networks (CNN)

a. Dropout

b. Softmax

c. Maxpooling
d. Relu

e. Allofthe above
Objective of Activation Function is to:

a. Increase the Size of Network

b. Handle Non-Linearity in the Network
c. Handle Linearity in the Network:

d. Reduce the Size of Network

e. None of the above

What things we can do with unsupervised learning?

a. Data dimensionality reduction

b. Object recognition

c. Feature extraction =
d. Pattern recognition

e. Allofthe above a

How many layers has a RBM (Restricted Boltzmann Machine)?

a. Infinte :
b. 4 ;
E |
--- page 3 ---
c 2
d. 3
e. Allofthe above

How RBM compares to PCA?

a. RBM cannot reduce dimensionality

b. PCA cannot generate original data

c. PCA is another type of Neural Network
d. Both can regenerate input data

e. Allofthe above

Select the True statement about Restricted means in RBM?

a. Itis a Boltzmann machine, but with no connections between nodes in the same layer

b. Each node in the first layer has a bias.

c. The RBM reconstructs data by making several forward and backward passes between the
visible and hidden layers.

d. At the hidden layer's nodes, X is multiplied by a W (weight matrix) and added to h_bias.

e. Allofthe above

Select the TRUE statement about RBM:

a. The objective function is to maximize the likelihood of our data being drawn from the
reconstructed data distribution

b. The Negative phase of RBM decreases the probability of samples generated by the model.

c. Contrastive Divergence (CD) is used to approximate the negative phase of RBM.

d. The Positive phase of RBM increases the probability of training data.

e. Allofthe above

Autoencoders are also known as:

a. LSTM Networks

b. Diabolo Networks

c. Deep Belief Network
d. Siamese networks
e. None of the above

Question 5:
Which of the following problems cannot be solved by Autoencoders:

a. Dimensionality Reduction
b. Time series prediction

c. Image Reconstruction

d. Emotion Detection

e. Allofthe above

What is TRUE about Autoencoders:

a. Help to reduce Curse of Dimensionality
b. Are Shallow Neural Networks
c. Used to Learn Most important Features in Data
d. Used for Unsupervised Learning
als
--- page 4 ---
e. All ofthe Above

What are Autoencoders:

a. A Neural Network that is designed to replace Non-Linear Regression

b, *A Neural Network that is trained to attempt to copy its input to its output
c. A Neural Network that learns all the weights by using labeled Data

d. A Neural Network Where different layer inputs are controled by gates

e. All ofthe Above

What is a Deep Autoencoder:

a. Autoencoder with Multiple Hidden Layers

b. Autoencoder with multiple input and output layers
c. Autoencoder stacked with Deep Belief Network

d. Autoencoder stacked with

e. None of the Above

Which statement about TensorFlow is FALSE?

a. TensorFlow is well suitable for Deep Learning Problems

b. TensorFlow is not proper for Machine Learning Problems

c. TensorFlow has a C/C++ backend as well as Python modules
d. TensorFlow is an open source library

e. All ofthe above

What is a Data Flow Graph?

a. Arepresentation of data dependencies between operations
b. Acartesian (x,y) chart

c. Agraphics user interface

d. A flowchart describing an algorithm

e. None of the above

Which function is NOT used as an Activation Function? a
a. sigmoid()

b.   softplus()

c. sin()

d. tanh()

e. relu()

Which statement about TensorFlow is TRUE?

a. runs on FPGA

b. runs on CPU only =
c. runs on CPU and GPU

d. runs on GPU only

ha
a

Why TensorFlow is proper library for Deep Learning?

a. It will benefit from TensorFlow’s auto-differentiation and suite of first-rate optimizers.

b. Provides helpful tools to assemble subgraphs common in neural networks and deep learning
c. TensorFlow has extensive built-in support for deep learning
--- page 5 ---
d. Allofthe above

What is a Recurrent Neural Network?

a. A Neural Network that can recurs to itself

b. An infinite layered Neural Network

c. Aspecial kind of Neural Network to predict weather
d. Amarkovian model

Question 6:
What is TRUE about RNNs?

a. RNNs are VERY suitable for sequential data
b. RNNs are NOT suitable for sequential data

c. RNNs are ONLY suitabie for sequential data
d. All of the above

What application(s) is (are) suitable for RNNs?

a. Estimate temperatures from weather Data
b. Natural Language Processing

c. Video context retriever

d. Speech Recognition

e. Allof the above

Why RNNs are susceptible to issues with their gradients?

a. Numerical computation of gradients can drive into instabilities
b. Gradients can quickly drop and stabilize at near zero

c. Propagation of errors due to the recurrent characteristic

d. Gradients can grow exponentially

e. All of the above

What LSTM Stands for?

a. Last State Threshold Model

b. Limit Sinusoidal Term Memory

c. Long Short Term Memory

d. Least Squares Topological Minimization
e. None of the above

Question 7: {20 Marks]

a. Pick up car and truck data. Pre-process if required

b. Divide the data into test and train in random

c. Create an CNN model

d. Find model accuracy

e. What is effect of dropout percentage on your model?

s[5
````

## 2018-19 · Final-Exam · Sem 2 · paper e126996fa512

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENT
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ARTIFICIAL INTELLIGENT/SEM II/DEEP LEARNING/Deep Learning 2018-19 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 24 April 2019
- Text: ocr (5 pages), mean OCR confidence 91.8

````text
/ S
MUKESH PATEL SCHOOL OF TE NT ENGINEERING

Program M Tech (Artificial Intelligence) ear: I Semester: II
Academic

Subject: Deep Learning Marks: 100

Date : 24 April 2019 Time:2.00 pm to 5.00 pm

Duration: 3 (hrs)
No. of Pages:_ 3

Final Examination (2018-19)

a eee gee

Instructions: Candidates should read carefully the instructions printed on the question paper
and on the cover of the Answer Book, which may be provided for their use.
‘ 1) Answer any one from question 1, 2 or 3 (carries 50 marks)
2) Answer question no.4 to 28 questions (each carrying 2 marks).
3) Assume suitable data if necessary. (..)

Answer any one from below three questions:
Question 1: [5 X 10 marks]

a. Pick/Download your images of three types (Dogs, Cats and Birds). Do some pre-processing of
data if required and explain your steps.

b. Write a CNN model to predict unseen images from above types.

c. White all the mathematics equation that you are using explaining various layers that you are
using in the model.

d. Explain lose function and your optimization algorithm that you are using and why.

e. Explain the accuracy with respect to parameters and hyper parameters that you are using.

Question 2: [5 X 10 marks]

a. Pick/Download some stock market or time series data. Do some pre-processing of data if
required and explain your steps.

b. Write a RNN/LSTM/GRU model to predict future.

c. White all the mathematics equation that you are using explaining various layers that you are
using in the model.

d. Explain lose function and your optimization algorithm that you are using and why.

e. Explain the accuracy with respect to parameters and hyper parameters that you are using.

Question 3: [5 X 10 marks]

a. Pick/Download your images of three types (Dogs, Cats and Birds). Do some pre-processing of
data if required and explain your steps

b. Write a RBM model to predict unseen images from above types.

c. White all the mathematics equation that you are using explaining various layers that you are
using in the model

d. Explain lose function and your optimization algorithm that you are using and why.

e. Explain the accuracy with respect to parameters and hyper parameters that you are using.
--- page 2 ---
2

Answer all 25 question below [2 X 25 marks]
Question 4: What can be achieved with "Convolution" operation on Images?

a. Noise Filtering

b. Image Smoothing
c. Image Blurring

d. Edge Detection
e. Allof the above

Question 5: For convolution, it is better to store Images in TensorFlow Graph as:

a. Placehoider

b. CSVfile   .
c. Numpy array
d. Variable

e. None of the above
Question 6: Which of the following statements is TRUE about Convolution Neural Networks (CNN)?

a. CNN can be applied Only on Image and Text data.

b. CNN can be applied on ANY 2D and 3D array of data.
c. CNN can be applied Only on Text and speech data.
d. CNN can be applied Only on Image data.

e. All of the above

Question 7: Which of the following Layers can be part of Convolution Neural Networks (CNN)

a. Dropout

b. Softmax

c. Maxpooling °
d. Relu

e. Allofthe above

Question 8: Objective of Activation Function is to:

a. Increase the Size of Network

b. Handle Non-Linearity in the Network
c. Handle Linearity in the Network

d. Reduce the Size of Network

e. None of the above

Question 9: What things we can do with unsupervised learning?

a. Data dimensionality reduction
b. Object recognition

c. Feature extraction

d. Pattern recognition

e. Allof the above
--- page 3 ---
Question 10: How many layers has a RBM (Restricted Boltzmann Machine)?

a. Infinte
b. 4
G 2
d. 3

e. Allof the above
Question 11: How RBM compares to PCA?

a. RBM cannot reduce dimensionality

b. PCA cannot generate original data

c. PCAis another type of Neural Network
d. Both can regenerate input data

e. Allof the above

Question 12: Select the True statement about Restricted means in RBM.

a. Itis a Boltzmann machine, but with no connections between nodes in the same layer

b. Each node in the first layer has a bias.

c. The RBM reconstructs data by making several forward and backward passes between the
visible and hidden layers.

d. At the hidden layer's nodes, X is multiplied by a W (weight matrix) and added to h_bias.

e. All ofthe above

Question 13: Select the TRUE statement about RBM:

a. The objective function is to maximize the likelihood of our data being drawn from the
reconstructed data distribution.

b. The Negative phase of RBM decreases the probability of samples generated by the model.

c. Contrastive Divergence (CD) is used to approximate the negative phase of RBM.

d. The Positive phase of RBM increases the probability of training data.

e. All ofthe above.

Question 14: Autoencoders are also known as:

a. LSTM Networks

b. Diabolo Networks

c. Deep Belief Network
d. Siamese networks

e. None of the above

Question 15: Which of the following problems cannot be solved by Autoencoders:

a. Dimensionality Reduction
b. Time series prediction

c. Image Reconstruction

d. Emotion Detection

e. Allof the above
--- page 4 ---
4/x-

Question 16: What is TRUE about Autoencoders:

a. Help to reduce Curse of Dimensionality

b. Are Shallow Neural Networks

c. Used to Learn Most important Features in Data
d. Used for Unsupervised Learning

e. Allof the Above

Question 17: What are Autoencoders:

a. ANeural Network that is designed to replace Non-Linear Regression

b. *A Neural Network that is trained to attempt to copy its input to its output
c. ANeural Network that learns all the weights by using labeled Data

d. ANeuralNetwork Where different layer inputs are controled by gates

e. All of the Above

Question 18: What is a Deep Autoencoder:

a. Autoencoder with Multiple Hidden Layers

b. Autoencoder with multiple input and output layers
c. Autoencoder stacked with Deep Belief Network

d. Autoencoder stacked with

e. None of the Above

Question 19: Which statement about TensorFlow is FALSE?

a. TensorFlow is well suitable for Deep Learning Problems

b. TensorFlow is not proper for Machine Learning Problems

¢. TensorFlow has a C/C++ backend as well as Python modules
d. TensorFlow is an open source library

e. Allof the above

Question 20: What is a Data Flow Graph?

a. Arepresentation of data dependencies between operations
b. Acartesian (x,y) chart

c. Agraphics user interface

d. A flowchart describing an algorithm

e. None of the above

Question 21: Which function is NOT used as an Activation Function?

a. sigmoid()
b. softplus()
c. sin()

d. tanh()

e. relu()

Question 22: Which statement about TensorFlow is TRUE?

a. runs on FPGA

b. runs on CPU only

c. runs on CPU and GPU
d. runs on GPU only
--- page 5 ---
Question 23: Why TensorFlow is proper library for Deep Learning?

a. It will benefit from TensorFlow’s auto-differentiation and suite of first-rate optimizers

b. Provides helpful tools to assemble subgraphs common in neural networks and deep learning
c. TensorFlow has extensive built-in support for deep learning

d. Allof the above

Question 24: What is a Recurrent Neural Network?

a. A Neural Network that can recurs to itself

b. An infinite layered Neural Network

c. Aspecial kind of Neural Network to predict weather
d. Amarkovian model

Question 25: What is TRUE about RNNs?

a. RNNs are VERY suitable for sequential data
b. RNNs are NOT suitable for sequential data
c. RNNs are ONLY suitable for sequential data
d. All of the above

Question 26: What application(s) is (are) suitable for RNNs?

a. Estimate temperatures from weather Data
b. Natural Language Processing

c. Video context retriever

d. Speech Recognition

e. All of the above

Question 27: Why RNNs are susceptible to issues with their gradients?

a. Numerical computation of gradients can drive into instabilities
b. Gradients can quickly drop and stabilize at near zero

c. Propagation of errors due to the recurrent characteristic

d. Gradients can grow exponentially

e. All of the above

Question 28: What LSTM Stands for?

a. Last State Threshold Model

b. Limit Sinusoidal Term Memory

c. Long Short Term Memory

d. Least Squares Topological Minimization
e. None of the above

Shir
````

## 2018-19 · Final-Exam · Sem 3 · paper 49a847f03e2d

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCES FALL BACH
- Source: `02_Question_Papers/Legacy/M TECH/2ND YEAR/DATA SCIENCES FALL BACH/SEM III/DEEP LEARNING/Deep Learning 2018-19 Final.pdf`
- Printed on paper: exam date: 19 November 2018
- Text: ocr (1 page), mean OCR confidence 92.8

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: M. Tech Data Science (Business Analytics) Year: II _ Semester: FALL SEM 3.
Academic Year: 2018-2019
Subject: Deep Learning ~

Date: 19 November 2018 ‘ Ti

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Attempt 5 questions from PART A and 2 questions from part B.

2) Answer to each new question to be started on a fresh page.

3) Figures in brackets on the right hand side indicate full marks.

4) Assume suitable data if necessary.

PARTA.
Attempt any 5 question. Each question carry 6 marks (5X6 30 marks)
Q1. How to Tune Batch Size and Number of Epochs?

Q2. Explain activation function and any two activation function in detail.

Q3.lllustrate the working of gradient decent algorithm.

Q4. Explain stride and padding in convolutional neural network.

QS. Describe any one Optimization techniques for Training Deep Models -

Q6. Compare Max and average pooling methods in Convolutional neural network.

Q7. Explain the backward propagation for neurai network with 3 layers (Input, hidden and output ).

PART B
Qs. Build and train your own neural network from scratch to predict the number of bike share users ona given

day (Data : day.csv and hour.csv),
Or
Implement sentiment prediction with RNN (Data : reviews.txt and labels.txt)

(20 mark)

Q9. Implement any one image classification using CNN- (20 mark)

— 9
````

## 2018-19 · Re-Exam · Sem 3 · paper 673229dacbe6

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCES FALL BACH
- Source: `02_Question_Papers/Legacy/M TECH/2ND YEAR/DATA SCIENCES FALL BACH/SEM III/DEEP LEARNING/DEEP LEARNING BATCH 2018-19 RE EXAM0001.pdf`
- Printed on paper: exam date: 12 January 2019
- Text: ocr (1 page), mean OCR confidence 93.3

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: M. Tech Data Science (Business Analytics) Year: II ~ Semester: FALL SEM 3

Academic Year: 2018-2019

Subject: Deep Learning
MarkX%~Ge -
Date: 12 January 2019 .- Time bo ieee

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Attempt 5 questions from PART A and 2 questions from part B.

2) Answer to each new question to be started on a fresh page.

3) Figures in brackets on the right hand side indicate full marks.

4) Assume <uitable data if necessary.

PARTA
Attempt any 5 question. Each question carry 6 marks (5X6 30 marks)
Q1. Explain stride and padding in convolutional neural network.

Q2. Describe any one Optimization techniques for Training Deep Models.

Q3. Compare Max and average pooling methods in Convolutional neural network.

Q4. Explain the backward propagation for neural network with 3 layers.(Input, hidden and output )
Q5. Describe the working of any two loss function in deep learning,

Q6. Give an explanation of Vanishing gradient problem in neural network.

Q7. Briefly explain Long Short Term Memory Networks,

PART B
Qs. Build and train your own neural network from scratch to predict the number of bike share users on a given

day.(Data : day.csv and hour.csv)
Or
Implement sentiment prediction with RNN.(Data : reviews.txt and labels.txt)

(20 mark)

Q9. Implement any one image classification using CNN. (20 mark)

/
````
