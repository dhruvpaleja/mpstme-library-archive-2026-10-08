# Deep Learning: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 4a28d67c9a07

- Departments: Artificial Intelligence, Computer Engineering, Data Science, Information Technology
- Programmes: BTech AI 7012, BTech CSE DS 7011, BTech IT 7001, MBATech AI 7051, MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_AI_7012/Deep Learning/ANS_Deep Learning(702AI0C008)_2025-2026.pdf` (+4 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: mixed (11 pages), mean OCR confidence 34.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech (IT)/MBA Tech (AI)/MBA Tech
(Comp)/MBA Tech (EXTC)
Year: III/Semester V/Semester VII/Semester XI(Exam Year: NA)
Subject: Deep Learning
Date: 03 Dec 2025   Time: 2.00 pm to 05.00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i. Differentiate between Machine Learning and Deep Learning by explaining any four key   [5]
BL-2   differences between them. Support your answer with examples relevant to real-world
applications.
ii. Choose between machine learning or deep learning for the following tasks and justify:
1.Sentiment analysis on a dataset of 2,000 product reviews (short text).
2. Detecting fraudulent transactions in a financial dataset with labelled records.
3. Generating captions for a collection of 100,000 labelled images of natural scenes.
Solution:
Differentiate between Machine Learning and Deep Learning (2 marks)
Aspect   Machine Learning (ML)   Deep Learning (DL)
Requires   large amounts   of
1. Data   Works well with smaller,
labeled   data   for   effective
Requirement   structured datasets.
training.
Features   are   manually   Learns features automatically
2. Feature
engineered by humans (e.g.,   through multiple neural network
Extraction
texture, color).   layers.
Uses simple models   like
3. Model   Uses complex architectures like
Decision Trees, SVMs, or
Complexity   CNNs, RNNs, or Transformers.
Linear Regression.
4. Computational   Requires high computational
Can run efficiently on CPUs.
Power   resources (GPUs/TPUs).
Example   Spam email detection, credit Image   recognition,   speech
Application   scoring.   translation, autonomous driving.
1. Sentiment analysis on a dataset of 2,000 product reviews (short text) (1 mark)
o   Choice: Machine Learning
o   Justification:
▪   The dataset is relatively small (2,000 entries), so deep learning
may overfit.
▪   Classical ML algorithms (e.g., Naive Bayes, SVM) can achieve
good accuracy on small text datasets with feature extraction like
TF-IDF or word embeddings.
2.   Detecting fraudulent transactions in a financial dataset with labeled records (1
mark)
o   Choice: Machine Learning
o   Justification:
********** 1 **********
--- page 2 ---
▪   Fraud datasets are structured (tabular) and labeled, which is well-
suited for ML models like Random Forest, Gradient Boosting, or
Logistic Regression.
▪   Deep learning isn’t necessary unless the dataset is extremely large
or contains complex unstructured features.
3. Generating captions for a collection of 100,000 labeled images of natural scenes
(1 mark)
o   Choice: Deep Learning
o   Justification:
▪   Image captioning is a complex task requiring understanding of
visual content and natural language generation.
▪   Deep learning architectures like CNNs for image feature
extraction combined with RNNs/Transformers for text generation
are ideal.
The dataset is sufficiently large (100,000 images), making DL feasible.
CO-2;   b. Researchers are developing a deep learning system for automated leaf Disease classification   [5]
BL-3   using images. During model design, they must choose an appropriate loss function for training
and evaluate how it behaves on specific predictions.
i. Discuss the major factors that influence the selection of a suitable loss function in machine
learning and deep learning applications.
ii. Suppose their classifier predicts the probability distribution for three Disease classes
(Normal, Mild, and Severe). For one validation image the true one-hot label is Mild Disease
(0,1,0). Their model outputs class probabilities [0.1, 0.8, 0.1]. Compute the categorical
cross-entropy for this sample and interpret it.
Solution:
Major factors that influence the selection (3 marks)
The decision mainly depends on
Task type & output form – classification (binary – cross entropy, multi class- categorical cross
entropy), regression (MSE/MAE)
Nature of the output – Continuous, categorical, etc.
Compatibility with activation function – e.g., softmax (cross-entropy).
Numerical (2 marks)
CO-2;   c.   i. Which regularization method leads to weight sparsity? Explain why.   [5]
BL-2   ii. You are training a deep convolutional neural network to classify images of handwritten
digits using the MNIST dataset. After several epochs, you notice that your training
accuracy is very high, but your validation accuracy is much lower. Explain how applying
Dropout can help in this situation. Describe what Dropout does during training and how it
affects the model’s performance and generalization ability.
Solution:
L1 regularization leads to weight sparsity (1 mark)
This comes from the shape of the L1 loss. Since even small weights are penalised the same
amount as large weights, more weight values will tend closer to 0. L2 on the other hand penalizes
smaller weights less, which leads to smaller weights but does not ensure sparsity.
Dropout (1 mark)
It is a regularization technique used in neural networks to prevent overfitting. During training,
it randomly “drops out” (i.e., sets to zero) a fraction of the neurons in a given layer on each
forward pass.
How applying Dropout can help in this situation (1 mark)
•   It adds noise to the training process, making the model more robust.
•   It reduces overfitting by preventing complex co-adaptations of neurons.
•   It improves generalization, leading to better validation accuracy.
How it affects the model’s performance and generalization ability (2 marks)
1. Random deactivation: During each forward pass, Dropout randomly deactivates some neurons
(along with their outgoing connections).
2. Independent masks each iteration: On the next iteration (batch), a different random subset of
neurons is dropped.
********** 2 **********
--- page 3 ---
This makes the model learn redundant representations — multiple different ways to extract
features.
3. Weight updates: Only the active neurons are updated during backpropagation.
Testing phase: Dropout is turned off during inference/validation. Instead, all neurons are active,
but their outputs are scaled down (by the dropout rate) to account for the reduced activity during
training.
CO-4;   d. Describe how RNNs process sequential data, how they capture context between words, and why   [5]
BL-2   they are suitable for handling variable-length sentences. Explain how Recurrent Neural
Networks (RNNs) are used in language translation applications like Google Translate.
Solution:
Why Suitable for Translation: (2 marks)
RNNs can model temporal dependencies and understand word order, which are critical for
accurate translation. For example, “I am eating an apple” should not translate the same as “An
apple is eating me.”
Sequential Data Handling (1 mark): RNNs process input text word by word, keeping track of
previous words through hidden states. This helps capture context in translation, since the
meaning of a word depends on the words before and after it.
Context Learning (1 mark): As the RNN reads each word, it updates its hidden state to reflect
the overall meaning of the sentence so far. This enables it to generate context-aware translations
rather than translating each word in isolation.
Variable-Length Sequences (1 mark): RNNs can handle sentences of different lengths, making
them suitable for real-world translation where input and output sentences vary in size. Encoder–
Decoder Structure (Conceptually): The encoder RNN reads the source language sentence and
summarizes it into a context vector. The decoder RNN generates the translated sentence word
by word in the target language.
Q2   a   [10]
CO-2;
BL-3
Given a network with the following parameters
𝜃11 (1) = 0.5, 𝜃12 (1) = 0.5, 𝜃21 (1) = 0.5, 𝜃22 (1) = 0.5, 𝜃11 (2) = 0.25, 𝜃21 (2) = 0.25, 𝑏1 = 𝑏2 = 0.
All neurons have a Sigmoid activation function. The actual output at O is 1. Perform a forward
pass and backward pass to update weights of 𝜃11 (1) , 𝜃11 (2) 𝑎𝑛𝑑 𝑏2 using Gradient Descent
algorithm (Assume learning rate = 0.5).
Solution:
Assume input values
Forward pass (outh1, outo1, total error – each 1 mark)
Backward pass (updated 𝜃11 (1) , 𝜃11 (2)– each 2.5 marks and b2 – 2 mark)
********** 3 **********
--- page 4 ---
oth be

ey) — +6% gsr te 5h
at © ash, ¥ 6) ath, Or) ca
4 4 (oe) Ho 4rulo2d = o4bT
Soe
oho = 06 \5 v
oe teed) Epc ons
ie ee
oe youbo sk ©

x Sue p-084 | )
UE). cay Ee . pens) om
8), 20 = > 2, ih ( a

0ONn _ 9.99235

FORK 7) a dG kok ok ok ak
--- page 5 ---
b2=0.0455
Q2   b   i. Discuss how skip connections in ResNet influence gradient flow, feature reuse, and help in   [10]
CO-3;   addressing the vanishing gradient problem during backpropagation.
BL-2   ii. Explain how the learning approach and feature extraction strategy of InceptionNet differ
from the AlexNet.
Solution:
Skip connection and its importance (5 marks)
Problem with Deep Networks: As networks became deeper, performance degraded due to
vanishing or exploding gradients, making training very deep networks difficult.
Concept of Residual Learning: ResNet introduced residual blocks where the network learns a
residual function F(x) = H(x) - x, so H(x) = F(x) + x. Skip connections directly add the input to
the output after a few convolutional layers.
Skip Connections and Vanishing Gradient Solution:
• Allow gradients to flow directly through identity paths.
• Prevent gradient vanishing in very deep networks (even 152+ layers).
• Improves training speed and convergence.
Comparison of InceptionNet and AlexNet (5 marks)
1. Learning Approach:
AlexNet follows a sequential, deep feedforward design where each layer processes the entire
output of the previous layer. It uses large convolutional filters (e.g., 11×11, 5×5) and learns
features in a hierarchical manner — from simple edges in early layers to complex shapes in
deeper ones.
InceptionNet, a parallel multi-branch architecture within each Inception module. It processes the
same input through multiple convolutional kernels (1×1, 3×3, 5×5) and a pooling path
simultaneously. This allows the network to learn features at multiple spatial scales in a single
layer rather than relying on depth alone.
********** 5 **********
--- page 6 ---
2. Feature Extraction Strategy:
AlexNet extracts one type of feature per layer, with fixed receptive field sizes determined by
kernel size.
InceptionNet captures a diverse set of features — fine details, textures, and global patterns —
by combining outputs from different kernel sizes.
Additionally, 1×1 convolutions in InceptionNet act as bottlenecks, reducing computational cost
while increasing nonlinearity and enabling more efficient feature mixing across channels.
Q3   a   i. Determine the weights required to perform the classification as per the table using single   [10]
CO-2;   layer perceptron network. Assume learning rate is 1 and initial weights are 0. Consider
BL-3   threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   0
-1   1   1   1
1   -1   1   1
-1   1   1   1
ii. Illustrate the correspondence between components of a biological neuron and an artificial
neuron.
Solution:
Problem with formulas (7 marks)
x1 x2 x3   t   α   yin y Δw1 Δw2 Δw3 Δb w1 w2 w3 b
-1   1   -1 0 1 0   0 0   0   0   0   0   0   0   0
-1   1   1   1 1 0   0   -1   1   1   1   -1   1   1   1
1   -1   1   1 1 0   0 1   -1   1   1   0   0   2   2
-1   1   1   1 1 4   1 0   0   0   1   0   0   2   2
Correspondence (3 marks)
Artificial   Neuron
Biological Neuron   Analogy
(Perceptron)
Dendrites   Inputs (x1,x2,…,xn)   Receive signals
Determines   input
Synaptic Strength   Weights (w1,w2,…,wn)
importance
Soma (Cell Body)   Summation + Bias   Aggregates inputs
Activation Threshold   Activation Function   Decides if neuron “fires”
Axon   Output   Sends signal to next neuron
Q3   b A system is being designed for marking the attendance of students using face recognition. This   [10]
CO-3;   task is given to you. You and your team are planning to use convolutional neural network for
BL-2   this task, but the dataset provided to you is very small. Suggest and discuss different approaches
to handle this issue. How transfer learning can be applied to improve the model’s performance
in this situation.
Solution:
1. Data Augmentation – 4 Marks
Artificially increasing the dataset size by applying transformations such as rotation,
flipping, scaling, translation, brightness/contrast changes, or adding noise can help the
network learn robust features. This effectively increases diversity in the training data,
helping the model generalize better
2. Transfer learning – 6 Marks
Transfer learning involves using a pre-trained CNN (e.g., VGG16) that was trained on
a large face dataset. The early layers of these models have already learned general
feature representations like edges, textures, and facial patterns. You can fine-tune the
later layers on your small dataset, allowing the network to adapt to the specific students
in your system while reducing training time and avoiding overfitting.
Q4   a   i. A neural network uses a dataset with 1000 samples and batch size of 100. If the learning   [10]
CO-2;   rate and other parameters remain constant, explain how many weight updates occur in:
BL-3   (i) Batch Gradient Descent
(ii) Stochastic Gradient Descent (SGD)
(iii)   Mini-Batch Gradient Descent
ii.   Consider the cost function J(θ)=0.5𝜃2. Perform two iterations of SGD with Momentum,
where learning rate (η or α) is 0.1, momentum is 0.9, initial velocity 𝑣0=0, initial parameter
𝜃0=1. Write the update rule and compute the velocity & parameter after each iteration.
********** 6 **********
--- page 7 ---
iii.   List the number of hyperparameters required in training a model using Stochastic Gradient
Descent with Momentum.
Solution:
(i)   Each 1 mark
Method   Weight Updates   Explanation
per Epoch
Batch GD   1   Entire dataset (1000 samples) is used
for one weight update per epoch
SGD   1000   Each sample updates weights
individually, so, 1000 updates per
epoch
Mini-Batch GD   1000 / 100 = 10   Dataset divided into 10 batches, so, 10
updates per epoch
(ii)   2 mark for update rule, 1 mark for correct derivative, 1 mark for first θ and
v update, 1 mark for second θ and v update. Partial marks for intermediate
correct calculations.
(iii)   Correct listing of hyperparameters – 2 marks
•   Learning Rate (η or α) – Controls the step size of each update.
•   Momentum Coefficient (μ or α) – Determines how much of the previous velocity is
retained to accelerate convergence.
•   Number of Epochs
Q4   b   i.   Define the vanishing gradient problem in RNNs. Why does it occur?   [10]
CO-4;   ii.   In a sentence like “The dogs barked at the thief and … were appreciated”, why does
BL-2   a simple RNN fail to predict the correct verb form?
iii.   Justify how the forget gate in LSTM helps preserve long-term dependencies.
iv.   Assuming that the forget gate output is ft=[0.1,0.9] and the previous cell state
Ct−1=[2,1], compute the updated cell memory contribution from the forget gate.
Solution:
i. Vanishing gradient problem: 3 marks
•   Gradients shrink exponentially across many time steps/layers.
•   Caused by repeated multiplication by smaller gradient values with across
many layers (e.g., saturating activations).
ii. Why simple RNN fails: 2 marks
•   Long-range dependency from plural subject to verb; simple RNN can’t
retain number info due to vanishing gradients.
•   In RNNs because of the vanishing gradients problem, for the outputs of the
errors associated with the later time steps to affect the computations that are
earlier.
iii. Forget gate :3 marks
• A forget gate is responsible for removing information from the cell state.
•   The information that is no longer required for the LSTM to understand
things or the information that is of less importance is removed via
multiplication of a filter.
•   This is required for optimizing the performance of the LSTM network.
•   Keeps salient info (values near 1) and decays irrelevant memory (near 0).
iv. Numerical: 2 marks
********** 7 **********
--- page 8 ---
•   Given ft= [0.1,0.9], Ct−1= [2,1]:
•   ft⊙Ct−1= [0.2,0.9]
Q5   a   With respect to LSTM, answer the following questions:   [10]
CO-4;   i.   Identify the purpose of each gate (input, forget, output) in an LSTM unit.
BL-2   ii.   Consider the sentence “Artificial Intelligence has revolutionized every domain. The
work force will have to update themselves to remain relevant.” Explain how the input
and forget gates update memory as context changes.
Given: it=0.7,  ft=0.4,  ot=0.8,  𝐶𝑡̃=0.9,  Ct−1=0.5. Compute the new cell state Ct and
hidden state ht. Assume ht=ot × tanh(Ct)
iii.   Why are LSTM models more effective for language modelling than simple RNNs?
Solution:
i. Purpose of each gate: 3 marks
• Forget Gate (ft): A forget gate is responsible for removing information from the
cell state.
• The information that is no longer required for the LSTM to understand things or
the information that is of less importance is removed via multiplication of a filter.
• This is required for optimizing the performance of the LSTM network.
• how much old memory to keep.
• Input/Update Gate: The update gate is responsible for the addition of
information to the cell state.
• how much new info 𝐶𝑡̃ to add.
• Output Gate (ot): job of selecting useful information from the current cell state
and showing it out as an output is done via the output gate.
• how much cell state to expose as hidden ht.
ii. Updation of input and forget gate: 3 marks
•   “Artificial Intelligence has revolutionized every domain. The work force” context
change
• When topic shifts, forget gate drops prior subject info; input gate admits new
subject (“work force”) into cell state (Ct).
Numerical :2 marks
• Given it=0.7, ft=0.4, ot=0.8, 𝐶𝑡=0.9, Ct−1=0.5:
Ct=0.4⋅0.5+0.7⋅0.9=0.2+0.63=0.83
ht=ot×tanh(Ct)=0.8×tanh(0.83)≈0.8×0.6805≈0.5444
iii. Interpretation: 2 marks
• Gating preserves long-range info, mitigates vanishing gradients → better long-
context predictions.
Q5   b   Explain the working principle of the AdaGrad optimizer. Write the update rule of AdaGrad. List   [10]
CO-2;   advantages and disadvantages of using AdaGrad compared to standard Stochastic Gradient
BL-2   Descent (SGD).
Solution
Working principle of the AdaGrad optimizer ( 2 marks)
AdaGrad (Adaptive Gradient Algorithm) is an adaptive learning rate optimization algorithm that
adjusts the learning rate for each parameter individually based on the historical gradients.
Parameters that receive frequent updates get a smaller learning rate. Parameters with infrequent
updates get a larger learning rate. It reduces the learning rate over time for parameters with large
accumulated gradients.
Update rule of AdaGrad (3 marks)
(OR)
Role of Accumulated Squared Gradients (1 mark)
********** 8 **********
--- page 9 ---
Reduces learning rate for parameters with large gradients. It increases learning rate for
parameters with small gradients and helps stabilize training and prevent oscillations along steep
directions.
Advantages: (2 marks)
•   Adaptive learning rates for each parameter, therefore, no need to manually tune
learning rate for each parameter.
•   Good for sparse data where some features appear infrequently.
•   Faster convergence in some cases due to adaptive step sizes.
Disadvantages: (2 marks)
•   Aggressive learning rate decay: Learning rate keeps decreasing, which may stop
learning prematurely. Can stop learning prematurely in long training sessions
•   Not ideal for non-convex problems where we need sustained learning over time.
• May require modifications like RMSProp or Adam to overcome the diminishing
learning rate problem.
• May not perform well on dense datasets
Q6   a   i. Consider input image of size 128 X 128 X 3.   [10]
CO-3;   1)   It is passed through convolution layer 1 with filter size 3x3, no. of filters = 16,
BL-3   no padding and stride = 1.
2)   It is followed by pooling layer of mask size 2X2 with stride=2.
3) Then it is passed through convolution layer 2 with filter size 3X3, no. of filters
= 32, no padding and stride = 1.
4)   It is followed by pooling layer of mask size 2X2 with stride=2.
5) Further it is passed through fully connected layer 1 consisting of 240 neurons
and then FC2 with 120 neurons.
6) Finally, SoftMax layer of 5 neurons is used. Calculate the size of activation
and trainable parameters at the end of each layer.
ii. Determine the output of the given 5x5 image after convoluting with the 3x3 kernel.
Given padding=valid and stride=2
1   0   -1
2   0   -2
3   1   2   2   1   1   0   -1
2   1   2   1   0
3   2   1   0   1
0   3   0   1   2
1   1   0   2   3
Solution: 1 mark for each calculation
Conv layer → ((kernel_width × kernel_height × input_channels) + 1) × num_filters
Pooling layer → number of parameters = 0
FC→ (number of neurons in previous layer × number of neurons in current layer) + number of
biases
No of
Layer   Size of activation
parameters
Input   128 × 128 × 3   0
Conv1 (3×3, 16 filters, stride=1, valid)   126 × 126 × 16   448
Pool1 (2×2, s=2)   63 × 63 × 16   0
Conv2 (3×3, 32 filters, stride=1, valid)   61 × 61 × 32   4,640
Pool2 (2×2, s=2)   30 × 30 × 32   0
Flatten   28,800   0
FC1 (240 units)   240   6,912,240
FC2 (120 units)   120   28,920
SoftMax (5 units)   5   605
Total trainable parameters: 69,46,853.
Convolution operation (2 marks)
3   5
3   -7
********** 9 **********
--- page 10 ---
Q6   b   i. Explain the concept of activation functions in deep neural networks. Discuss the role of non-   [10]
CO-2;   linearity.
BL-3   ii. Compare the following activation functions: Sigmoid, Tanh, ReLU, and Leaky ReLU. Include
their advantages, disadvantages.
Solution:
Concept of Activation Functions (1 marks)
Mathematical functions applied to the output of each neuron. They determine whether a neuron
should be “activated” or not, i.e., whether its output should contribute to the next layer. Without
activation functions, a neural network would effectively behave like a linear model, regardless
of its depth, because a series of linear transformations can be combined into a single linear
function.
Activation functions introduce non-linearity, enabling the network to learn complex patterns and
hierarchical representations.
Role of Non-Linearity (1 marks)
•   Non-linear activation functions allow networks to model non-linear relationships
between inputs and outputs.
•   They enable feature abstraction across layers, letting deeper layers combine simpler
features into more complex ones.
•   Non-linearity also allows networks to approximate any continuous function (Universal
Approximation Theorem).
Comparison of Common Activation Functions (each 2 marks)
Activation   Formula   Advantages   Disadvantages
Smooth, outputs in
Vanishing gradient
[0,1]; interpretable as
Sigmoid   for large
probability
Zero-centered;
Vanishing gradient
Tanh   stronger gradients than
for large
sigmoid; smooth
Simple,
computationally   Dying ReLU
ReLU   f(x)=max(0,x)   efficient; mitigates   problem (neurons
vanishing gradient;   stuck at 0)
fast convergence
Prevents dying ReLU;   Not zero-centered;
Leaky   f(x)=x if x>0
allows small gradient   small negative slope
ReLU   else 0.01x
when x<0   may affect learning
Q7   a   Explain how information flows through a feedforward network during the forward propagation   [10]
CO-2;   process, describing the role of weights, biases, and activation functions in transforming inputs
BL-3   to outputs. Then, compute the output of the following FNN:
•   Network structure: 2 input neurons → 2 hidden neurons (ReLU activation) → 1 output
neuron (ReLU activation).
•   Input: X=[1,0]
•   Weights and biases:
𝑊1 = [0.2 0.4 0.7], 𝑏1 = [0.1 0.2]
0.3
𝑊2 = [0.5 0.6] 𝑏2 = 0.1
Solution:
How Information flows in a feedforward network: (3 marks)
•   Inputs X are fed to the network layer-by-layer.
•   At each layer the neuron computes a linear combination of its inputs: Z=W X+b. Here,
each weight Wij scales the contribution from input j to neuron i.
•   The bias b shifts the linear combination (acts like an adjustable intercept).
•   The result Z is passed through a non-linear activation function f to produce the layer’s
output (activation) A= f (Z).
•   The activation lets the network model non-linear relationships and controls whether a
neuron “fires.”
•   This activated output becomes the input to the next layer. For the final layer, the
activation   may   be   linear   (regression)   or   nonlinear   (classification).
(A brief arrow diagram to be included similar to the following diagram) (2 marks)
********** 10 **********
--- page 11 ---
Computation of the Output:
Network: 2 inputs → 2 hidden (ReLU) → 1 output (linear)
Step 1 : Linear combination at hidden layer (pre-activation Z1): (2 marks)
•   First hidden neuron: 0.2×1+0.3×0+0.1=0.2+0+0.1=0.3
•   Second hidden neuron: 0.4×1+0.7×0+0.2=0.4+0+0.2=0.6
Step 2: Apply ReLU activation to get hidden activations A1: (1 mark)
ReLU: ReLU(x)=max(0,x)
•   ReLU(0.3)=0.3
•   ReLU(0.6)=0.6
Step 3: Linear combination at output (pre-activation Z2) (1 mark)
Compute:
•   0.5×0.3=0.15
•   0.6×0.6=0.36
• Sum = 0.15+0.36=0.51
• Add bias: 0.51+0.1=0.61
Step 4: Output activation: output neuron uses linear activation, so final output A2=Z2=0.61
(1 mark)
b   i. Explain how Convolutional Neural Networks (CNNs) extract hierarchical features from an   [10]
Q7   input image. Include the roles of convolutional, pooling, and fully connected layers in this
CO-3   process.
BL-2   ii. Discuss why CNNs are preferred over traditional fully connected Artificial Neural Networks
(ANNs) for image processing tasks.
iii. Describe how CNNs can be applied in Medical Image Analysis and Autonomous Vehicles.
Provide an example for each application and highlight the advantages of using CNNs in
these scenarios.
Solution:
How CNNs process images, explanation of convolutional, pooling, and fully connected
layers – (3 marks)
•   Convolutional Layers: Apply learnable filters/kernels to the input image to detect local
features like edges, corners, and textures. Early layers detect simple features, middle
layers detect patterns and shapes, and deeper layers detect high-level features like
objects or faces.
•   Pooling Layers: Perform downsampling (e.g., max pooling or average pooling) to
reduce spatial dimensions while retaining important features. Helps in translational
invariance and reduces computational cost.
•   Fully Connected (FC) Layers: Connect all neurons from the previous layer to output
neurons, performing high-level reasoning based on the features extracted by
convolutional and pooling layers. Map the learned hierarchical features to the final
classification or regression output.
Reason for preferring CNNs over ANNs (any three each 1 mark)
•   Parameter Efficiency: CNNs share weights via convolutional filters, reducing the
number of parameters compared to fully connected ANNs, which require separate
weights for each input neuron.
•   Spatial Feature Learning: CNNs exploit the spatial structure of images; they can detect
patterns regardless of their location. ANNs treat every pixel independently, ignoring
local spatial correlations.
•   Hierarchical Feature Extraction: CNNs automatically learn multi-level features,
whereas ANNs require manual feature engineering.
•   Better Generalization: Pooling layers and local connectivity improve robustness and
reduce overfitting, which is challenging for standard ANNs on high-dimensional image
data.
Application 1 — Medical Image Analysis (example + advantage). (2 marks)
Application 2 — Autonomous Vehicles (example + advantage). (2 marks)
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 896a0ec6b087

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIDS_7056/Deep Learning/ANS_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (11 pages)

````text
SYNOPTICS
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
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Attempt any 4 questions from the remaining questions.
6. Attempt five (5) questions in total.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1. (a)   A company is working on a face recognition system. Provide five reasons why would   5
CO1/BL2   deep learning be more suitable than traditional machine learning for this task?
Answer:
•   Automatically learns features (no manual feature extraction required)
• Handles complex patterns in images (faces, expressions, angles)
• Robust to variations (lighting, pose, background)
• Uses CNNs for effective image processing
• Performs better with large datasets
•   Provides higher accuracy than traditional machine learning methods
Rubrics:
• 5 Marks: Covers all key points clearly
• 3–4 Marks: Covers most points but lacks depth or misses 1–2 aspects
• 1–2 Marks: Basic idea but incomplete explanation
• 0 Marks: Incorrect or irrelevant answer
Q1. (b)   Mention five differences between single layer perceptron (SLP) and multilayer 5
CO2/BL3   perceptron (MLP) in terms of model architecture, decision boundary, application,
computational cost, and learning algorithm.
Answer:
Feature   Single Layer   Multilayer Perceptron
Perceptron
Architecture   Input layer , Output   Input layer, Hidden
layer (no hidden layer)   layer(s), Output Layer
Problem Type   Linearly separable   Both linear and non-linear
problems only   problems
Decision   Linear   Non-linear
Boundary
Learning   Perceptron learning   Backpropagation
Algorithm   rule
Capability   Cannot solve complex   Can solve complex
problems (e.g., XOR)   problems
********** 1 **********
--- page 2 ---
Computationa Low   Higher
l Cost
Rubrics:
5 Marks: All five differences clearly mentioned
3–4 Marks: Any 3–4 correct differences
1–2 Marks: Only 1–2 correct points
0 Marks: Incorrect or irrelevant answer
Q1. (c)   A 6 × 6 image uses a 3 × 3 kernel with stride = 1. Compare the output sizes for:   5
CO3/BL3   i.   No padding (P = 0)
ii.   With padding (P = 1).
iii.   Also state why padding helps for border pixels.
Answer:
i. Without Padding (P = 0)
Formula:
(𝑁−𝐹+ 2𝑃)
Output size =   + 1
𝑆
(6 −3 + 0)
=   + 1 = 4
1
⇒Output = 4 × 4
ii. With Padding (P = 1): (6−3+2∗1) + 1 = 𝑂𝑢𝑡𝑝𝑢𝑡 𝑆𝑖𝑧𝑒= 6 × 6
1
iii. Padding preserves border information, meaning:
• Edge pixels (like shorelines in satellite images) are included in convolution
•   Without padding → borders shrink → important edge features lost
• With padding → shoreline edges are not “shrunk away”, improving feature
detection
Rubrics:
• Without Padding: 2 Marks
• With Padding: 2 Marks
•   Shoreline Boundaries: 1 Mark
Q1. (d)   Why does LSTM handle long dependencies better than vanilla RNN?   5
CO4/BL3
Answer:
LSTM handles long dependencies better than a vanilla RNN because it uses a memory
cell and gating mechanisms (input, forget, and output gates) to control the flow of
information. These gates allow the network to retain important information and discard
irrelevant data over long sequences, preventing the vanishing gradient problem. As a
result, LSTMs can effectively learn long-term dependencies that vanilla RNNs struggle
with.
Rubrics:
• Mentions cell state (2M)
• Mentions gates and selective memory (2M)
• Links to long-dependency benefit (1M)
Q2 (a)   A company is building a system that takes an image as input, detects objects and   5
CO2/BL1,   generates a caption. Which deep learning models are required in this pipeline. Also,
2   mention challenges in building such a system.
Answer:
A system that takes an image as input, detects objects, and generates a caption typically
uses a Convolutional Neural Network (CNN) for feature extraction, an object detection
model such as YOLO to identify and localize objects, and a sequence model like Long
Short-Term Memory (LSTM) to generate captions.
The pipeline involves passing the image through a CNN to extract features, applying
the object detection model to recognize objects and their positions, encoding these
features, and then feeding them into the sequence model to generate a descriptive
********** 2 **********
--- page 3 ---
caption word-by-word. Challenges in building such a system include the need for large
labeled datasets, high computational cost, difficulty in integrating multiple models,
errors in object detection affecting caption quality, and challenges in capturing
contextual relationships between objects in complex scenes.
Rubrics:
• 5 Marks: Complete answer with models, clear pipeline, and challenges
• 3–4 Marks: Missing one component (e.g., weak pipeline or fewer challenges)
• 1–2 Marks: Partial understanding (only models or only pipeline)
• 0 Marks: Incorrect or irrelevant answer
Q2 (b)   Identify suitable loss functions and calculate it’s value for the following cases:   5
CO2/BL4   i.   You are building a model to classify emails as Spam (1) or Not Spam (0). The
output of the model is a probability between 0 and 1. For a given email, the
model outputs a probability of 0.8, and the actual label is 1.
ii. A regression model is used to predict house prices based on features like area,
location, and number of rooms. The output is a continuous value. For a given
house, the predicted price is ₹52 lakh, while the actual price is ₹50 lakh.
Answer:
i.   Loss Function: Binary Cross-Entropy
Loss = −[y log(p) + (1 − y) log(1 − p)]
= −[1 log(0.8)] ≈ 0.223
ii.   Loss Function: Mean Squared Error (MSE)
Loss = (52 − 50)² = 4
Rubrics:
• 1 Mark: Correct identification of loss function for classification
• 1 Mark: Correct numerical calculation for classification loss
• 1 Mark: Correct identification of loss function for regression
• 1 Mark: Correct numerical calculation for regression loss
• 1 Mark: Proper formula representation and clear steps
Q2 (c)   A retailer needs on-device detection of missing items from shelf images. Compare   10
CO3/BL4   AlexNet vs Inception vs ResNet in terms of their characteristics, network depth,
accuracy, and compute memory. Recommend any one architecture with reasons.
Answer:
Inception: multi-branch compute-efficient; ResNet: strong accuracy & deep training via
residuals; AlexNet: older/heavier for its accuracy. For on-device efficiency, prefer
Inception-style; if accuracy priority with optimization.
Rubric (10M):
•   Correct comparative dimensions (network depth/ accuracy/memory) (3M)
• AlexNet characteristics (2M)
•   Inception characteristics (2M)
• ResNet characteristics (2M)
•   Clear justified recommendation (1M)
Q3 (a)   An input grayscale image of size 28 × 28 × 1 is passed through the following 10
CO3/BL5   architecture:
• Conv Layer 1: 32 filters of size 3 × 3, stride = 1, padding = valid
• Max Pooling 1: 2 × 2, stride = 2
• Conv Layer 2: 64 filters of size 3 × 3, stride = 1, padding = valid
• Max Pooling 2: 2 × 2, stride = 2
• Conv Layer 3: 128 filters of size 3 × 3, stride = 1, padding = valid
•   Flatten Layer
• Dense Layer 1: 128 neurons
•   Output Layer: 10 neurons
********** 3 **********
--- page 4 ---
Compute the output shape at each layer, calculate the number of parameters for each
trainable layer and find the total number of trainable parameters. Note: Consider floor
wherever required
Answer:
Formulas Used
• Conv Output: (𝑁−𝐹+ 1)(valid padding, stride = 1)
•   Pool Output: 𝑁
2
• Conv Params: (𝐹× 𝐹× 𝐶𝑖𝑛+ 1) × 𝐶𝑜𝑢𝑡
• Dense Params: (𝑛𝑖𝑛× 𝑛𝑜𝑢𝑡) + 𝑛𝑜𝑢𝑡
Completed Table
Layer Type Filter Size / Neurons Output Shape No. of Parameters
Input   —   28 × 28 × 1 0
Conv 1: (28 −3 + 1) = 26
Output: 26 × 26 × 32
Params:(3 × 3 × 1 + 1) × 32 = (9 + 1) × 32 = 320
Max Pool 1: 26/2 = 13
Output: 13 × 13 × 32
Params: 0
Conv 2:(13 −3 + 1) = 11
Output: 11 × 11 × 64
Params:(3 × 3 × 32 + 1) × 64 = (288 + 1) × 64 = 18,496
Max Pool 2:11/2 = 5  (floor)
Output: 5 × 5 × 64
Params: 0
Conv 3: (5 −3 + 1) = 3
Output: 3 × 3 × 128
Params:(3 × 3 × 64 + 1) × 128 = (576 + 1) × 128 = 73,856
Flatten: 3 × 3 × 128 = 1152
Output: 1152
Params: 0
Dense Layer (128 neurons)
Params:1152 × 128 + 128 = 147,456 + 128 = 147,584
Output: 128
Output Layer (10 neurons)
Params:128 × 10 + 10 = 1280 + 10 = 1,290
Output: 10
Final Answer (Synoptic)
•   Layer Outputs:
o Conv1: 26 × 26 × 32
o Pool1: 13 × 13 × 32
o Conv2: 11 × 11 × 64
o Pool2: 5 × 5 × 64
o Conv3: 3 × 3 × 128
o   Flatten: 1152
o Dense: 128
********** 4 **********
--- page 5 ---
o Output: 10
Total Parameters
320 + 18,496 + 73,856 + 147,584 + 1,290 = 241,546
Rubrics:
•   Correct output shapes (4M)
• Conv layer parameter calculations (2M)
• Dense layer parameter calculations (2M)
•   Total parameters correct (1M)
Clear tabular presentation (1M)
Q3 (b)   For a wearable device that recognizes daily activities (e.g., walking, running) with 10
CO4/BL4   limited battery. Answer the following:
i.   Compare LSTM and GRU models.
ii.   Which model has fewer parameters and is faster?
iii.   Which model may give slightly better accuracy for complex patterns?
iv.   Which model would you recommend for this scenario and why?
Answer:
1. Structural Comparison (4M)
o LSTM: Has input, forget, and output gates + separate cell state
o GRU: Has only update and reset gates (simpler structure)
o Hence, GRU is more lightweight
2. Compute / Parameters (3M)
o GRU has fewer parameters → less memory usage
o Requires fewer computations → faster inference
o More suitable for low-power devices
3. Accuracy / Robustness (2M)
o LSTM can sometimes model longer dependencies better
o GRU performs similarly in many practical cases with slightly lower
complexity
4. Recommendation (1M)
o For battery-limited wearable devices → GRU is preferred
o Reason: Good trade-off between efficiency and performance
Rubrics:
•   Correct structural comparison (4M)
•   Compute/parameter reasoning (3M)
• Accuracy discussion (2M)
•   Suitable recommendation for scenario (1M)
Q4 (a)   i.   Apply perceptron training algorithm for single epoch to determine the 10
CO2/BL3   weights and bias for AND function using bipolar inputs and targets. Use
learning rate 𝜂=1, initial weights 𝑤1=0, 𝑤2=0,and bias 𝑏=0. Use activation
function:
𝑦𝑜𝑢𝑡 = 1, if 𝑦𝑖𝑛>=0
𝑦𝑜𝑢𝑡 = −1, otherwise
Show the complete training table for each sample.
ii.   Identify the equation of decision boundary.
Answer:
i.
Sa   x₁   x₂   t w w b   net = y Updat Ne Ne Ne
m   ₁   ₂   w₁x₁   e   w   w w b
pl   +   Applie w₁   w₂
e   w₂x₂   d
+ b
1   -1   -1   -1 0   0   0   0   1   Yes   1   1   -1
2   -1 1   -1 1   1   -1   -1   -1 No   1   1   -1
3   1   -1   -1 1   1   -1   -1   -1 No   1   1   -1
********** 5 **********
--- page 6 ---
4   1   1   1   1   1   -1 1   1 No   1   1   -1
ii.   The decision boundary is given by
w1*x1 + w2*x2 + bias = 0
The obtained weights are 1,1 and bias=-1.
Therefore, the equation of decision boundary will be
x1 + x2 – 1 = 0.
Rubrics:
• 8 Marks: Correct computation of net input (y_in) and output (y) for all samples,
update only when misclassified.
• 2 Mark: Correct decision boundary equation x1+x2−1=0x_1 + x_2 - 1 = 0x1
+x2−1=0
Q4 (b)   Explain why early CNN layers transfer well across domains and later layers are task-   10
CO3/BL1,   specific. Use an example (e.g., cats vs X-rays).
2
Answer:
Early layers learn generic edges/textures; later layers encode high-level class
semantics; so freeze early, fine-tune later for domain shift ResNet
Rubrics:
•   Correct hierarchy explanation (4M)
• Domain shift example (3M)
•   Practical transfer strategy (3M)
Q5 (a)   i.   Explain the network architecture of gated recurrent neural network with   10
CO4/BL3   formulas.
ii.   You train an RNN on sequences of length 200 but use truncated BPTT with
window 25. How many timesteps does each gradient flow through?
Answer:
i.
ii.   Each gradient flows through 25 timesteps, not the full sequence length of
200.
Rubrics:
• 7 Marks: GRU
• 3 Marks Gradient flow computation
Q5 (b)   i.   While training a model, you observe: highly fluctuating loss curve and faster initial 10
CO2/BL4   convergence. Which gradient descent variant is being used? With the help of an
algorithm explain why this behaviour occurs.
ii.   Compare L1 and L2 regularization technique. You are working on a model with
many irrelevant features. Which regularization would you use and why?
Answer:
i.   Stochastic Gradient Descent (SGD).
The observed behaviour indicates Stochastic Gradient Descent, because it updates
weights using individual samples, leading to noisy loss fluctuations but faster initial
convergence due to frequent updates.
********** 6 **********
--- page 7 ---
ii.   L1 regularization, also known as Lasso regularization, involves adding a penalty
equal to the absolute value of the magnitude of coefficients to the loss function.
L2 regularization, also known as Ridge regularization, involves adding a penalty
equal to the square of the magnitude of coefficients to the loss function.
Use L1 Regularization. Some weights become exactly 0 and important features are
retained, which results in sparse model
Rubrics:
• 1 Mark: Correct identification of Stochastic Gradient Descent (SGD)
• 4 Mark: Correct algorithm steps / update rule with explanation.
• 4 Marks: Clear comparison between L1 and L2
• 1 Mark: Correct selection of L1 for irrelevant features
Q6 (a)   Consider   the following   neural network with   inputs   [x1,x2]=[0.5,0.1] and 10
CO2/BL5   targets=[0.6,0.3]. Consider bias on all nodes at hidden layer b1=0.1 and bias on all nodes
at output layer b2 = 0.1, learning rate η =0.5 and sigmoid activation function. The weights
are: w13=0.45, w14=0.32, w23=0.45, w24=0.67, w35=0.56, w36=0.50, w45=0.23,
w46=0.12.
i.   Compute output of node 3, 4, 5, and 6.
ii.   Calculate mean square error at output layer.
iii.   Update weights w46 and w24.
Answer:
********** 7 **********
--- page 8 ---
Rubrics:
• 4 Mark: Compute output of node 3, 4, 5, and 6 (1 mark each).
• 2 Mark: Correct mean square error at output layer.
• 4 Marks: Correct weight updates. (2 marks each)
Q6 (b)   i.   While training a model using AdaGrad, you observe that the learning rate 10
CO2/BL3   becomes extremely small after several iterations. Explain why this happens.
Show how RMSProp modifies the learning rate calculation to resolve this
problem with an algorithm.
ii.   A neural network is overfitting the training data. Explain any three
techniques to reduce overfitting.
Answer:
i.
AdaGrad adapts the learning rate using the sum of squared gradients.
********** 8 **********
--- page 9 ---
ϵ is the learning rate. Gradient keeps accumulating over time. Denominator r keeps
increasing. Hence, effective learning rate keeps decreasing. Eventually becomes too
small → training stops (vanishing updates).
RMSProp uses exponential moving average instead of full accumulation:
ii.   Overfitting occurs when a model learns the training data too well, including
noise, resulting in poor generalization on unseen data.
Technique to reduce overfitting are:
• L2 Regularization (Weight Decay): Adds a penalty term to the loss
function. Reduces model complexity.
•   Dropout: Randomly deactivates a fraction of neurons during training.
Prevents neurons from becoming overly dependent on each other
•   Early Stopping: Training is stopped when validation loss starts increasing.
Prevents the model from learning noise in later epochs.
Rubrics:
• 1 Mark: Correct explanation of AdaGrad issue (accumulation of squared
gradients). Why learning rate becomes very small over time
• 3 Mark: Correct explanation of RMSProp idea (moving average instead of full
accumulation) with Correct algorithm
• 6 Marks: Explanation of techniques (2 marks each)
Q7 (a)   i.   Compare sigmoid, relu, and tanh activation functions in terms of output range   10
CO2/BL3   and their respective drawbacks. Apply these activation functions for input
x=−2.
ii.   Identify whether the learning rate and bias are a parameter or a
hyperparameter. Explain the role of learning rate in neural network training.
What happens when the learning rate is too small or too large.
Answer:
i.
Function   Output Range   Key Issue   Output
at x = -2
Sigmoid   (0,1)   Vanishing gradient   0.119
ReLU   [0,∞)   Dying ReLU   0
Tanh   (-1,1)   Vanishing gradient   -0.964
********** 9 **********
--- page 10 ---
ii.   Learning Rate (η) is a hyperparameter and bias (b) is a parameter.
The learning rate determines the step size taken during weight updates. It
controls how quickly or slowly a model learns from errors. Plays a crucial
role in convergence and stability.
• Too Small learning rate causes very slow learning, takes many
iterations to converge and may get stuck in local minima.
• Too large learning rate may overshoots minima, loss may oscillate
or diverge, training becomes unstable.
Rubrics:
• 6 Marks: Comparison of Activation Functions.
• 2 Mark: Correct identification of Learning Rate (η) as a hyperparameter and
bias (b) as a parameter
• 1 Marks: Role of learning rate.
• 1 Mark: Effect of too small learning rate and too large learning rate
Q7 (b)   Explain Backpropagation Through Time in recurrent neural networks with diagram.   10
CO4/BL4   Discuss vanishing and exploding gradients problem with solution.
Answer:
Backpropagation Through Time Diagram
In an RNN, the forward pass computes outputs and hidden states for each time step, as
shown by the blue arrows in the diagram below. The backward pass (red arrows)
propagates the error gradients from the final time step back through time, allowing the
model to adjust its weights based on the entire sequence's error.
• X (Input): Input vectors at each time step.
• h (Hidden state): The network's "memory" passed from one time step to the next.
• Y (Output): Output vectors at each time step.
• U, W, V (Weight matrices): Parameters shared across all time steps that are
updated during BPTT.
• Red Arrows: Represent the flow of gradients backward through time during the
backpropagation phase.
• Blue Arrows: Represent the forward flow of information during the forward
pass.
Vanishing and Exploding Gradients
These problems are a direct consequence of the chain rule used during BPTT, where
gradients are repeatedly multiplied by the weight matrix and the derivative of the
activation function over many time steps.
•   Vanishing Gradients
o Explanation: When derivatives of the activation functions (like sigmoid
or tanh) are consistently small (e.g., between 0 and 1, or close to zero for
large inputs), the repeated multiplication of these small numbers causes
the gradients to shrink exponentially as they propagate backward through
time.
********** 10 **********
--- page 11 ---
o   Effect: The gradients for earlier layers become negligible, meaning the
weights in those layers receive minimal updates. This makes it difficult
for the network to learn long-term dependencies, effectively causing it to
"forget" information from the distant past of the sequence.
•   Exploding Gradients
o Explanation: Conversely, if the weight matrices contain values greater
than one, or the activation function's derivatives are large, the gradients
grow exponentially with each time step.
o   Effect: The gradients become too large, leading to unstable training,
erratic and massive weight updates, and potentially causing the model's
loss to diverge (result in "NaN" values).
Solutions to these problems include using modern architectures like Long Short-Term
Memory (LSTM) and Gated Recurrent Units (GRU) which use gates to regulate
information flow, using the ReLU activation function, and applying techniques
like gradient clipping (for exploding gradients).
Rubrics:
Backpropagation Through Time: 5 Marks
Discuss vanishing and exploding gradients. 4 Marks
Solution: 1 Marks
********** 11 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper bd0636f4efef

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_Computer_7002/Deep Learning/ANS_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: mixed (12 pages), mean OCR confidence 33.0

````text
SYNOPTICS
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
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i. Differentiate between Machine Learning and Deep Learning by explaining any four key   [5]
BL-2   differences between them. Support your answer with examples relevant to real-world
applications.
ii. Choose between machine learning or deep learning for the following tasks and justify:
1.Sentiment analysis on a dataset of 2,000 product reviews (short text).
2. Detecting fraudulent transactions in a financial dataset with labelled records.
3. Generating captions for a collection of 100,000 labelled images of natural scenes.
Solution:
Differentiate between Machine Learning and Deep Learning (2 marks)
Aspect   Machine Learning (ML)   Deep Learning (DL)
Requires large amounts of
1. Data   Works well with smaller,
labeled data for effective
Requirement   structured datasets.
training.
Features are manually   Learns features automatically
2. Feature
engineered by humans (e.g.,   through multiple neural network
Extraction
texture, color).   layers.
Uses simple models like
3. Model   Uses complex architectures like
Decision Trees, SVMs, or
Complexity   CNNs, RNNs, or Transformers.
Linear Regression.
4. Computational   Requires high computational
Can run efficiently on CPUs.
Power   resources (GPUs/TPUs).
Example   Spam email detection, credit   Image recognition, speech
Application   scoring.   translation, autonomous driving.
1. Sentiment analysis on a dataset of 2,000 product reviews (short text) (1 mark)
o   Choice: Machine Learning
o   Justification:
▪   The dataset is relatively small (2,000 entries), so deep learning
may overfit.
▪   Classical ML algorithms (e.g., Naive Bayes, SVM) can achieve
good accuracy on small text datasets with feature extraction
like TF-IDF or word embeddings.
2.   Detecting fraudulent transactions in a financial dataset with labeled records
(1 mark)
o   Choice: Machine Learning
o   Justification:
********** 1 **********
--- page 2 ---
▪   Fraud datasets are structured (tabular) and labeled, which is
well-suited for ML models like Random Forest, Gradient
Boosting, or Logistic Regression.
▪   Deep learning isn’t necessary unless the dataset is extremely
large or contains complex unstructured features.
3. Generating captions for a collection of 100,000 labeled images of natural
scenes (1 mark)
o   Choice: Deep Learning
o   Justification:
▪   Image captioning is a complex task requiring understanding of
visual content and natural language generation.
▪   Deep learning architectures like CNNs for image feature
extraction combined with RNNs/Transformers for text
generation are ideal.
The dataset is sufficiently large (100,000 images), making DL feasible.
CO-2;   b.   Researchers are developing a deep learning system for automated leaf Disease classification   [5]
BL-3   using images. During model design, they must choose an appropriate loss function for
training and evaluate how it behaves on specific predictions.
i. Discuss the major factors that influence the selection of a suitable loss function in
machine learning and deep learning applications.
ii. Suppose their classifier predicts the probability distribution for three Disease classes
(Normal, Mild, and Severe). For one validation image the true one-hot label is Mild
Disease (0,1,0). Their model outputs class probabilities [0.1, 0.8, 0.1]. Compute the
categorical cross-entropy for this sample and interpret it.
Solution:
Major factors that influence the selection (3 marks)
The decision mainly depends on
Task type & output form – classification (binary – cross entropy, multi class- categorical
cross entropy), regression (MSE/MAE)
Nature of the output – Continuous, categorical, etc.
Compatibility with activation function – e.g., softmax (cross-entropy).
Numerical (2 marks)
CO-2;   c.   i. Which regularization method leads to weight sparsity? Explain why.   [5]
BL-2   ii. You are training a deep convolutional neural network to classify images of handwritten
digits using the MNIST dataset. After several epochs, you notice that your training
accuracy is very high, but your validation accuracy is much lower. Explain how
applying Dropout can help in this situation. Describe what Dropout does during
training and how it affects the model’s performance and generalization ability.
Solution:
L1 regularization leads to weight sparsity (1 mark)
This comes from the shape of the L1 loss. Since even small weights are penalised the same
amount as large weights, more weight values will tend closer to 0. L2 on the other hand
penalizes smaller weights less, which leads to smaller weights but does not ensure sparsity.
Dropout (1 mark)
It is a regularization technique used in neural networks to prevent overfitting. During
training, it randomly “drops out” (i.e., sets to zero) a fraction of the neurons in a given layer
on each forward pass.
How applying Dropout can help in this situation (1 mark)
•   It adds noise to the training process, making the model more robust.
•   It reduces overfitting by preventing complex co-adaptations of neurons.
•   It improves generalization, leading to better validation accuracy.
How it affects the model’s performance and generalization ability (2 marks)
1. Random deactivation: During each forward pass, Dropout randomly deactivates some
neurons (along with their outgoing connections).
********** 2 **********
--- page 3 ---
2. Independent masks each iteration: On the next iteration (batch), a different random subset
of neurons is dropped.
This makes the model learn redundant representations — multiple different ways to extract
features.
3. Weight updates: Only the active neurons are updated during backpropagation.
Testing phase: Dropout is turned off during inference/validation. Instead, all neurons are
active, but their outputs are scaled down (by the dropout rate) to account for the reduced
activity during training.
CO-4;   d.   Describe how RNNs process sequential data, how they capture context between words, and   [5]
BL-2   why they are suitable for handling variable-length sentences. Explain how Recurrent Neural
Networks (RNNs) are used in language translation applications like Google Translate.
Solution:
Why Suitable for Translation: (2 marks)
RNNs can model temporal dependencies and understand word order, which are critical for
accurate translation. For example, “I am eating an apple” should not translate the same as
“An apple is eating me.”
Sequential Data Handling (1 mark): RNNs process input text word by word, keeping track
of previous words through hidden states. This helps capture context in translation, since the
meaning of a word depends on the words before and after it.
Context Learning (1 mark): As the RNN reads each word, it updates its hidden state to
reflect the overall meaning of the sentence so far. This enables it to generate context-aware
translations rather than translating each word in isolation.
Variable-Length Sequences (1 mark): RNNs can handle sentences of different lengths,
making them suitable for real-world translation where input and output sentences vary in
size. Encoder–Decoder Structure (Conceptually): The encoder RNN reads the source
language sentence and summarizes it into a context vector. The decoder RNN generates the
translated sentence word by word in the target language.
Q2   a   [10]
CO-2;
BL-3
Given a network with the following parameters
𝜃11 (1) = 0.5, 𝜃12 (1) = 0.5, 𝜃21 (1) = 0.5, 𝜃22 (1) = 0.5, 𝜃11 (2) = 0.25, 𝜃21 (2) = 0.25, 𝑏1 = 𝑏2 = 0.
All neurons have a Sigmoid activation function. The actual output at O is 1. Perform a
forward pass and backward pass to update weights of 𝜃11 (1), 𝜃11 (2) 𝑎𝑛𝑑 𝑏2 using Gradient
Descent algorithm (Assume learning rate = 0.5).
Solution
Forward pass (outh1, outo1, total error – each 1 mark)
Backward pass (updated 𝜃11 (1) , 𝜃11 (2)– each 2.5 marks and b2 – 2 mark)
********** 3 **********
--- page 4 ---
25) 4o Aru 2). =. 0-46

=-o4ek (©
&. 0:6 \> =
a ,-0°613) 29-015
= -ode) >
E Joube Yak ©

Hah ‘ ob yeah ot A
coast)Leest) (2)
A a = 7-084 |
dD >) () N att - o:25- (0S) Loony)
Wa Sas wD

2On _ 9.929235

FIC 7) IC HOH
--- page 5 ---
Q2   b   i. Discuss how skip connections in ResNet influence gradient flow, feature reuse, and help   [10]
CO-3;   in addressing the vanishing gradient problem during backpropagation.
BL-2   ii. Explain how the learning approach and feature extraction strategy of InceptionNet differ
from the AlexNet.
Solution:
Skip connection and its importance (5 marks)
Problem with Deep Networks: As networks became deeper, performance degraded due to
vanishing or exploding gradients, making training very deep networks difficult.
Concept of Residual Learning: ResNet introduced residual blocks where the network learns
a residual function F(x) = H(x) - x, so H(x) = F(x) + x. Skip connections directly add the
input to the output after a few convolutional layers.
Skip Connections and Vanishing Gradient Solution:
• Allow gradients to flow directly through identity paths.
• Prevent gradient vanishing in very deep networks (even 152+ layers).
• Improves training speed and convergence.
Comparison of InceptionNet and AlexNet (5 marks)
1. Learning Approach:
AlexNet follows a sequential, deep feedforward design where each layer processes the entire
output of the previous layer. It uses large convolutional filters (e.g., 11×11, 5×5) and learns
features in a hierarchical manner — from simple edges in early layers to complex shapes in
deeper ones.
InceptionNet, a parallel multi-branch architecture within each Inception module. It processes
the same input through multiple convolutional kernels (1×1, 3×3, 5×5) and a pooling path
********** 5 **********
--- page 6 ---
simultaneously. This allows the network to learn features at multiple spatial scales in a single
layer rather than relying on depth alone.
2. Feature Extraction Strategy:
AlexNet extracts one type of feature per layer, with fixed receptive field sizes determined by
kernel size.
InceptionNet captures a diverse set of features — fine details, textures, and global patterns
— by combining outputs from different kernel sizes.
Additionally, 1×1 convolutions in InceptionNet act as bottlenecks, reducing computational
cost while increasing nonlinearity and enabling more efficient feature mixing across
channels.
Q3   a   i. Determine the weights required to perform the classification as per the table using single   [10]
CO-2;   layer perceptron network. Assume learning rate is 1 and initial weights are 0. Consider
BL-3   threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   0
-1   1   1   1
1   -1   1   1
-1   1   1   1
ii. Illustrate the correspondence between components of a biological neuron and an
artificial neuron.
Solution:
Problem with formulas (7 marks)
X1 X2 X3   t   α   yin   y   Δ   Δ   Δ   Δb w1 w2 w3   b
w1 w2 w3
-1   1   -1   1   1   0   0   -1   1   -1   1   -1   1   -1   1
-1   1   1   1   1   2   1   0   0   0   0   -1   1   -1   1
1   -1   1   0   1   4   1   0   0   0   0   -1   1   -1   1
-1   -1   1   -1   1   0   0   1   1   -1   -1   0   2   -2   0
Correspondence (3 marks)
Artificial   Neuron
Biological Neuron   Analogy
(Perceptron)
Dendrites   Inputs (x1,x2,…,xn)   Receive signals
Determines   input
Synaptic Strength   Weights (w1,w2,…,wn)
importance
Soma (Cell Body)   Summation + Bias   Aggregates inputs
Activation Threshold   Activation Function   Decides if neuron “fires”
Axon   Output   Sends signal to next neuron
Q3   b A system is being designed for marking the attendance of students using face recognition.   [10]
CO-3;   This task is given to you. You and your team are planning to use convolutional neural network
BL-2   for this task, but the dataset provided to you is very small. Suggest and discuss different
approaches to handle this issue. How transfer learning can be applied to improve the model’s
performance in this situation.
Solution:
1. Data Augmentation – 4 Marks
Artificially increasing the dataset size by applying transformations such as rotation,
flipping, scaling, translation, brightness/contrast changes, or adding noise can help
the network learn robust features. This effectively increases diversity in the training
data, helping the model generalize better
2. Transfer learning – 6 Marks
Transfer learning involves using a pre-trained CNN (e.g., VGG16) that was trained
on a large face dataset. The early layers of these models have already learned
general feature representations like edges, textures, and facial patterns. You can
fine-tune the later layers on your small dataset, allowing the network to adapt to the
specific students in your system while reducing training time and avoiding
overfitting.
Q4   a   i. A neural network uses a dataset with 1000 samples and batch size of 100. If the learning   [10]
CO-2;   rate and other parameters remain constant, explain how many weight updates occur in:
BL-3   (i) Batch Gradient Descent
(ii) Stochastic Gradient Descent (SGD)
(iii)   Mini-Batch Gradient Descent
********** 6 **********
--- page 7 ---
ii.   Consider the cost function J(θ)=0.5𝜃2. Perform two iterations of SGD with Momentum,
where learning rate (η or α) is 0.1, momentum is 0.9, initial velocity 𝑣0=0, initial
parameter 𝜃0=1. Write the update rule and compute the velocity & parameter after each
iteration.
iii.   List the number of hyperparameters required in training a model using Stochastic
Gradient Descent with Momentum.
Solution:
(i)   Each 1 mark
Method   Weight Updates   Explanation
per Epoch
Batch GD   1   Entire dataset (1000 samples) is used
for one weight update per epoch
SGD   1000   Each sample updates weights
individually, so, 1000 updates per
epoch
Mini-Batch GD   1000 / 100 = 10   Dataset divided into 10 batches, so, 10
updates per epoch
(ii)   2 mark for update rule, 1 mark for correct derivative, 1 mark for first θ
and v update, 1 mark for second θ and v update. Partial marks for
intermediate correct calculations.
(iii)   Correct listing of hyperparameters – 2 marks
•   Learning Rate (η or α) – Controls the step size of each update.
•   Momentum Coefficient (μ or α) – Determines how much of the previous velocity is
retained to accelerate convergence.
•   Number of Epochs
Q4   b   i.   Define the vanishing gradient problem in RNNs. Why does it occur?   [10]
CO-4;   ii.   In a sentence like “The dogs barked at the thief and … were appreciated”, why
BL-2   does a simple RNN fail to predict the correct verb form?
iii.   Justify how the forget gate in LSTM helps preserve long-term dependencies.
iv.   Assuming that the forget gate output is ft=[0.1,0.9] and the previous cell state
Ct−1=[2,1], compute the updated cell memory contribution from the forget gate.
Solution:
i. Vanishing gradient problem: 3 marks
•   Gradients shrink exponentially across many time steps/layers.
•   Caused by repeated multiplication by smaller gradient values with across
many layers (e.g., saturating activations).
ii. Why simple RNN fails: 2 marks
•   Long-range dependency from plural subject to verb; simple RNN can’t
retain number info due to vanishing gradients.
•   In RNNs because of the vanishing gradients problem, for the outputs of
the errors associated with the later time steps to affect the computations
that are earlier.
iii. Forget gate :3 marks
• A forget gate is responsible for removing information from the cell state.
********** 7 **********
--- page 8 ---
•   The information that is no longer required for the LSTM to understand
things or the information that is of less importance is removed via
multiplication of a filter.
•   This is required for optimizing the performance of the LSTM network.
•   Keeps salient info (values near 1) and decays irrelevant memory (near
0).
iv. Numerical: 2 marks
•   Given ft= [0.1,0.9], Ct−1= [2,1]:
•   ft⊙Ct−1= [0.2,0.9]
Q5   a   With respect to LSTM, answer the following questions:   [10]
CO-4;   i.   Identify the purpose of each gate (input, forget, output) in an LSTM unit.
BL-2   ii.   Consider the sentence “Artificial Intelligence has revolutionized every domain.
The work force will have to update themselves to remain relevant.” Explain how
the input and forget gates update memory as context changes.
Given: it=0.7,  ft=0.4,  ot=0.8,  𝐶𝑡̃=0.9,  Ct−1=0.5. Compute the new cell state Ct and
hidden state ht. Assume ht=ot × tanh(Ct)
iii.   Why are LSTM models more effective for language modelling than simple
RNNs?
Solution:
i. Purpose of each gate: 3 marks
• Forget Gate (ft): A forget gate is responsible for removing information from
the cell state.
• The information that is no longer required for the LSTM to understand things
or the information that is of less importance is removed via multiplication of a
filter.
• This is required for optimizing the performance of the LSTM network.
• how much old memory to keep.
• Input/Update Gate: The update gate is responsible for the addition of
information to the cell state.
• how much new info 𝐶𝑡̃ to add.
• Output Gate (ot): job of selecting useful information from the current cell
state and showing it out as an output is done via the output gate.
• how much cell state to expose as hidden ht.
ii. Updation of input and forget gate: 3 marks
•   “Artificial Intelligence has revolutionized every domain. The work force”
context change
• When topic shifts, forget gate drops prior subject info; input gate admits new
subject (“work force”) into cell state (Ct).
Numerical :2 marks
• Given it=0.7, ft=0.4, ot=0.8, 𝐶𝑡=0.9, Ct−1=0.5:
Ct=0.4⋅0.5+0.7⋅0.9=0.2+0.63=0.83
ht=ot×tanh(Ct)=0.8×tanh(0.83)≈0.8×0.6805≈0.5444
iii. Interpretation: 2 marks
• Gating preserves long-range info, mitigates vanishing gradients → better
long-context predictions.
Q5   b   Explain the working principle of the AdaGrad optimizer. Write the update rule of AdaGrad.   [10]
CO-2;   List advantages and disadvantages of using AdaGrad compared to standard Stochastic
BL-2   Gradient Descent (SGD).
Solution
Working principle of the AdaGrad optimizer ( 2 marks)
AdaGrad (Adaptive Gradient Algorithm) is an adaptive learning rate optimization algorithm
that adjusts the learning rate for each parameter individually based on the historical gradients.
Parameters that receive frequent updates get a smaller learning rate. Parameters with
infrequent updates get a larger learning rate. It reduces the learning rate over time for
parameters with large accumulated gradients.
Update rule of AdaGrad (3 marks)
(OR)
********** 8 **********
--- page 9 ---
Role of Accumulated Squared Gradients (1 mark)
Reduces learning rate for parameters with large gradients. It increases learning rate for
parameters with small gradients and helps stabilize training and prevent oscillations along
steep directions.
Advantages: (2 marks)
•   Adaptive learning rates for each parameter, therefore, no need to manually tune
learning rate for each parameter.
•   Good for sparse data where some features appear infrequently.
•   Faster convergence in some cases due to adaptive step sizes.
Disadvantages: (2 marks)
•   Aggressive learning rate decay: Learning rate keeps decreasing, which may stop
learning prematurely. Can stop learning prematurely in long training sessions
•   Not ideal for non-convex problems where we need sustained learning over time.
• May require modifications like RMSProp or Adam to overcome the diminishing
learning rate problem.
• May not perform well on dense datasets
Q6   a   i. Consider input image of size 128 X 128 X 3.   [10]
CO-3;   1)   It is passed through convolution layer 1 with filter size 3x3, no. of filters =
BL-3   16, no padding and stride = 1.
2)   It is followed by pooling layer of mask size 2X2 with stride=2.
3) Then it is passed through convolution layer 2 with filter size 3X3, no. of
filters = 32, no padding and stride = 1.
4)   It is followed by pooling layer of mask size 2X2 with stride=2.
5) Further it is passed through fully connected layer 1 consisting of 240
neurons and then FC2 with 120 neurons.
6) Finally, SoftMax layer of 5 neurons is used. Calculate the size of activation
and trainable parameters at the end of each layer.
ii. Determine the output of the given 5x5 image after convoluting with the 3x3
kernel. Given padding=valid and stride=2
1   0   -1
2   0   -2
3   1   2   2   1   1   0   -1
2   1   2   1   0
3   2   1   0   1
0   3   0   1   2
1   1   0   2   3
Solution: 1 mark for each calculation
Conv layer → ((kernel_width × kernel_height × input_channels) + 1) × num_filters
Pooling layer → number of parameters = 0
FC→ (number of neurons in previous layer × number of neurons in current layer) + number
of biases
Size of   No of
Layer
activation   parameters
Input   128 × 128 × 3   0
Conv1 (3×3, 16 filters, stride=1,
126 × 126 × 16   448
valid)
Pool1 (2×2, s=2)   63 × 63 × 16   0
Conv2 (3×3, 32 filters, stride=1,
61 × 61 × 32   4,640
valid)
Pool2 (2×2, s=2)   30 × 30 × 32   0
Flatten   28,800   0
********** 9 **********
--- page 10 ---
FC1 (240 units)   240   6,912,240
FC2 (120 units)   120   28,920
SoftMax (5 units)   5   605
Total trainable parameters: 69,46,853.
Convolution operation (2 marks)
Q6   b   i. Explain the concept of activation functions in deep neural networks. Discuss the role of non-   [10]
CO-2;   linearity.
BL-3   ii. Compare the following activation functions: Sigmoid, Tanh, ReLU, and Leaky ReLU. Include
their advantages, disadvantages.
Solution:
Concept of Activation Functions (1 marks)
Mathematical functions applied to the output of each neuron. They determine whether a
neuron should be “activated” or not, i.e., whether its output should contribute to the next
layer. Without activation functions, a neural network would effectively behave like a linear
model, regardless of its depth, because a series of linear transformations can be combined
into a single linear function.
Activation functions introduce non-linearity, enabling the network to learn complex
patterns and hierarchical representations.
Role of Non-Linearity (1 marks)
•   Non-linear activation functions allow networks to model non-linear relationships
between inputs and outputs.
•   They enable feature abstraction across layers, letting deeper layers combine
simpler features into more complex ones.
•   Non-linearity also allows networks to approximate any continuous function
(Universal Approximation Theorem).
Comparison of Common Activation Functions (each 2 marks)
Activation   Formula   Advantages   Disadvantages
Smooth, outputs in
Vanishing gradient
[0,1]; interpretable as
Sigmoid   for large
probability
Zero-centered;
Vanishing gradient
Tanh   stronger gradients than
for large
sigmoid; smooth
Simple,
computationally   Dying ReLU
ReLU   f(x)=max(0,x)   efficient; mitigates   problem (neurons
vanishing gradient;   stuck at 0)
fast convergence
Prevents dying ReLU;   Not zero-centered;
Leaky   f(x)=x if x>0
allows small gradient   small negative slope
ReLU   else 0.01x
when x<0   may affect learning
Q7   a   Explain how information flows through a feedforward network during the forward   [10]
CO-2;   propagation process, describing the role of weights, biases, and activation functions in
BL-3   transforming inputs to outputs. Then, compute the output of the following FNN:
•   Network structure: 2 input neurons → 2 hidden neurons (ReLU activation) → 1
output neuron (ReLU activation).
•   Input: X=[1,0]
•   Weights and biases:
𝑊1 = [0.2 0.4 0.7], 𝑏1 = [0.1 0.2]
0.3
𝑊2 = [0.5 0.6] 𝑏2 = 0.1
Solution:
How Information flows in a feedforward network: (3 marks)
•   Inputs X are fed to the network layer-by-layer.
•   At each layer the neuron computes a linear combination of its inputs: Z=W X+b.
Here, each weight Wij scales the contribution from input j to neuron i.
********** 10 **********
--- page 11 ---
•   The bias b shifts the linear combination (acts like an adjustable intercept).
•   The result Z is passed through a non-linear activation function f to produce the
layer’s output (activation) A= f (Z).
•   The activation lets the network model non-linear relationships and controls
whether a neuron “fires.”
•   This activated output becomes the input to the next layer. For the final layer, the
activation may be linear (regression) or nonlinear (classification).
(A brief arrow diagram to be included similar to the following diagram) (2
marks)
Computation of the Output:
Network: 2 inputs → 2 hidden (ReLU) → 1 output (linear)
Step 1 : Linear combination at hidden layer (pre-activation Z1): (2 marks)
•   First hidden neuron: 0.2×1+0.4×0+0.1=0.2+0+0.1=0.3
•   Second hidden neuron: 0.3×1+0.7×0+0.2=0.3+0+0.2=0.5
Step 2: Apply ReLU activation to get hidden activations A1: (1 mark)
ReLU: ReLU(x)=max(0,x)
•   ReLU(0.3)=0.3
•   ReLU(0.5)=0.5
Step 3: Linear combination at output (pre-activation Z2) (1 mark)
Compute:
•   0.5×0.3=0.15
•   0.6×0.5=0.30
• Sum = 0.15+0.30=0.45
• Add bias: 0.45+0.1=0.55
Step 4: Output activation: output neuron uses linear activation, so final output
A2=Z2=0.55 ( 1 mark)
b   i. Explain how Convolutional Neural Networks (CNNs) extract hierarchical features from   [10]
Q7   an input image. Include the roles of convolutional, pooling, and fully connected layers
CO-3   in this process.
BL-2   ii. Discuss why CNNs are preferred over traditional fully connected Artificial Neural
Networks (ANNs) for image processing tasks.
iii. Describe how CNNs can be applied in Medical Image Analysis and Autonomous
Vehicles. Provide an example for each application and highlight the advantages of using
CNNs in these scenarios.
Solution:
How CNNs process images, explanation of convolutional, pooling, and fully connected
layers – (3 marks)
•   Convolutional Layers: Apply learnable filters/kernels to the input image to detect
local features like edges, corners, and textures. Early layers detect simple
features, middle layers detect patterns and shapes, and deeper layers detect high-
level features like objects or faces.
•   Pooling Layers: Perform downsampling (e.g., max pooling or average pooling) to
reduce spatial dimensions while retaining important features. Helps in
translational invariance and reduces computational cost.
•   Fully Connected (FC) Layers: Connect all neurons from the previous layer to
output neurons, performing high-level reasoning based on the features extracted
by convolutional and pooling layers. Map the learned hierarchical features to the
final classification or regression output.
Reason for preferring CNNs over ANNs (any three each 1 mark)
•   Parameter Efficiency: CNNs share weights via convolutional filters, reducing the
number of parameters compared to fully connected ANNs, which require separate
weights for each input neuron.
•   Spatial Feature Learning: CNNs exploit the spatial structure of images; they can
detect patterns regardless of their location. ANNs treat every pixel independently,
ignoring local spatial correlations.
•   Hierarchical Feature Extraction: CNNs automatically learn multi-level features,
whereas ANNs require manual feature engineering.
•   Better Generalization: Pooling layers and local connectivity improve robustness
and reduce overfitting, which is challenging for standard ANNs on high-
dimensional image data.
********** 11 **********
--- page 12 ---
Application 1 — Medical Image Analysis (example + advantage). (2 marks)
Application 2 — Autonomous Vehicles (example + advantage). (2 marks)
********** 12 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper ee2d4c557cda

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_EXTC_7006/Deep Learning/ANS_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: mixed (12 pages), mean OCR confidence 33.0

````text
SYNOPTICS
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
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i. Differentiate between Machine Learning and Deep Learning by explaining any four key   [5]
BL-2   differences between them. Support your answer with examples relevant to real-world
applications.
ii. Choose between machine learning or deep learning for the following tasks and justify:
1.Sentiment analysis on a dataset of 2,000 product reviews (short text).
2. Detecting fraudulent transactions in a financial dataset with labelled records.
3. Generating captions for a collection of 100,000 labelled images of natural scenes.
Solution:
Differentiate between Machine Learning and Deep Learning (2 marks)
Aspect   Machine Learning (ML)   Deep Learning (DL)
Requires large amounts of
1. Data   Works well with smaller,
labeled data for effective
Requirement   structured datasets.
training.
Features are manually   Learns features automatically
2. Feature
engineered by humans (e.g.,   through multiple neural network
Extraction
texture, color).   layers.
Uses simple models like
3. Model   Uses complex architectures like
Decision Trees, SVMs, or
Complexity   CNNs, RNNs, or Transformers.
Linear Regression.
4. Computational   Requires high computational
Can run efficiently on CPUs.
Power   resources (GPUs/TPUs).
Example   Spam email detection, credit   Image recognition, speech
Application   scoring.   translation, autonomous driving.
1. Sentiment analysis on a dataset of 2,000 product reviews (short text) (1 mark)
o   Choice: Machine Learning
o   Justification:
▪   The dataset is relatively small (2,000 entries), so deep learning
may overfit.
▪   Classical ML algorithms (e.g., Naive Bayes, SVM) can achieve
good accuracy on small text datasets with feature extraction
like TF-IDF or word embeddings.
2.   Detecting fraudulent transactions in a financial dataset with labeled records
(1 mark)
o   Choice: Machine Learning
o   Justification:
********** 1 **********
--- page 2 ---
▪   Fraud datasets are structured (tabular) and labeled, which is
well-suited for ML models like Random Forest, Gradient
Boosting, or Logistic Regression.
▪   Deep learning isn’t necessary unless the dataset is extremely
large or contains complex unstructured features.
3. Generating captions for a collection of 100,000 labeled images of natural
scenes (1 mark)
o   Choice: Deep Learning
o   Justification:
▪   Image captioning is a complex task requiring understanding of
visual content and natural language generation.
▪   Deep learning architectures like CNNs for image feature
extraction combined with RNNs/Transformers for text
generation are ideal.
The dataset is sufficiently large (100,000 images), making DL feasible.
CO-2;   b.   Researchers are developing a deep learning system for automated leaf Disease classification   [5]
BL-3   using images. During model design, they must choose an appropriate loss function for
training and evaluate how it behaves on specific predictions.
i. Discuss the major factors that influence the selection of a suitable loss function in
machine learning and deep learning applications.
ii. Suppose their classifier predicts the probability distribution for three Disease classes
(Normal, Mild, and Severe). For one validation image the true one-hot label is Mild
Disease (0,1,0). Their model outputs class probabilities [0.1, 0.8, 0.1]. Compute the
categorical cross-entropy for this sample and interpret it.
Solution:
Major factors that influence the selection (3 marks)
The decision mainly depends on
Task type & output form – classification (binary – cross entropy, multi class- categorical
cross entropy), regression (MSE/MAE)
Nature of the output – Continuous, categorical, etc.
Compatibility with activation function – e.g., softmax (cross-entropy).
Numerical (2 marks)
CO-2;   c.   i. Which regularization method leads to weight sparsity? Explain why.   [5]
BL-2   ii. You are training a deep convolutional neural network to classify images of handwritten
digits using the MNIST dataset. After several epochs, you notice that your training
accuracy is very high, but your validation accuracy is much lower. Explain how
applying Dropout can help in this situation. Describe what Dropout does during
training and how it affects the model’s performance and generalization ability.
Solution:
L1 regularization leads to weight sparsity (1 mark)
This comes from the shape of the L1 loss. Since even small weights are penalised the same
amount as large weights, more weight values will tend closer to 0. L2 on the other hand
penalizes smaller weights less, which leads to smaller weights but does not ensure sparsity.
Dropout (1 mark)
It is a regularization technique used in neural networks to prevent overfitting. During
training, it randomly “drops out” (i.e., sets to zero) a fraction of the neurons in a given layer
on each forward pass.
How applying Dropout can help in this situation (1 mark)
•   It adds noise to the training process, making the model more robust.
•   It reduces overfitting by preventing complex co-adaptations of neurons.
•   It improves generalization, leading to better validation accuracy.
How it affects the model’s performance and generalization ability (2 marks)
1. Random deactivation: During each forward pass, Dropout randomly deactivates some
neurons (along with their outgoing connections).
********** 2 **********
--- page 3 ---
2. Independent masks each iteration: On the next iteration (batch), a different random subset
of neurons is dropped.
This makes the model learn redundant representations — multiple different ways to extract
features.
3. Weight updates: Only the active neurons are updated during backpropagation.
Testing phase: Dropout is turned off during inference/validation. Instead, all neurons are
active, but their outputs are scaled down (by the dropout rate) to account for the reduced
activity during training.
CO-4;   d.   Describe how RNNs process sequential data, how they capture context between words, and   [5]
BL-2   why they are suitable for handling variable-length sentences. Explain how Recurrent Neural
Networks (RNNs) are used in language translation applications like Google Translate.
Solution:
Why Suitable for Translation: (2 marks)
RNNs can model temporal dependencies and understand word order, which are critical for
accurate translation. For example, “I am eating an apple” should not translate the same as
“An apple is eating me.”
Sequential Data Handling (1 mark): RNNs process input text word by word, keeping track
of previous words through hidden states. This helps capture context in translation, since the
meaning of a word depends on the words before and after it.
Context Learning (1 mark): As the RNN reads each word, it updates its hidden state to
reflect the overall meaning of the sentence so far. This enables it to generate context-aware
translations rather than translating each word in isolation.
Variable-Length Sequences (1 mark): RNNs can handle sentences of different lengths,
making them suitable for real-world translation where input and output sentences vary in
size. Encoder–Decoder Structure (Conceptually): The encoder RNN reads the source
language sentence and summarizes it into a context vector. The decoder RNN generates the
translated sentence word by word in the target language.
Q2   a   [10]
CO-2;
BL-3
Given a network with the following parameters
𝜃11 (1) = 0.5, 𝜃12 (1) = 0.5, 𝜃21 (1) = 0.5, 𝜃22 (1) = 0.5, 𝜃11 (2) = 0.25, 𝜃21 (2) = 0.25, 𝑏1 = 𝑏2 = 0.
All neurons have a Sigmoid activation function. The actual output at O is 1. Perform a
forward pass and backward pass to update weights of 𝜃11 (1), 𝜃11 (2) 𝑎𝑛𝑑 𝑏2 using Gradient
Descent algorithm (Assume learning rate = 0.5).
Solution
Forward pass (outh1, outo1, total error – each 1 mark)
Backward pass (updated 𝜃11 (1) , 𝜃11 (2)– each 2.5 marks and b2 – 2 mark)
********** 3 **********
--- page 4 ---
25) 4o Aru 2). =. 0-46

=-o4ek (©
&. 0:6 \> =
a ,-0°613) 29-015
= -ode) >
E Joube Yak ©

Hah ‘ ob yeah ot A
coast)Leest) (2)
A a = 7-084 |
dD >) () N att - o:25- (0S) Loony)
Wa Sas wD

2On _ 9.929235

FIC 7) IC HOH
--- page 5 ---
Q2   b   i. Discuss how skip connections in ResNet influence gradient flow, feature reuse, and help   [10]
CO-3;   in addressing the vanishing gradient problem during backpropagation.
BL-2   ii. Explain how the learning approach and feature extraction strategy of InceptionNet differ
from the AlexNet.
Solution:
Skip connection and its importance (5 marks)
Problem with Deep Networks: As networks became deeper, performance degraded due to
vanishing or exploding gradients, making training very deep networks difficult.
Concept of Residual Learning: ResNet introduced residual blocks where the network learns
a residual function F(x) = H(x) - x, so H(x) = F(x) + x. Skip connections directly add the
input to the output after a few convolutional layers.
Skip Connections and Vanishing Gradient Solution:
• Allow gradients to flow directly through identity paths.
• Prevent gradient vanishing in very deep networks (even 152+ layers).
• Improves training speed and convergence.
Comparison of InceptionNet and AlexNet (5 marks)
1. Learning Approach:
AlexNet follows a sequential, deep feedforward design where each layer processes the entire
output of the previous layer. It uses large convolutional filters (e.g., 11×11, 5×5) and learns
features in a hierarchical manner — from simple edges in early layers to complex shapes in
deeper ones.
InceptionNet, a parallel multi-branch architecture within each Inception module. It processes
the same input through multiple convolutional kernels (1×1, 3×3, 5×5) and a pooling path
********** 5 **********
--- page 6 ---
simultaneously. This allows the network to learn features at multiple spatial scales in a single
layer rather than relying on depth alone.
2. Feature Extraction Strategy:
AlexNet extracts one type of feature per layer, with fixed receptive field sizes determined by
kernel size.
InceptionNet captures a diverse set of features — fine details, textures, and global patterns
— by combining outputs from different kernel sizes.
Additionally, 1×1 convolutions in InceptionNet act as bottlenecks, reducing computational
cost while increasing nonlinearity and enabling more efficient feature mixing across
channels.
Q3   a   i. Determine the weights required to perform the classification as per the table using single   [10]
CO-2;   layer perceptron network. Assume learning rate is 1 and initial weights are 0. Consider
BL-3   threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   0
-1   1   1   1
1   -1   1   1
-1   1   1   1
ii. Illustrate the correspondence between components of a biological neuron and an
artificial neuron.
Solution:
Problem with formulas (7 marks)
X1 X2 X3   t   α   yin   y   Δ   Δ   Δ   Δb w1 w2 w3   b
w1 w2 w3
-1   1   -1   1   1   0   0   -1   1   -1   1   -1   1   -1   1
-1   1   1   1   1   2   1   0   0   0   0   -1   1   -1   1
1   -1   1   0   1   4   1   0   0   0   0   -1   1   -1   1
-1   -1   1   -1   1   0   0   1   1   -1   -1   0   2   -2   0
Correspondence (3 marks)
Artificial   Neuron
Biological Neuron   Analogy
(Perceptron)
Dendrites   Inputs (x1,x2,…,xn)   Receive signals
Determines   input
Synaptic Strength   Weights (w1,w2,…,wn)
importance
Soma (Cell Body)   Summation + Bias   Aggregates inputs
Activation Threshold   Activation Function   Decides if neuron “fires”
Axon   Output   Sends signal to next neuron
Q3   b A system is being designed for marking the attendance of students using face recognition.   [10]
CO-3;   This task is given to you. You and your team are planning to use convolutional neural network
BL-2   for this task, but the dataset provided to you is very small. Suggest and discuss different
approaches to handle this issue. How transfer learning can be applied to improve the model’s
performance in this situation.
Solution:
1. Data Augmentation – 4 Marks
Artificially increasing the dataset size by applying transformations such as rotation,
flipping, scaling, translation, brightness/contrast changes, or adding noise can help
the network learn robust features. This effectively increases diversity in the training
data, helping the model generalize better
2. Transfer learning – 6 Marks
Transfer learning involves using a pre-trained CNN (e.g., VGG16) that was trained
on a large face dataset. The early layers of these models have already learned
general feature representations like edges, textures, and facial patterns. You can
fine-tune the later layers on your small dataset, allowing the network to adapt to the
specific students in your system while reducing training time and avoiding
overfitting.
Q4   a   i. A neural network uses a dataset with 1000 samples and batch size of 100. If the learning   [10]
CO-2;   rate and other parameters remain constant, explain how many weight updates occur in:
BL-3   (i) Batch Gradient Descent
(ii) Stochastic Gradient Descent (SGD)
(iii)   Mini-Batch Gradient Descent
********** 6 **********
--- page 7 ---
ii.   Consider the cost function J(θ)=0.5𝜃2. Perform two iterations of SGD with Momentum,
where learning rate (η or α) is 0.1, momentum is 0.9, initial velocity 𝑣0=0, initial
parameter 𝜃0=1. Write the update rule and compute the velocity & parameter after each
iteration.
iii.   List the number of hyperparameters required in training a model using Stochastic
Gradient Descent with Momentum.
Solution:
(i)   Each 1 mark
Method   Weight Updates   Explanation
per Epoch
Batch GD   1   Entire dataset (1000 samples) is used
for one weight update per epoch
SGD   1000   Each sample updates weights
individually, so, 1000 updates per
epoch
Mini-Batch GD   1000 / 100 = 10   Dataset divided into 10 batches, so, 10
updates per epoch
(ii)   2 mark for update rule, 1 mark for correct derivative, 1 mark for first θ
and v update, 1 mark for second θ and v update. Partial marks for
intermediate correct calculations.
(iii)   Correct listing of hyperparameters – 2 marks
•   Learning Rate (η or α) – Controls the step size of each update.
•   Momentum Coefficient (μ or α) – Determines how much of the previous velocity is
retained to accelerate convergence.
•   Number of Epochs
Q4   b   i.   Define the vanishing gradient problem in RNNs. Why does it occur?   [10]
CO-4;   ii.   In a sentence like “The dogs barked at the thief and … were appreciated”, why
BL-2   does a simple RNN fail to predict the correct verb form?
iii.   Justify how the forget gate in LSTM helps preserve long-term dependencies.
iv.   Assuming that the forget gate output is ft=[0.1,0.9] and the previous cell state
Ct−1=[2,1], compute the updated cell memory contribution from the forget gate.
Solution:
i. Vanishing gradient problem: 3 marks
•   Gradients shrink exponentially across many time steps/layers.
•   Caused by repeated multiplication by smaller gradient values with across
many layers (e.g., saturating activations).
ii. Why simple RNN fails: 2 marks
•   Long-range dependency from plural subject to verb; simple RNN can’t
retain number info due to vanishing gradients.
•   In RNNs because of the vanishing gradients problem, for the outputs of
the errors associated with the later time steps to affect the computations
that are earlier.
iii. Forget gate :3 marks
• A forget gate is responsible for removing information from the cell state.
********** 7 **********
--- page 8 ---
•   The information that is no longer required for the LSTM to understand
things or the information that is of less importance is removed via
multiplication of a filter.
•   This is required for optimizing the performance of the LSTM network.
•   Keeps salient info (values near 1) and decays irrelevant memory (near
0).
iv. Numerical: 2 marks
•   Given ft= [0.1,0.9], Ct−1= [2,1]:
•   ft⊙Ct−1= [0.2,0.9]
Q5   a   With respect to LSTM, answer the following questions:   [10]
CO-4;   i.   Identify the purpose of each gate (input, forget, output) in an LSTM unit.
BL-2   ii.   Consider the sentence “Artificial Intelligence has revolutionized every domain.
The work force will have to update themselves to remain relevant.” Explain how
the input and forget gates update memory as context changes.
Given: it=0.7,  ft=0.4,  ot=0.8,  𝐶𝑡̃=0.9,  Ct−1=0.5. Compute the new cell state Ct and
hidden state ht. Assume ht=ot × tanh(Ct)
iii.   Why are LSTM models more effective for language modelling than simple
RNNs?
Solution:
i. Purpose of each gate: 3 marks
• Forget Gate (ft): A forget gate is responsible for removing information from
the cell state.
• The information that is no longer required for the LSTM to understand things
or the information that is of less importance is removed via multiplication of a
filter.
• This is required for optimizing the performance of the LSTM network.
• how much old memory to keep.
• Input/Update Gate: The update gate is responsible for the addition of
information to the cell state.
• how much new info 𝐶𝑡̃ to add.
• Output Gate (ot): job of selecting useful information from the current cell
state and showing it out as an output is done via the output gate.
• how much cell state to expose as hidden ht.
ii. Updation of input and forget gate: 3 marks
•   “Artificial Intelligence has revolutionized every domain. The work force”
context change
• When topic shifts, forget gate drops prior subject info; input gate admits new
subject (“work force”) into cell state (Ct).
Numerical :2 marks
• Given it=0.7, ft=0.4, ot=0.8, 𝐶𝑡=0.9, Ct−1=0.5:
Ct=0.4⋅0.5+0.7⋅0.9=0.2+0.63=0.83
ht=ot×tanh(Ct)=0.8×tanh(0.83)≈0.8×0.6805≈0.5444
iii. Interpretation: 2 marks
• Gating preserves long-range info, mitigates vanishing gradients → better
long-context predictions.
Q5   b   Explain the working principle of the AdaGrad optimizer. Write the update rule of AdaGrad.   [10]
CO-2;   List advantages and disadvantages of using AdaGrad compared to standard Stochastic
BL-2   Gradient Descent (SGD).
Solution
Working principle of the AdaGrad optimizer ( 2 marks)
AdaGrad (Adaptive Gradient Algorithm) is an adaptive learning rate optimization algorithm
that adjusts the learning rate for each parameter individually based on the historical gradients.
Parameters that receive frequent updates get a smaller learning rate. Parameters with
infrequent updates get a larger learning rate. It reduces the learning rate over time for
parameters with large accumulated gradients.
Update rule of AdaGrad (3 marks)
(OR)
********** 8 **********
--- page 9 ---
Role of Accumulated Squared Gradients (1 mark)
Reduces learning rate for parameters with large gradients. It increases learning rate for
parameters with small gradients and helps stabilize training and prevent oscillations along
steep directions.
Advantages: (2 marks)
•   Adaptive learning rates for each parameter, therefore, no need to manually tune
learning rate for each parameter.
•   Good for sparse data where some features appear infrequently.
•   Faster convergence in some cases due to adaptive step sizes.
Disadvantages: (2 marks)
•   Aggressive learning rate decay: Learning rate keeps decreasing, which may stop
learning prematurely. Can stop learning prematurely in long training sessions
•   Not ideal for non-convex problems where we need sustained learning over time.
• May require modifications like RMSProp or Adam to overcome the diminishing
learning rate problem.
• May not perform well on dense datasets
Q6   a   i. Consider input image of size 128 X 128 X 3.   [10]
CO-3;   1)   It is passed through convolution layer 1 with filter size 3x3, no. of filters =
BL-3   16, no padding and stride = 1.
2)   It is followed by pooling layer of mask size 2X2 with stride=2.
3) Then it is passed through convolution layer 2 with filter size 3X3, no. of
filters = 32, no padding and stride = 1.
4)   It is followed by pooling layer of mask size 2X2 with stride=2.
5) Further it is passed through fully connected layer 1 consisting of 240
neurons and then FC2 with 120 neurons.
6) Finally, SoftMax layer of 5 neurons is used. Calculate the size of activation
and trainable parameters at the end of each layer.
ii. Determine the output of the given 5x5 image after convoluting with the 3x3
kernel. Given padding=valid and stride=2
1   0   -1
2   0   -2
3   1   2   2   1   1   0   -1
2   1   2   1   0
3   2   1   0   1
0   3   0   1   2
1   1   0   2   3
Solution: 1 mark for each calculation
Conv layer → ((kernel_width × kernel_height × input_channels) + 1) × num_filters
Pooling layer → number of parameters = 0
FC→ (number of neurons in previous layer × number of neurons in current layer) + number
of biases
Size of   No of
Layer
activation   parameters
Input   128 × 128 × 3   0
Conv1 (3×3, 16 filters, stride=1,
126 × 126 × 16   448
valid)
Pool1 (2×2, s=2)   63 × 63 × 16   0
Conv2 (3×3, 32 filters, stride=1,
61 × 61 × 32   4,640
valid)
Pool2 (2×2, s=2)   30 × 30 × 32   0
Flatten   28,800   0
********** 9 **********
--- page 10 ---
FC1 (240 units)   240   6,912,240
FC2 (120 units)   120   28,920
SoftMax (5 units)   5   605
Total trainable parameters: 69,46,853.
Convolution operation (2 marks)
Q6   b   i. Explain the concept of activation functions in deep neural networks. Discuss the role of non-   [10]
CO-2;   linearity.
BL-3   ii. Compare the following activation functions: Sigmoid, Tanh, ReLU, and Leaky ReLU. Include
their advantages, disadvantages.
Solution:
Concept of Activation Functions (1 marks)
Mathematical functions applied to the output of each neuron. They determine whether a
neuron should be “activated” or not, i.e., whether its output should contribute to the next
layer. Without activation functions, a neural network would effectively behave like a linear
model, regardless of its depth, because a series of linear transformations can be combined
into a single linear function.
Activation functions introduce non-linearity, enabling the network to learn complex
patterns and hierarchical representations.
Role of Non-Linearity (1 marks)
•   Non-linear activation functions allow networks to model non-linear relationships
between inputs and outputs.
•   They enable feature abstraction across layers, letting deeper layers combine
simpler features into more complex ones.
•   Non-linearity also allows networks to approximate any continuous function
(Universal Approximation Theorem).
Comparison of Common Activation Functions (each 2 marks)
Activation   Formula   Advantages   Disadvantages
Smooth, outputs in
Vanishing gradient
[0,1]; interpretable as
Sigmoid   for large
probability
Zero-centered;
Vanishing gradient
Tanh   stronger gradients than
for large
sigmoid; smooth
Simple,
computationally   Dying ReLU
ReLU   f(x)=max(0,x)   efficient; mitigates   problem (neurons
vanishing gradient;   stuck at 0)
fast convergence
Prevents dying ReLU;   Not zero-centered;
Leaky   f(x)=x if x>0
allows small gradient   small negative slope
ReLU   else 0.01x
when x<0   may affect learning
Q7   a   Explain how information flows through a feedforward network during the forward   [10]
CO-2;   propagation process, describing the role of weights, biases, and activation functions in
BL-3   transforming inputs to outputs. Then, compute the output of the following FNN:
•   Network structure: 2 input neurons → 2 hidden neurons (ReLU activation) → 1
output neuron (ReLU activation).
•   Input: X=[1,0]
•   Weights and biases:
𝑊1 = [0.2 0.4 0.7], 𝑏1 = [0.1 0.2]
0.3
𝑊2 = [0.5 0.6] 𝑏2 = 0.1
Solution:
How Information flows in a feedforward network: (3 marks)
•   Inputs X are fed to the network layer-by-layer.
•   At each layer the neuron computes a linear combination of its inputs: Z=W X+b.
Here, each weight Wij scales the contribution from input j to neuron i.
********** 10 **********
--- page 11 ---
•   The bias b shifts the linear combination (acts like an adjustable intercept).
•   The result Z is passed through a non-linear activation function f to produce the
layer’s output (activation) A= f (Z).
•   The activation lets the network model non-linear relationships and controls
whether a neuron “fires.”
•   This activated output becomes the input to the next layer. For the final layer, the
activation may be linear (regression) or nonlinear (classification).
(A brief arrow diagram to be included similar to the following diagram) (2
marks)
Computation of the Output:
Network: 2 inputs → 2 hidden (ReLU) → 1 output (linear)
Step 1 : Linear combination at hidden layer (pre-activation Z1): (2 marks)
•   First hidden neuron: 0.2×1+0.4×0+0.1=0.2+0+0.1=0.3
•   Second hidden neuron: 0.3×1+0.7×0+0.2=0.3+0+0.2=0.5
Step 2: Apply ReLU activation to get hidden activations A1: (1 mark)
ReLU: ReLU(x)=max(0,x)
•   ReLU(0.3)=0.3
•   ReLU(0.5)=0.5
Step 3: Linear combination at output (pre-activation Z2) (1 mark)
Compute:
•   0.5×0.3=0.15
•   0.6×0.5=0.30
• Sum = 0.15+0.30=0.45
• Add bias: 0.45+0.1=0.55
Step 4: Output activation: output neuron uses linear activation, so final output
A2=Z2=0.55 ( 1 mark)
b   i. Explain how Convolutional Neural Networks (CNNs) extract hierarchical features from   [10]
Q7   an input image. Include the roles of convolutional, pooling, and fully connected layers
CO-3   in this process.
BL-2   ii. Discuss why CNNs are preferred over traditional fully connected Artificial Neural
Networks (ANNs) for image processing tasks.
iii. Describe how CNNs can be applied in Medical Image Analysis and Autonomous
Vehicles. Provide an example for each application and highlight the advantages of using
CNNs in these scenarios.
Solution:
How CNNs process images, explanation of convolutional, pooling, and fully connected
layers – (3 marks)
•   Convolutional Layers: Apply learnable filters/kernels to the input image to detect
local features like edges, corners, and textures. Early layers detect simple
features, middle layers detect patterns and shapes, and deeper layers detect high-
level features like objects or faces.
•   Pooling Layers: Perform downsampling (e.g., max pooling or average pooling) to
reduce spatial dimensions while retaining important features. Helps in
translational invariance and reduces computational cost.
•   Fully Connected (FC) Layers: Connect all neurons from the previous layer to
output neurons, performing high-level reasoning based on the features extracted
by convolutional and pooling layers. Map the learned hierarchical features to the
final classification or regression output.
Reason for preferring CNNs over ANNs (any three each 1 mark)
•   Parameter Efficiency: CNNs share weights via convolutional filters, reducing the
number of parameters compared to fully connected ANNs, which require separate
weights for each input neuron.
•   Spatial Feature Learning: CNNs exploit the spatial structure of images; they can
detect patterns regardless of their location. ANNs treat every pixel independently,
ignoring local spatial correlations.
•   Hierarchical Feature Extraction: CNNs automatically learn multi-level features,
whereas ANNs require manual feature engineering.
•   Better Generalization: Pooling layers and local connectivity improve robustness
and reduce overfitting, which is challenging for standard ANNs on high-
dimensional image data.
********** 11 **********
--- page 12 ---
Application 1 — Medical Image Analysis (example + advantage). (2 marks)
Application 2 — Autonomous Vehicles (example + advantage). (2 marks)
********** 12 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 79487bab27d8

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006, MBATech (ELECTRONICS TELECOMMUNICATION
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_EXTC_7006/Deep Learning/ANS_Deep Learning(702AI0C008)_2025-2026_79487bab27.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: mixed (12 pages), mean OCR confidence 33.0

````text
SYNOPTICS
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
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i. Differentiate between Machine Learning and Deep Learning by explaining any four key   [5]
BL-2   differences between them. Support your answer with examples relevant to real-world
applications.
ii. Choose between machine learning or deep learning for the following tasks and justify:
1.Sentiment analysis on a dataset of 2,000 product reviews (short text).
2. Detecting fraudulent transactions in a financial dataset with labelled records.
3. Generating captions for a collection of 100,000 labelled images of natural scenes.
Solution:
Differentiate between Machine Learning and Deep Learning (2 marks)
Aspect   Machine Learning (ML)   Deep Learning (DL)
Requires large amounts of
1. Data   Works well with smaller,
labeled data for effective
Requirement   structured datasets.
training.
Features are manually   Learns features automatically
2. Feature
engineered by humans (e.g.,   through multiple neural network
Extraction
texture, color).   layers.
Uses simple models like
3. Model   Uses complex architectures like
Decision Trees, SVMs, or
Complexity   CNNs, RNNs, or Transformers.
Linear Regression.
4. Computational   Requires high computational
Can run efficiently on CPUs.
Power   resources (GPUs/TPUs).
Example   Spam email detection, credit   Image recognition, speech
Application   scoring.   translation, autonomous driving.
1. Sentiment analysis on a dataset of 2,000 product reviews (short text) (1 mark)
o   Choice: Machine Learning
o   Justification:
▪   The dataset is relatively small (2,000 entries), so deep learning
may overfit.
▪   Classical ML algorithms (e.g., Naive Bayes, SVM) can achieve
good accuracy on small text datasets with feature extraction
like TF-IDF or word embeddings.
2.   Detecting fraudulent transactions in a financial dataset with labeled records
(1 mark)
o   Choice: Machine Learning
o   Justification:
********** 1 **********
--- page 2 ---
▪   Fraud datasets are structured (tabular) and labeled, which is
well-suited for ML models like Random Forest, Gradient
Boosting, or Logistic Regression.
▪   Deep learning isn’t necessary unless the dataset is extremely
large or contains complex unstructured features.
3. Generating captions for a collection of 100,000 labeled images of natural
scenes (1 mark)
o   Choice: Deep Learning
o   Justification:
▪   Image captioning is a complex task requiring understanding of
visual content and natural language generation.
▪   Deep learning architectures like CNNs for image feature
extraction combined with RNNs/Transformers for text
generation are ideal.
The dataset is sufficiently large (100,000 images), making DL feasible.
CO-2;   b.   Researchers are developing a deep learning system for automated leaf Disease classification   [5]
BL-3   using images. During model design, they must choose an appropriate loss function for
training and evaluate how it behaves on specific predictions.
i. Discuss the major factors that influence the selection of a suitable loss function in
machine learning and deep learning applications.
ii. Suppose their classifier predicts the probability distribution for three Disease classes
(Normal, Mild, and Severe). For one validation image the true one-hot label is Mild
Disease (0,1,0). Their model outputs class probabilities [0.1, 0.8, 0.1]. Compute the
categorical cross-entropy for this sample and interpret it.
Solution:
Major factors that influence the selection (3 marks)
The decision mainly depends on
Task type & output form – classification (binary – cross entropy, multi class- categorical
cross entropy), regression (MSE/MAE)
Nature of the output – Continuous, categorical, etc.
Compatibility with activation function – e.g., softmax (cross-entropy).
Numerical (2 marks)
CO-2;   c.   i. Which regularization method leads to weight sparsity? Explain why.   [5]
BL-2   ii. You are training a deep convolutional neural network to classify images of handwritten
digits using the MNIST dataset. After several epochs, you notice that your training
accuracy is very high, but your validation accuracy is much lower. Explain how
applying Dropout can help in this situation. Describe what Dropout does during
training and how it affects the model’s performance and generalization ability.
Solution:
L1 regularization leads to weight sparsity (1 mark)
This comes from the shape of the L1 loss. Since even small weights are penalised the same
amount as large weights, more weight values will tend closer to 0. L2 on the other hand
penalizes smaller weights less, which leads to smaller weights but does not ensure sparsity.
Dropout (1 mark)
It is a regularization technique used in neural networks to prevent overfitting. During
training, it randomly “drops out” (i.e., sets to zero) a fraction of the neurons in a given layer
on each forward pass.
How applying Dropout can help in this situation (1 mark)
•   It adds noise to the training process, making the model more robust.
•   It reduces overfitting by preventing complex co-adaptations of neurons.
•   It improves generalization, leading to better validation accuracy.
How it affects the model’s performance and generalization ability (2 marks)
1. Random deactivation: During each forward pass, Dropout randomly deactivates some
neurons (along with their outgoing connections).
********** 2 **********
--- page 3 ---
2. Independent masks each iteration: On the next iteration (batch), a different random subset
of neurons is dropped.
This makes the model learn redundant representations — multiple different ways to extract
features.
3. Weight updates: Only the active neurons are updated during backpropagation.
Testing phase: Dropout is turned off during inference/validation. Instead, all neurons are
active, but their outputs are scaled down (by the dropout rate) to account for the reduced
activity during training.
CO-4;   d.   Describe how RNNs process sequential data, how they capture context between words, and   [5]
BL-2   why they are suitable for handling variable-length sentences. Explain how Recurrent Neural
Networks (RNNs) are used in language translation applications like Google Translate.
Solution:
Why Suitable for Translation: (2 marks)
RNNs can model temporal dependencies and understand word order, which are critical for
accurate translation. For example, “I am eating an apple” should not translate the same as
“An apple is eating me.”
Sequential Data Handling (1 mark): RNNs process input text word by word, keeping track
of previous words through hidden states. This helps capture context in translation, since the
meaning of a word depends on the words before and after it.
Context Learning (1 mark): As the RNN reads each word, it updates its hidden state to
reflect the overall meaning of the sentence so far. This enables it to generate context-aware
translations rather than translating each word in isolation.
Variable-Length Sequences (1 mark): RNNs can handle sentences of different lengths,
making them suitable for real-world translation where input and output sentences vary in
size. Encoder–Decoder Structure (Conceptually): The encoder RNN reads the source
language sentence and summarizes it into a context vector. The decoder RNN generates the
translated sentence word by word in the target language.
Q2   a   [10]
CO-2;
BL-3
Given a network with the following parameters
𝜃11 (1) = 0.5, 𝜃12 (1) = 0.5, 𝜃21 (1) = 0.5, 𝜃22 (1) = 0.5, 𝜃11 (2) = 0.25, 𝜃21 (2) = 0.25, 𝑏1 = 𝑏2 = 0.
All neurons have a Sigmoid activation function. The actual output at O is 1. Perform a
forward pass and backward pass to update weights of 𝜃11 (1), 𝜃11 (2) 𝑎𝑛𝑑 𝑏2 using Gradient
Descent algorithm (Assume learning rate = 0.5).
Solution
Forward pass (outh1, outo1, total error – each 1 mark)
Backward pass (updated 𝜃11 (1) , 𝜃11 (2)– each 2.5 marks and b2 – 2 mark)
********** 3 **********
--- page 4 ---
25) 4o Aru 2). =. 0-46

=-o4ek (©
&. 0:6 \> =
a ,-0°613) 29-015
= -ode) >
E Joube Yak ©

Hah ‘ ob yeah ot A
coast)Leest) (2)
A a = 7-084 |
dD >) () N att - o:25- (0S) Loony)
Wa Sas wD

2On _ 9.929235

FIC 7) IC HOH
--- page 5 ---
Q2   b   i. Discuss how skip connections in ResNet influence gradient flow, feature reuse, and help   [10]
CO-3;   in addressing the vanishing gradient problem during backpropagation.
BL-2   ii. Explain how the learning approach and feature extraction strategy of InceptionNet differ
from the AlexNet.
Solution:
Skip connection and its importance (5 marks)
Problem with Deep Networks: As networks became deeper, performance degraded due to
vanishing or exploding gradients, making training very deep networks difficult.
Concept of Residual Learning: ResNet introduced residual blocks where the network learns
a residual function F(x) = H(x) - x, so H(x) = F(x) + x. Skip connections directly add the
input to the output after a few convolutional layers.
Skip Connections and Vanishing Gradient Solution:
• Allow gradients to flow directly through identity paths.
• Prevent gradient vanishing in very deep networks (even 152+ layers).
• Improves training speed and convergence.
Comparison of InceptionNet and AlexNet (5 marks)
1. Learning Approach:
AlexNet follows a sequential, deep feedforward design where each layer processes the entire
output of the previous layer. It uses large convolutional filters (e.g., 11×11, 5×5) and learns
features in a hierarchical manner — from simple edges in early layers to complex shapes in
deeper ones.
InceptionNet, a parallel multi-branch architecture within each Inception module. It processes
the same input through multiple convolutional kernels (1×1, 3×3, 5×5) and a pooling path
********** 5 **********
--- page 6 ---
simultaneously. This allows the network to learn features at multiple spatial scales in a single
layer rather than relying on depth alone.
2. Feature Extraction Strategy:
AlexNet extracts one type of feature per layer, with fixed receptive field sizes determined by
kernel size.
InceptionNet captures a diverse set of features — fine details, textures, and global patterns
— by combining outputs from different kernel sizes.
Additionally, 1×1 convolutions in InceptionNet act as bottlenecks, reducing computational
cost while increasing nonlinearity and enabling more efficient feature mixing across
channels.
Q3   a   i. Determine the weights required to perform the classification as per the table using single   [10]
CO-2;   layer perceptron network. Assume learning rate is 1 and initial weights are 0. Consider
BL-3   threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   0
-1   1   1   1
1   -1   1   1
-1   1   1   1
ii. Illustrate the correspondence between components of a biological neuron and an
artificial neuron.
Solution:
Problem with formulas (7 marks)
X1 X2 X3   t   α   yin   y   Δ   Δ   Δ   Δb w1 w2 w3   b
w1 w2 w3
-1   1   -1   1   1   0   0   -1   1   -1   1   -1   1   -1   1
-1   1   1   1   1   2   1   0   0   0   0   -1   1   -1   1
1   -1   1   0   1   4   1   0   0   0   0   -1   1   -1   1
-1   -1   1   -1   1   0   0   1   1   -1   -1   0   2   -2   0
Correspondence (3 marks)
Artificial   Neuron
Biological Neuron   Analogy
(Perceptron)
Dendrites   Inputs (x1,x2,…,xn)   Receive signals
Determines   input
Synaptic Strength   Weights (w1,w2,…,wn)
importance
Soma (Cell Body)   Summation + Bias   Aggregates inputs
Activation Threshold   Activation Function   Decides if neuron “fires”
Axon   Output   Sends signal to next neuron
Q3   b A system is being designed for marking the attendance of students using face recognition.   [10]
CO-3;   This task is given to you. You and your team are planning to use convolutional neural network
BL-2   for this task, but the dataset provided to you is very small. Suggest and discuss different
approaches to handle this issue. How transfer learning can be applied to improve the model’s
performance in this situation.
Solution:
1. Data Augmentation – 4 Marks
Artificially increasing the dataset size by applying transformations such as rotation,
flipping, scaling, translation, brightness/contrast changes, or adding noise can help
the network learn robust features. This effectively increases diversity in the training
data, helping the model generalize better
2. Transfer learning – 6 Marks
Transfer learning involves using a pre-trained CNN (e.g., VGG16) that was trained
on a large face dataset. The early layers of these models have already learned
general feature representations like edges, textures, and facial patterns. You can
fine-tune the later layers on your small dataset, allowing the network to adapt to the
specific students in your system while reducing training time and avoiding
overfitting.
Q4   a   i. A neural network uses a dataset with 1000 samples and batch size of 100. If the learning   [10]
CO-2;   rate and other parameters remain constant, explain how many weight updates occur in:
BL-3   (i) Batch Gradient Descent
(ii) Stochastic Gradient Descent (SGD)
(iii)   Mini-Batch Gradient Descent
********** 6 **********
--- page 7 ---
ii.   Consider the cost function J(θ)=0.5𝜃2. Perform two iterations of SGD with Momentum,
where learning rate (η or α) is 0.1, momentum is 0.9, initial velocity 𝑣0=0, initial
parameter 𝜃0=1. Write the update rule and compute the velocity & parameter after each
iteration.
iii.   List the number of hyperparameters required in training a model using Stochastic
Gradient Descent with Momentum.
Solution:
(i)   Each 1 mark
Method   Weight Updates   Explanation
per Epoch
Batch GD   1   Entire dataset (1000 samples) is used
for one weight update per epoch
SGD   1000   Each sample updates weights
individually, so, 1000 updates per
epoch
Mini-Batch GD   1000 / 100 = 10   Dataset divided into 10 batches, so, 10
updates per epoch
(ii)   2 mark for update rule, 1 mark for correct derivative, 1 mark for first θ
and v update, 1 mark for second θ and v update. Partial marks for
intermediate correct calculations.
(iii)   Correct listing of hyperparameters – 2 marks
•   Learning Rate (η or α) – Controls the step size of each update.
•   Momentum Coefficient (μ or α) – Determines how much of the previous velocity is
retained to accelerate convergence.
•   Number of Epochs
Q4   b   i.   Define the vanishing gradient problem in RNNs. Why does it occur?   [10]
CO-4;   ii.   In a sentence like “The dogs barked at the thief and … were appreciated”, why
BL-2   does a simple RNN fail to predict the correct verb form?
iii.   Justify how the forget gate in LSTM helps preserve long-term dependencies.
iv.   Assuming that the forget gate output is ft=[0.1,0.9] and the previous cell state
Ct−1=[2,1], compute the updated cell memory contribution from the forget gate.
Solution:
i. Vanishing gradient problem: 3 marks
•   Gradients shrink exponentially across many time steps/layers.
•   Caused by repeated multiplication by smaller gradient values with across
many layers (e.g., saturating activations).
ii. Why simple RNN fails: 2 marks
•   Long-range dependency from plural subject to verb; simple RNN can’t
retain number info due to vanishing gradients.
•   In RNNs because of the vanishing gradients problem, for the outputs of
the errors associated with the later time steps to affect the computations
that are earlier.
iii. Forget gate :3 marks
• A forget gate is responsible for removing information from the cell state.
********** 7 **********
--- page 8 ---
•   The information that is no longer required for the LSTM to understand
things or the information that is of less importance is removed via
multiplication of a filter.
•   This is required for optimizing the performance of the LSTM network.
•   Keeps salient info (values near 1) and decays irrelevant memory (near
0).
iv. Numerical: 2 marks
•   Given ft= [0.1,0.9], Ct−1= [2,1]:
•   ft⊙Ct−1= [0.2,0.9]
Q5   a   With respect to LSTM, answer the following questions:   [10]
CO-4;   i.   Identify the purpose of each gate (input, forget, output) in an LSTM unit.
BL-2   ii.   Consider the sentence “Artificial Intelligence has revolutionized every domain.
The work force will have to update themselves to remain relevant.” Explain how
the input and forget gates update memory as context changes.
Given: it=0.7,  ft=0.4,  ot=0.8,  𝐶𝑡̃=0.9,  Ct−1=0.5. Compute the new cell state Ct and
hidden state ht. Assume ht=ot × tanh(Ct)
iii.   Why are LSTM models more effective for language modelling than simple
RNNs?
Solution:
i. Purpose of each gate: 3 marks
• Forget Gate (ft): A forget gate is responsible for removing information from
the cell state.
• The information that is no longer required for the LSTM to understand things
or the information that is of less importance is removed via multiplication of a
filter.
• This is required for optimizing the performance of the LSTM network.
• how much old memory to keep.
• Input/Update Gate: The update gate is responsible for the addition of
information to the cell state.
• how much new info 𝐶𝑡̃ to add.
• Output Gate (ot): job of selecting useful information from the current cell
state and showing it out as an output is done via the output gate.
• how much cell state to expose as hidden ht.
ii. Updation of input and forget gate: 3 marks
•   “Artificial Intelligence has revolutionized every domain. The work force”
context change
• When topic shifts, forget gate drops prior subject info; input gate admits new
subject (“work force”) into cell state (Ct).
Numerical :2 marks
• Given it=0.7, ft=0.4, ot=0.8, 𝐶𝑡=0.9, Ct−1=0.5:
Ct=0.4⋅0.5+0.7⋅0.9=0.2+0.63=0.83
ht=ot×tanh(Ct)=0.8×tanh(0.83)≈0.8×0.6805≈0.5444
iii. Interpretation: 2 marks
• Gating preserves long-range info, mitigates vanishing gradients → better
long-context predictions.
Q5   b   Explain the working principle of the AdaGrad optimizer. Write the update rule of AdaGrad.   [10]
CO-2;   List advantages and disadvantages of using AdaGrad compared to standard Stochastic
BL-2   Gradient Descent (SGD).
Solution
Working principle of the AdaGrad optimizer ( 2 marks)
AdaGrad (Adaptive Gradient Algorithm) is an adaptive learning rate optimization algorithm
that adjusts the learning rate for each parameter individually based on the historical gradients.
Parameters that receive frequent updates get a smaller learning rate. Parameters with
infrequent updates get a larger learning rate. It reduces the learning rate over time for
parameters with large accumulated gradients.
Update rule of AdaGrad (3 marks)
(OR)
********** 8 **********
--- page 9 ---
Role of Accumulated Squared Gradients (1 mark)
Reduces learning rate for parameters with large gradients. It increases learning rate for
parameters with small gradients and helps stabilize training and prevent oscillations along
steep directions.
Advantages: (2 marks)
•   Adaptive learning rates for each parameter, therefore, no need to manually tune
learning rate for each parameter.
•   Good for sparse data where some features appear infrequently.
•   Faster convergence in some cases due to adaptive step sizes.
Disadvantages: (2 marks)
•   Aggressive learning rate decay: Learning rate keeps decreasing, which may stop
learning prematurely. Can stop learning prematurely in long training sessions
•   Not ideal for non-convex problems where we need sustained learning over time.
• May require modifications like RMSProp or Adam to overcome the diminishing
learning rate problem.
• May not perform well on dense datasets
Q6   a   i. Consider input image of size 128 X 128 X 3.   [10]
CO-3;   1)   It is passed through convolution layer 1 with filter size 3x3, no. of filters =
BL-3   16, no padding and stride = 1.
2)   It is followed by pooling layer of mask size 2X2 with stride=2.
3) Then it is passed through convolution layer 2 with filter size 3X3, no. of
filters = 32, no padding and stride = 1.
4)   It is followed by pooling layer of mask size 2X2 with stride=2.
5) Further it is passed through fully connected layer 1 consisting of 240
neurons and then FC2 with 120 neurons.
6) Finally, SoftMax layer of 5 neurons is used. Calculate the size of activation
and trainable parameters at the end of each layer.
ii. Determine the output of the given 5x5 image after convoluting with the 3x3
kernel. Given padding=valid and stride=2
1   0   -1
2   0   -2
3   1   2   2   1   1   0   -1
2   1   2   1   0
3   2   1   0   1
0   3   0   1   2
1   1   0   2   3
Solution: 1 mark for each calculation
Conv layer → ((kernel_width × kernel_height × input_channels) + 1) × num_filters
Pooling layer → number of parameters = 0
FC→ (number of neurons in previous layer × number of neurons in current layer) + number
of biases
Size of   No of
Layer
activation   parameters
Input   128 × 128 × 3   0
Conv1 (3×3, 16 filters, stride=1,
126 × 126 × 16   448
valid)
Pool1 (2×2, s=2)   63 × 63 × 16   0
Conv2 (3×3, 32 filters, stride=1,
61 × 61 × 32   4,640
valid)
Pool2 (2×2, s=2)   30 × 30 × 32   0
Flatten   28,800   0
********** 9 **********
--- page 10 ---
FC1 (240 units)   240   6,912,240
FC2 (120 units)   120   28,920
SoftMax (5 units)   5   605
Total trainable parameters: 69,46,853.
Convolution operation (2 marks)
Q6   b   i. Explain the concept of activation functions in deep neural networks. Discuss the role of non-   [10]
CO-2;   linearity.
BL-3   ii. Compare the following activation functions: Sigmoid, Tanh, ReLU, and Leaky ReLU. Include
their advantages, disadvantages.
Solution:
Concept of Activation Functions (1 marks)
Mathematical functions applied to the output of each neuron. They determine whether a
neuron should be “activated” or not, i.e., whether its output should contribute to the next
layer. Without activation functions, a neural network would effectively behave like a linear
model, regardless of its depth, because a series of linear transformations can be combined
into a single linear function.
Activation functions introduce non-linearity, enabling the network to learn complex
patterns and hierarchical representations.
Role of Non-Linearity (1 marks)
•   Non-linear activation functions allow networks to model non-linear relationships
between inputs and outputs.
•   They enable feature abstraction across layers, letting deeper layers combine
simpler features into more complex ones.
•   Non-linearity also allows networks to approximate any continuous function
(Universal Approximation Theorem).
Comparison of Common Activation Functions (each 2 marks)
Activation   Formula   Advantages   Disadvantages
Smooth, outputs in
Vanishing gradient
[0,1]; interpretable as
Sigmoid   for large
probability
Zero-centered;
Vanishing gradient
Tanh   stronger gradients than
for large
sigmoid; smooth
Simple,
computationally   Dying ReLU
ReLU   f(x)=max(0,x)   efficient; mitigates   problem (neurons
vanishing gradient;   stuck at 0)
fast convergence
Prevents dying ReLU;   Not zero-centered;
Leaky   f(x)=x if x>0
allows small gradient   small negative slope
ReLU   else 0.01x
when x<0   may affect learning
Q7   a   Explain how information flows through a feedforward network during the forward   [10]
CO-2;   propagation process, describing the role of weights, biases, and activation functions in
BL-3   transforming inputs to outputs. Then, compute the output of the following FNN:
•   Network structure: 2 input neurons → 2 hidden neurons (ReLU activation) → 1
output neuron (ReLU activation).
•   Input: X=[1,0]
•   Weights and biases:
𝑊1 = [0.2 0.4 0.7], 𝑏1 = [0.1 0.2]
0.3
𝑊2 = [0.5 0.6] 𝑏2 = 0.1
Solution:
How Information flows in a feedforward network: (3 marks)
•   Inputs X are fed to the network layer-by-layer.
•   At each layer the neuron computes a linear combination of its inputs: Z=W X+b.
Here, each weight Wij scales the contribution from input j to neuron i.
********** 10 **********
--- page 11 ---
•   The bias b shifts the linear combination (acts like an adjustable intercept).
•   The result Z is passed through a non-linear activation function f to produce the
layer’s output (activation) A= f (Z).
•   The activation lets the network model non-linear relationships and controls
whether a neuron “fires.”
•   This activated output becomes the input to the next layer. For the final layer, the
activation may be linear (regression) or nonlinear (classification).
(A brief arrow diagram to be included similar to the following diagram) (2
marks)
Computation of the Output:
Network: 2 inputs → 2 hidden (ReLU) → 1 output (linear)
Step 1 : Linear combination at hidden layer (pre-activation Z1): (2 marks)
•   First hidden neuron: 0.2×1+0.4×0+0.1=0.2+0+0.1=0.3
•   Second hidden neuron: 0.3×1+0.7×0+0.2=0.3+0+0.2=0.5
Step 2: Apply ReLU activation to get hidden activations A1: (1 mark)
ReLU: ReLU(x)=max(0,x)
•   ReLU(0.3)=0.3
•   ReLU(0.5)=0.5
Step 3: Linear combination at output (pre-activation Z2) (1 mark)
Compute:
•   0.5×0.3=0.15
•   0.6×0.5=0.30
• Sum = 0.15+0.30=0.45
• Add bias: 0.45+0.1=0.55
Step 4: Output activation: output neuron uses linear activation, so final output
A2=Z2=0.55 ( 1 mark)
b   i. Explain how Convolutional Neural Networks (CNNs) extract hierarchical features from   [10]
Q7   an input image. Include the roles of convolutional, pooling, and fully connected layers
CO-3   in this process.
BL-2   ii. Discuss why CNNs are preferred over traditional fully connected Artificial Neural
Networks (ANNs) for image processing tasks.
iii. Describe how CNNs can be applied in Medical Image Analysis and Autonomous
Vehicles. Provide an example for each application and highlight the advantages of using
CNNs in these scenarios.
Solution:
How CNNs process images, explanation of convolutional, pooling, and fully connected
layers – (3 marks)
•   Convolutional Layers: Apply learnable filters/kernels to the input image to detect
local features like edges, corners, and textures. Early layers detect simple
features, middle layers detect patterns and shapes, and deeper layers detect high-
level features like objects or faces.
•   Pooling Layers: Perform downsampling (e.g., max pooling or average pooling) to
reduce spatial dimensions while retaining important features. Helps in
translational invariance and reduces computational cost.
•   Fully Connected (FC) Layers: Connect all neurons from the previous layer to
output neurons, performing high-level reasoning based on the features extracted
by convolutional and pooling layers. Map the learned hierarchical features to the
final classification or regression output.
Reason for preferring CNNs over ANNs (any three each 1 mark)
•   Parameter Efficiency: CNNs share weights via convolutional filters, reducing the
number of parameters compared to fully connected ANNs, which require separate
weights for each input neuron.
•   Spatial Feature Learning: CNNs exploit the spatial structure of images; they can
detect patterns regardless of their location. ANNs treat every pixel independently,
ignoring local spatial correlations.
•   Hierarchical Feature Extraction: CNNs automatically learn multi-level features,
whereas ANNs require manual feature engineering.
•   Better Generalization: Pooling layers and local connectivity improve robustness
and reduce overfitting, which is challenging for standard ANNs on high-
dimensional image data.
********** 11 **********
--- page 12 ---
Application 1 — Medical Image Analysis (example + advantage). (2 marks)
Application 2 — Autonomous Vehicles (example + advantage). (2 marks)
********** 12 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper e712441c821a

- Departments: Electronics and Telecommunication
- Programmes: MBATech (ELECTRONICS & TELECOMMUNICATIO
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/MBATech (ELECTRONICS & TELECOMMUNICATIO_ba3ceaa3/Deep Learning/ANS_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: mixed (12 pages), mean OCR confidence 33.0

````text
SYNOPTICS
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
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a.   i. Differentiate between Machine Learning and Deep Learning by explaining any four key   [5]
BL-2   differences between them. Support your answer with examples relevant to real-world
applications.
ii. Choose between machine learning or deep learning for the following tasks and justify:
1.Sentiment analysis on a dataset of 2,000 product reviews (short text).
2. Detecting fraudulent transactions in a financial dataset with labelled records.
3. Generating captions for a collection of 100,000 labelled images of natural scenes.
Solution:
Differentiate between Machine Learning and Deep Learning (2 marks)
Aspect   Machine Learning (ML)   Deep Learning (DL)
Requires large amounts of
1. Data   Works well with smaller,
labeled data for effective
Requirement   structured datasets.
training.
Features are manually   Learns features automatically
2. Feature
engineered by humans (e.g.,   through multiple neural network
Extraction
texture, color).   layers.
Uses simple models like
3. Model   Uses complex architectures like
Decision Trees, SVMs, or
Complexity   CNNs, RNNs, or Transformers.
Linear Regression.
4. Computational   Requires high computational
Can run efficiently on CPUs.
Power   resources (GPUs/TPUs).
Example   Spam email detection, credit   Image recognition, speech
Application   scoring.   translation, autonomous driving.
1. Sentiment analysis on a dataset of 2,000 product reviews (short text) (1 mark)
o   Choice: Machine Learning
o   Justification:
▪   The dataset is relatively small (2,000 entries), so deep learning
may overfit.
▪   Classical ML algorithms (e.g., Naive Bayes, SVM) can achieve
good accuracy on small text datasets with feature extraction
like TF-IDF or word embeddings.
2.   Detecting fraudulent transactions in a financial dataset with labeled records
(1 mark)
o   Choice: Machine Learning
o   Justification:
********** 1 **********
--- page 2 ---
▪   Fraud datasets are structured (tabular) and labeled, which is
well-suited for ML models like Random Forest, Gradient
Boosting, or Logistic Regression.
▪   Deep learning isn’t necessary unless the dataset is extremely
large or contains complex unstructured features.
3. Generating captions for a collection of 100,000 labeled images of natural
scenes (1 mark)
o   Choice: Deep Learning
o   Justification:
▪   Image captioning is a complex task requiring understanding of
visual content and natural language generation.
▪   Deep learning architectures like CNNs for image feature
extraction combined with RNNs/Transformers for text
generation are ideal.
The dataset is sufficiently large (100,000 images), making DL feasible.
CO-2;   b.   Researchers are developing a deep learning system for automated leaf Disease classification   [5]
BL-3   using images. During model design, they must choose an appropriate loss function for
training and evaluate how it behaves on specific predictions.
i. Discuss the major factors that influence the selection of a suitable loss function in
machine learning and deep learning applications.
ii. Suppose their classifier predicts the probability distribution for three Disease classes
(Normal, Mild, and Severe). For one validation image the true one-hot label is Mild
Disease (0,1,0). Their model outputs class probabilities [0.1, 0.8, 0.1]. Compute the
categorical cross-entropy for this sample and interpret it.
Solution:
Major factors that influence the selection (3 marks)
The decision mainly depends on
Task type & output form – classification (binary – cross entropy, multi class- categorical
cross entropy), regression (MSE/MAE)
Nature of the output – Continuous, categorical, etc.
Compatibility with activation function – e.g., softmax (cross-entropy).
Numerical (2 marks)
CO-2;   c.   i. Which regularization method leads to weight sparsity? Explain why.   [5]
BL-2   ii. You are training a deep convolutional neural network to classify images of handwritten
digits using the MNIST dataset. After several epochs, you notice that your training
accuracy is very high, but your validation accuracy is much lower. Explain how
applying Dropout can help in this situation. Describe what Dropout does during
training and how it affects the model’s performance and generalization ability.
Solution:
L1 regularization leads to weight sparsity (1 mark)
This comes from the shape of the L1 loss. Since even small weights are penalised the same
amount as large weights, more weight values will tend closer to 0. L2 on the other hand
penalizes smaller weights less, which leads to smaller weights but does not ensure sparsity.
Dropout (1 mark)
It is a regularization technique used in neural networks to prevent overfitting. During
training, it randomly “drops out” (i.e., sets to zero) a fraction of the neurons in a given layer
on each forward pass.
How applying Dropout can help in this situation (1 mark)
•   It adds noise to the training process, making the model more robust.
•   It reduces overfitting by preventing complex co-adaptations of neurons.
•   It improves generalization, leading to better validation accuracy.
How it affects the model’s performance and generalization ability (2 marks)
1. Random deactivation: During each forward pass, Dropout randomly deactivates some
neurons (along with their outgoing connections).
********** 2 **********
--- page 3 ---
2. Independent masks each iteration: On the next iteration (batch), a different random subset
of neurons is dropped.
This makes the model learn redundant representations — multiple different ways to extract
features.
3. Weight updates: Only the active neurons are updated during backpropagation.
Testing phase: Dropout is turned off during inference/validation. Instead, all neurons are
active, but their outputs are scaled down (by the dropout rate) to account for the reduced
activity during training.
CO-4;   d.   Describe how RNNs process sequential data, how they capture context between words, and   [5]
BL-2   why they are suitable for handling variable-length sentences. Explain how Recurrent Neural
Networks (RNNs) are used in language translation applications like Google Translate.
Solution:
Why Suitable for Translation: (2 marks)
RNNs can model temporal dependencies and understand word order, which are critical for
accurate translation. For example, “I am eating an apple” should not translate the same as
“An apple is eating me.”
Sequential Data Handling (1 mark): RNNs process input text word by word, keeping track
of previous words through hidden states. This helps capture context in translation, since the
meaning of a word depends on the words before and after it.
Context Learning (1 mark): As the RNN reads each word, it updates its hidden state to
reflect the overall meaning of the sentence so far. This enables it to generate context-aware
translations rather than translating each word in isolation.
Variable-Length Sequences (1 mark): RNNs can handle sentences of different lengths,
making them suitable for real-world translation where input and output sentences vary in
size. Encoder–Decoder Structure (Conceptually): The encoder RNN reads the source
language sentence and summarizes it into a context vector. The decoder RNN generates the
translated sentence word by word in the target language.
Q2   a   [10]
CO-2;
BL-3
Given a network with the following parameters
𝜃11 (1) = 0.5, 𝜃12 (1) = 0.5, 𝜃21 (1) = 0.5, 𝜃22 (1) = 0.5, 𝜃11 (2) = 0.25, 𝜃21 (2) = 0.25, 𝑏1 = 𝑏2 = 0.
All neurons have a Sigmoid activation function. The actual output at O is 1. Perform a
forward pass and backward pass to update weights of 𝜃11 (1), 𝜃11 (2) 𝑎𝑛𝑑 𝑏2 using Gradient
Descent algorithm (Assume learning rate = 0.5).
Solution
Forward pass (outh1, outo1, total error – each 1 mark)
Backward pass (updated 𝜃11 (1) , 𝜃11 (2)– each 2.5 marks and b2 – 2 mark)
********** 3 **********
--- page 4 ---
25) 4o Aru 2). =. 0-46

=-o4ek (©
&. 0:6 \> =
a ,-0°613) 29-015
= -ode) >
E Joube Yak ©

Hah ‘ ob yeah ot A
coast)Leest) (2)
A a = 7-084 |
dD >) () N att - o:25- (0S) Loony)
Wa Sas wD

2On _ 9.929235

FIC 7) IC HOH
--- page 5 ---
Q2   b   i. Discuss how skip connections in ResNet influence gradient flow, feature reuse, and help   [10]
CO-3;   in addressing the vanishing gradient problem during backpropagation.
BL-2   ii. Explain how the learning approach and feature extraction strategy of InceptionNet differ
from the AlexNet.
Solution:
Skip connection and its importance (5 marks)
Problem with Deep Networks: As networks became deeper, performance degraded due to
vanishing or exploding gradients, making training very deep networks difficult.
Concept of Residual Learning: ResNet introduced residual blocks where the network learns
a residual function F(x) = H(x) - x, so H(x) = F(x) + x. Skip connections directly add the
input to the output after a few convolutional layers.
Skip Connections and Vanishing Gradient Solution:
• Allow gradients to flow directly through identity paths.
• Prevent gradient vanishing in very deep networks (even 152+ layers).
• Improves training speed and convergence.
Comparison of InceptionNet and AlexNet (5 marks)
1. Learning Approach:
AlexNet follows a sequential, deep feedforward design where each layer processes the entire
output of the previous layer. It uses large convolutional filters (e.g., 11×11, 5×5) and learns
features in a hierarchical manner — from simple edges in early layers to complex shapes in
deeper ones.
InceptionNet, a parallel multi-branch architecture within each Inception module. It processes
the same input through multiple convolutional kernels (1×1, 3×3, 5×5) and a pooling path
********** 5 **********
--- page 6 ---
simultaneously. This allows the network to learn features at multiple spatial scales in a single
layer rather than relying on depth alone.
2. Feature Extraction Strategy:
AlexNet extracts one type of feature per layer, with fixed receptive field sizes determined by
kernel size.
InceptionNet captures a diverse set of features — fine details, textures, and global patterns
— by combining outputs from different kernel sizes.
Additionally, 1×1 convolutions in InceptionNet act as bottlenecks, reducing computational
cost while increasing nonlinearity and enabling more efficient feature mixing across
channels.
Q3   a   i. Determine the weights required to perform the classification as per the table using single   [10]
CO-2;   layer perceptron network. Assume learning rate is 1 and initial weights are 0. Consider
BL-3   threshold=0 and solve for 1 epoch.
X1   X2   X3   target
-1   1   -1   0
-1   1   1   1
1   -1   1   1
-1   1   1   1
ii. Illustrate the correspondence between components of a biological neuron and an
artificial neuron.
Solution:
Problem with formulas (7 marks)
X1 X2 X3   t   α   yin   y   Δ   Δ   Δ   Δb w1 w2 w3   b
w1 w2 w3
-1   1   -1   1   1   0   0   -1   1   -1   1   -1   1   -1   1
-1   1   1   1   1   2   1   0   0   0   0   -1   1   -1   1
1   -1   1   0   1   4   1   0   0   0   0   -1   1   -1   1
-1   -1   1   -1   1   0   0   1   1   -1   -1   0   2   -2   0
Correspondence (3 marks)
Artificial   Neuron
Biological Neuron   Analogy
(Perceptron)
Dendrites   Inputs (x1,x2,…,xn)   Receive signals
Determines   input
Synaptic Strength   Weights (w1,w2,…,wn)
importance
Soma (Cell Body)   Summation + Bias   Aggregates inputs
Activation Threshold   Activation Function   Decides if neuron “fires”
Axon   Output   Sends signal to next neuron
Q3   b A system is being designed for marking the attendance of students using face recognition.   [10]
CO-3;   This task is given to you. You and your team are planning to use convolutional neural network
BL-2   for this task, but the dataset provided to you is very small. Suggest and discuss different
approaches to handle this issue. How transfer learning can be applied to improve the model’s
performance in this situation.
Solution:
1. Data Augmentation – 4 Marks
Artificially increasing the dataset size by applying transformations such as rotation,
flipping, scaling, translation, brightness/contrast changes, or adding noise can help
the network learn robust features. This effectively increases diversity in the training
data, helping the model generalize better
2. Transfer learning – 6 Marks
Transfer learning involves using a pre-trained CNN (e.g., VGG16) that was trained
on a large face dataset. The early layers of these models have already learned
general feature representations like edges, textures, and facial patterns. You can
fine-tune the later layers on your small dataset, allowing the network to adapt to the
specific students in your system while reducing training time and avoiding
overfitting.
Q4   a   i. A neural network uses a dataset with 1000 samples and batch size of 100. If the learning   [10]
CO-2;   rate and other parameters remain constant, explain how many weight updates occur in:
BL-3   (i) Batch Gradient Descent
(ii) Stochastic Gradient Descent (SGD)
(iii)   Mini-Batch Gradient Descent
********** 6 **********
--- page 7 ---
ii.   Consider the cost function J(θ)=0.5𝜃2. Perform two iterations of SGD with Momentum,
where learning rate (η or α) is 0.1, momentum is 0.9, initial velocity 𝑣0=0, initial
parameter 𝜃0=1. Write the update rule and compute the velocity & parameter after each
iteration.
iii.   List the number of hyperparameters required in training a model using Stochastic
Gradient Descent with Momentum.
Solution:
(i)   Each 1 mark
Method   Weight Updates   Explanation
per Epoch
Batch GD   1   Entire dataset (1000 samples) is used
for one weight update per epoch
SGD   1000   Each sample updates weights
individually, so, 1000 updates per
epoch
Mini-Batch GD   1000 / 100 = 10   Dataset divided into 10 batches, so, 10
updates per epoch
(ii)   2 mark for update rule, 1 mark for correct derivative, 1 mark for first θ
and v update, 1 mark for second θ and v update. Partial marks for
intermediate correct calculations.
(iii)   Correct listing of hyperparameters – 2 marks
•   Learning Rate (η or α) – Controls the step size of each update.
•   Momentum Coefficient (μ or α) – Determines how much of the previous velocity is
retained to accelerate convergence.
•   Number of Epochs
Q4   b   i.   Define the vanishing gradient problem in RNNs. Why does it occur?   [10]
CO-4;   ii.   In a sentence like “The dogs barked at the thief and … were appreciated”, why
BL-2   does a simple RNN fail to predict the correct verb form?
iii.   Justify how the forget gate in LSTM helps preserve long-term dependencies.
iv.   Assuming that the forget gate output is ft=[0.1,0.9] and the previous cell state
Ct−1=[2,1], compute the updated cell memory contribution from the forget gate.
Solution:
i. Vanishing gradient problem: 3 marks
•   Gradients shrink exponentially across many time steps/layers.
•   Caused by repeated multiplication by smaller gradient values with across
many layers (e.g., saturating activations).
ii. Why simple RNN fails: 2 marks
•   Long-range dependency from plural subject to verb; simple RNN can’t
retain number info due to vanishing gradients.
•   In RNNs because of the vanishing gradients problem, for the outputs of
the errors associated with the later time steps to affect the computations
that are earlier.
iii. Forget gate :3 marks
• A forget gate is responsible for removing information from the cell state.
********** 7 **********
--- page 8 ---
•   The information that is no longer required for the LSTM to understand
things or the information that is of less importance is removed via
multiplication of a filter.
•   This is required for optimizing the performance of the LSTM network.
•   Keeps salient info (values near 1) and decays irrelevant memory (near
0).
iv. Numerical: 2 marks
•   Given ft= [0.1,0.9], Ct−1= [2,1]:
•   ft⊙Ct−1= [0.2,0.9]
Q5   a   With respect to LSTM, answer the following questions:   [10]
CO-4;   i.   Identify the purpose of each gate (input, forget, output) in an LSTM unit.
BL-2   ii.   Consider the sentence “Artificial Intelligence has revolutionized every domain.
The work force will have to update themselves to remain relevant.” Explain how
the input and forget gates update memory as context changes.
Given: it=0.7,  ft=0.4,  ot=0.8,  𝐶𝑡̃=0.9,  Ct−1=0.5. Compute the new cell state Ct and
hidden state ht. Assume ht=ot × tanh(Ct)
iii.   Why are LSTM models more effective for language modelling than simple
RNNs?
Solution:
i. Purpose of each gate: 3 marks
• Forget Gate (ft): A forget gate is responsible for removing information from
the cell state.
• The information that is no longer required for the LSTM to understand things
or the information that is of less importance is removed via multiplication of a
filter.
• This is required for optimizing the performance of the LSTM network.
• how much old memory to keep.
• Input/Update Gate: The update gate is responsible for the addition of
information to the cell state.
• how much new info 𝐶𝑡̃ to add.
• Output Gate (ot): job of selecting useful information from the current cell
state and showing it out as an output is done via the output gate.
• how much cell state to expose as hidden ht.
ii. Updation of input and forget gate: 3 marks
•   “Artificial Intelligence has revolutionized every domain. The work force”
context change
• When topic shifts, forget gate drops prior subject info; input gate admits new
subject (“work force”) into cell state (Ct).
Numerical :2 marks
• Given it=0.7, ft=0.4, ot=0.8, 𝐶𝑡=0.9, Ct−1=0.5:
Ct=0.4⋅0.5+0.7⋅0.9=0.2+0.63=0.83
ht=ot×tanh(Ct)=0.8×tanh(0.83)≈0.8×0.6805≈0.5444
iii. Interpretation: 2 marks
• Gating preserves long-range info, mitigates vanishing gradients → better
long-context predictions.
Q5   b   Explain the working principle of the AdaGrad optimizer. Write the update rule of AdaGrad.   [10]
CO-2;   List advantages and disadvantages of using AdaGrad compared to standard Stochastic
BL-2   Gradient Descent (SGD).
Solution
Working principle of the AdaGrad optimizer ( 2 marks)
AdaGrad (Adaptive Gradient Algorithm) is an adaptive learning rate optimization algorithm
that adjusts the learning rate for each parameter individually based on the historical gradients.
Parameters that receive frequent updates get a smaller learning rate. Parameters with
infrequent updates get a larger learning rate. It reduces the learning rate over time for
parameters with large accumulated gradients.
Update rule of AdaGrad (3 marks)
(OR)
********** 8 **********
--- page 9 ---
Role of Accumulated Squared Gradients (1 mark)
Reduces learning rate for parameters with large gradients. It increases learning rate for
parameters with small gradients and helps stabilize training and prevent oscillations along
steep directions.
Advantages: (2 marks)
•   Adaptive learning rates for each parameter, therefore, no need to manually tune
learning rate for each parameter.
•   Good for sparse data where some features appear infrequently.
•   Faster convergence in some cases due to adaptive step sizes.
Disadvantages: (2 marks)
•   Aggressive learning rate decay: Learning rate keeps decreasing, which may stop
learning prematurely. Can stop learning prematurely in long training sessions
•   Not ideal for non-convex problems where we need sustained learning over time.
• May require modifications like RMSProp or Adam to overcome the diminishing
learning rate problem.
• May not perform well on dense datasets
Q6   a   i. Consider input image of size 128 X 128 X 3.   [10]
CO-3;   1)   It is passed through convolution layer 1 with filter size 3x3, no. of filters =
BL-3   16, no padding and stride = 1.
2)   It is followed by pooling layer of mask size 2X2 with stride=2.
3) Then it is passed through convolution layer 2 with filter size 3X3, no. of
filters = 32, no padding and stride = 1.
4)   It is followed by pooling layer of mask size 2X2 with stride=2.
5) Further it is passed through fully connected layer 1 consisting of 240
neurons and then FC2 with 120 neurons.
6) Finally, SoftMax layer of 5 neurons is used. Calculate the size of activation
and trainable parameters at the end of each layer.
ii. Determine the output of the given 5x5 image after convoluting with the 3x3
kernel. Given padding=valid and stride=2
1   0   -1
2   0   -2
3   1   2   2   1   1   0   -1
2   1   2   1   0
3   2   1   0   1
0   3   0   1   2
1   1   0   2   3
Solution: 1 mark for each calculation
Conv layer → ((kernel_width × kernel_height × input_channels) + 1) × num_filters
Pooling layer → number of parameters = 0
FC→ (number of neurons in previous layer × number of neurons in current layer) + number
of biases
Size of   No of
Layer
activation   parameters
Input   128 × 128 × 3   0
Conv1 (3×3, 16 filters, stride=1,
126 × 126 × 16   448
valid)
Pool1 (2×2, s=2)   63 × 63 × 16   0
Conv2 (3×3, 32 filters, stride=1,
61 × 61 × 32   4,640
valid)
Pool2 (2×2, s=2)   30 × 30 × 32   0
Flatten   28,800   0
********** 9 **********
--- page 10 ---
FC1 (240 units)   240   6,912,240
FC2 (120 units)   120   28,920
SoftMax (5 units)   5   605
Total trainable parameters: 69,46,853.
Convolution operation (2 marks)
Q6   b   i. Explain the concept of activation functions in deep neural networks. Discuss the role of non-   [10]
CO-2;   linearity.
BL-3   ii. Compare the following activation functions: Sigmoid, Tanh, ReLU, and Leaky ReLU. Include
their advantages, disadvantages.
Solution:
Concept of Activation Functions (1 marks)
Mathematical functions applied to the output of each neuron. They determine whether a
neuron should be “activated” or not, i.e., whether its output should contribute to the next
layer. Without activation functions, a neural network would effectively behave like a linear
model, regardless of its depth, because a series of linear transformations can be combined
into a single linear function.
Activation functions introduce non-linearity, enabling the network to learn complex
patterns and hierarchical representations.
Role of Non-Linearity (1 marks)
•   Non-linear activation functions allow networks to model non-linear relationships
between inputs and outputs.
•   They enable feature abstraction across layers, letting deeper layers combine
simpler features into more complex ones.
•   Non-linearity also allows networks to approximate any continuous function
(Universal Approximation Theorem).
Comparison of Common Activation Functions (each 2 marks)
Activation   Formula   Advantages   Disadvantages
Smooth, outputs in
Vanishing gradient
[0,1]; interpretable as
Sigmoid   for large
probability
Zero-centered;
Vanishing gradient
Tanh   stronger gradients than
for large
sigmoid; smooth
Simple,
computationally   Dying ReLU
ReLU   f(x)=max(0,x)   efficient; mitigates   problem (neurons
vanishing gradient;   stuck at 0)
fast convergence
Prevents dying ReLU;   Not zero-centered;
Leaky   f(x)=x if x>0
allows small gradient   small negative slope
ReLU   else 0.01x
when x<0   may affect learning
Q7   a   Explain how information flows through a feedforward network during the forward   [10]
CO-2;   propagation process, describing the role of weights, biases, and activation functions in
BL-3   transforming inputs to outputs. Then, compute the output of the following FNN:
•   Network structure: 2 input neurons → 2 hidden neurons (ReLU activation) → 1
output neuron (ReLU activation).
•   Input: X=[1,0]
•   Weights and biases:
𝑊1 = [0.2 0.4 0.7], 𝑏1 = [0.1 0.2]
0.3
𝑊2 = [0.5 0.6] 𝑏2 = 0.1
Solution:
How Information flows in a feedforward network: (3 marks)
•   Inputs X are fed to the network layer-by-layer.
•   At each layer the neuron computes a linear combination of its inputs: Z=W X+b.
Here, each weight Wij scales the contribution from input j to neuron i.
********** 10 **********
--- page 11 ---
•   The bias b shifts the linear combination (acts like an adjustable intercept).
•   The result Z is passed through a non-linear activation function f to produce the
layer’s output (activation) A= f (Z).
•   The activation lets the network model non-linear relationships and controls
whether a neuron “fires.”
•   This activated output becomes the input to the next layer. For the final layer, the
activation may be linear (regression) or nonlinear (classification).
(A brief arrow diagram to be included similar to the following diagram) (2
marks)
Computation of the Output:
Network: 2 inputs → 2 hidden (ReLU) → 1 output (linear)
Step 1 : Linear combination at hidden layer (pre-activation Z1): (2 marks)
•   First hidden neuron: 0.2×1+0.4×0+0.1=0.2+0+0.1=0.3
•   Second hidden neuron: 0.3×1+0.7×0+0.2=0.3+0+0.2=0.5
Step 2: Apply ReLU activation to get hidden activations A1: (1 mark)
ReLU: ReLU(x)=max(0,x)
•   ReLU(0.3)=0.3
•   ReLU(0.5)=0.5
Step 3: Linear combination at output (pre-activation Z2) (1 mark)
Compute:
•   0.5×0.3=0.15
•   0.6×0.5=0.30
• Sum = 0.15+0.30=0.45
• Add bias: 0.45+0.1=0.55
Step 4: Output activation: output neuron uses linear activation, so final output
A2=Z2=0.55 ( 1 mark)
b   i. Explain how Convolutional Neural Networks (CNNs) extract hierarchical features from   [10]
Q7   an input image. Include the roles of convolutional, pooling, and fully connected layers
CO-3   in this process.
BL-2   ii. Discuss why CNNs are preferred over traditional fully connected Artificial Neural
Networks (ANNs) for image processing tasks.
iii. Describe how CNNs can be applied in Medical Image Analysis and Autonomous
Vehicles. Provide an example for each application and highlight the advantages of using
CNNs in these scenarios.
Solution:
How CNNs process images, explanation of convolutional, pooling, and fully connected
layers – (3 marks)
•   Convolutional Layers: Apply learnable filters/kernels to the input image to detect
local features like edges, corners, and textures. Early layers detect simple
features, middle layers detect patterns and shapes, and deeper layers detect high-
level features like objects or faces.
•   Pooling Layers: Perform downsampling (e.g., max pooling or average pooling) to
reduce spatial dimensions while retaining important features. Helps in
translational invariance and reduces computational cost.
•   Fully Connected (FC) Layers: Connect all neurons from the previous layer to
output neurons, performing high-level reasoning based on the features extracted
by convolutional and pooling layers. Map the learned hierarchical features to the
final classification or regression output.
Reason for preferring CNNs over ANNs (any three each 1 mark)
•   Parameter Efficiency: CNNs share weights via convolutional filters, reducing the
number of parameters compared to fully connected ANNs, which require separate
weights for each input neuron.
•   Spatial Feature Learning: CNNs exploit the spatial structure of images; they can
detect patterns regardless of their location. ANNs treat every pixel independently,
ignoring local spatial correlations.
•   Hierarchical Feature Extraction: CNNs automatically learn multi-level features,
whereas ANNs require manual feature engineering.
•   Better Generalization: Pooling layers and local connectivity improve robustness
and reduce overfitting, which is challenging for standard ANNs on high-
dimensional image data.
********** 11 **********
--- page 12 ---
Application 1 — Medical Image Analysis (example + advantage). (2 marks)
Application 2 — Autonomous Vehicles (example + advantage). (2 marks)
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 7f70bf2b3c31

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_AI_7012/Deep Learning/ANS_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: mixed (15 pages), mean OCR confidence 29.6

````text
SYNOPTICS
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
1. This question paper contains 15 pages.
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
Solution:
i) Two situations where deep learning models outperform traditional
machine learning algorithms (each 1 marks)
1. When working with unstructured and high-dimensional data: Deep
learning models (such as CNNs and RNNs) can automatically learn complex
patterns from images, audio, and text, whereas traditional ML models require
manual   feature   extraction. Example: Image   classification, speech
recognition, and natural language understanding.
2. When large volumes of labelled data are available: Deep learning requires
vast amounts of data to learn millions of parameters effectively. With
sufficient data and computational power, DL models outperform ML
algorithms in terms of accuracy and generalization. Example: Autonomous
driving, medical image analysis, and translation systems trained on huge
datasets.
ii. Application-based choice and justification (3 marks)
********** 1 **********
--- page 2 ---
Suitable
Application   Approa   Justification
ch
The dataset is small and features are
Machin   numerical and well-defined. Traditional
1. Predicting house
e   ML algorithms like Linear Regression
prices using 1,000
Learnin   or Random Forests perform well
structured records
g   without requiring large data or deep
architectures.
Involves processing image frames and
learning   spatial-temporal   features.
2.   Detecting
Deep   Deep   learning   models   such   as
emotions from facial
Learnin   Convolutional   Neural   Networks
expressions in real-
g   (CNNs) or 3D-CNNs can automatically
time video streams
extract   complex   visual   patterns,
outperforming ML methods.
Requires   understanding   long-range
language dependencies. Models like
3. Translating text
Deep   Recurrent Neural Networks (RNNs),
from one language to
Learnin LSTMs, or Transformers (e.g., Google
another (millions of
g   Translate) handle such   large-scale
sentence pairs)
sequential   data   far   better   than
traditional ML algorithms.
CO-2;   b.   i. Explain how   different   activation   functions   influence   gradient   [5]
BL-3   propagation, convergence behavior, and the overall performance of a deep
neural network.
ii. Discuss the scenarios or types of problems where specific activation
functions such as Sigmoid, Tanh, ReLU, and Leaky ReLU are preferred.
Solution:
Role of Activation Functions (2 marks): Activation functions introduce
non-linearity into deep neural networks. Without them, even multi-layer
networks behave like a single linear model and cannot learn complex
relationships.
Activation functions affect:
• Gradient propagation during backpropagation,
• Convergence speed during training, and
• Model performance and generalization.
Usage of activation functions (3 marks)
CO-2;   c.   i. Explain the role of L1 and L2 regularization in deep neural networks, and   [5]
BL-2   discuss how these techniques help prevent overfitting and improve the
model’s generalization to unseen data. You are training a fully connected
neural network layer with 4 neurons during training.
ii. The outputs of the neurons before applying dropout are: [0.8, −0.4, 0.6,
0.2]. A dropout rate of 50% is applied to this layer. Randomly determine
which neurons are dropped (assume a possible dropout mask) and
compute the output after applying dropout.
Solution:
Role of L1 and L2 regularization (2 mark)
Regularization is a technique used in deep learning to reduce overfitting by
discouraging the model from learning overly complex or large weight
values. It adds a penalty term to the loss function based on the magnitude of
the weights.
********** 2 **********
--- page 3 ---
The modified loss functions are:
• L1 Regularization (Lasso):
Adds the absolute value of the weights as a penalty.
• L2 Regularization (Ridge):
Adds the square of the weights as a penalty.
Here,
λ = regularization parameter (controls the strength of the penalty), wi=
weights of the model.
How They Help Prevent Overfitting (2 marks)
1. Controls weight magnitude: Both L1 and L2 regularization restrict
large weights, forcing the network to learn smaller and more general
weight values that perform better on unseen data.
2. Reduces model complexity:
o L1 tends to make many weights zero, leading to sparse models (some
neurons become inactive).
o L2 spreads weight values more evenly and helps smooth learning,
preventing any single weight from dominating.
By penalizing large weights, the network becomes less sensitive to noise,
improves generalization in the training data and performs better on test data
Output after dropout (1 mark)
Assume a random dropout mask (1 = keep, 0 = drop).
For example: mask=[1,0,1,0]
Multiply the neuron outputs by the mask:
output after dropout=[0.8x1, −0.4x0, 0.6x1, 0.2x0]=[0.8,0,0.6,0]
CO-4;   d. An e-commerce platform wants to automatically determine whether customer   [5]
BL-2   reviews are positive, negative, or neutral. Explain how an RNN model
processes customer review text to perform sentiment classification. Why is
RNN suitable for this task, and what role does word order play in determining
sentiment?
Solution:
How an RNN processes customer review text to perform sentiment
classification (2 marks)
• In sentiment analysis, a review (e.g., “The product is not good”) is treated
as a sequence of words.
• Each word is converted into a numerical vector (using embeddings like
Word2Vec or GloVe).
• The RNN reads these words sequentially, one at a time, maintaining a
hidden state that stores information from previous words.
• As the sequence progresses, the hidden state accumulates contextual
information — understanding how earlier words influence the meaning
of later ones.
• After processing the entire review, the final hidden state represents the
overall context and sentiment of the sentence.
• This representation is then passed to a fully connected (dense) layer with
a softmax activation to classify the sentiment as positive, negative, or
neutral.
Why RNN is suitable for sentiment analysis: (2 marks)
********** 3 **********
--- page 4 ---
RNNs are designed to handle sequential and contextual data, making them
ideal for text where word order and context matter. They can capture
dependencies between words that are far apart (e.g., “not good” vs. “good”).
Unlike traditional feedforward networks, RNNs remember what came before
in the sentence, giving them the ability to understand contextual polarity.
Role of word order in sentiment detection: (1 mark)
Word order changes meaning. For example: This phone is not bad” →
positive sentiment.
“This phone is bad” → negative sentiment.
RNNs preserve this order by processing words sequentially, ensuring that the
position of each word affects the final interpretation.
If the model ignored order, it might misclassify sentences with negations or
complex phrasing.
Q2   a   [10]
CO-2;
BL-3
The given network with the following i1= 0.25, i2= 0.7, w1= 0.2, w2=0.15,
w3= 0.28, w4=0.3, w5= 0.1, w6= 0.24, w7 = 0.12, w8= 0.21, b1= 1 and b2=1.
All neurons have a Sigmoid activation function. The actual output at O1 is
0.7 and at O2 is 0.3. Perform a forward pass and backward pass to update
weights of w1, w5 and w7 using Gradient Descent algorithm (Assume
learning rate = 1).
Solution:
Forward pass (outh1, outo1, total error – each 1 mark)
Backward pass (updated w7 and w5 - each 2 marks, and w1 – 3 marks)
********** 4 **********
--- page 5 ---
aod gos |
5\\o
gat ‘(1
at Te eh
panterdx ose | y
= pe (2>)* 3)

iy zi \\55
ale Ta cles Tees
la he Tae

[oct]
[oct]

O1 7 we ae 16 or: ad
ti . Dales a ey eae
e
te: uae 2) Co. | ie
t 2) fo * CAEWIV
23
= Aten =
(on arent) 0-18
Ea ahs (a

. sien sen tace

ae

HEA o-2Y4ol
=O NES
> ubor gabe
setae 88 STE AR one
ad at cubo, ) G* 0) O- cares:

Ow4 Fs

ait hye"

DO o- eae

-o-> lo © es

=0-062 5
- abt . ore -() (0-04) oe
wy = Pana ies
ste _ 2EE yD pokey x Dubey anit oy
BEE = Faro, ame, Pe

acre) (esky i-ested CH)
peer tomy Corey(etey(e Lest tf

2K
FIR Fok aC i Gk
--- page 6 ---
Q2   b   i. Explain how AlexNet’s design improved upon earlier traditional CNNs [10]
CO-3;   in terms of regularization, and training methodology.
BL-2   ii. Discuss how the Inception Network captures features at multiple scales
efficiently and the role of 1×1 convolutions in enhancing both
computational efficiency and feature representation in deep CNNs.
iii. Based on your analysis, which architecture would you recommend for
classification of large-scale image dataset and why?
Solution:
AlexNet (2012): (4 marks)
• Regularization Techniques: Introduced Dropout in fully connected layers
to prevent overfitting by randomly deactivating neurons during training.
Applied Data Augmentation (image translations, reflections, and patch
extractions) to improve generalization.
• Training Methodology: Adopted ReLU (Rectified Linear Unit) activation
instead of sigmoid/tanh, avoiding vanishing gradients and speeding up
training. Trained on GPUs, which significantly reduced training time for
large datasets. Used Local Response Normalization (LRN) to encourage
competition among neurons and improve generalization.
Inception Network (GoogleNet, 2014): (4 marks)
• Inception Modules: Each module applied 1×1, 3×3, and 5×5 convolutions
in parallel, along with a max-pooling branch. Captured features at multiple
spatial scales simultaneously, improving representational richness.
• Dimensionality Reduction: Introduced 1×1 convolutions before expensive
3×3 and 5×5 filters to reduce the number of channels, drastically lowering
computation and parameters.
• Depth with Efficiency: Built a 22-layer deep network but used only about
5 million parameters (vs. 60 million in AlexNet). Replaced fully connected
layers with global average pooling, reducing overfitting and model size.
• Regularization: Employed ReLU activations and dropout for stability and
generalization
• Performance: Achieved top-5 error rate of 6.7% on ImageNet.
Analysis (2 marks)
Both models revolutionized computer vision, AlexNet demonstrated the
power of deep CNNs, and Inception showed deep networks could be efficient
and scalable.
Q3   a   i. Determine the weights required to perform the classification as per the [10]
CO-2;   table using single layer perceptron network. Assume learning rate is 1 and
BL-3   initial weights are 0. Consider threshold=0 and solve for 1 epoch.
********** 6 **********
--- page 7 ---
X1   X2   X3   target
-1   1   -1   -1
1   1   1   1
-1   -1   1   -1
-1   1   1   -1
ii. Discuss its limitations and provide suitable examples to illustrate these
limitations.
Solution:
Problem with formulas (7 marks)
X X X   t   α   yi   y Δ Δ Δ Δ w w w   b
1   2   3   n   w w w   b   1   2   3
1   2   3
-1   1   -1   -1   1   0   0   1   -1   1   -1   1   -1   1   -1
1   1   1   1   1   0   0   1   1   1   1   2   0   2   0
-1   -1   1   -1   1   4   1   -1   1   -1   -1   1   1   1   -1
-1   1   1   -1   1   0   0   0   0   0   0   2   0   0   2
Limitations and explanation with examples (3 marks)
•   Single-Layer Perceptron cannot classify non-linearly separable data
points.
• Complex problems, that involve a lot of parameters cannot be
solved by Single-Layer Perceptron.
Q3   b   How to decide number of filters in CNN? How it will influence the following [10]
CO-3;   parameters. 1) feature extraction capability, 2) dimensionality, 3)
BL-2   computational and memory cost, 4) risk of overfitting, 5) Hierarchical
Feature Learning.
Solution:
Each point for 2 marks
The number of filters in a CNN is often determined empirically through
experimentation, balancing model complexity and performance on the
validation set.
The depth of a convolutional layer—defined by the number of filters (or
kernels)—plays important role in determining the learning capacity of a
Convolutional Neural Network (CNN). Here's how:
1. Feature Extraction Capacity
• Each filter in a convolutional layer learns to detect a specific type of
feature (e.g., edges, textures, shapes etc.).
• More filters = more diverse features can be learned from the input
data.
•   This increases the representational power of the network, allowing it
to capture more complex patterns.
2. Dimensionality of Feature Maps
• The output of a convolutional layer is a set of feature maps, one for
each filter.
•   Increasing the number of filters increases the depth of the output
volume, which extracts richer information into subsequent layers.
3. Computational and Memory Cost
•   Increasing depth also increases the number of trainable parameters
(weights and biases).
•   This leads to higher computational cost, memory usage, and slower
training.
•   This leads to longer training times and greater memory usage,
especially in deeper networks.
4. Risk of Overfitting
********** 7 **********
--- page 8 ---
• A very deep layer with many filters might overfit the training data,
especially if the dataset is small or lacks diversity.
•   Regularization techniques can be used to address this issue.
5. Hierarchical Feature Learning
•   In early layers, filters typically learn low-level features (edges,
colours).
•   In deeper layers, filters learn high-level features (object parts,
shapes).
•   Increasing depth in later layers helps the network understand abstract
concepts.
Q4   a   i.   Illustrate how batch gradient descent and Stochastic Gradient Descent   [10]
CO-2;   (SGD) differ in terms of 1) oscillations in the loss function (with
BL-3   diagram/graph), 2) memory usage, and 3) suitability for large datasets.
ii. Discuss the impact of the learning rate being too high or too low during
training.
iii. Consider the cost function J(θ)=0.7𝜃3. Perform two iterations of SGD,
where learning rate (η or α) is 0.1, initial parameter 𝜃0=1. Write the
update rule and compute the updated parameter after each iteration.
Solution:
(i)   Three differences ( 3 marks)
Aspect   Batch Gradient Descent   Stochastic Gradient
(BGD)   Descent (SGD)
Oscillations   Smooth convergence;   Loss fluctuates a lot due to
in Loss   smaller oscillations   single-sample updates
Memory   High; needs to load entire   Low; processes one or few
Usage   dataset in memory   samples at a time
Suitability   Less suitable; slow and   More suitable; can handle
for Large   memory intensive   large datasets efficiently
Datasets
(ii)   Learning rate (2 marks)
Learning   Effect
Rate
Too high   Overshooting minima → may diverge or oscillate
without convergence
Too low   Very slow convergence → training may take too long
(iii)   Problem (5 marks)
********** 8 **********
--- page 9 ---
Q4   b   With reference to Gated Recurrent Unit (GRU) answer the following [10]
CO-4;   questions:
BL-2   i.   State the difference between LSTM and GRU in terms of architecture
and number of gates.
ii. Why is GRU computationally more efficient for smaller datasets?
iii.   Explain how GRUs “decide” to skip irrelevant tokens in a text
sequence.
iv.   Justify the advantage of bidirectional RNNs.
Solution:
i.   Difference: 3 marks
• LSTM: 3 gates (input, forget, output) + explicit cell state.
• GRU: 2 gates (update z, reset r); merges cell/hidden → simpler.
ii.   Computational efficiency of GRU: 2 marks
• Fewer parameters → faster training, less overfitting, adequate
capacity for shorter sequences.
iii.   Skipping irrelevant tokens :3 marks
• GRUs skip irrelevant tokens using their update (zt) and reset (rt)
gates.
• When a token provides little new information, zt is small — the
hidden state barely changes, effectively skipping that word.
• Similarly, rt can reduce the influence of past states if old information
is no longer relevant.
• This gating mechanism allows GRUs to focus on meaningful words
and ignore filler tokens in text sequences.
iv.   Advantage of bidirectional RNN: 2 marks
• Bidirectional RNN processes a sequence in both directions —
• forward (left → right) using past context, and
• backward (right → left) using future context.
This dual processing allows the model to consider information from the
entire sequence before making a prediction at any time step.
• In many NLP tasks (like named entity recognition, speech
recognition, or translation), the meaning of a word depends on both
what comes before and after it.
********** 9 **********
--- page 10 ---
Q5   a.   i.   Explain why a feedforward neural network fails to capture sequential [10]
CO-4;   context in language modelling.
BL-2   ii.   Describe how a recurrent connection in an RNN overcomes this
limitation.
iii.   Consider a RNN with a single hidden layer. Calculate the output of
the hidden layer ht given the following values: (use tanh as activation
function)
Wxh= [0.6 0.4   , Whh= [0.5 0.3 ht-1=[0 xt=[0
0.3 0.7]   0.2   0.4],   1],   1]
iv.   Explain how RNN-based language models predict the next word
probability distribution in a sentence.
Solution:
i. Why neural network fails: 2 marks
• Decisions are based on current input
• No memory about the past
• No future scope
ii. How RNN overcomes: 2 marks
• Can handle sequential data
• Considers current input as well as past inputs using memory
(recurrent connections) ht=f(xt,ht−1)
iii. Numerical :3 marks
ht=tanh(Wxhxt+Whhht−1)
iv. How RNN predicts next word: 3 marks
•   Uses hidden state ht to parameterize P(wt+1∣w≤t) =
Softmax(Whht+b).
•   Trained with cross-entropy over true next token; left-to-right
factorization of sentence probability.
•   wt+1: the next word the model is trying to predict.
•   w≤t: all previous words in the sentence (the context).
•   ht: the hidden state at time step t, which summarizes all the
contextual information from w1,w2,…,wt.
********** 10 **********
--- page 11 ---
•   Wh: a weight matrix that transforms this hidden state into a vector
of scores, one per word in the vocabulary.
•   b: a bias term.
•   Softmax: converts those scores into probabilities over the
vocabulary.
•   This mechanism allows the model to generate sentences word by
word, always conditioning on all previous words.
Q5   b   Explain the working principle of the RMSProp optimizer. Write the update [10]
CO-2;   rule and explain the role of the accumulated squared gradients. List
BL-2   advantages and disadvantages of RMSProp compared to standard SGD.
Solution:
Working Principle of RMSProp (3 marks)
RMSProp (Root Mean Square Propagation) is an adaptive learning rate
optimizer that improves upon AdaGrad. Its key idea is to maintain a moving
average of the squared gradients to scale the learning rate for each parameter
individually. This prevents the learning rate from diminishing too quickly,
which is a problem with AdaGrad.
RMSProp Update Rule (3 marks)
Where ρ is the decay rate and δ is a small constant to avoid division by zero.
(OR)
Where β is the decay rate and ɛ is a small constant to avoid division by zero
Role of Accumulated Squared Gradients (2 marks)
Reduces learning rate for parameters with large gradients. It increases
learning rate for parameters with small gradients and helps stabilize training
and prevent oscillations along steep directions.
Advantage and disadvantages (2 marks)
Advantages of RMSProp: (i) Addresses diminishing learning rate of
AdaGrad (ii) Adapts learning rate based on recent gradients
Disadvantages of RMSProp: (i) Can still get stuck in local minima on non-
convex problems (ii) Requires tuning of decay rate
Q6   a   Consider the CNN for binary classification as below. Compute the shape of   [10]
CO-3;   the output volume dimension and trainable parameters at each layer.
BL-3
Layer   Volume   No of
Dimension   parameters
Input   256 X 256 X 3
Conv2D
Filter = 32, stride = 1,
Kernel Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 64, stride = 1,
Kernel Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
********** 11 **********
--- page 12 ---
Filter = 128, stride = 1,
Kernel Size = 5x5,
padding=1
Pool2D Kernel Size = 2,
stride = 2
Flatten
Fully connected dense units
= 84
Fully connected dense units
= 32
Output
Solution: 1 mark for each calculation
Conv layer → ((kernel_width × kernel_height × input_channels) + 1) ×
num_filters
Pooling layer → number of parameters = 0
FC→ (number of neurons in previous layer × number of neurons in current
layer) + number of biases
Layer   Volume   No of
Dimension   parameters
Input   256 × 256 × 3   0
Conv2D
Filter = 32, stride = 1,   252 × 252 × 32   2,432
Kernel Size = 5X5
Pool2D Kernel Size = 2,
126 × 126 × 32   0
stride = 2
Conv2D
Filter = 64, stride = 1,   122 × 122 × 64   51,264
Kernel Size = 5X5
Pool2D Kernel Size = 2,
61 × 61 × 64   0
stride = 2
Conv2D
Filter = 128, stride = 1,
59 × 59 × 128   73,856
Kernel Size = 5x5,
padding=1
Pool2D Kernel Size = 2,
29 × 29 × 128   0
stride = 2
Flatten   29 × 29 × 128
0
= 1,07,648
Fully connected dense units
84 (vector)   9,042,516
= 84
Fully connected dense units
32 (vector)   2,720
= 32
Output   1 (vector)   33
Total trainable parameters: 91,72,821.
********** 12 **********
--- page 13 ---
Q6   b   Fully connected Neural Network with 10-layer is training using the sigmoid [10]
CO-2;   activation function.
BL-3   i. What is the activation output f (6)?
ii. What is the first derivative of gradient f 1(x) at x=6?
iii. Explain how this affects backpropagation in deeper layers.
iv. Solve the SoftMax values for y= [2.3, 4.5, 3.2]
Solution: f(6) ( 1mark)
Derivative (1 mark)
Interpretation: (1 mark)
The gradient is very small (~0.0025). In a deep network, multiplying many
such small gradients leads to the vanishing gradient problem (weights in
earlier layers barely update).
Compare the Loss function vs the Activation function.
Soft max values (2 marks)
Q7   a   Differentiate between single-layer and multi-layer feedforward neural [10]
CO-2;   networks. Explain the importance of non-linearity in hidden layers. Illustrate
BL-3   your answer by computing the output of a feedforward neural network with
the following configuration:
•   Structure: 3 input neurons → 2 hidden neurons (sigmoid activation)
→ 1 output neuron (sigmoid activation)
•   Input: X=[0.5,0.2,0.1]
• Weights and biases:
𝑊1 = [0.1 0.4 0.2 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.6 0.9], 𝑏2 = 0.5
0.3 0.5
Solution:
Difference (any three points - each 1 mark)
Aspect   Single-layer FNN   Multi-layer FNN
********** 13 **********
--- page 14 ---
Architecture   Has only one layer of Has one or more hidden
weights connecting   layers between input and
inputs directly to   output layers.
outputs.
Computation   Performs only a   Performs successive linear
linear mapping of   and nonlinear
input to output.   transformations, enabling
complex mappings.
Representatio   Can only solve   Can approximate non-linear
n Power   linearly separable   and complex functions
problems.   (universal approximators).
Activation   Typically linear.   Non-linear activations (e.g.,
Function   ReLU, Sigmoid, Tanh) used
in hidden layers.
Importance of Non-linearity (any two points- each 1 mark)
•   Without non-linear activation functions, a multi-layer network
collapses mathematically into an equivalent single-layer linear model
(since a composition of linear functions is still linear).
•   Non-linearity (e.g., sigmoid) allows the network to capture complex
patterns, decision boundaries, and feature interactions.
•   It enables hierarchical feature learning — each layer extracts
progressively more abstract representations.
Compute for each hidden neuron: (each step 1 mark)
For hidden neuron 1:
Z11 = (0.1)(0.5)+(0.4)(0.2)+(0.2)(0.1)+0.1= 0.25
b   Explain the concept of Transfer Learning using CNNs. Describe how pre-   [10]
Q7   trained models can be adapted for a new image classification task. Explain
CO-3   with any example model.
BL-2   Solution:
Concept Explanation (3 Marks):
Steps Involved (4 Marks):
1. Select a pre-trained model (e.g., VGG16, ResNet50, InceptionV3).
2. Load pre-trained weights trained on ImageNet or similar dataset.
3. Freeze base layers to retain generic features.
********** 14 **********
--- page 15 ---
4. Add new layers (Dense/SoftMax) to suit the new classification task.
5. Compile and train the model on the new dataset.
6. Fine-tune (optional): Unfreeze some deeper layers and retrain with
a small learning rate.
Example (3 Marks):
A suitable example using any pretrained VGG16, ResNet50, InceptionV3
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 50dce21bdc43

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_AI_7051/Deep Learning/ANS_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: mixed (15 pages), mean OCR confidence 29.6

````text
SYNOPTICS
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
1. This question paper contains 15 pages.
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
Solution:
i) Two situations where deep learning models outperform traditional
machine learning algorithms (each 1 marks)
1. When working with unstructured and high-dimensional data: Deep
learning models (such as CNNs and RNNs) can automatically learn complex
patterns from images, audio, and text, whereas traditional ML models require
manual   feature   extraction. Example: Image   classification, speech
recognition, and natural language understanding.
2. When large volumes of labelled data are available: Deep learning requires
vast amounts of data to learn millions of parameters effectively. With
sufficient data and computational power, DL models outperform ML
algorithms in terms of accuracy and generalization. Example: Autonomous
driving, medical image analysis, and translation systems trained on huge
datasets.
ii. Application-based choice and justification (3 marks)
********** 1 **********
--- page 2 ---
Suitable
Application   Approa   Justification
ch
The dataset is small and features are
Machin   numerical and well-defined. Traditional
1. Predicting house
e   ML algorithms like Linear Regression
prices using 1,000
Learnin   or Random Forests perform well
structured records
g   without requiring large data or deep
architectures.
Involves processing image frames and
learning   spatial-temporal   features.
2.   Detecting
Deep   Deep   learning   models   such   as
emotions from facial
Learnin   Convolutional   Neural   Networks
expressions in real-
g   (CNNs) or 3D-CNNs can automatically
time video streams
extract   complex   visual   patterns,
outperforming ML methods.
Requires   understanding   long-range
language dependencies. Models like
3. Translating text
Deep   Recurrent Neural Networks (RNNs),
from one language to
Learnin LSTMs, or Transformers (e.g., Google
another (millions of
g   Translate) handle such   large-scale
sentence pairs)
sequential   data   far   better   than
traditional ML algorithms.
CO-2;   b.   i. Explain how   different   activation   functions   influence   gradient   [5]
BL-3   propagation, convergence behavior, and the overall performance of a deep
neural network.
ii. Discuss the scenarios or types of problems where specific activation
functions such as Sigmoid, Tanh, ReLU, and Leaky ReLU are preferred.
Solution:
Role of Activation Functions (2 marks): Activation functions introduce
non-linearity into deep neural networks. Without them, even multi-layer
networks behave like a single linear model and cannot learn complex
relationships.
Activation functions affect:
• Gradient propagation during backpropagation,
• Convergence speed during training, and
• Model performance and generalization.
Usage of activation functions (3 marks)
CO-2;   c.   i. Explain the role of L1 and L2 regularization in deep neural networks, and   [5]
BL-2   discuss how these techniques help prevent overfitting and improve the
model’s generalization to unseen data. You are training a fully connected
neural network layer with 4 neurons during training.
ii. The outputs of the neurons before applying dropout are: [0.8, −0.4, 0.6,
0.2]. A dropout rate of 50% is applied to this layer. Randomly determine
which neurons are dropped (assume a possible dropout mask) and
compute the output after applying dropout.
Solution:
Role of L1 and L2 regularization (2 mark)
Regularization is a technique used in deep learning to reduce overfitting by
discouraging the model from learning overly complex or large weight
values. It adds a penalty term to the loss function based on the magnitude of
the weights.
********** 2 **********
--- page 3 ---
The modified loss functions are:
• L1 Regularization (Lasso):
Adds the absolute value of the weights as a penalty.
• L2 Regularization (Ridge):
Adds the square of the weights as a penalty.
Here,
λ = regularization parameter (controls the strength of the penalty), wi=
weights of the model.
How They Help Prevent Overfitting (2 marks)
1. Controls weight magnitude: Both L1 and L2 regularization restrict
large weights, forcing the network to learn smaller and more general
weight values that perform better on unseen data.
2. Reduces model complexity:
o L1 tends to make many weights zero, leading to sparse models (some
neurons become inactive).
o L2 spreads weight values more evenly and helps smooth learning,
preventing any single weight from dominating.
By penalizing large weights, the network becomes less sensitive to noise,
improves generalization in the training data and performs better on test data
Output after dropout (1 mark)
Assume a random dropout mask (1 = keep, 0 = drop).
For example: mask=[1,0,1,0]
Multiply the neuron outputs by the mask:
output after dropout=[0.8x1, −0.4x0, 0.6x1, 0.2x0]=[0.8,0,0.6,0]
CO-4;   d. An e-commerce platform wants to automatically determine whether customer   [5]
BL-2   reviews are positive, negative, or neutral. Explain how an RNN model
processes customer review text to perform sentiment classification. Why is
RNN suitable for this task, and what role does word order play in determining
sentiment?
Solution:
How an RNN processes customer review text to perform sentiment
classification (2 marks)
• In sentiment analysis, a review (e.g., “The product is not good”) is treated
as a sequence of words.
• Each word is converted into a numerical vector (using embeddings like
Word2Vec or GloVe).
• The RNN reads these words sequentially, one at a time, maintaining a
hidden state that stores information from previous words.
• As the sequence progresses, the hidden state accumulates contextual
information — understanding how earlier words influence the meaning
of later ones.
• After processing the entire review, the final hidden state represents the
overall context and sentiment of the sentence.
• This representation is then passed to a fully connected (dense) layer with
a softmax activation to classify the sentiment as positive, negative, or
neutral.
Why RNN is suitable for sentiment analysis: (2 marks)
********** 3 **********
--- page 4 ---
RNNs are designed to handle sequential and contextual data, making them
ideal for text where word order and context matter. They can capture
dependencies between words that are far apart (e.g., “not good” vs. “good”).
Unlike traditional feedforward networks, RNNs remember what came before
in the sentence, giving them the ability to understand contextual polarity.
Role of word order in sentiment detection: (1 mark)
Word order changes meaning. For example: This phone is not bad” →
positive sentiment.
“This phone is bad” → negative sentiment.
RNNs preserve this order by processing words sequentially, ensuring that the
position of each word affects the final interpretation.
If the model ignored order, it might misclassify sentences with negations or
complex phrasing.
Q2   a   [10]
CO-2;
BL-3
The given network with the following i1= 0.25, i2= 0.7, w1= 0.2, w2=0.15,
w3= 0.28, w4=0.3, w5= 0.1, w6= 0.24, w7 = 0.12, w8= 0.21, b1= 1 and b2=1.
All neurons have a Sigmoid activation function. The actual output at O1 is
0.7 and at O2 is 0.3. Perform a forward pass and backward pass to update
weights of w1, w5 and w7 using Gradient Descent algorithm (Assume
learning rate = 1).
Solution:
Forward pass (outh1, outo1, total error – each 1 mark)
Backward pass (updated w7 and w5 - each 2 marks, and w1 – 3 marks)
********** 4 **********
--- page 5 ---
aod gos |
5\\o
gat ‘(1
at Te eh
panterdx ose | y
= pe (2>)* 3)

iy zi \\55
ale Ta cles Tees
la he Tae

[oct]
[oct]

O1 7 we ae 16 or: ad
ti . Dales a ey eae
e
te: uae 2) Co. | ie
t 2) fo * CAEWIV
23
= Aten =
(on arent) 0-18
Ea ahs (a

. sien sen tace

ae

HEA o-2Y4ol
=O NES
> ubor gabe
setae 88 STE AR one
ad at cubo, ) G* 0) O- cares:

Ow4 Fs

ait hye"

DO o- eae

-o-> lo © es

=0-062 5
- abt . ore -() (0-04) oe
wy = Pana ies
ste _ 2EE yD pokey x Dubey anit oy
BEE = Faro, ame, Pe

acre) (esky i-ested CH)
peer tomy Corey(etey(e Lest tf

2K
FIR Fok aC i Gk
--- page 6 ---
Q2   b   i. Explain how AlexNet’s design improved upon earlier traditional CNNs [10]
CO-3;   in terms of regularization, and training methodology.
BL-2   ii. Discuss how the Inception Network captures features at multiple scales
efficiently and the role of 1×1 convolutions in enhancing both
computational efficiency and feature representation in deep CNNs.
iii. Based on your analysis, which architecture would you recommend for
classification of large-scale image dataset and why?
Solution:
AlexNet (2012): (4 marks)
• Regularization Techniques: Introduced Dropout in fully connected layers
to prevent overfitting by randomly deactivating neurons during training.
Applied Data Augmentation (image translations, reflections, and patch
extractions) to improve generalization.
• Training Methodology: Adopted ReLU (Rectified Linear Unit) activation
instead of sigmoid/tanh, avoiding vanishing gradients and speeding up
training. Trained on GPUs, which significantly reduced training time for
large datasets. Used Local Response Normalization (LRN) to encourage
competition among neurons and improve generalization.
Inception Network (GoogleNet, 2014): (4 marks)
• Inception Modules: Each module applied 1×1, 3×3, and 5×5 convolutions
in parallel, along with a max-pooling branch. Captured features at multiple
spatial scales simultaneously, improving representational richness.
• Dimensionality Reduction: Introduced 1×1 convolutions before expensive
3×3 and 5×5 filters to reduce the number of channels, drastically lowering
computation and parameters.
• Depth with Efficiency: Built a 22-layer deep network but used only about
5 million parameters (vs. 60 million in AlexNet). Replaced fully connected
layers with global average pooling, reducing overfitting and model size.
• Regularization: Employed ReLU activations and dropout for stability and
generalization
• Performance: Achieved top-5 error rate of 6.7% on ImageNet.
Analysis (2 marks)
Both models revolutionized computer vision, AlexNet demonstrated the
power of deep CNNs, and Inception showed deep networks could be efficient
and scalable.
Q3   a   i. Determine the weights required to perform the classification as per the [10]
CO-2;   table using single layer perceptron network. Assume learning rate is 1 and
BL-3   initial weights are 0. Consider threshold=0 and solve for 1 epoch.
********** 6 **********
--- page 7 ---
X1   X2   X3   target
-1   1   -1   -1
1   1   1   1
-1   -1   1   -1
-1   1   1   -1
ii. Discuss its limitations and provide suitable examples to illustrate these
limitations.
Solution:
Problem with formulas (7 marks)
X X X   t   α   yi   y Δ Δ Δ Δ w w w   b
1   2   3   n   w w w   b   1   2   3
1   2   3
-1   1   -1   -1   1   0   0   1   -1   1   -1   1   -1   1   -1
1   1   1   1   1   0   0   1   1   1   1   2   0   2   0
-1   -1   1   -1   1   4   1   -1   1   -1   -1   1   1   1   -1
-1   1   1   -1   1   0   0   0   0   0   0   2   0   0   2
Limitations and explanation with examples (3 marks)
•   Single-Layer Perceptron cannot classify non-linearly separable data
points.
• Complex problems, that involve a lot of parameters cannot be
solved by Single-Layer Perceptron.
Q3   b   How to decide number of filters in CNN? How it will influence the following [10]
CO-3;   parameters. 1) feature extraction capability, 2) dimensionality, 3)
BL-2   computational and memory cost, 4) risk of overfitting, 5) Hierarchical
Feature Learning.
Solution:
Each point for 2 marks
The number of filters in a CNN is often determined empirically through
experimentation, balancing model complexity and performance on the
validation set.
The depth of a convolutional layer—defined by the number of filters (or
kernels)—plays important role in determining the learning capacity of a
Convolutional Neural Network (CNN). Here's how:
1. Feature Extraction Capacity
• Each filter in a convolutional layer learns to detect a specific type of
feature (e.g., edges, textures, shapes etc.).
• More filters = more diverse features can be learned from the input
data.
•   This increases the representational power of the network, allowing it
to capture more complex patterns.
2. Dimensionality of Feature Maps
• The output of a convolutional layer is a set of feature maps, one for
each filter.
•   Increasing the number of filters increases the depth of the output
volume, which extracts richer information into subsequent layers.
3. Computational and Memory Cost
•   Increasing depth also increases the number of trainable parameters
(weights and biases).
•   This leads to higher computational cost, memory usage, and slower
training.
•   This leads to longer training times and greater memory usage,
especially in deeper networks.
4. Risk of Overfitting
********** 7 **********
--- page 8 ---
• A very deep layer with many filters might overfit the training data,
especially if the dataset is small or lacks diversity.
•   Regularization techniques can be used to address this issue.
5. Hierarchical Feature Learning
•   In early layers, filters typically learn low-level features (edges,
colours).
•   In deeper layers, filters learn high-level features (object parts,
shapes).
•   Increasing depth in later layers helps the network understand abstract
concepts.
Q4   a   i.   Illustrate how batch gradient descent and Stochastic Gradient Descent   [10]
CO-2;   (SGD) differ in terms of 1) oscillations in the loss function (with
BL-3   diagram/graph), 2) memory usage, and 3) suitability for large datasets.
ii. Discuss the impact of the learning rate being too high or too low during
training.
iii. Consider the cost function J(θ)=0.7𝜃3. Perform two iterations of SGD,
where learning rate (η or α) is 0.1, initial parameter 𝜃0=1. Write the
update rule and compute the updated parameter after each iteration.
Solution:
(i)   Three differences ( 3 marks)
Aspect   Batch Gradient Descent   Stochastic Gradient
(BGD)   Descent (SGD)
Oscillations   Smooth convergence;   Loss fluctuates a lot due to
in Loss   smaller oscillations   single-sample updates
Memory   High; needs to load entire   Low; processes one or few
Usage   dataset in memory   samples at a time
Suitability   Less suitable; slow and   More suitable; can handle
for Large   memory intensive   large datasets efficiently
Datasets
(ii)   Learning rate (2 marks)
Learning   Effect
Rate
Too high   Overshooting minima → may diverge or oscillate
without convergence
Too low   Very slow convergence → training may take too long
(iii)   Problem (5 marks)
********** 8 **********
--- page 9 ---
Q4   b   With reference to Gated Recurrent Unit (GRU) answer the following [10]
CO-4;   questions:
BL-2   i.   State the difference between LSTM and GRU in terms of architecture
and number of gates.
ii. Why is GRU computationally more efficient for smaller datasets?
iii.   Explain how GRUs “decide” to skip irrelevant tokens in a text
sequence.
iv.   Justify the advantage of bidirectional RNNs.
Solution:
i.   Difference: 3 marks
• LSTM: 3 gates (input, forget, output) + explicit cell state.
• GRU: 2 gates (update z, reset r); merges cell/hidden → simpler.
ii.   Computational efficiency of GRU: 2 marks
• Fewer parameters → faster training, less overfitting, adequate
capacity for shorter sequences.
iii.   Skipping irrelevant tokens :3 marks
• GRUs skip irrelevant tokens using their update (zt) and reset (rt)
gates.
• When a token provides little new information, zt is small — the
hidden state barely changes, effectively skipping that word.
• Similarly, rt can reduce the influence of past states if old information
is no longer relevant.
• This gating mechanism allows GRUs to focus on meaningful words
and ignore filler tokens in text sequences.
iv.   Advantage of bidirectional RNN: 2 marks
• Bidirectional RNN processes a sequence in both directions —
• forward (left → right) using past context, and
• backward (right → left) using future context.
This dual processing allows the model to consider information from the
entire sequence before making a prediction at any time step.
• In many NLP tasks (like named entity recognition, speech
recognition, or translation), the meaning of a word depends on both
what comes before and after it.
********** 9 **********
--- page 10 ---
Q5   a.   i.   Explain why a feedforward neural network fails to capture sequential [10]
CO-4;   context in language modelling.
BL-2   ii.   Describe how a recurrent connection in an RNN overcomes this
limitation.
iii.   Consider a RNN with a single hidden layer. Calculate the output of
the hidden layer ht given the following values: (use tanh as activation
function)
Wxh= [0.6 0.4   , Whh= [0.5 0.3 ht-1=[0 xt=[0
0.3 0.7]   0.2   0.4],   1],   1]
iv.   Explain how RNN-based language models predict the next word
probability distribution in a sentence.
Solution:
i. Why neural network fails: 2 marks
• Decisions are based on current input
• No memory about the past
• No future scope
ii. How RNN overcomes: 2 marks
• Can handle sequential data
• Considers current input as well as past inputs using memory
(recurrent connections) ht=f(xt,ht−1)
iii. Numerical :3 marks
ht=tanh(Wxhxt+Whhht−1)
iv. How RNN predicts next word: 3 marks
•   Uses hidden state ht to parameterize P(wt+1∣w≤t) =
Softmax(Whht+b).
•   Trained with cross-entropy over true next token; left-to-right
factorization of sentence probability.
•   wt+1: the next word the model is trying to predict.
•   w≤t: all previous words in the sentence (the context).
•   ht: the hidden state at time step t, which summarizes all the
contextual information from w1,w2,…,wt.
********** 10 **********
--- page 11 ---
•   Wh: a weight matrix that transforms this hidden state into a vector
of scores, one per word in the vocabulary.
•   b: a bias term.
•   Softmax: converts those scores into probabilities over the
vocabulary.
•   This mechanism allows the model to generate sentences word by
word, always conditioning on all previous words.
Q5   b   Explain the working principle of the RMSProp optimizer. Write the update [10]
CO-2;   rule and explain the role of the accumulated squared gradients. List
BL-2   advantages and disadvantages of RMSProp compared to standard SGD.
Solution:
Working Principle of RMSProp (3 marks)
RMSProp (Root Mean Square Propagation) is an adaptive learning rate
optimizer that improves upon AdaGrad. Its key idea is to maintain a moving
average of the squared gradients to scale the learning rate for each parameter
individually. This prevents the learning rate from diminishing too quickly,
which is a problem with AdaGrad.
RMSProp Update Rule (3 marks)
Where ρ is the decay rate and δ is a small constant to avoid division by zero.
(OR)
Where β is the decay rate and ɛ is a small constant to avoid division by zero
Role of Accumulated Squared Gradients (2 marks)
Reduces learning rate for parameters with large gradients. It increases
learning rate for parameters with small gradients and helps stabilize training
and prevent oscillations along steep directions.
Advantage and disadvantages (2 marks)
Advantages of RMSProp: (i) Addresses diminishing learning rate of
AdaGrad (ii) Adapts learning rate based on recent gradients
Disadvantages of RMSProp: (i) Can still get stuck in local minima on non-
convex problems (ii) Requires tuning of decay rate
Q6   a   Consider the CNN for binary classification as below. Compute the shape of   [10]
CO-3;   the output volume dimension and trainable parameters at each layer.
BL-3
Layer   Volume   No of
Dimension   parameters
Input   256 X 256 X 3
Conv2D
Filter = 32, stride = 1,
Kernel Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 64, stride = 1,
Kernel Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
********** 11 **********
--- page 12 ---
Filter = 128, stride = 1,
Kernel Size = 5x5,
padding=1
Pool2D Kernel Size = 2,
stride = 2
Flatten
Fully connected dense units
= 84
Fully connected dense units
= 32
Output
Solution: 1 mark for each calculation
Conv layer → ((kernel_width × kernel_height × input_channels) + 1) ×
num_filters
Pooling layer → number of parameters = 0
FC→ (number of neurons in previous layer × number of neurons in current
layer) + number of biases
Layer   Volume   No of
Dimension   parameters
Input   256 × 256 × 3   0
Conv2D
Filter = 32, stride = 1,   252 × 252 × 32   2,432
Kernel Size = 5X5
Pool2D Kernel Size = 2,
126 × 126 × 32   0
stride = 2
Conv2D
Filter = 64, stride = 1,   122 × 122 × 64   51,264
Kernel Size = 5X5
Pool2D Kernel Size = 2,
61 × 61 × 64   0
stride = 2
Conv2D
Filter = 128, stride = 1,
59 × 59 × 128   73,856
Kernel Size = 5x5,
padding=1
Pool2D Kernel Size = 2,
29 × 29 × 128   0
stride = 2
Flatten   29 × 29 × 128
0
= 1,07,648
Fully connected dense units
84 (vector)   9,042,516
= 84
Fully connected dense units
32 (vector)   2,720
= 32
Output   1 (vector)   33
Total trainable parameters: 91,72,821.
********** 12 **********
--- page 13 ---
Q6   b   Fully connected Neural Network with 10-layer is training using the sigmoid [10]
CO-2;   activation function.
BL-3   i. What is the activation output f (6)?
ii. What is the first derivative of gradient f 1(x) at x=6?
iii. Explain how this affects backpropagation in deeper layers.
iv. Solve the SoftMax values for y= [2.3, 4.5, 3.2]
Solution: f(6) ( 1mark)
Derivative (1 mark)
Interpretation: (1 mark)
The gradient is very small (~0.0025). In a deep network, multiplying many
such small gradients leads to the vanishing gradient problem (weights in
earlier layers barely update).
Compare the Loss function vs the Activation function.
Soft max values (2 marks)
Q7   a   Differentiate between single-layer and multi-layer feedforward neural [10]
CO-2;   networks. Explain the importance of non-linearity in hidden layers. Illustrate
BL-3   your answer by computing the output of a feedforward neural network with
the following configuration:
•   Structure: 3 input neurons → 2 hidden neurons (sigmoid activation)
→ 1 output neuron (sigmoid activation)
•   Input: X=[0.5,0.2,0.1]
• Weights and biases:
𝑊1 = [0.1 0.4 0.2 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.6 0.9], 𝑏2 = 0.5
0.3 0.5
Solution:
Difference (any three points - each 1 mark)
Aspect   Single-layer FNN   Multi-layer FNN
********** 13 **********
--- page 14 ---
Architecture   Has only one layer of Has one or more hidden
weights connecting   layers between input and
inputs directly to   output layers.
outputs.
Computation   Performs only a   Performs successive linear
linear mapping of   and nonlinear
input to output.   transformations, enabling
complex mappings.
Representatio   Can only solve   Can approximate non-linear
n Power   linearly separable   and complex functions
problems.   (universal approximators).
Activation   Typically linear.   Non-linear activations (e.g.,
Function   ReLU, Sigmoid, Tanh) used
in hidden layers.
Importance of Non-linearity (any two points- each 1 mark)
•   Without non-linear activation functions, a multi-layer network
collapses mathematically into an equivalent single-layer linear model
(since a composition of linear functions is still linear).
•   Non-linearity (e.g., sigmoid) allows the network to capture complex
patterns, decision boundaries, and feature interactions.
•   It enables hierarchical feature learning — each layer extracts
progressively more abstract representations.
Compute for each hidden neuron: (each step 1 mark)
For hidden neuron 1:
Z11 = (0.1)(0.5)+(0.4)(0.2)+(0.2)(0.1)+0.1= 0.25
b   Explain the concept of Transfer Learning using CNNs. Describe how pre-   [10]
Q7   trained models can be adapted for a new image classification task. Explain
CO-3   with any example model.
BL-2   Solution:
Concept Explanation (3 Marks):
Steps Involved (4 Marks):
1. Select a pre-trained model (e.g., VGG16, ResNet50, InceptionV3).
2. Load pre-trained weights trained on ImageNet or similar dataset.
3. Freeze base layers to retain generic features.
********** 14 **********
--- page 15 ---
4. Add new layers (Dense/SoftMax) to suit the new classification task.
5. Compile and train the model on the new dataset.
6. Fine-tune (optional): Unfreeze some deeper layers and retrain with
a small learning rate.
Example (3 Marks):
A suitable example using any pretrained VGG16, ResNet50, InceptionV3
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 50cf43dfe17d

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_AIDS_7056/Deep Learning/ANS_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 Jul 2026
- Text: mixed (12 pages), mean OCR confidence 38.4

````text
SYNOPTICS
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
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Attempt any 4 questions from the remaining questions.
6. Attempt five (5) questions in total.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1. (a)   Justify why deep learning is preferred over traditional image processing techniques   5
CO1;   with atleast five reasons.
SO1;BL2   Answer:
• Can handle high-dimensional data
• Automatic Feature Extraction
• Higher Accuracy and Performance
• End-to-End Learning
• Performance on Large Scale Datasets
Rubrics:
1 Mark for each reason.
Q1. (b)   A neural network model is designed using a 3-layer architecture (Input Layer - Hidden 5
CO2;   Layer - Output Layer).
SO1;BL3   i.   Compute the total number of trainable parameters (weights and biases), if the
input layer has 𝑛=4 neurons, the hidden layer has ℎ=5 neurons, and the output
layer has 𝑜=2 neurons.
ii.   Differentiate between parameters and hyperparameters in neural networks.
Answer:
i.   Total Trainable Parameters
Input → Hidden Layer: 4×5=20 weights and biases =5
Hidden → Output Layer: 5×2=10 weights and biases =2
Total = 20 + 5 + 10 + 2 = 37
ii.
Aspect   Parameters   Hyperparameters
Definition   Learned during training   Set before training
Examples   Weights, Biases   Learning rate, epochs, batch size
Role   Define model behavior   Control training process
Updated by   Backpropagation   Manual tuning / optimization
Rubrics:
3 Marks: Parameter calculation
2 Marks: Comparison between parameter and hyperparameter
Q1. (c)   Calculate the output size and compute the output feature map with stride =1 and 5
padding = 0 with input image (4×4):
********** 1 **********
--- page 2 ---
CO3;   2   4   6   8
SO1;BL3   1   3   5   7
2   4   6   8
1   3   5   7
Kernel:
1   0   1
0   2   0
1   0   1
Answer:
Step 1: Output Size (1M)
(4 −3 + 0)
Output size =   + 1 = 2
1
⇒2 × 2
Step 2: Convolution Computation
Corner Cell 1: (Top-Left) (1M)
2 4 6
[ 1 3 5 ]
2 4 6
= (2 ⋅1 + 6 ⋅1 + 2 ⋅1 + 6 ⋅1 + 3 ⋅2)
= (2 + 6 + 2 + 6) + 6 = 16 + 6 = 22
Corner Cell 2: (Top-Right) (1M)
4 6 8
[ 3 5 7 ]
4 6 8
= (4 + 8 + 4 + 8) + (5 ⋅2) = 24 + 10 = 34
Corner Cell 3: (Bottom-Left) (1M)
1 3 5
[ 2 4 6 ]
1 3 5
= (1 + 5 + 1 + 5) + (4 ⋅2) = 12 + 8 = 20
Corner Cell 4: (Bottom-Right) (1M)
3 5 7
[ 4 6 8 ]
3 5 7
= (3 + 7 + 3 + 7) + (6 ⋅2) = 20 + 12 = 32
Final Output Feature Map (1M)
[22 34
20 32]
Rubrics:
•   Correct output size (1M)
•   Correct computation of corner cells. (4M)
Q1. (d)   Explain how a vanilla RNN models sequence data and give one reason it may fail on   5
CO4;   long call transcripts.
SO1;BL3
Answer:
A vanilla RNN models sequence data by processing inputs one time step at a time and
maintaining a hidden state that carries information from previous steps, allowing it to
capture temporal dependencies in the sequence. However, it may fail on long call
transcripts due to the vanishing gradient problem, where information from earlier time
steps fades away, making it difficult to learn long-term dependencies.
Rubrics:
********** 2 **********
--- page 3 ---
Correct recurrence idea (2M)
Role of hidden state/context (1M)
Long-sequence failure reason (2M)
Q2 (a)   For each of the following scenarios, identify whether machine learning or deep   5
CO2;   learning is more appropriate. If deep learning is used, specify the suitable architecture:
SO1;BL1, CNN, RNN, or both. Justify
2   i. A system predicts house prices based on features such as location, size, and
number of rooms.
ii. A model analyzes medical images (X-rays) to detect signs of pneumonia.
iii. A chatbot processes user queries and generates meaningful responses in natural
language.
iv. A model generates captions automatically for images uploaded on a social media
platform.
v. A system predicts stock prices using historical time-series data.
Answer:
Scenario   ML /   Architect   Justification
DL   ure
(i) House price prediction ML —   Structured data, therefore,
regression models
(ii) Medical image   DL   CNN   Extracts spatial features from
analysis (X-rays)   images
(iii) Chatbot (NLP)   DL   RNN   Handles sequential text and
context
(iv) Image caption   DL   CNN +   Image features + text generation
generation   RNN
(v) Stock price prediction DL   RNN   Captures time-series dependencies
Rubrics:
1 Mark for each case.
Q2 (b)   Justify why the XOR problem is not linearly separable (with graph) and cannot be   5
CO2;   solved using a single-layer perceptron. Suggest a suitable solution to address this
SO1;BL4   issue.
Answer:
XOR Truth Table:
When plotted, the classes cannot be separated by a single straight line.
A single-layer perceptron can only learn linear decision boundaries. XOR requires a
non-linear boundary, which a perceptron cannot model. Hence, it fails to converge for
XOR.
Use a Multi-Layer Perceptron (MLP) with at least one hidden layer. Hidden neurons
create non-linear decision boundaries. Use activation functions like ReLU / Sigmoid.
Rubrics:
• 5 Marks: Clearly explains XOR truth table, correctly justifies non-linear
separability (with graph explanation), explains why SLP fails (linear boundary
limitation), and suggests MLP with hidden layer as solution with proper
reasoning.
• 4 Marks: XOR explanation + SLP limitation + correct solution, but graph
explanation or reasoning is brief/missing detail.
• 3 Marks: explains XOR or SLP limitation OR suggests MLP, but lacks complete
justification.
********** 3 **********
--- page 4 ---
• 2 Marks: Mentions only basic idea (e.g., XOR not separable or use MLP) with
minimal explanation.
• 1 Mark: Very limited or vague response.
• 0 Marks: Incorrect or irrelevant answer.
Q2 (c)   Identify key design choices that made AlexNet successful (at least five) and explain   10
CO3;   how each affects training/performance.
SO1;BL4
Answer:
Deeper CNN, ReLU, dropout, data augmentation, GPU training/parallelism,
overlapping pooling/local response normalization (historical), large-scale ImageNet
training AlexNet.
Rubrics:
• Any 5 correct innovations (5M; 1M each)
•   Effect/explanation for each (4M)
•   Overall coherence (1M)
Q3 (a)   An RGB image of size 64 × 64 × 3is given as input to a convolutional neural network. 10
CO3;   The architecture consist of:
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
Compute the output size after each layer and calculate the total number of trainable
parameters. Note: Consider floor wherever required.
Answer:
Step 1: Conv Layer 1
Input: 64 × 64 × 3
Kernel: 3 × 3, stride = 1, valid
Output size = (64 −3 + 1) = 62
Output: 62 × 62 × 8
Parameters:
(3 × 3 × 3 + 1) × 8 = (27 + 1) × 8 = 224
Step 2: Max Pooling 1
62/2 = 31
Output: 31 × 31 × 8
(No parameters)
Step 3: Conv Layer 2
Input: 31 × 31 × 8
Output size = (31 −3 + 1) = 29
Output: 29 × 29 × 16
Parameters:
(3 × 3 × 8 + 1) × 16 = (72 + 1) × 16 = 1168
Step 4: Max Pooling 2
********** 4 **********
--- page 5 ---
29/2 = 14  (floor)
Output: 14 × 14 × 16
Step 5: Flatten
14 × 14 × 16 = 3136
Step 6: Dense Layer (64 neurons)
3136 × 64 + 64 = 200704 + 64 = 200768
Step 7: Output Layer (10 neurons)
64 × 10 + 10 = 640 + 10 = 650
Final Answers (Synoptic Form)
•   Layer-wise outputs:
o Conv1: 62 × 62 × 8
o Pool1: 31 × 31 × 8
o Conv2: 29 × 29 × 16
o Pool2: 14 × 14 × 16
o   Flatten: 3136
•   Total Parameters:
224 + 1168 + 200768 + 650 = 202810
Rubrics:
•   Correct layer-wise output sizes (4M)
• Conv layer parameter calculations (2M)
• Dense layer parameter calculations (2M)
•   Final total correct (1M)
•   Clear presentation (1M)
Q3 (b)   Design a simple LSTM-based model to predict the next day’s product demand for a 10
CO4;   retail store. Clearly specify:
SO1;BL4   1. What will be the input features and output of the model?
2. What window size (number of past days) will you use and why?
3. Which loss function will you choose?
Which evaluation metric(s) will you use to assess performance?
Answer:
1. Input & Output (3M)
o   Input: Past 7–14 days demand (optionally include price, promotion flag)
o Output: Demand for the next day (single value)
2. Window Length & Features (3M)
o Window size: 7 or 14 days
o Reason: Captures weekly buying patterns (simple and sufficient for
basic forecasting)
o   Features:
▪   Past demand (mandatory)
▪   Optional: price, discount (basic exogenous variables)
3. Model Architecture (Implicit understanding)
o LSTM layer (captures temporal dependency)
o Dense layer (maps to output demand)
4. Loss Function (2M)
o MAE (robust to outliers) OR
o MSE (penalizes large errors more strongly)
5. Evaluation Metrics (2M)
o MAE (easy interpretation in units of demand)
o MAPE (percentage error, useful for business understanding)
********** 5 **********
--- page 6 ---
Rubrics:
•   Correct input-output definition (3M)
•   Logical window size and basic features (3M)
•   Appropriate loss function with reason (2M)
•   Suitable evaluation metrics (2M)
Q4 (a)   Implement OR function with bipolar inputs and bipolar targets using perceptron training 10
CO2;   algorithm for 2 epochs. Assume initial weights 𝑤1=0, 𝑤2=0, bias (b)=0, learning rate
SO1;BL3   (η)=1. Consider the following activation function:
𝑦𝑜𝑢𝑡 = −1 if 𝑦𝑖𝑛≤0,
𝑦𝑜𝑢𝑡 = 1 if 𝑦𝑖𝑛>0
Show the complete training table for each sample in both epochs.
Answer:
Epoch 1
net =
Sa   Ne
w₁x₁ +   Update New New
mpl   x₁   x₂   t   w₁   w₂   b   y   w
w₂x₂ +   Applied   w₁   w₂
e   b
b
1   -1   -1   -1   0   0   0   0   -1   No   0   0   0
2   -1   1   1   0   0   0   0   -1   Yes   -1   1   1
3   1   -1 1   -1   1   1   -1   -1   Yes   0   0   2
4   1   1   1   0   0   2   2   1   No   0   0   2
Epoch 2
net =
Sa
w₁x₁ +   Update New New Ne
mpl   x₁   x₂   t   w₁   w₂   b   y
w₂x₂ +   Applied   w₁   w₂ w b
e
b
1   -1   -1   -1   0   0   2   2   1   Yes   1   1   1
2   -1   1   1   1   1   1   1   1   No   1   1   1
3   1   -1 1   1   1   1   1   1   No   1   1   1
4   1   1   1   1   1   1   3   1   No   1   1   1
Rubrics:
• 9–10 Marks: Complete solution with correct updates across both epochs
• 6–8 Marks: Minor calculation errors OR one epoch partially incorrect
• 3–5 Marks: Partial steps shown (incomplete updates or table)
• 1–2 Marks: Very basic understanding
• 0 Marks: Incorrect approach
Q4 (b)   i.   Explain why a fully connected (FC) neural network is inefficient for processing 10
CO3;   raw images. How does the design of a Convolutional Neural Network (CNN)—
SO1;BL1,   specifically local receptive fields and weight sharing—address these
2   limitations?
ii.   Consider the following: An input image of size 64 × 64 × 3 is fed to:
Case 1: A fully connected layer with 100 neurons
Case 2: A convolutional layer with 10 filters of size 3 × 3 (stride = 1, padding
= valid, bias included).
• Compute the number of parameters in both cases
• Compare the results and justify why CNN is more efficient
Answer:
i.
Why FC is Inefficient
• Every input pixel connects to every neuron , thus, large number of
parameters
•   Ignores spatial structure (pixels treated independently)
• High memory + computation → prone to overfitting
********** 6 **********
--- page 7 ---
How CNN Solves This
•   Local Receptive Fields: Each neuron looks at only a small region (3×3). It
captures meaningful local features (edges, textures)
• Weight Sharing: Same filter is applied across the image. Instead of learning
separate weights for each location, CNN learns one feature detector
ii.
•   Fully Connected (FC) Layer Parameters
= 64 × 64 × 3 × 100 + 100 = 1,228,800 + 100 = 1,228,900
•   Convolutional Layer Parameters
Params per filter = (3 × 3 × 3 + 1) = 27 + 1 = 28
Total CNN params = 28 × 10 = 280
Parameter Comparison
• FC Layer: 1,228,900 parameters
• CNN Layer: 280 parameters
CNN uses ~4,389× fewer parameters
Rubrics:
• FC inefficiency (3M)
• CNN concepts (4M)
•   Correct calculations (2M)
•   Conclusion (1M)
Q5 (a)   i.   Explain the architecture of LSTM network architecture with formulas.   10
CO4;   ii.   An LSTM network has input   size = 3 and hidden   size =   2.
SO1;BL3   Calculate the total number of trainable parameters in the LSTM cell (consider
all 4 gates and include biases).
Answer:
i.
ii.   Parameters:
For each gate:
o Input weights = input_size × hidden_size = 3 × 2 = 6
o Hidden weights = hidden_size × hidden_size = 2 × 2 = 4
o Bias = hidden_size = 2
o Total per gate = 6 + 4 + 2 = 12
Total Parameters
o Total = 4 gates × 12 = 48 parameters
********** 7 **********
--- page 8 ---
Rubrics:
6 Marks: Architecture of LSTM network architecture with formulas
4 Marks: Parameter Calculation
Q5 (b)   i.   Explain Momentum based Stochastic Gradient Descent Algorithm.   10
CO2;   ii. A machine learning model is trained using Momentum based Stochastic
SO1;BL4   Gradient Descent to minimize the function:
𝐿(𝜃) = 𝜃3
Consider initial parameter 𝜃0=1, momentum coefficient α=0.8, learning rate
η=0.5, initial velocity 𝑣0 = 2. Calculate parameter update for single iteration.
iii. How Nesterov Accelerated Gradient Descent improves convergence as
compared to Momentum based Stochastic Gradient Descent.
Answer:
i.
ii.
iii.
Property   Momentum SGD   Nesterov AGD
Gradient location   Current 𝜃𝑡   Lookahead 𝜃𝑡+α𝑣𝑡
Self-correction   Reactive (next step)   Proactive (current step)
Oscillation   More prone   Dampened
Extra compute cost —   Negligible
Rubrics:
• 4 Mark: Momentum based SGD Explanation
• 4 Marks: Numerical
• 2 Marks: Nesterov vs Momentum
Q6 (a)   Apply back-propagation algorithm on the neural network shown below with input 𝑥1=4, 10
CO2;   𝑥2=3 and target = [0.4, 0.2]. Consider w13=0.25, w14=0.45, w15=0.32, w23=0.55,
SO1;BL5   w24=0.45, w25=0.67, w36=0.23, w37=0.36, w46=0.56, w47=0.50, w56=0.23,
w57=0.12, bias on all nodes at hidden layer b1=0.6 and bias on all nodes at output layer
b2 = 0.5. Use learning rate η=0.5, and sigmoid activation function.
********** 8 **********
--- page 9 ---
i.   Compute output of node 3, 4, 5, 6 and node 7.
ii.   Calculate mean square error at output layer.
iii.   Update weights w25 and w57.
Answer:
********** 9 **********
--- page 10 ---
FOI 7 QF ICR Ir
--- page 11 ---
Rubrics:
(5 Marks): Correct output of node 3, 4, 5, 6 and node 7.
(1 Mark): Correct mean square error at output layer.
(4 Marks): Correct weights update w25 and w57.
Q6 (b)   Consider a dataset with 5,000 samples trained for 20 epochs.   10
CO2;   Answer the following:
SO1;BL3   i.   Calculate number of weight updates for batch gradient descent and stochastic
gradient descent algorithms.
ii.   Compare batch gradient descent, mini batch gradient descent and stochastic
gradient descent algorithms in terms of memory cost and convergence
behaviour.
iii.   Compare the number of weight updates when Batch size = 500 and 1000 in mini-
batch gradient descent.
iv. A student claims that increasing batch size always improves learning. Is this
correct? Justify.
Answer:
i.   Number of weight updates in Batch Gradient Descent=20, stochastic gradient
descent =5000x20=1,00,000
ii.
Algorithm   Memory Cost   Convergence Behavior
Batch Gradient   High – requires   Smooth and stable
Descent   entire dataset in   convergence; slow but
memory   consistent
Mini-Batch   Moderate –   Faster convergence than
Gradient Descent   processes small   BGD; slightly noisy but
batches   generally stable
Stochastic Gradient Low – processes   Very fast but highly noisy;
Descent   one sample at a   fluctuates around minimum
time   and may not converge
exactly
iii.   When Batch size=500: Updates=(5000/500)x20=200
When Batch Size=1000: Updates=(5000/1000)x20=100
iv.   Increasing batch size does not always improve learning, it must be chosen
carefully. Too small batch size leads to noisy but better generalization and too
large batch size leads to stable training but may overfit or generalize poorly
Rubrics:
• Number of Weight Updates (3 Marks)
• Comparison of GD Variants (3 Marks)
• Mini-Batch Updates (2 Marks)
• Conceptual Justification (2 Marks)
Q7 (a)   A neural network is designed to classify plant diseases into three mutually exclusive 10
CO2;   classes: Healthy, Disease A, and Disease B. The network has an output layer with 3
SO1;BL3   neurons. The weighted sum (logits) at the output layer is given as: 𝑧 = [2.1, 0.5, 1.2].
The model achieves training accuracy = 96% and testing accuracy = 58%.
i.   List any four hyperparameters used in training this network.
ii.   State whether the model is overfitting or underfitting. Identify whether the
model suffers from:
• High Bias or Low Bias
• High Variance or Low Variance
iii.   Which activation function should be applied at the output layer to obtain a
probabilistic distribution? Calculate the output after applying this activation
function.
********** 11 **********
--- page 12 ---
iv.   Identify the most appropriate loss function for this classification problem.
Assume the one-hot-encoded target outputs as [0,1,0] and calculate the loss.
Answer:
i.   Hyperparamters: Learning rate, Number of epochs, Batch size, Number of
hidden neurons, Activation function, Optimizer (e.g., SGD, Adam)
ii.   Model suffers overfitting. High Variance and Low Bias.
iii.   The appropriate activation function is Softmax.
Softmax Formula:
𝑒2.1 ≈ 8.166, 𝑒0.5 ≈ 1.648, 𝑒1.2 ≈ 3.320
 8.166 + 1.648 + 3.320 = 13.134
P1 = 8.166/13.134 = 0.621
P2 = 1.648/13.134 = 0.125
P3 = 3.320/13.134 = 0.252
Final Answer: [0.621, 0.125, 0.252]
iv.   Appropriate Loss Function: Categorical Cross-Entropy:
L = −∑ 𝑦𝑖 log(𝑝𝑖)=−log(0.125)=2.07
Rubrics:
Hyperparameters (1 Mark)
Overfitting / Bias-Variance (2 Marks)
Activation Function & Calculation (3 Marks)
Loss Function & Calculation (4 Marks)
Q7 (b)   Explain why repeated multiplication in BPTT causes vanishing gradients, and give   10
CO4;   two mitigations (one architectural, one training trick) to resolve this issue.
SO1;BL4
Answer:
Chain rule multiplies many Jacobians; if norms <1, gradients decay exponentially.
Mitigate via gated units (LSTM/GRU) and training tricks like gradient clipping / careful
init / normalization / truncated BPTT Source.
Rubrics:
•   Correct chain-rule explanation (5M)
• One architectural mitigation (3M)
• One training mitigation (2M)
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper a6e78aa2e490

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CSE_DS_7011/Deep Learning/ANS_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: mixed (15 pages), mean OCR confidence 29.6

````text
SYNOPTICS
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
1. This question paper contains 15 pages.
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
Solution:
i) Two situations where deep learning models outperform traditional
machine learning algorithms (each 1 marks)
1. When working with unstructured and high-dimensional data: Deep
learning models (such as CNNs and RNNs) can automatically learn complex
patterns from images, audio, and text, whereas traditional ML models require
manual   feature   extraction. Example: Image   classification, speech
recognition, and natural language understanding.
2. When large volumes of labelled data are available: Deep learning requires
vast amounts of data to learn millions of parameters effectively. With
sufficient data and computational power, DL models outperform ML
algorithms in terms of accuracy and generalization. Example: Autonomous
driving, medical image analysis, and translation systems trained on huge
datasets.
ii. Application-based choice and justification (3 marks)
********** 1 **********
--- page 2 ---
Suitable
Application   Approa   Justification
ch
The dataset is small and features are
Machin   numerical and well-defined. Traditional
1. Predicting house
e   ML algorithms like Linear Regression
prices using 1,000
Learnin   or Random Forests perform well
structured records
g   without requiring large data or deep
architectures.
Involves processing image frames and
learning   spatial-temporal   features.
2.   Detecting
Deep   Deep   learning   models   such   as
emotions from facial
Learnin   Convolutional   Neural   Networks
expressions in real-
g   (CNNs) or 3D-CNNs can automatically
time video streams
extract   complex   visual   patterns,
outperforming ML methods.
Requires   understanding   long-range
language dependencies. Models like
3. Translating text
Deep   Recurrent Neural Networks (RNNs),
from one language to
Learnin LSTMs, or Transformers (e.g., Google
another (millions of
g   Translate) handle such   large-scale
sentence pairs)
sequential   data   far   better   than
traditional ML algorithms.
CO-2;   b.   i. Explain how   different   activation   functions   influence   gradient   [5]
BL-3   propagation, convergence behavior, and the overall performance of a deep
neural network.
ii. Discuss the scenarios or types of problems where specific activation
functions such as Sigmoid, Tanh, ReLU, and Leaky ReLU are preferred.
Solution:
Role of Activation Functions (2 marks): Activation functions introduce
non-linearity into deep neural networks. Without them, even multi-layer
networks behave like a single linear model and cannot learn complex
relationships.
Activation functions affect:
• Gradient propagation during backpropagation,
• Convergence speed during training, and
• Model performance and generalization.
Usage of activation functions (3 marks)
CO-2;   c.   i. Explain the role of L1 and L2 regularization in deep neural networks, and   [5]
BL-2   discuss how these techniques help prevent overfitting and improve the
model’s generalization to unseen data. You are training a fully connected
neural network layer with 4 neurons during training.
ii. The outputs of the neurons before applying dropout are: [0.8, −0.4, 0.6,
0.2]. A dropout rate of 50% is applied to this layer. Randomly determine
which neurons are dropped (assume a possible dropout mask) and
compute the output after applying dropout.
Solution:
Role of L1 and L2 regularization (2 mark)
Regularization is a technique used in deep learning to reduce overfitting by
discouraging the model from learning overly complex or large weight
values. It adds a penalty term to the loss function based on the magnitude of
the weights.
********** 2 **********
--- page 3 ---
The modified loss functions are:
• L1 Regularization (Lasso):
Adds the absolute value of the weights as a penalty.
• L2 Regularization (Ridge):
Adds the square of the weights as a penalty.
Here,
λ = regularization parameter (controls the strength of the penalty), wi=
weights of the model.
How They Help Prevent Overfitting (2 marks)
1. Controls weight magnitude: Both L1 and L2 regularization restrict
large weights, forcing the network to learn smaller and more general
weight values that perform better on unseen data.
2. Reduces model complexity:
o L1 tends to make many weights zero, leading to sparse models (some
neurons become inactive).
o L2 spreads weight values more evenly and helps smooth learning,
preventing any single weight from dominating.
By penalizing large weights, the network becomes less sensitive to noise,
improves generalization in the training data and performs better on test data
Output after dropout (1 mark)
Assume a random dropout mask (1 = keep, 0 = drop).
For example: mask=[1,0,1,0]
Multiply the neuron outputs by the mask:
output after dropout=[0.8x1, −0.4x0, 0.6x1, 0.2x0]=[0.8,0,0.6,0]
CO-4;   d. An e-commerce platform wants to automatically determine whether customer   [5]
BL-2   reviews are positive, negative, or neutral. Explain how an RNN model
processes customer review text to perform sentiment classification. Why is
RNN suitable for this task, and what role does word order play in determining
sentiment?
Solution:
How an RNN processes customer review text to perform sentiment
classification (2 marks)
• In sentiment analysis, a review (e.g., “The product is not good”) is treated
as a sequence of words.
• Each word is converted into a numerical vector (using embeddings like
Word2Vec or GloVe).
• The RNN reads these words sequentially, one at a time, maintaining a
hidden state that stores information from previous words.
• As the sequence progresses, the hidden state accumulates contextual
information — understanding how earlier words influence the meaning
of later ones.
• After processing the entire review, the final hidden state represents the
overall context and sentiment of the sentence.
• This representation is then passed to a fully connected (dense) layer with
a softmax activation to classify the sentiment as positive, negative, or
neutral.
Why RNN is suitable for sentiment analysis: (2 marks)
********** 3 **********
--- page 4 ---
RNNs are designed to handle sequential and contextual data, making them
ideal for text where word order and context matter. They can capture
dependencies between words that are far apart (e.g., “not good” vs. “good”).
Unlike traditional feedforward networks, RNNs remember what came before
in the sentence, giving them the ability to understand contextual polarity.
Role of word order in sentiment detection: (1 mark)
Word order changes meaning. For example: This phone is not bad” →
positive sentiment.
“This phone is bad” → negative sentiment.
RNNs preserve this order by processing words sequentially, ensuring that the
position of each word affects the final interpretation.
If the model ignored order, it might misclassify sentences with negations or
complex phrasing.
Q2   a   [10]
CO-2;
BL-3
The given network with the following i1= 0.25, i2= 0.7, w1= 0.2, w2=0.15,
w3= 0.28, w4=0.3, w5= 0.1, w6= 0.24, w7 = 0.12, w8= 0.21, b1= 1 and b2=1.
All neurons have a Sigmoid activation function. The actual output at O1 is
0.7 and at O2 is 0.3. Perform a forward pass and backward pass to update
weights of w1, w5 and w7 using Gradient Descent algorithm (Assume
learning rate = 1).
Solution:
Forward pass (outh1, outo1, total error – each 1 mark)
Backward pass (updated w7 and w5 - each 2 marks, and w1 – 3 marks)
********** 4 **********
--- page 5 ---
aod gos |
5\\o
gat ‘(1
at Te eh
panterdx ose | y
= pe (2>)* 3)

iy zi \\55
ale Ta cles Tees
la he Tae

[oct]
[oct]

O1 7 we ae 16 or: ad
ti . Dales a ey eae
e
te: uae 2) Co. | ie
t 2) fo * CAEWIV
23
= Aten =
(on arent) 0-18
Ea ahs (a

. sien sen tace

ae

HEA o-2Y4ol
=O NES
> ubor gabe
setae 88 STE AR one
ad at cubo, ) G* 0) O- cares:

Ow4 Fs

ait hye"

DO o- eae

-o-> lo © es

=0-062 5
- abt . ore -() (0-04) oe
wy = Pana ies
ste _ 2EE yD pokey x Dubey anit oy
BEE = Faro, ame, Pe

acre) (esky i-ested CH)
peer tomy Corey(etey(e Lest tf

2K
FIR Fok aC i Gk
--- page 6 ---
Q2   b   i. Explain how AlexNet’s design improved upon earlier traditional CNNs [10]
CO-3;   in terms of regularization, and training methodology.
BL-2   ii. Discuss how the Inception Network captures features at multiple scales
efficiently and the role of 1×1 convolutions in enhancing both
computational efficiency and feature representation in deep CNNs.
iii. Based on your analysis, which architecture would you recommend for
classification of large-scale image dataset and why?
Solution:
AlexNet (2012): (4 marks)
• Regularization Techniques: Introduced Dropout in fully connected layers
to prevent overfitting by randomly deactivating neurons during training.
Applied Data Augmentation (image translations, reflections, and patch
extractions) to improve generalization.
• Training Methodology: Adopted ReLU (Rectified Linear Unit) activation
instead of sigmoid/tanh, avoiding vanishing gradients and speeding up
training. Trained on GPUs, which significantly reduced training time for
large datasets. Used Local Response Normalization (LRN) to encourage
competition among neurons and improve generalization.
Inception Network (GoogleNet, 2014): (4 marks)
• Inception Modules: Each module applied 1×1, 3×3, and 5×5 convolutions
in parallel, along with a max-pooling branch. Captured features at multiple
spatial scales simultaneously, improving representational richness.
• Dimensionality Reduction: Introduced 1×1 convolutions before expensive
3×3 and 5×5 filters to reduce the number of channels, drastically lowering
computation and parameters.
• Depth with Efficiency: Built a 22-layer deep network but used only about
5 million parameters (vs. 60 million in AlexNet). Replaced fully connected
layers with global average pooling, reducing overfitting and model size.
• Regularization: Employed ReLU activations and dropout for stability and
generalization
• Performance: Achieved top-5 error rate of 6.7% on ImageNet.
Analysis (2 marks)
Both models revolutionized computer vision, AlexNet demonstrated the
power of deep CNNs, and Inception showed deep networks could be efficient
and scalable.
Q3   a   i. Determine the weights required to perform the classification as per the [10]
CO-2;   table using single layer perceptron network. Assume learning rate is 1 and
BL-3   initial weights are 0. Consider threshold=0 and solve for 1 epoch.
********** 6 **********
--- page 7 ---
X1   X2   X3   target
-1   1   -1   -1
1   1   1   1
-1   -1   1   -1
-1   1   1   -1
ii. Discuss its limitations and provide suitable examples to illustrate these
limitations.
Solution:
Problem with formulas (7 marks)
X X X   t   α   yi   y Δ Δ Δ Δ w w w   b
1   2   3   n   w w w   b   1   2   3
1   2   3
-1   1   -1   -1   1   0   0   1   -1   1   -1   1   -1   1   -1
1   1   1   1   1   0   0   1   1   1   1   2   0   2   0
-1   -1   1   -1   1   4   1   -1   1   -1   -1   1   1   1   -1
-1   1   1   -1   1   0   0   0   0   0   0   2   0   0   2
Limitations and explanation with examples (3 marks)
•   Single-Layer Perceptron cannot classify non-linearly separable data
points.
• Complex problems, that involve a lot of parameters cannot be
solved by Single-Layer Perceptron.
Q3   b   How to decide number of filters in CNN? How it will influence the following [10]
CO-3;   parameters. 1) feature extraction capability, 2) dimensionality, 3)
BL-2   computational and memory cost, 4) risk of overfitting, 5) Hierarchical
Feature Learning.
Solution:
Each point for 2 marks
The number of filters in a CNN is often determined empirically through
experimentation, balancing model complexity and performance on the
validation set.
The depth of a convolutional layer—defined by the number of filters (or
kernels)—plays important role in determining the learning capacity of a
Convolutional Neural Network (CNN). Here's how:
1. Feature Extraction Capacity
• Each filter in a convolutional layer learns to detect a specific type of
feature (e.g., edges, textures, shapes etc.).
• More filters = more diverse features can be learned from the input
data.
•   This increases the representational power of the network, allowing it
to capture more complex patterns.
2. Dimensionality of Feature Maps
• The output of a convolutional layer is a set of feature maps, one for
each filter.
•   Increasing the number of filters increases the depth of the output
volume, which extracts richer information into subsequent layers.
3. Computational and Memory Cost
•   Increasing depth also increases the number of trainable parameters
(weights and biases).
•   This leads to higher computational cost, memory usage, and slower
training.
•   This leads to longer training times and greater memory usage,
especially in deeper networks.
4. Risk of Overfitting
********** 7 **********
--- page 8 ---
• A very deep layer with many filters might overfit the training data,
especially if the dataset is small or lacks diversity.
•   Regularization techniques can be used to address this issue.
5. Hierarchical Feature Learning
•   In early layers, filters typically learn low-level features (edges,
colours).
•   In deeper layers, filters learn high-level features (object parts,
shapes).
•   Increasing depth in later layers helps the network understand abstract
concepts.
Q4   a   i.   Illustrate how batch gradient descent and Stochastic Gradient Descent   [10]
CO-2;   (SGD) differ in terms of 1) oscillations in the loss function (with
BL-3   diagram/graph), 2) memory usage, and 3) suitability for large datasets.
ii. Discuss the impact of the learning rate being too high or too low during
training.
iii. Consider the cost function J(θ)=0.7𝜃3. Perform two iterations of SGD,
where learning rate (η or α) is 0.1, initial parameter 𝜃0=1. Write the
update rule and compute the updated parameter after each iteration.
Solution:
(i)   Three differences ( 3 marks)
Aspect   Batch Gradient Descent   Stochastic Gradient
(BGD)   Descent (SGD)
Oscillations   Smooth convergence;   Loss fluctuates a lot due to
in Loss   smaller oscillations   single-sample updates
Memory   High; needs to load entire   Low; processes one or few
Usage   dataset in memory   samples at a time
Suitability   Less suitable; slow and   More suitable; can handle
for Large   memory intensive   large datasets efficiently
Datasets
(ii)   Learning rate (2 marks)
Learning   Effect
Rate
Too high   Overshooting minima → may diverge or oscillate
without convergence
Too low   Very slow convergence → training may take too long
(iii)   Problem (5 marks)
********** 8 **********
--- page 9 ---
Q4   b   With reference to Gated Recurrent Unit (GRU) answer the following [10]
CO-4;   questions:
BL-2   i.   State the difference between LSTM and GRU in terms of architecture
and number of gates.
ii. Why is GRU computationally more efficient for smaller datasets?
iii.   Explain how GRUs “decide” to skip irrelevant tokens in a text
sequence.
iv.   Justify the advantage of bidirectional RNNs.
Solution:
i.   Difference: 3 marks
• LSTM: 3 gates (input, forget, output) + explicit cell state.
• GRU: 2 gates (update z, reset r); merges cell/hidden → simpler.
ii.   Computational efficiency of GRU: 2 marks
• Fewer parameters → faster training, less overfitting, adequate
capacity for shorter sequences.
iii.   Skipping irrelevant tokens :3 marks
• GRUs skip irrelevant tokens using their update (zt) and reset (rt)
gates.
• When a token provides little new information, zt is small — the
hidden state barely changes, effectively skipping that word.
• Similarly, rt can reduce the influence of past states if old information
is no longer relevant.
• This gating mechanism allows GRUs to focus on meaningful words
and ignore filler tokens in text sequences.
iv.   Advantage of bidirectional RNN: 2 marks
• Bidirectional RNN processes a sequence in both directions —
• forward (left → right) using past context, and
• backward (right → left) using future context.
This dual processing allows the model to consider information from the
entire sequence before making a prediction at any time step.
• In many NLP tasks (like named entity recognition, speech
recognition, or translation), the meaning of a word depends on both
what comes before and after it.
********** 9 **********
--- page 10 ---
Q5   a.   i.   Explain why a feedforward neural network fails to capture sequential [10]
CO-4;   context in language modelling.
BL-2   ii.   Describe how a recurrent connection in an RNN overcomes this
limitation.
iii.   Consider a RNN with a single hidden layer. Calculate the output of
the hidden layer ht given the following values: (use tanh as activation
function)
Wxh= [0.6 0.4   , Whh= [0.5 0.3 ht-1=[0 xt=[0
0.3 0.7]   0.2   0.4],   1],   1]
iv.   Explain how RNN-based language models predict the next word
probability distribution in a sentence.
Solution:
i. Why neural network fails: 2 marks
• Decisions are based on current input
• No memory about the past
• No future scope
ii. How RNN overcomes: 2 marks
• Can handle sequential data
• Considers current input as well as past inputs using memory
(recurrent connections) ht=f(xt,ht−1)
iii. Numerical :3 marks
ht=tanh(Wxhxt+Whhht−1)
iv. How RNN predicts next word: 3 marks
•   Uses hidden state ht to parameterize P(wt+1∣w≤t) =
Softmax(Whht+b).
•   Trained with cross-entropy over true next token; left-to-right
factorization of sentence probability.
•   wt+1: the next word the model is trying to predict.
•   w≤t: all previous words in the sentence (the context).
•   ht: the hidden state at time step t, which summarizes all the
contextual information from w1,w2,…,wt.
********** 10 **********
--- page 11 ---
•   Wh: a weight matrix that transforms this hidden state into a vector
of scores, one per word in the vocabulary.
•   b: a bias term.
•   Softmax: converts those scores into probabilities over the
vocabulary.
•   This mechanism allows the model to generate sentences word by
word, always conditioning on all previous words.
Q5   b   Explain the working principle of the RMSProp optimizer. Write the update [10]
CO-2;   rule and explain the role of the accumulated squared gradients. List
BL-2   advantages and disadvantages of RMSProp compared to standard SGD.
Solution:
Working Principle of RMSProp (3 marks)
RMSProp (Root Mean Square Propagation) is an adaptive learning rate
optimizer that improves upon AdaGrad. Its key idea is to maintain a moving
average of the squared gradients to scale the learning rate for each parameter
individually. This prevents the learning rate from diminishing too quickly,
which is a problem with AdaGrad.
RMSProp Update Rule (3 marks)
Where ρ is the decay rate and δ is a small constant to avoid division by zero.
(OR)
Where β is the decay rate and ɛ is a small constant to avoid division by zero
Role of Accumulated Squared Gradients (2 marks)
Reduces learning rate for parameters with large gradients. It increases
learning rate for parameters with small gradients and helps stabilize training
and prevent oscillations along steep directions.
Advantage and disadvantages (2 marks)
Advantages of RMSProp: (i) Addresses diminishing learning rate of
AdaGrad (ii) Adapts learning rate based on recent gradients
Disadvantages of RMSProp: (i) Can still get stuck in local minima on non-
convex problems (ii) Requires tuning of decay rate
Q6   a   Consider the CNN for binary classification as below. Compute the shape of   [10]
CO-3;   the output volume dimension and trainable parameters at each layer.
BL-3
Layer   Volume   No of
Dimension   parameters
Input   256 X 256 X 3
Conv2D
Filter = 32, stride = 1,
Kernel Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 64, stride = 1,
Kernel Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
********** 11 **********
--- page 12 ---
Filter = 128, stride = 1,
Kernel Size = 5x5,
padding=1
Pool2D Kernel Size = 2,
stride = 2
Flatten
Fully connected dense units
= 84
Fully connected dense units
= 32
Output
Solution: 1 mark for each calculation
Conv layer → ((kernel_width × kernel_height × input_channels) + 1) ×
num_filters
Pooling layer → number of parameters = 0
FC→ (number of neurons in previous layer × number of neurons in current
layer) + number of biases
Layer   Volume   No of
Dimension   parameters
Input   256 × 256 × 3   0
Conv2D
Filter = 32, stride = 1,   252 × 252 × 32   2,432
Kernel Size = 5X5
Pool2D Kernel Size = 2,
126 × 126 × 32   0
stride = 2
Conv2D
Filter = 64, stride = 1,   122 × 122 × 64   51,264
Kernel Size = 5X5
Pool2D Kernel Size = 2,
61 × 61 × 64   0
stride = 2
Conv2D
Filter = 128, stride = 1,
59 × 59 × 128   73,856
Kernel Size = 5x5,
padding=1
Pool2D Kernel Size = 2,
29 × 29 × 128   0
stride = 2
Flatten   29 × 29 × 128
0
= 1,07,648
Fully connected dense units
84 (vector)   9,042,516
= 84
Fully connected dense units
32 (vector)   2,720
= 32
Output   1 (vector)   33
Total trainable parameters: 91,72,821.
********** 12 **********
--- page 13 ---
Q6   b   Fully connected Neural Network with 10-layer is training using the sigmoid [10]
CO-2;   activation function.
BL-3   i. What is the activation output f (6)?
ii. What is the first derivative of gradient f 1(x) at x=6?
iii. Explain how this affects backpropagation in deeper layers.
iv. Solve the SoftMax values for y= [2.3, 4.5, 3.2]
Solution: f(6) ( 1mark)
Derivative (1 mark)
Interpretation: (1 mark)
The gradient is very small (~0.0025). In a deep network, multiplying many
such small gradients leads to the vanishing gradient problem (weights in
earlier layers barely update).
Compare the Loss function vs the Activation function.
Soft max values (2 marks)
Q7   a   Differentiate between single-layer and multi-layer feedforward neural [10]
CO-2;   networks. Explain the importance of non-linearity in hidden layers. Illustrate
BL-3   your answer by computing the output of a feedforward neural network with
the following configuration:
•   Structure: 3 input neurons → 2 hidden neurons (sigmoid activation)
→ 1 output neuron (sigmoid activation)
•   Input: X=[0.5,0.2,0.1]
• Weights and biases:
𝑊1 = [0.1 0.4 0.2 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.6 0.9], 𝑏2 = 0.5
0.3 0.5
Solution:
Difference (any three points - each 1 mark)
Aspect   Single-layer FNN   Multi-layer FNN
********** 13 **********
--- page 14 ---
Architecture   Has only one layer of Has one or more hidden
weights connecting   layers between input and
inputs directly to   output layers.
outputs.
Computation   Performs only a   Performs successive linear
linear mapping of   and nonlinear
input to output.   transformations, enabling
complex mappings.
Representatio   Can only solve   Can approximate non-linear
n Power   linearly separable   and complex functions
problems.   (universal approximators).
Activation   Typically linear.   Non-linear activations (e.g.,
Function   ReLU, Sigmoid, Tanh) used
in hidden layers.
Importance of Non-linearity (any two points- each 1 mark)
•   Without non-linear activation functions, a multi-layer network
collapses mathematically into an equivalent single-layer linear model
(since a composition of linear functions is still linear).
•   Non-linearity (e.g., sigmoid) allows the network to capture complex
patterns, decision boundaries, and feature interactions.
•   It enables hierarchical feature learning — each layer extracts
progressively more abstract representations.
Compute for each hidden neuron: (each step 1 mark)
For hidden neuron 1:
Z11 = (0.1)(0.5)+(0.4)(0.2)+(0.2)(0.1)+0.1= 0.25
b   Explain the concept of Transfer Learning using CNNs. Describe how pre-   [10]
Q7   trained models can be adapted for a new image classification task. Explain
CO-3   with any example model.
BL-2   Solution:
Concept Explanation (3 Marks):
Steps Involved (4 Marks):
1. Select a pre-trained model (e.g., VGG16, ResNet50, InceptionV3).
2. Load pre-trained weights trained on ImageNet or similar dataset.
3. Freeze base layers to retain generic features.
********** 14 **********
--- page 15 ---
4. Add new layers (Dense/SoftMax) to suit the new classification task.
5. Compile and train the model on the new dataset.
6. Fine-tune (optional): Unfreeze some deeper layers and retrain with
a small learning rate.
Example (3 Marks):
A suitable example using any pretrained VGG16, ResNet50, InceptionV3
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 10db29f19e87

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_Computer_7002/Deep Learning/ANS_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: mixed (15 pages), mean OCR confidence 29.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. TECH (CSE - DS)/B. Tech
(CSE - DS) (311)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech (IT)/MBA Tech (AI)/MBA Tech
(Comp)/MBA Tech (EXTC)
Year: III / IV / VI/Sem 11 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Deep Learning
Date: 10 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
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
Solution:
i) Two situations where deep learning models outperform traditional
machine learning algorithms (each 1 marks)
1. When working with unstructured and high-dimensional data: Deep
learning models (such as CNNs and RNNs) can automatically learn complex
patterns from images, audio, and text, whereas traditional ML models require
manual   feature   extraction. Example: Image   classification, speech
recognition, and natural language understanding.
2. When large volumes of labelled data are available: Deep learning requires
vast amounts of data to learn millions of parameters effectively. With
sufficient data and computational power, DL models outperform ML
algorithms in terms of accuracy and generalization. Example: Autonomous
driving, medical image analysis, and translation systems trained on huge
datasets.
ii. Application-based choice and justification (3 marks)
Suitable
Application   Approa   Justification
ch
********** 1 **********
--- page 2 ---
The dataset is small and features are
Machin   numerical and well-defined. Traditional
1. Predicting house
e   ML algorithms like Linear Regression
prices using 1,000
Learnin   or Random Forests perform well
structured records
g   without requiring large data or deep
architectures.
Involves processing image frames and
learning   spatial-temporal   features.
2.   Detecting
Deep   Deep   learning   models   such   as
emotions from facial
Learnin   Convolutional   Neural   Networks
expressions in real-
g   (CNNs) or 3D-CNNs can automatically
time video streams
extract   complex   visual   patterns,
outperforming ML methods.
Requires   understanding   long-range
language dependencies. Models like
3. Translating text
Deep   Recurrent Neural Networks (RNNs),
from one language to
Learnin LSTMs, or Transformers (e.g., Google
another (millions of
g   Translate) handle such   large-scale
sentence pairs)
sequential   data   far   better   than
traditional ML algorithms.
CO-2;   b.   i. Explain how   different   activation   functions   influence   gradient   [5]
BL-3   propagation, convergence behavior, and the overall performance of a deep
neural network.
ii. Discuss the scenarios or types of problems where specific activation
functions such as Sigmoid, Tanh, ReLU, and Leaky ReLU are preferred.
Solution:
Role of Activation Functions (2 marks): Activation functions introduce
non-linearity into deep neural networks. Without them, even multi-layer
networks behave like a single linear model and cannot learn complex
relationships.
Activation functions affect:
• Gradient propagation during backpropagation,
• Convergence speed during training, and
• Model performance and generalization.
Usage of activation functions (3 marks)
CO-2;   c.   i. Explain the role of L1 and L2 regularization in deep neural networks, and   [5]
BL-2   discuss how these techniques help prevent overfitting and improve the
model’s generalization to unseen data. You are training a fully connected
neural network layer with 4 neurons during training.
ii. The outputs of the neurons before applying dropout are: [0.8, −0.4, 0.6,
0.2]. A dropout rate of 50% is applied to this layer. Randomly determine
which neurons are dropped (assume a possible dropout mask) and
compute the output after applying dropout.
Solution:
Role of L1 and L2 regularization (2 mark)
Regularization is a technique used in deep learning to reduce overfitting by
discouraging the model from learning overly complex or large weight
values. It adds a penalty term to the loss function based on the magnitude of
the weights.
The modified loss functions are:
• L1 Regularization (Lasso):
********** 2 **********
--- page 3 ---
Adds the absolute value of the weights as a penalty.
• L2 Regularization (Ridge):
Adds the square of the weights as a penalty.
Here,
λ = regularization parameter (controls the strength of the penalty), wi=
weights of the model.
How They Help Prevent Overfitting (2 marks)
1. Controls weight magnitude: Both L1 and L2 regularization restrict
large weights, forcing the network to learn smaller and more general
weight values that perform better on unseen data.
2. Reduces model complexity:
o L1 tends to make many weights zero, leading to sparse models (some
neurons become inactive).
o L2 spreads weight values more evenly and helps smooth learning,
preventing any single weight from dominating.
By penalizing large weights, the network becomes less sensitive to noise,
improves generalization in the training data and performs better on test data
Output after dropout (1 mark)
Assume a random dropout mask (1 = keep, 0 = drop).
For example: mask=[1,0,1,0]
Multiply the neuron outputs by the mask:
output after dropout=[0.8x1, −0.4x0, 0.6x1, 0.2x0]=[0.8,0,0.6,0]
CO-4;   d. An e-commerce platform wants to automatically determine whether customer   [5]
BL-2   reviews are positive, negative, or neutral. Explain how an RNN model
processes customer review text to perform sentiment classification. Why is
RNN suitable for this task, and what role does word order play in determining
sentiment?
Solution:
How an RNN processes customer review text to perform sentiment
classification (2 marks)
• In sentiment analysis, a review (e.g., “The product is not good”) is treated
as a sequence of words.
• Each word is converted into a numerical vector (using embeddings like
Word2Vec or GloVe).
• The RNN reads these words sequentially, one at a time, maintaining a
hidden state that stores information from previous words.
• As the sequence progresses, the hidden state accumulates contextual
information — understanding how earlier words influence the meaning
of later ones.
• After processing the entire review, the final hidden state represents the
overall context and sentiment of the sentence.
• This representation is then passed to a fully connected (dense) layer with
a softmax activation to classify the sentiment as positive, negative, or
neutral.
Why RNN is suitable for sentiment analysis: (2 marks)
RNNs are designed to handle sequential and contextual data, making them
ideal for text where word order and context matter. They can capture
dependencies between words that are far apart (e.g., “not good” vs. “good”).
********** 3 **********
--- page 4 ---
Unlike traditional feedforward networks, RNNs remember what came before
in the sentence, giving them the ability to understand contextual polarity.
Role of word order in sentiment detection: (1 mark)
Word order changes meaning. For example: This phone is not bad” →
positive sentiment.
“This phone is bad” → negative sentiment.
RNNs preserve this order by processing words sequentially, ensuring that the
position of each word affects the final interpretation.
If the model ignored order, it might misclassify sentences with negations or
complex phrasing.
Q2   a   [10]
CO-2;
BL-3
The given network with the following i1= 0.25, i2= 0.7, w1= 0.2, w2=0.15,
w3= 0.28, w4=0.3, w5= 0.1, w6= 0.24, w7 = 0.12, w8= 0.21, b1= 1 and b2=1.
All neurons have a Sigmoid activation function. The actual output at O1 is
0.7 and at O2 is 0.3. Perform a forward pass and backward pass to update
weights of w1, w5 and w7 using Gradient Descent algorithm (Assume
learning rate = 1).
Solution:
Forward pass (outh1, outo1, total error – each 1 mark)
Backward pass (updated w7 and w5 - each 2 marks, and w1 – 3 marks)
********** 4 **********
--- page 5 ---
aod gos |
5\\o
gat (i
ac Te eh
panerdr ore | y
= io (2>)* 3)

iy zi \\55
ale Ta cles Tees
la he Tae

[ct]
[ct]

O1 a we ae 16 or: wd
is . Dale a pean (o
e
te: see a) (9. | ie
t 2) fo * CADEWIL
(23
= Aten =
(on agrees 0-8
Eas (ra

. asian ses

cae

a att. o24ol
= ONES

pig «EL OEE anudon 4 dnebee
ockuod QR OE =O Sub, RO

(ore = (2 3s0* oben Me sa .*

ows

tiaras:

aa hye"

ewe
cm oy EE a :
© Bo ‘
5 Or
pei
“76
Dee - (o2x0d (en alee >)
ae ea et
= 0-062 5
- abt 2 ore -() (0-04) oe
4 = eae et
stk _ VEE Pye x obey
Sa a deni ig

gases) (osbeyinested CH)
peer tomy Corey(ceten(e LE sort tf

2K
FIR Fok aC i Gk
--- page 6 ---
Q2   b   i. Explain how AlexNet’s design improved upon earlier traditional CNNs [10]
CO-3;   in terms of regularization, and training methodology.
BL-2   ii. Discuss how the Inception Network captures features at multiple scales
efficiently and the role of 1×1 convolutions in enhancing both
computational efficiency and feature representation in deep CNNs.
iii. Based on your analysis, which architecture would you recommend for
classification of large-scale image dataset and why?
Solution:
AlexNet (2012): (4 marks)
• Regularization Techniques: Introduced Dropout in fully connected layers
to prevent overfitting by randomly deactivating neurons during training.
Applied Data Augmentation (image translations, reflections, and patch
extractions) to improve generalization.
• Training Methodology: Adopted ReLU (Rectified Linear Unit) activation
instead of sigmoid/tanh, avoiding vanishing gradients and speeding up
training. Trained on GPUs, which significantly reduced training time for
large datasets. Used Local Response Normalization (LRN) to encourage
competition among neurons and improve generalization.
Inception Network (GoogleNet, 2014): (4 marks)
• Inception Modules: Each module applied 1×1, 3×3, and 5×5 convolutions
in parallel, along with a max-pooling branch. Captured features at multiple
spatial scales simultaneously, improving representational richness.
• Dimensionality Reduction: Introduced 1×1 convolutions before expensive
3×3 and 5×5 filters to reduce the number of channels, drastically lowering
computation and parameters.
• Depth with Efficiency: Built a 22-layer deep network but used only about
5 million parameters (vs. 60 million in AlexNet). Replaced fully connected
layers with global average pooling, reducing overfitting and model size.
• Regularization: Employed ReLU activations and dropout for stability and
generalization
• Performance: Achieved top-5 error rate of 6.7% on ImageNet.
Analysis (2 marks)
Both models revolutionized computer vision, AlexNet demonstrated the
power of deep CNNs, and Inception showed deep networks could be efficient
and scalable.
Q3   a   i. Determine the weights required to perform the classification as per the [10]
CO-2;   table using single layer perceptron network. Assume learning rate is 1 and
BL-3   initial weights are 0. Consider threshold=0 and solve for 1 epoch.
********** 6 **********
--- page 7 ---
X1   X2   X3   target
-1   1   -1   -1
1   1   1   1
-1   -1   1   -1
-1   1   1   -1
ii. Discuss its limitations and provide suitable examples to illustrate these
limitations.
Solution:
Problem with formulas (7 marks)
X X X   t   α   yi   y Δ Δ Δ Δ w w w   b
1   2   3   n   w w w   b   1   2   3
1   2   3
-1   1   -1   -1   1   0   0   1   -1   1   -1   1   -1   1   -1
1   1   1   1   1   0   0   1   1   1   1   2   0   2   0
-1   -1   1   -1   1   4   1   -1   1   -1   -1   1   1   1   -1
-1   1   1   -1   1   0   0   0   0   0   0   2   0   0   2
Limitations and explanation with examples (3 marks)
•   Single-Layer Perceptron cannot classify non-linearly separable data
points.
• Complex problems, that involve a lot of parameters cannot be
solved by Single-Layer Perceptron.
Q3   b   How to decide number of filters in CNN? How it will influence the following [10]
CO-3;   parameters. 1) feature extraction capability, 2) dimensionality, 3)
BL-2   computational and memory cost, 4) risk of overfitting, 5) Hierarchical
Feature Learning.
Solution:
Each point for 2 marks
The number of filters in a CNN is often determined empirically through
experimentation, balancing model complexity and performance on the
validation set.
The depth of a convolutional layer—defined by the number of filters (or
kernels)—plays important role in determining the learning capacity of a
Convolutional Neural Network (CNN). Here's how:
1. Feature Extraction Capacity
• Each filter in a convolutional layer learns to detect a specific type of
feature (e.g., edges, textures, shapes etc.).
• More filters = more diverse features can be learned from the input
data.
•   This increases the representational power of the network, allowing it
to capture more complex patterns.
2. Dimensionality of Feature Maps
• The output of a convolutional layer is a set of feature maps, one for
each filter.
•   Increasing the number of filters increases the depth of the output
volume, which extracts richer information into subsequent layers.
3. Computational and Memory Cost
•   Increasing depth also increases the number of trainable parameters
(weights and biases).
•   This leads to higher computational cost, memory usage, and slower
training.
•   This leads to longer training times and greater memory usage,
especially in deeper networks.
4. Risk of Overfitting
********** 7 **********
--- page 8 ---
• A very deep layer with many filters might overfit the training data,
especially if the dataset is small or lacks diversity.
•   Regularization techniques can be used to address this issue.
5. Hierarchical Feature Learning
•   In early layers, filters typically learn low-level features (edges,
colours).
•   In deeper layers, filters learn high-level features (object parts,
shapes).
•   Increasing depth in later layers helps the network understand abstract
concepts.
Q4   a   i.   Illustrate how batch gradient descent and Stochastic Gradient Descent   [10]
CO-2;   (SGD) differ in terms of 1) oscillations in the loss function (with
BL-3   diagram/graph), 2) memory usage, and 3) suitability for large datasets.
ii. Discuss the impact of the learning rate being too high or too low during
training.
iii. Consider the cost function J(θ)=0.7𝜃3. Perform two iterations of SGD,
where learning rate (η or α) is 0.1, initial parameter 𝜃0=1. Write the
update rule and compute the updated parameter after each iteration.
Solution:
(i)   Three differences ( 3 marks)
Aspect   Batch Gradient Descent   Stochastic Gradient
(BGD)   Descent (SGD)
Oscillations   Smooth convergence;   Loss fluctuates a lot due to
in Loss   smaller oscillations   single-sample updates
Memory   High; needs to load entire   Low; processes one or few
Usage   dataset in memory   samples at a time
Suitability   Less suitable; slow and   More suitable; can handle
for Large   memory intensive   large datasets efficiently
Datasets
(ii)   Learning rate (2 marks)
Learning   Effect
Rate
Too high   Overshooting minima → may diverge or oscillate
without convergence
Too low   Very slow convergence → training may take too long
(iii)   Problem (5 marks)
********** 8 **********
--- page 9 ---
Q4   b   With reference to Gated Recurrent Unit (GRU) answer the following [10]
CO-4;   questions:
BL-2   i.   State the difference between LSTM and GRU in terms of architecture
and number of gates.
ii. Why is GRU computationally more efficient for smaller datasets?
iii.   Explain how GRUs “decide” to skip irrelevant tokens in a text
sequence.
iv.   Justify the advantage of bidirectional RNNs.
Solution:
i.   Difference: 3 marks
• LSTM: 3 gates (input, forget, output) + explicit cell state.
• GRU: 2 gates (update z, reset r); merges cell/hidden → simpler.
ii.   Computational efficiency of GRU: 2 marks
• Fewer parameters → faster training, less overfitting, adequate
capacity for shorter sequences.
iii.   Skipping irrelevant tokens :3 marks
• GRUs skip irrelevant tokens using their update (zt) and reset (rt)
gates.
• When a token provides little new information, zt is small — the
hidden state barely changes, effectively skipping that word.
• Similarly, rt can reduce the influence of past states if old information
is no longer relevant.
• This gating mechanism allows GRUs to focus on meaningful words
and ignore filler tokens in text sequences.
iv.   Advantage of bidirectional RNN: 2 marks
• Bidirectional RNN processes a sequence in both directions —
• forward (left → right) using past context, and
• backward (right → left) using future context.
This dual processing allows the model to consider information from the
entire sequence before making a prediction at any time step.
• In many NLP tasks (like named entity recognition, speech
recognition, or translation), the meaning of a word depends on both
what comes before and after it.
********** 9 **********
--- page 10 ---
Q5   a.   i.   Explain why a feedforward neural network fails to capture sequential [10]
CO-4;   context in language modelling.
BL-2   ii.   Describe how a recurrent connection in an RNN overcomes this
limitation.
iii.   Consider a RNN with a single hidden layer. Calculate the output of
the hidden layer ht given the following values: (use tanh as activation
function)
Wxh= [0.6 0.4   , Whh= [0.5 0.3 ht-1=[0 xt=[0
0.3 0.7]   0.2   0.4],   1],   1]
iv.   Explain how RNN-based language models predict the next word
probability distribution in a sentence.
Solution:
i. Why neural network fails: 2 marks
• Decisions are based on current input
• No memory about the past
• No future scope
ii. How RNN overcomes: 2 marks
• Can handle sequential data
• Considers current input as well as past inputs using memory
(recurrent connections) ht=f(xt,ht−1)
iii. Numerical :3 marks
ht=tanh(Wxhxt+Whhht−1)
iv. How RNN predicts next word: 3 marks
•   Uses hidden state ht to parameterize P(wt+1∣w≤t) =
Softmax(Whht+b).
•   Trained with cross-entropy over true next token; left-to-right
factorization of sentence probability.
•   wt+1: the next word the model is trying to predict.
•   w≤t: all previous words in the sentence (the context).
•   ht: the hidden state at time step t, which summarizes all the
contextual information from w1,w2,…,wt.
********** 10 **********
--- page 11 ---
•   Wh: a weight matrix that transforms this hidden state into a vector
of scores, one per word in the vocabulary.
•   b: a bias term.
•   Softmax: converts those scores into probabilities over the
vocabulary.
•   This mechanism allows the model to generate sentences word by
word, always conditioning on all previous words.
Q5   b   Explain the working principle of the RMSProp optimizer. Write the update [10]
CO-2;   rule and explain the role of the accumulated squared gradients. List
BL-2   advantages and disadvantages of RMSProp compared to standard SGD.
Solution:
Working Principle of RMSProp (3 marks)
RMSProp (Root Mean Square Propagation) is an adaptive learning rate
optimizer that improves upon AdaGrad. Its key idea is to maintain a moving
average of the squared gradients to scale the learning rate for each parameter
individually. This prevents the learning rate from diminishing too quickly,
which is a problem with AdaGrad.
RMSProp Update Rule (3 marks)
Where ρ is the decay rate and δ is a small constant to avoid division by zero.
(OR)
Where β is the decay rate and ɛ is a small constant to avoid division by zero
Role of Accumulated Squared Gradients (2 marks)
Reduces learning rate for parameters with large gradients. It increases
learning rate for parameters with small gradients and helps stabilize training
and prevent oscillations along steep directions.
Advantage and disadvantages (2 marks)
Advantages of RMSProp: (i) Addresses diminishing learning rate of
AdaGrad (ii) Adapts learning rate based on recent gradients
Disadvantages of RMSProp: (i) Can still get stuck in local minima on non-
convex problems (ii) Requires tuning of decay rate
Q6   a   Consider the CNN for binary classification as below. Compute the shape of   [10]
CO-3;   the output volume dimension and trainable parameters at each layer.
BL-3
Layer   Volume   No of
Dimension   parameters
Input   256 X 256 X 3
Conv2D
Filter = 32, stride = 1,
Kernel Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 64, stride = 1,
Kernel Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
********** 11 **********
--- page 12 ---
Filter = 128, stride = 1,
Kernel Size = 5x5,
padding=1
Pool2D Kernel Size = 2,
stride = 2
Flatten
Fully connected dense units
= 84
Fully connected dense units
= 32
Output
Solution: 1 mark for each calculation
Conv layer → ((kernel_width × kernel_height × input_channels) + 1) ×
num_filters
Pooling layer → number of parameters = 0
FC→ (number of neurons in previous layer × number of neurons in current
layer) + number of biases
Layer   Volume   No of
Dimension   parameters
Input   256 × 256 × 3   0
Conv2D
Filter = 32, stride = 1,   252 × 252 × 32   2,432
Kernel Size = 5X5
Pool2D Kernel Size = 2,
126 × 126 × 32   0
stride = 2
Conv2D
Filter = 64, stride = 1,   122 × 122 × 64   51,264
Kernel Size = 5X5
Pool2D Kernel Size = 2,
61 × 61 × 64   0
stride = 2
Conv2D
Filter = 128, stride = 1,
59 × 59 × 128   73,856
Kernel Size = 5x5,
padding=1
Pool2D Kernel Size = 2,
29 × 29 × 128   0
stride = 2
Flatten   29 × 29 × 128
0
= 1,07,648
Fully connected dense units
84 (vector)   9,042,516
= 84
Fully connected dense units
32 (vector)   2,720
= 32
Output   1 (vector)   33
Total trainable parameters: 91,72,821.
********** 12 **********
--- page 13 ---
Q6   b   Fully connected Neural Network with 10-layer is training using the sigmoid [10]
CO-2;   activation function.
BL-3   i. What is the activation output f (6)?
ii. What is the first derivative of gradient f 1(x) at x=6?
iii. Explain how this affects backpropagation in deeper layers.
iv. Solve the SoftMax values for y= [2.3, 4.5, 3.2]
Solution: f(6) ( 1mark)
Derivative (1 mark)
Interpretation: (1 mark)
The gradient is very small (~0.0025). In a deep network, multiplying many
such small gradients leads to the vanishing gradient problem (weights in
earlier layers barely update).
Compare the Loss function vs the Activation function.
Soft max values (2 marks)
Q7   a   Differentiate between single-layer and multi-layer feedforward neural [10]
CO-2;   networks. Explain the importance of non-linearity in hidden layers. Illustrate
BL-3   your answer by computing the output of a feedforward neural network with
the following configuration:
•   Structure: 3 input neurons → 2 hidden neurons (sigmoid activation)
→ 1 output neuron (sigmoid activation)
•   Input: X=[0.5,0.2,0.1]
• Weights and biases:
𝑊1 = [0.1 0.4 0.2 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.6 0.9], 𝑏2 = 0.5
0.3 0.5
Solution:
Difference (any three points - each 1 mark)
Aspect   Single-layer FNN   Multi-layer FNN
********** 13 **********
--- page 14 ---
Architecture   Has only one layer of Has one or more hidden
weights connecting   layers between input and
inputs directly to   output layers.
outputs.
Computation   Performs only a   Performs successive linear
linear mapping of   and nonlinear
input to output.   transformations, enabling
complex mappings.
Representatio   Can only solve   Can approximate non-linear
n Power   linearly separable   and complex functions
problems.   (universal approximators).
Activation   Typically linear.   Non-linear activations (e.g.,
Function   ReLU, Sigmoid, Tanh) used
in hidden layers.
Importance of Non-linearity (any two points- each 1 mark)
•   Without non-linear activation functions, a multi-layer network
collapses mathematically into an equivalent single-layer linear model
(since a composition of linear functions is still linear).
•   Non-linearity (e.g., sigmoid) allows the network to capture complex
patterns, decision boundaries, and feature interactions.
•   It enables hierarchical feature learning — each layer extracts
progressively more abstract representations.
Compute for each hidden neuron: (each step 1 mark)
For hidden neuron 1:
Z11 = (0.1)(0.5)+(0.4)(0.2)+(0.2)(0.1)+0.1= 0.25
b   Explain the concept of Transfer Learning using CNNs. Describe how pre-   [10]
Q7   trained models can be adapted for a new image classification task. Explain
CO-3   with any example model.
BL-2   Solution:
Concept Explanation (3 Marks):
Steps Involved (4 Marks):
1. Select a pre-trained model (e.g., VGG16, ResNet50, InceptionV3).
2. Load pre-trained weights trained on ImageNet or similar dataset.
3. Freeze base layers to retain generic features.
********** 14 **********
--- page 15 ---
4. Add new layers (Dense/SoftMax) to suit the new classification task.
5. Compile and train the model on the new dataset.
6. Fine-tune (optional): Unfreeze some deeper layers and retrain with
a small learning rate.
Example (3 Marks):
A suitable example using any pretrained VGG16, ResNet50, InceptionV3
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper f2dd39db4f11

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/MBATech_Computer_7047/Deep Learning/ANS_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: mixed (15 pages), mean OCR confidence 29.6

````text
SYNOPTICS
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
1. This question paper contains 15 pages.
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
Solution:
i) Two situations where deep learning models outperform traditional
machine learning algorithms (each 1 marks)
1. When working with unstructured and high-dimensional data: Deep
learning models (such as CNNs and RNNs) can automatically learn complex
patterns from images, audio, and text, whereas traditional ML models require
manual   feature   extraction. Example: Image   classification, speech
recognition, and natural language understanding.
2. When large volumes of labelled data are available: Deep learning requires
vast amounts of data to learn millions of parameters effectively. With
sufficient data and computational power, DL models outperform ML
algorithms in terms of accuracy and generalization. Example: Autonomous
driving, medical image analysis, and translation systems trained on huge
datasets.
ii. Application-based choice and justification (3 marks)
********** 1 **********
--- page 2 ---
Suitable
Application   Approa   Justification
ch
The dataset is small and features are
Machin   numerical and well-defined. Traditional
1. Predicting house
e   ML algorithms like Linear Regression
prices using 1,000
Learnin   or Random Forests perform well
structured records
g   without requiring large data or deep
architectures.
Involves processing image frames and
learning   spatial-temporal   features.
2.   Detecting
Deep   Deep   learning   models   such   as
emotions from facial
Learnin   Convolutional   Neural   Networks
expressions in real-
g   (CNNs) or 3D-CNNs can automatically
time video streams
extract   complex   visual   patterns,
outperforming ML methods.
Requires   understanding   long-range
language dependencies. Models like
3. Translating text
Deep   Recurrent Neural Networks (RNNs),
from one language to
Learnin LSTMs, or Transformers (e.g., Google
another (millions of
g   Translate) handle such   large-scale
sentence pairs)
sequential   data   far   better   than
traditional ML algorithms.
CO-2;   b.   i. Explain how   different   activation   functions   influence   gradient   [5]
BL-3   propagation, convergence behavior, and the overall performance of a deep
neural network.
ii. Discuss the scenarios or types of problems where specific activation
functions such as Sigmoid, Tanh, ReLU, and Leaky ReLU are preferred.
Solution:
Role of Activation Functions (2 marks): Activation functions introduce
non-linearity into deep neural networks. Without them, even multi-layer
networks behave like a single linear model and cannot learn complex
relationships.
Activation functions affect:
• Gradient propagation during backpropagation,
• Convergence speed during training, and
• Model performance and generalization.
Usage of activation functions (3 marks)
CO-2;   c.   i. Explain the role of L1 and L2 regularization in deep neural networks, and   [5]
BL-2   discuss how these techniques help prevent overfitting and improve the
model’s generalization to unseen data. You are training a fully connected
neural network layer with 4 neurons during training.
ii. The outputs of the neurons before applying dropout are: [0.8, −0.4, 0.6,
0.2]. A dropout rate of 50% is applied to this layer. Randomly determine
which neurons are dropped (assume a possible dropout mask) and
compute the output after applying dropout.
Solution:
Role of L1 and L2 regularization (2 mark)
Regularization is a technique used in deep learning to reduce overfitting by
discouraging the model from learning overly complex or large weight
values. It adds a penalty term to the loss function based on the magnitude of
the weights.
********** 2 **********
--- page 3 ---
The modified loss functions are:
• L1 Regularization (Lasso):
Adds the absolute value of the weights as a penalty.
• L2 Regularization (Ridge):
Adds the square of the weights as a penalty.
Here,
λ = regularization parameter (controls the strength of the penalty), wi=
weights of the model.
How They Help Prevent Overfitting (2 marks)
1. Controls weight magnitude: Both L1 and L2 regularization restrict
large weights, forcing the network to learn smaller and more general
weight values that perform better on unseen data.
2. Reduces model complexity:
o L1 tends to make many weights zero, leading to sparse models (some
neurons become inactive).
o L2 spreads weight values more evenly and helps smooth learning,
preventing any single weight from dominating.
By penalizing large weights, the network becomes less sensitive to noise,
improves generalization in the training data and performs better on test data
Output after dropout (1 mark)
Assume a random dropout mask (1 = keep, 0 = drop).
For example: mask=[1,0,1,0]
Multiply the neuron outputs by the mask:
output after dropout=[0.8x1, −0.4x0, 0.6x1, 0.2x0]=[0.8,0,0.6,0]
CO-4;   d. An e-commerce platform wants to automatically determine whether customer   [5]
BL-2   reviews are positive, negative, or neutral. Explain how an RNN model
processes customer review text to perform sentiment classification. Why is
RNN suitable for this task, and what role does word order play in determining
sentiment?
Solution:
How an RNN processes customer review text to perform sentiment
classification (2 marks)
• In sentiment analysis, a review (e.g., “The product is not good”) is treated
as a sequence of words.
• Each word is converted into a numerical vector (using embeddings like
Word2Vec or GloVe).
• The RNN reads these words sequentially, one at a time, maintaining a
hidden state that stores information from previous words.
• As the sequence progresses, the hidden state accumulates contextual
information — understanding how earlier words influence the meaning
of later ones.
• After processing the entire review, the final hidden state represents the
overall context and sentiment of the sentence.
• This representation is then passed to a fully connected (dense) layer with
a softmax activation to classify the sentiment as positive, negative, or
neutral.
Why RNN is suitable for sentiment analysis: (2 marks)
********** 3 **********
--- page 4 ---
RNNs are designed to handle sequential and contextual data, making them
ideal for text where word order and context matter. They can capture
dependencies between words that are far apart (e.g., “not good” vs. “good”).
Unlike traditional feedforward networks, RNNs remember what came before
in the sentence, giving them the ability to understand contextual polarity.
Role of word order in sentiment detection: (1 mark)
Word order changes meaning. For example: This phone is not bad” →
positive sentiment.
“This phone is bad” → negative sentiment.
RNNs preserve this order by processing words sequentially, ensuring that the
position of each word affects the final interpretation.
If the model ignored order, it might misclassify sentences with negations or
complex phrasing.
Q2   a   [10]
CO-2;
BL-3
The given network with the following i1= 0.25, i2= 0.7, w1= 0.2, w2=0.15,
w3= 0.28, w4=0.3, w5= 0.1, w6= 0.24, w7 = 0.12, w8= 0.21, b1= 1 and b2=1.
All neurons have a Sigmoid activation function. The actual output at O1 is
0.7 and at O2 is 0.3. Perform a forward pass and backward pass to update
weights of w1, w5 and w7 using Gradient Descent algorithm (Assume
learning rate = 1).
Solution:
Forward pass (outh1, outo1, total error – each 1 mark)
Backward pass (updated w7 and w5 - each 2 marks, and w1 – 3 marks)
********** 4 **********
--- page 5 ---
aod gos |
5\\o
gat ‘(1
at Te eh
panterdx ose | y
= pe (2>)* 3)

iy zi \\55
ale Ta cles Tees
la he Tae

[oct]
[oct]

O1 7 we ae 16 or: ad
ti . Dales a ey eae
e
te: uae 2) Co. | ie
t 2) fo * CAEWIV
23
= Aten =
(on arent) 0-18
Ea ahs (a

. sien sen tace

ae

HEA o-2Y4ol
=O NES
> ubor gabe
setae 88 STE AR one
ad at cubo, ) G* 0) O- cares:

Ow4 Fs

ait hye"

DO o- eae

-o-> lo © es

=0-062 5
- abt . ore -() (0-04) oe
wy = Pana ies
ste _ 2EE yD pokey x Dubey anit oy
BEE = Faro, ame, Pe

acre) (esky i-ested CH)
peer tomy Corey(etey(e Lest tf

2K
FIR Fok aC i Gk
--- page 6 ---
Q2   b   i. Explain how AlexNet’s design improved upon earlier traditional CNNs [10]
CO-3;   in terms of regularization, and training methodology.
BL-2   ii. Discuss how the Inception Network captures features at multiple scales
efficiently and the role of 1×1 convolutions in enhancing both
computational efficiency and feature representation in deep CNNs.
iii. Based on your analysis, which architecture would you recommend for
classification of large-scale image dataset and why?
Solution:
AlexNet (2012): (4 marks)
• Regularization Techniques: Introduced Dropout in fully connected layers
to prevent overfitting by randomly deactivating neurons during training.
Applied Data Augmentation (image translations, reflections, and patch
extractions) to improve generalization.
• Training Methodology: Adopted ReLU (Rectified Linear Unit) activation
instead of sigmoid/tanh, avoiding vanishing gradients and speeding up
training. Trained on GPUs, which significantly reduced training time for
large datasets. Used Local Response Normalization (LRN) to encourage
competition among neurons and improve generalization.
Inception Network (GoogleNet, 2014): (4 marks)
• Inception Modules: Each module applied 1×1, 3×3, and 5×5 convolutions
in parallel, along with a max-pooling branch. Captured features at multiple
spatial scales simultaneously, improving representational richness.
• Dimensionality Reduction: Introduced 1×1 convolutions before expensive
3×3 and 5×5 filters to reduce the number of channels, drastically lowering
computation and parameters.
• Depth with Efficiency: Built a 22-layer deep network but used only about
5 million parameters (vs. 60 million in AlexNet). Replaced fully connected
layers with global average pooling, reducing overfitting and model size.
• Regularization: Employed ReLU activations and dropout for stability and
generalization
• Performance: Achieved top-5 error rate of 6.7% on ImageNet.
Analysis (2 marks)
Both models revolutionized computer vision, AlexNet demonstrated the
power of deep CNNs, and Inception showed deep networks could be efficient
and scalable.
Q3   a   i. Determine the weights required to perform the classification as per the [10]
CO-2;   table using single layer perceptron network. Assume learning rate is 1 and
BL-3   initial weights are 0. Consider threshold=0 and solve for 1 epoch.
********** 6 **********
--- page 7 ---
X1   X2   X3   target
-1   1   -1   -1
1   1   1   1
-1   -1   1   -1
-1   1   1   -1
ii. Discuss its limitations and provide suitable examples to illustrate these
limitations.
Solution:
Problem with formulas (7 marks)
X X X   t   α   yi   y Δ Δ Δ Δ w w w   b
1   2   3   n   w w w   b   1   2   3
1   2   3
-1   1   -1   -1   1   0   0   1   -1   1   -1   1   -1   1   -1
1   1   1   1   1   0   0   1   1   1   1   2   0   2   0
-1   -1   1   -1   1   4   1   -1   1   -1   -1   1   1   1   -1
-1   1   1   -1   1   0   0   0   0   0   0   2   0   0   2
Limitations and explanation with examples (3 marks)
•   Single-Layer Perceptron cannot classify non-linearly separable data
points.
• Complex problems, that involve a lot of parameters cannot be
solved by Single-Layer Perceptron.
Q3   b   How to decide number of filters in CNN? How it will influence the following [10]
CO-3;   parameters. 1) feature extraction capability, 2) dimensionality, 3)
BL-2   computational and memory cost, 4) risk of overfitting, 5) Hierarchical
Feature Learning.
Solution:
Each point for 2 marks
The number of filters in a CNN is often determined empirically through
experimentation, balancing model complexity and performance on the
validation set.
The depth of a convolutional layer—defined by the number of filters (or
kernels)—plays important role in determining the learning capacity of a
Convolutional Neural Network (CNN). Here's how:
1. Feature Extraction Capacity
• Each filter in a convolutional layer learns to detect a specific type of
feature (e.g., edges, textures, shapes etc.).
• More filters = more diverse features can be learned from the input
data.
•   This increases the representational power of the network, allowing it
to capture more complex patterns.
2. Dimensionality of Feature Maps
• The output of a convolutional layer is a set of feature maps, one for
each filter.
•   Increasing the number of filters increases the depth of the output
volume, which extracts richer information into subsequent layers.
3. Computational and Memory Cost
•   Increasing depth also increases the number of trainable parameters
(weights and biases).
•   This leads to higher computational cost, memory usage, and slower
training.
•   This leads to longer training times and greater memory usage,
especially in deeper networks.
4. Risk of Overfitting
********** 7 **********
--- page 8 ---
• A very deep layer with many filters might overfit the training data,
especially if the dataset is small or lacks diversity.
•   Regularization techniques can be used to address this issue.
5. Hierarchical Feature Learning
•   In early layers, filters typically learn low-level features (edges,
colours).
•   In deeper layers, filters learn high-level features (object parts,
shapes).
•   Increasing depth in later layers helps the network understand abstract
concepts.
Q4   a   i.   Illustrate how batch gradient descent and Stochastic Gradient Descent   [10]
CO-2;   (SGD) differ in terms of 1) oscillations in the loss function (with
BL-3   diagram/graph), 2) memory usage, and 3) suitability for large datasets.
ii. Discuss the impact of the learning rate being too high or too low during
training.
iii. Consider the cost function J(θ)=0.7𝜃3. Perform two iterations of SGD,
where learning rate (η or α) is 0.1, initial parameter 𝜃0=1. Write the
update rule and compute the updated parameter after each iteration.
Solution:
(i)   Three differences ( 3 marks)
Aspect   Batch Gradient Descent   Stochastic Gradient
(BGD)   Descent (SGD)
Oscillations   Smooth convergence;   Loss fluctuates a lot due to
in Loss   smaller oscillations   single-sample updates
Memory   High; needs to load entire   Low; processes one or few
Usage   dataset in memory   samples at a time
Suitability   Less suitable; slow and   More suitable; can handle
for Large   memory intensive   large datasets efficiently
Datasets
(ii)   Learning rate (2 marks)
Learning   Effect
Rate
Too high   Overshooting minima → may diverge or oscillate
without convergence
Too low   Very slow convergence → training may take too long
(iii)   Problem (5 marks)
********** 8 **********
--- page 9 ---
Q4   b   With reference to Gated Recurrent Unit (GRU) answer the following [10]
CO-4;   questions:
BL-2   i.   State the difference between LSTM and GRU in terms of architecture
and number of gates.
ii. Why is GRU computationally more efficient for smaller datasets?
iii.   Explain how GRUs “decide” to skip irrelevant tokens in a text
sequence.
iv.   Justify the advantage of bidirectional RNNs.
Solution:
i.   Difference: 3 marks
• LSTM: 3 gates (input, forget, output) + explicit cell state.
• GRU: 2 gates (update z, reset r); merges cell/hidden → simpler.
ii.   Computational efficiency of GRU: 2 marks
• Fewer parameters → faster training, less overfitting, adequate
capacity for shorter sequences.
iii.   Skipping irrelevant tokens :3 marks
• GRUs skip irrelevant tokens using their update (zt) and reset (rt)
gates.
• When a token provides little new information, zt is small — the
hidden state barely changes, effectively skipping that word.
• Similarly, rt can reduce the influence of past states if old information
is no longer relevant.
• This gating mechanism allows GRUs to focus on meaningful words
and ignore filler tokens in text sequences.
iv.   Advantage of bidirectional RNN: 2 marks
• Bidirectional RNN processes a sequence in both directions —
• forward (left → right) using past context, and
• backward (right → left) using future context.
This dual processing allows the model to consider information from the
entire sequence before making a prediction at any time step.
• In many NLP tasks (like named entity recognition, speech
recognition, or translation), the meaning of a word depends on both
what comes before and after it.
********** 9 **********
--- page 10 ---
Q5   a.   i.   Explain why a feedforward neural network fails to capture sequential [10]
CO-4;   context in language modelling.
BL-2   ii.   Describe how a recurrent connection in an RNN overcomes this
limitation.
iii.   Consider a RNN with a single hidden layer. Calculate the output of
the hidden layer ht given the following values: (use tanh as activation
function)
Wxh= [0.6 0.4   , Whh= [0.5 0.3 ht-1=[0 xt=[0
0.3 0.7]   0.2   0.4],   1],   1]
iv.   Explain how RNN-based language models predict the next word
probability distribution in a sentence.
Solution:
i. Why neural network fails: 2 marks
• Decisions are based on current input
• No memory about the past
• No future scope
ii. How RNN overcomes: 2 marks
• Can handle sequential data
• Considers current input as well as past inputs using memory
(recurrent connections) ht=f(xt,ht−1)
iii. Numerical :3 marks
ht=tanh(Wxhxt+Whhht−1)
iv. How RNN predicts next word: 3 marks
•   Uses hidden state ht to parameterize P(wt+1∣w≤t) =
Softmax(Whht+b).
•   Trained with cross-entropy over true next token; left-to-right
factorization of sentence probability.
•   wt+1: the next word the model is trying to predict.
•   w≤t: all previous words in the sentence (the context).
•   ht: the hidden state at time step t, which summarizes all the
contextual information from w1,w2,…,wt.
********** 10 **********
--- page 11 ---
•   Wh: a weight matrix that transforms this hidden state into a vector
of scores, one per word in the vocabulary.
•   b: a bias term.
•   Softmax: converts those scores into probabilities over the
vocabulary.
•   This mechanism allows the model to generate sentences word by
word, always conditioning on all previous words.
Q5   b   Explain the working principle of the RMSProp optimizer. Write the update [10]
CO-2;   rule and explain the role of the accumulated squared gradients. List
BL-2   advantages and disadvantages of RMSProp compared to standard SGD.
Solution:
Working Principle of RMSProp (3 marks)
RMSProp (Root Mean Square Propagation) is an adaptive learning rate
optimizer that improves upon AdaGrad. Its key idea is to maintain a moving
average of the squared gradients to scale the learning rate for each parameter
individually. This prevents the learning rate from diminishing too quickly,
which is a problem with AdaGrad.
RMSProp Update Rule (3 marks)
Where ρ is the decay rate and δ is a small constant to avoid division by zero.
(OR)
Where β is the decay rate and ɛ is a small constant to avoid division by zero
Role of Accumulated Squared Gradients (2 marks)
Reduces learning rate for parameters with large gradients. It increases
learning rate for parameters with small gradients and helps stabilize training
and prevent oscillations along steep directions.
Advantage and disadvantages (2 marks)
Advantages of RMSProp: (i) Addresses diminishing learning rate of
AdaGrad (ii) Adapts learning rate based on recent gradients
Disadvantages of RMSProp: (i) Can still get stuck in local minima on non-
convex problems (ii) Requires tuning of decay rate
Q6   a   Consider the CNN for binary classification as below. Compute the shape of   [10]
CO-3;   the output volume dimension and trainable parameters at each layer.
BL-3
Layer   Volume   No of
Dimension   parameters
Input   256 X 256 X 3
Conv2D
Filter = 32, stride = 1,
Kernel Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 64, stride = 1,
Kernel Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
********** 11 **********
--- page 12 ---
Filter = 128, stride = 1,
Kernel Size = 5x5,
padding=1
Pool2D Kernel Size = 2,
stride = 2
Flatten
Fully connected dense units
= 84
Fully connected dense units
= 32
Output
Solution: 1 mark for each calculation
Conv layer → ((kernel_width × kernel_height × input_channels) + 1) ×
num_filters
Pooling layer → number of parameters = 0
FC→ (number of neurons in previous layer × number of neurons in current
layer) + number of biases
Layer   Volume   No of
Dimension   parameters
Input   256 × 256 × 3   0
Conv2D
Filter = 32, stride = 1,   252 × 252 × 32   2,432
Kernel Size = 5X5
Pool2D Kernel Size = 2,
126 × 126 × 32   0
stride = 2
Conv2D
Filter = 64, stride = 1,   122 × 122 × 64   51,264
Kernel Size = 5X5
Pool2D Kernel Size = 2,
61 × 61 × 64   0
stride = 2
Conv2D
Filter = 128, stride = 1,
59 × 59 × 128   73,856
Kernel Size = 5x5,
padding=1
Pool2D Kernel Size = 2,
29 × 29 × 128   0
stride = 2
Flatten   29 × 29 × 128
0
= 1,07,648
Fully connected dense units
84 (vector)   9,042,516
= 84
Fully connected dense units
32 (vector)   2,720
= 32
Output   1 (vector)   33
Total trainable parameters: 91,72,821.
********** 12 **********
--- page 13 ---
Q6   b   Fully connected Neural Network with 10-layer is training using the sigmoid [10]
CO-2;   activation function.
BL-3   i. What is the activation output f (6)?
ii. What is the first derivative of gradient f 1(x) at x=6?
iii. Explain how this affects backpropagation in deeper layers.
iv. Solve the SoftMax values for y= [2.3, 4.5, 3.2]
Solution: f(6) ( 1mark)
Derivative (1 mark)
Interpretation: (1 mark)
The gradient is very small (~0.0025). In a deep network, multiplying many
such small gradients leads to the vanishing gradient problem (weights in
earlier layers barely update).
Compare the Loss function vs the Activation function.
Soft max values (2 marks)
Q7   a   Differentiate between single-layer and multi-layer feedforward neural [10]
CO-2;   networks. Explain the importance of non-linearity in hidden layers. Illustrate
BL-3   your answer by computing the output of a feedforward neural network with
the following configuration:
•   Structure: 3 input neurons → 2 hidden neurons (sigmoid activation)
→ 1 output neuron (sigmoid activation)
•   Input: X=[0.5,0.2,0.1]
• Weights and biases:
𝑊1 = [0.1 0.4 0.2 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.6 0.9], 𝑏2 = 0.5
0.3 0.5
Solution:
Difference (any three points - each 1 mark)
Aspect   Single-layer FNN   Multi-layer FNN
********** 13 **********
--- page 14 ---
Architecture   Has only one layer of Has one or more hidden
weights connecting   layers between input and
inputs directly to   output layers.
outputs.
Computation   Performs only a   Performs successive linear
linear mapping of   and nonlinear
input to output.   transformations, enabling
complex mappings.
Representatio   Can only solve   Can approximate non-linear
n Power   linearly separable   and complex functions
problems.   (universal approximators).
Activation   Typically linear.   Non-linear activations (e.g.,
Function   ReLU, Sigmoid, Tanh) used
in hidden layers.
Importance of Non-linearity (any two points- each 1 mark)
•   Without non-linear activation functions, a multi-layer network
collapses mathematically into an equivalent single-layer linear model
(since a composition of linear functions is still linear).
•   Non-linearity (e.g., sigmoid) allows the network to capture complex
patterns, decision boundaries, and feature interactions.
•   It enables hierarchical feature learning — each layer extracts
progressively more abstract representations.
Compute for each hidden neuron: (each step 1 mark)
For hidden neuron 1:
Z11 = (0.1)(0.5)+(0.4)(0.2)+(0.2)(0.1)+0.1= 0.25
b   Explain the concept of Transfer Learning using CNNs. Describe how pre-   [10]
Q7   trained models can be adapted for a new image classification task. Explain
CO-3   with any example model.
BL-2   Solution:
Concept Explanation (3 Marks):
Steps Involved (4 Marks):
1. Select a pre-trained model (e.g., VGG16, ResNet50, InceptionV3).
2. Load pre-trained weights trained on ImageNet or similar dataset.
3. Freeze base layers to retain generic features.
********** 14 **********
--- page 15 ---
4. Add new layers (Dense/SoftMax) to suit the new classification task.
5. Compile and train the model on the new dataset.
6. Fine-tune (optional): Unfreeze some deeper layers and retrain with
a small learning rate.
Example (3 Marks):
A suitable example using any pretrained VGG16, ResNet50, InceptionV3
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 11 · Answer key · paper ac64c19b1157

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_11/Re-Exam/Integrated_Computer_7032/Deep Learning/ANS_Deep Learning(702AI0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: mixed (15 pages), mean OCR confidence 29.6

````text
SYNOPTICS
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
1. This question paper contains 15 pages.
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
Solution:
i) Two situations where deep learning models outperform traditional
machine learning algorithms (each 1 marks)
1. When working with unstructured and high-dimensional data: Deep
learning models (such as CNNs and RNNs) can automatically learn complex
patterns from images, audio, and text, whereas traditional ML models require
manual   feature   extraction. Example: Image   classification, speech
recognition, and natural language understanding.
2. When large volumes of labelled data are available: Deep learning requires
vast amounts of data to learn millions of parameters effectively. With
sufficient data and computational power, DL models outperform ML
algorithms in terms of accuracy and generalization. Example: Autonomous
driving, medical image analysis, and translation systems trained on huge
datasets.
ii. Application-based choice and justification (3 marks)
********** 1 **********
--- page 2 ---
Suitable
Application   Approa   Justification
ch
The dataset is small and features are
Machin   numerical and well-defined. Traditional
1. Predicting house
e   ML algorithms like Linear Regression
prices using 1,000
Learnin   or Random Forests perform well
structured records
g   without requiring large data or deep
architectures.
Involves processing image frames and
learning   spatial-temporal   features.
2.   Detecting
Deep   Deep   learning   models   such   as
emotions from facial
Learnin   Convolutional   Neural   Networks
expressions in real-
g   (CNNs) or 3D-CNNs can automatically
time video streams
extract   complex   visual   patterns,
outperforming ML methods.
Requires   understanding   long-range
language dependencies. Models like
3. Translating text
Deep   Recurrent Neural Networks (RNNs),
from one language to
Learnin LSTMs, or Transformers (e.g., Google
another (millions of
g   Translate) handle such   large-scale
sentence pairs)
sequential   data   far   better   than
traditional ML algorithms.
CO-2;   b.   i. Explain how   different   activation   functions   influence   gradient   [5]
BL-3   propagation, convergence behavior, and the overall performance of a deep
neural network.
ii. Discuss the scenarios or types of problems where specific activation
functions such as Sigmoid, Tanh, ReLU, and Leaky ReLU are preferred.
Solution:
Role of Activation Functions (2 marks): Activation functions introduce
non-linearity into deep neural networks. Without them, even multi-layer
networks behave like a single linear model and cannot learn complex
relationships.
Activation functions affect:
• Gradient propagation during backpropagation,
• Convergence speed during training, and
• Model performance and generalization.
Usage of activation functions (3 marks)
CO-2;   c.   i. Explain the role of L1 and L2 regularization in deep neural networks, and   [5]
BL-2   discuss how these techniques help prevent overfitting and improve the
model’s generalization to unseen data. You are training a fully connected
neural network layer with 4 neurons during training.
ii. The outputs of the neurons before applying dropout are: [0.8, −0.4, 0.6,
0.2]. A dropout rate of 50% is applied to this layer. Randomly determine
which neurons are dropped (assume a possible dropout mask) and
compute the output after applying dropout.
Solution:
Role of L1 and L2 regularization (2 mark)
Regularization is a technique used in deep learning to reduce overfitting by
discouraging the model from learning overly complex or large weight
values. It adds a penalty term to the loss function based on the magnitude of
the weights.
********** 2 **********
--- page 3 ---
The modified loss functions are:
• L1 Regularization (Lasso):
Adds the absolute value of the weights as a penalty.
• L2 Regularization (Ridge):
Adds the square of the weights as a penalty.
Here,
λ = regularization parameter (controls the strength of the penalty), wi=
weights of the model.
How They Help Prevent Overfitting (2 marks)
1. Controls weight magnitude: Both L1 and L2 regularization restrict
large weights, forcing the network to learn smaller and more general
weight values that perform better on unseen data.
2. Reduces model complexity:
o L1 tends to make many weights zero, leading to sparse models (some
neurons become inactive).
o L2 spreads weight values more evenly and helps smooth learning,
preventing any single weight from dominating.
By penalizing large weights, the network becomes less sensitive to noise,
improves generalization in the training data and performs better on test data
Output after dropout (1 mark)
Assume a random dropout mask (1 = keep, 0 = drop).
For example: mask=[1,0,1,0]
Multiply the neuron outputs by the mask:
output after dropout=[0.8x1, −0.4x0, 0.6x1, 0.2x0]=[0.8,0,0.6,0]
CO-4;   d. An e-commerce platform wants to automatically determine whether customer   [5]
BL-2   reviews are positive, negative, or neutral. Explain how an RNN model
processes customer review text to perform sentiment classification. Why is
RNN suitable for this task, and what role does word order play in determining
sentiment?
Solution:
How an RNN processes customer review text to perform sentiment
classification (2 marks)
• In sentiment analysis, a review (e.g., “The product is not good”) is treated
as a sequence of words.
• Each word is converted into a numerical vector (using embeddings like
Word2Vec or GloVe).
• The RNN reads these words sequentially, one at a time, maintaining a
hidden state that stores information from previous words.
• As the sequence progresses, the hidden state accumulates contextual
information — understanding how earlier words influence the meaning
of later ones.
• After processing the entire review, the final hidden state represents the
overall context and sentiment of the sentence.
• This representation is then passed to a fully connected (dense) layer with
a softmax activation to classify the sentiment as positive, negative, or
neutral.
Why RNN is suitable for sentiment analysis: (2 marks)
********** 3 **********
--- page 4 ---
RNNs are designed to handle sequential and contextual data, making them
ideal for text where word order and context matter. They can capture
dependencies between words that are far apart (e.g., “not good” vs. “good”).
Unlike traditional feedforward networks, RNNs remember what came before
in the sentence, giving them the ability to understand contextual polarity.
Role of word order in sentiment detection: (1 mark)
Word order changes meaning. For example: This phone is not bad” →
positive sentiment.
“This phone is bad” → negative sentiment.
RNNs preserve this order by processing words sequentially, ensuring that the
position of each word affects the final interpretation.
If the model ignored order, it might misclassify sentences with negations or
complex phrasing.
Q2   a   [10]
CO-2;
BL-3
The given network with the following i1= 0.25, i2= 0.7, w1= 0.2, w2=0.15,
w3= 0.28, w4=0.3, w5= 0.1, w6= 0.24, w7 = 0.12, w8= 0.21, b1= 1 and b2=1.
All neurons have a Sigmoid activation function. The actual output at O1 is
0.7 and at O2 is 0.3. Perform a forward pass and backward pass to update
weights of w1, w5 and w7 using Gradient Descent algorithm (Assume
learning rate = 1).
Solution:
Forward pass (outh1, outo1, total error – each 1 mark)
Backward pass (updated w7 and w5 - each 2 marks, and w1 – 3 marks)
********** 4 **********
--- page 5 ---
aod gos |
5\\o
gat ‘(1
at Te eh
panterdx ose | y
= pe (2>)* 3)

iy zi \\55
ale Ta cles Tees
la he Tae

[oct]
[oct]

O1 7 we ae 16 or: ad
ti . Dales a ey eae
e
te: uae 2) Co. | ie
t 2) fo * CAEWIV
23
= Aten =
(on arent) 0-18
Ea ahs (a

. sien sen tace

ae

HEA o-2Y4ol
=O NES
> ubor gabe
setae 88 STE AR one
ad at cubo, ) G* 0) O- cares:

Ow4 Fs

ait hye"

DO o- eae

-o-> lo © es

=0-062 5
- abt . ore -() (0-04) oe
wy = Pana ies
ste _ 2EE yD pokey x Dubey anit oy
BEE = Faro, ame, Pe

acre) (esky i-ested CH)
peer tomy Corey(etey(e Lest tf

2K
FIR Fok aC i Gk
--- page 6 ---
Q2   b   i. Explain how AlexNet’s design improved upon earlier traditional CNNs [10]
CO-3;   in terms of regularization, and training methodology.
BL-2   ii. Discuss how the Inception Network captures features at multiple scales
efficiently and the role of 1×1 convolutions in enhancing both
computational efficiency and feature representation in deep CNNs.
iii. Based on your analysis, which architecture would you recommend for
classification of large-scale image dataset and why?
Solution:
AlexNet (2012): (4 marks)
• Regularization Techniques: Introduced Dropout in fully connected layers
to prevent overfitting by randomly deactivating neurons during training.
Applied Data Augmentation (image translations, reflections, and patch
extractions) to improve generalization.
• Training Methodology: Adopted ReLU (Rectified Linear Unit) activation
instead of sigmoid/tanh, avoiding vanishing gradients and speeding up
training. Trained on GPUs, which significantly reduced training time for
large datasets. Used Local Response Normalization (LRN) to encourage
competition among neurons and improve generalization.
Inception Network (GoogleNet, 2014): (4 marks)
• Inception Modules: Each module applied 1×1, 3×3, and 5×5 convolutions
in parallel, along with a max-pooling branch. Captured features at multiple
spatial scales simultaneously, improving representational richness.
• Dimensionality Reduction: Introduced 1×1 convolutions before expensive
3×3 and 5×5 filters to reduce the number of channels, drastically lowering
computation and parameters.
• Depth with Efficiency: Built a 22-layer deep network but used only about
5 million parameters (vs. 60 million in AlexNet). Replaced fully connected
layers with global average pooling, reducing overfitting and model size.
• Regularization: Employed ReLU activations and dropout for stability and
generalization
• Performance: Achieved top-5 error rate of 6.7% on ImageNet.
Analysis (2 marks)
Both models revolutionized computer vision, AlexNet demonstrated the
power of deep CNNs, and Inception showed deep networks could be efficient
and scalable.
Q3   a   i. Determine the weights required to perform the classification as per the [10]
CO-2;   table using single layer perceptron network. Assume learning rate is 1 and
BL-3   initial weights are 0. Consider threshold=0 and solve for 1 epoch.
********** 6 **********
--- page 7 ---
X1   X2   X3   target
-1   1   -1   -1
1   1   1   1
-1   -1   1   -1
-1   1   1   -1
ii. Discuss its limitations and provide suitable examples to illustrate these
limitations.
Solution:
Problem with formulas (7 marks)
X X X   t   α   yi   y Δ Δ Δ Δ w w w   b
1   2   3   n   w w w   b   1   2   3
1   2   3
-1   1   -1   -1   1   0   0   1   -1   1   -1   1   -1   1   -1
1   1   1   1   1   0   0   1   1   1   1   2   0   2   0
-1   -1   1   -1   1   4   1   -1   1   -1   -1   1   1   1   -1
-1   1   1   -1   1   0   0   0   0   0   0   2   0   0   2
Limitations and explanation with examples (3 marks)
•   Single-Layer Perceptron cannot classify non-linearly separable data
points.
• Complex problems, that involve a lot of parameters cannot be
solved by Single-Layer Perceptron.
Q3   b   How to decide number of filters in CNN? How it will influence the following [10]
CO-3;   parameters. 1) feature extraction capability, 2) dimensionality, 3)
BL-2   computational and memory cost, 4) risk of overfitting, 5) Hierarchical
Feature Learning.
Solution:
Each point for 2 marks
The number of filters in a CNN is often determined empirically through
experimentation, balancing model complexity and performance on the
validation set.
The depth of a convolutional layer—defined by the number of filters (or
kernels)—plays important role in determining the learning capacity of a
Convolutional Neural Network (CNN). Here's how:
1. Feature Extraction Capacity
• Each filter in a convolutional layer learns to detect a specific type of
feature (e.g., edges, textures, shapes etc.).
• More filters = more diverse features can be learned from the input
data.
•   This increases the representational power of the network, allowing it
to capture more complex patterns.
2. Dimensionality of Feature Maps
• The output of a convolutional layer is a set of feature maps, one for
each filter.
•   Increasing the number of filters increases the depth of the output
volume, which extracts richer information into subsequent layers.
3. Computational and Memory Cost
•   Increasing depth also increases the number of trainable parameters
(weights and biases).
•   This leads to higher computational cost, memory usage, and slower
training.
•   This leads to longer training times and greater memory usage,
especially in deeper networks.
4. Risk of Overfitting
********** 7 **********
--- page 8 ---
• A very deep layer with many filters might overfit the training data,
especially if the dataset is small or lacks diversity.
•   Regularization techniques can be used to address this issue.
5. Hierarchical Feature Learning
•   In early layers, filters typically learn low-level features (edges,
colours).
•   In deeper layers, filters learn high-level features (object parts,
shapes).
•   Increasing depth in later layers helps the network understand abstract
concepts.
Q4   a   i.   Illustrate how batch gradient descent and Stochastic Gradient Descent   [10]
CO-2;   (SGD) differ in terms of 1) oscillations in the loss function (with
BL-3   diagram/graph), 2) memory usage, and 3) suitability for large datasets.
ii. Discuss the impact of the learning rate being too high or too low during
training.
iii. Consider the cost function J(θ)=0.7𝜃3. Perform two iterations of SGD,
where learning rate (η or α) is 0.1, initial parameter 𝜃0=1. Write the
update rule and compute the updated parameter after each iteration.
Solution:
(i)   Three differences ( 3 marks)
Aspect   Batch Gradient Descent   Stochastic Gradient
(BGD)   Descent (SGD)
Oscillations   Smooth convergence;   Loss fluctuates a lot due to
in Loss   smaller oscillations   single-sample updates
Memory   High; needs to load entire   Low; processes one or few
Usage   dataset in memory   samples at a time
Suitability   Less suitable; slow and   More suitable; can handle
for Large   memory intensive   large datasets efficiently
Datasets
(ii)   Learning rate (2 marks)
Learning   Effect
Rate
Too high   Overshooting minima → may diverge or oscillate
without convergence
Too low   Very slow convergence → training may take too long
(iii)   Problem (5 marks)
********** 8 **********
--- page 9 ---
Q4   b   With reference to Gated Recurrent Unit (GRU) answer the following [10]
CO-4;   questions:
BL-2   i.   State the difference between LSTM and GRU in terms of architecture
and number of gates.
ii. Why is GRU computationally more efficient for smaller datasets?
iii.   Explain how GRUs “decide” to skip irrelevant tokens in a text
sequence.
iv.   Justify the advantage of bidirectional RNNs.
Solution:
i.   Difference: 3 marks
• LSTM: 3 gates (input, forget, output) + explicit cell state.
• GRU: 2 gates (update z, reset r); merges cell/hidden → simpler.
ii.   Computational efficiency of GRU: 2 marks
• Fewer parameters → faster training, less overfitting, adequate
capacity for shorter sequences.
iii.   Skipping irrelevant tokens :3 marks
• GRUs skip irrelevant tokens using their update (zt) and reset (rt)
gates.
• When a token provides little new information, zt is small — the
hidden state barely changes, effectively skipping that word.
• Similarly, rt can reduce the influence of past states if old information
is no longer relevant.
• This gating mechanism allows GRUs to focus on meaningful words
and ignore filler tokens in text sequences.
iv.   Advantage of bidirectional RNN: 2 marks
• Bidirectional RNN processes a sequence in both directions —
• forward (left → right) using past context, and
• backward (right → left) using future context.
This dual processing allows the model to consider information from the
entire sequence before making a prediction at any time step.
• In many NLP tasks (like named entity recognition, speech
recognition, or translation), the meaning of a word depends on both
what comes before and after it.
********** 9 **********
--- page 10 ---
Q5   a.   i.   Explain why a feedforward neural network fails to capture sequential [10]
CO-4;   context in language modelling.
BL-2   ii.   Describe how a recurrent connection in an RNN overcomes this
limitation.
iii.   Consider a RNN with a single hidden layer. Calculate the output of
the hidden layer ht given the following values: (use tanh as activation
function)
Wxh= [0.6 0.4   , Whh= [0.5 0.3 ht-1=[0 xt=[0
0.3 0.7]   0.2   0.4],   1],   1]
iv.   Explain how RNN-based language models predict the next word
probability distribution in a sentence.
Solution:
i. Why neural network fails: 2 marks
• Decisions are based on current input
• No memory about the past
• No future scope
ii. How RNN overcomes: 2 marks
• Can handle sequential data
• Considers current input as well as past inputs using memory
(recurrent connections) ht=f(xt,ht−1)
iii. Numerical :3 marks
ht=tanh(Wxhxt+Whhht−1)
iv. How RNN predicts next word: 3 marks
•   Uses hidden state ht to parameterize P(wt+1∣w≤t) =
Softmax(Whht+b).
•   Trained with cross-entropy over true next token; left-to-right
factorization of sentence probability.
•   wt+1: the next word the model is trying to predict.
•   w≤t: all previous words in the sentence (the context).
•   ht: the hidden state at time step t, which summarizes all the
contextual information from w1,w2,…,wt.
********** 10 **********
--- page 11 ---
•   Wh: a weight matrix that transforms this hidden state into a vector
of scores, one per word in the vocabulary.
•   b: a bias term.
•   Softmax: converts those scores into probabilities over the
vocabulary.
•   This mechanism allows the model to generate sentences word by
word, always conditioning on all previous words.
Q5   b   Explain the working principle of the RMSProp optimizer. Write the update [10]
CO-2;   rule and explain the role of the accumulated squared gradients. List
BL-2   advantages and disadvantages of RMSProp compared to standard SGD.
Solution:
Working Principle of RMSProp (3 marks)
RMSProp (Root Mean Square Propagation) is an adaptive learning rate
optimizer that improves upon AdaGrad. Its key idea is to maintain a moving
average of the squared gradients to scale the learning rate for each parameter
individually. This prevents the learning rate from diminishing too quickly,
which is a problem with AdaGrad.
RMSProp Update Rule (3 marks)
Where ρ is the decay rate and δ is a small constant to avoid division by zero.
(OR)
Where β is the decay rate and ɛ is a small constant to avoid division by zero
Role of Accumulated Squared Gradients (2 marks)
Reduces learning rate for parameters with large gradients. It increases
learning rate for parameters with small gradients and helps stabilize training
and prevent oscillations along steep directions.
Advantage and disadvantages (2 marks)
Advantages of RMSProp: (i) Addresses diminishing learning rate of
AdaGrad (ii) Adapts learning rate based on recent gradients
Disadvantages of RMSProp: (i) Can still get stuck in local minima on non-
convex problems (ii) Requires tuning of decay rate
Q6   a   Consider the CNN for binary classification as below. Compute the shape of   [10]
CO-3;   the output volume dimension and trainable parameters at each layer.
BL-3
Layer   Volume   No of
Dimension   parameters
Input   256 X 256 X 3
Conv2D
Filter = 32, stride = 1,
Kernel Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
Filter = 64, stride = 1,
Kernel Size = 5X5
Pool2D Kernel Size = 2,
stride = 2
Conv2D
********** 11 **********
--- page 12 ---
Filter = 128, stride = 1,
Kernel Size = 5x5,
padding=1
Pool2D Kernel Size = 2,
stride = 2
Flatten
Fully connected dense units
= 84
Fully connected dense units
= 32
Output
Solution: 1 mark for each calculation
Conv layer → ((kernel_width × kernel_height × input_channels) + 1) ×
num_filters
Pooling layer → number of parameters = 0
FC→ (number of neurons in previous layer × number of neurons in current
layer) + number of biases
Layer   Volume   No of
Dimension   parameters
Input   256 × 256 × 3   0
Conv2D
Filter = 32, stride = 1,   252 × 252 × 32   2,432
Kernel Size = 5X5
Pool2D Kernel Size = 2,
126 × 126 × 32   0
stride = 2
Conv2D
Filter = 64, stride = 1,   122 × 122 × 64   51,264
Kernel Size = 5X5
Pool2D Kernel Size = 2,
61 × 61 × 64   0
stride = 2
Conv2D
Filter = 128, stride = 1,
59 × 59 × 128   73,856
Kernel Size = 5x5,
padding=1
Pool2D Kernel Size = 2,
29 × 29 × 128   0
stride = 2
Flatten   29 × 29 × 128
0
= 1,07,648
Fully connected dense units
84 (vector)   9,042,516
= 84
Fully connected dense units
32 (vector)   2,720
= 32
Output   1 (vector)   33
Total trainable parameters: 91,72,821.
********** 12 **********
--- page 13 ---
Q6   b   Fully connected Neural Network with 10-layer is training using the sigmoid [10]
CO-2;   activation function.
BL-3   i. What is the activation output f (6)?
ii. What is the first derivative of gradient f 1(x) at x=6?
iii. Explain how this affects backpropagation in deeper layers.
iv. Solve the SoftMax values for y= [2.3, 4.5, 3.2]
Solution: f(6) ( 1mark)
Derivative (1 mark)
Interpretation: (1 mark)
The gradient is very small (~0.0025). In a deep network, multiplying many
such small gradients leads to the vanishing gradient problem (weights in
earlier layers barely update).
Compare the Loss function vs the Activation function.
Soft max values (2 marks)
Q7   a   Differentiate between single-layer and multi-layer feedforward neural [10]
CO-2;   networks. Explain the importance of non-linearity in hidden layers. Illustrate
BL-3   your answer by computing the output of a feedforward neural network with
the following configuration:
•   Structure: 3 input neurons → 2 hidden neurons (sigmoid activation)
→ 1 output neuron (sigmoid activation)
•   Input: X=[0.5,0.2,0.1]
• Weights and biases:
𝑊1 = [0.1 0.4 0.2 0.7], 𝑏1 = [0.1 0.2], 𝑊2 = [0.6 0.9], 𝑏2 = 0.5
0.3 0.5
Solution:
Difference (any three points - each 1 mark)
Aspect   Single-layer FNN   Multi-layer FNN
********** 13 **********
--- page 14 ---
Architecture   Has only one layer of Has one or more hidden
weights connecting   layers between input and
inputs directly to   output layers.
outputs.
Computation   Performs only a   Performs successive linear
linear mapping of   and nonlinear
input to output.   transformations, enabling
complex mappings.
Representatio   Can only solve   Can approximate non-linear
n Power   linearly separable   and complex functions
problems.   (universal approximators).
Activation   Typically linear.   Non-linear activations (e.g.,
Function   ReLU, Sigmoid, Tanh) used
in hidden layers.
Importance of Non-linearity (any two points- each 1 mark)
•   Without non-linear activation functions, a multi-layer network
collapses mathematically into an equivalent single-layer linear model
(since a composition of linear functions is still linear).
•   Non-linearity (e.g., sigmoid) allows the network to capture complex
patterns, decision boundaries, and feature interactions.
•   It enables hierarchical feature learning — each layer extracts
progressively more abstract representations.
Compute for each hidden neuron: (each step 1 mark)
For hidden neuron 1:
Z11 = (0.1)(0.5)+(0.4)(0.2)+(0.2)(0.1)+0.1= 0.25
b   Explain the concept of Transfer Learning using CNNs. Describe how pre-   [10]
Q7   trained models can be adapted for a new image classification task. Explain
CO-3   with any example model.
BL-2   Solution:
Concept Explanation (3 Marks):
Steps Involved (4 Marks):
1. Select a pre-trained model (e.g., VGG16, ResNet50, InceptionV3).
2. Load pre-trained weights trained on ImageNet or similar dataset.
3. Freeze base layers to retain generic features.
********** 14 **********
--- page 15 ---
4. Add new layers (Dense/SoftMax) to suit the new classification task.
5. Compile and train the model on the new dataset.
6. Fine-tune (optional): Unfreeze some deeper layers and retrain with
a small learning rate.
Example (3 Marks):
A suitable example using any pretrained VGG16, ResNet50, InceptionV3
********** 15 **********
````

## 2024-25 · Re-Exam · Sem 8 · Answer key · paper 23dcb14db1c7

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2024/Sem_08/Re-Exam/BTech_CSBS_7036/Deep Learning/ANS_Deep Learning(702AI0C008)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: mixed (8 pages), mean OCR confidence 81.0

````text
SYNOPTICS
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
1. This question paper contains 8 pages.
2. Question No. 1 is compulsory
3. Out of the remianing questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Discuss CNN based two convolution.
CO-3
[5]
BL-1,2
b.
What will the convolution operation's output be over the following feature map?
Where the following kernel is applied with a stride of 2.
Input Feature map   Kernel
1 2 3
3   5   8   2   3
CO-3   3 2   3   2   5   4 5 6
[5]
BL-2,4
1 2 3
1   2   3   8   3
6   4   5   1   4
3   4   7   4
3
CO-4   c.   What are the computational challenges of BPTT? Suggest optimization   [5]
BL-3   techniques to improve efficiency
********** 1 **********
--- page 2 ---
CO-2   d.
In autonomous driving systems, deep learning models sometimes fail in unusual
BL-3
conditions. Explain two limitations responsible for this issue.
[5]
a.   [10]
Compare RNN, LSTM, and GRU based on:
1) Architecture
Q2   2) Computational complexity
CO-   3) Ability to capture long-term dependencies
b
4,BL-4   4) Training efficiency
Self Explanatory
CO-3,
BL-3   Design an LSTM-based model for:
1) Time-series prediction
2) Explain input representation, architecture, and training process.
********** 2 **********
--- page 3 ---
[5+5]
Explain the architecture of Gated Recurrent Unit (GRU) networks using a
a.   diagram. Then, use formulas to discuss the critical components of a GRU unit
(All gates).
Self explanatory
Write and explain the algorithm for ADAM and SGD with Nesterov momentum.
b.
Q3
[10]
CO-4
BL-4
CO-2
[10]
BL-2
Q4.   a.   Consider the neural network as shown in the figure.   [10]
The inputs x1, x2, and the initial weights and two biases are given. The actual
CO-2   output is [0.9, 0.1] for the two output neurons. The activation used is sigmoid.
BL-3   {w3 is between x1-h2, w6 is between h1-o2}, Learning rate is 0.55.
Calculate the following: (4 significants)
1. Predicted output after forward propagation.
2. Mean square error after the first forward pass
3. Calculate the updated weights w4 and w8 after the first iteration of
backpropagation.
********** 3 **********
--- page 4 ---
CO-2
BL-3
[10]
b.
Self explanatory
A fully connected Neural Network with 8 layers is being trained using the sigmoid
activation function.
i   What is the activation output f / (12.9)?
ii   What is the first derivative of the gradient f (x) at x=8?
iii   Explain how this affects backpropagation in deeper layers.
iv   Solve the SoftMax values for y = [3.5, 5.8, 4.4]
Selfexplanatory
[10]
a.
Discuss common problems in Gradient Descent:
1. Local minima
2. Saddle points
3. Vanishing gradients
Q5
CO-3
BL-1,2
CO-4
BL-2
********** 4 **********
--- page 5 ---
b.
[10]
Explain the application of deep learning in speech recognition systems:
1. Feature extraction
2. Model architecture
3. Training challenges
********** 5 **********
--- page 6 ---
Q6   a.   You are training a deep learning model on limited GPU memory.
CO-4   How would you choose the batch size? Justify your answer.
BL-4
CO-3
BL-   [10]
2,1,5
[10]
Explain the architecture of the Inception Model and why you use 1x1
convolution in it?
Self explanatory
Design an AlexNet-inspired architecture for a new image classification task.
b.   Specify how you would adapt the architecture to work with a dataset that
contains smaller images (e.g., 64 × 64 64×64 pixels) and fewer classes than
ImageNet. What modifications would you make to the original AlexNet
architecture to suit this task.
Modified AlexNet-Inspired Architecture for 64×64 Images:
•   Input Layer: 64×64×3
•   Conv1: 5×5 kernel, 32 filters, stride 1, padding 2 → Max Pooling (2×2,
stride 2) → Output size: 32×32×32
********** 6 **********
--- page 7 ---
•   Conv2: 3×3 kernel, 64 filters, stride 1, padding 1 → Max Pooling (2×2,
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
Self explanatory
a.   [5+5]
1) Interpret the trade-off between bias and variance over deep learning models
by taking relevant examples.
2) Implement EXNOR gates using perceptron models.
b.   Self explanatory
Explain how the learning rate affects:
1. Speed of convergence
2.   Stability of training
3. Risk of divergence
Q7.
CO-3
BL-2
CO-3
BL-4
********** 7 **********
--- page 8 ---
¢ 3. Risk of Divergence [545]

Very High Learning Rate
© Steps are too large
¢ Loss may increase instead of decrease

1) Consider a feature map as shown below[

l 2 |3 {4
5. 16 |7 [8
2. |4 l 3
9 |7 |5 |6

i. Perform 2x2 max pooling with a stride of 2 on this feature map
ii, Perform 2x2 average pooling with a stride of 1 (no padding)
iii. | Mention the significance of pooling in CNN architecture

Self Explanatory

FIC QF EH 1
````
