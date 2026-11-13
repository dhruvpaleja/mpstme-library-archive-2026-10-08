# Neural Networks and Deep Learning: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 191c8e48bfb5

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSE_DS_7057/Neural Networks and Deep Learning/ANS_Neural Networks and Deep Learning(702DB0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: mixed (18 pages), mean OCR confidence 65.0
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Neural Networks and Deep Learning
Date: 11 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Candidates should read carefully the instructions printed on the question paper and on the cover of the
Answer Book, which is provided for their use.
5. Question No. 1 is compulsory.
6. Out of remaining questions, attempt any 4 questions.
7. In all 5 questions to be attempted.
8. Assume Suitable data if necessary.
9. All code is to be deployed on Google Colab for creation and testing.
10. All coding question should also be submitted on answer book itself.
11. Internet is allowed during code implementation in google Colab.
Q1 (Answer briefly)   (20 Marks)
CO-1;   a.   (2 Marks – Concept)   [5]
BL-2   Vectorization refers to performing operations on entire vectors or
matrices instead of using loops. In neural networks, this allows
simultaneous computation over multiple training examples. For
example, instead of computing output for each input separately, we use
matrix multiplication:
(3 Marks – Explanation + GPU Impact)
Vectorization improves computational efficiency because matrix
multiplications are highly optimized. It reduces time complexity from
iterative operations to parallel operations. Memory usage is optimized
by avoiding repeated storage of intermediate variables. It also enables
batch processing:
********** 1 **********
--- page 2 ---
On GPUs, thousands of cores execute these matrix operations in
parallel, significantly accelerating training and making large-scale deep
learning feasible.
CO-1;   b.   (2 Marks – Core Idea)   [5]
BL-2
(3 Marks – Step-wise Explanation)
CO-2;   c.   (2 Marks – Problem Analysis)   [5]
BL-3   Overfitting occurs when the model fits training data too closely,
resulting in poor generalization. This is reflected in high training
accuracy but low validation accuracy. The loss function becomes overly
dependent on training data.
(3 Marks – Solutions with Equations)
********** 2 **********

[Text in pictures on this page, read by OCR]
The input features are represented as A") = X. For each layer I, the weighted sum Z"" is computed and

passed through an activation function such as ReLU:
A"! = max(0, Z")

This process continues until the final layer, where for classification problems, softmax is applied:

All = et
Se

Intermediate activations are stored for use during backpropagation.

Regularization modifies the loss function:
J = Joriginat + > > W? (L2 Regularization)
Dropout randomly deactivates neurons during training:
Au = A". p! (mask)

Early stopping halts training when validation loss increases. These methods reduce model complexity and
improve generalization.
--- page 3 ---
CO-3;   d.   (2 Marks – Components)   [5]
BL-3   CNNs consist of convolution, pooling, and activation layers for image
processing.
(3 Marks – Explanation with Equations)
Q2 (Attempt any 4)   (80 Marks)
Q1
CO-1;   a.   [10]
BL-1,2
********** 3 **********

[Text in pictures on this page, read by OCR]
Convolution operation:
Z(i,j) = S> X(i+ m,j +n) -W(m,n)
Pooling reduces dimensions:
Al = max(Z") (Max Pooling)
Activation:
A=max(0,Z) (ReLU)

These operations extract hierarchical features from edges to complex patterns.

(3 Marks — Model Formulation & Loss Function)
For binary classification, the model computes:
z=w'r+b
1
l+e?

9 = o(2) =
The binary cross-entropy loss is:

J = —[ylog(g) + (1 — y) log(1 — 9)]

This loss measures the difference between predicted output y and actual label y.
--- page 4 ---
(3 Marks — Gradient Derivation)

Using chain rule:

dw dg dz dw
Step-by-step:

1. Loss derivative:

2. Sigmoid derivative:

oY 91 9)
3. Linear derivative:
Oz
au x
Combining all:
a7 — (g— we

(4 Marks - Interpretation & Learning Significance)
The gradient:

OJ .

ae 7 Go we
has the following significance:
¢ (%— y) represents the prediction error

© « determines the contribution of each feature

Weight update rule:
w= w-al(g—y)z

Impact on Learning:
e Large error — larger updates
© Small error > fine adjustments
e Ensures model moves toward minimizing loss

Thus, this gradient enables efficient learning through gradient descent and improves classification
performance.

FIC 7) IC HOH
--- page 5 ---
Cco- 1; b. (3 Marks - Definitions with Equations) [ 10]
Sigmoid:
BL-2 A
a(x) = he=
Tanh:
tanh(x) = eve
e+e *
ReLU:

f(x) = max(0, x)

(3 Marks - Gradient Behavior)
Sigmoid derivative:

a'(x) = o(x)(1 — o(2))
Tanh derivative:
1 — tanh?(x)
ReLU derivative:
f'(x) =1ifa > 0,0 otherwise

(4 Marks — Justification)
ReLU avoids vanishing gradients and is computationally efficient. Sigmoid is suitable for binary outputs,
while softmax:

Softmax(z;) =

is used for multi-class classification.

Q2

FIC DI EH ar
--- page 6 ---
CO-1;   a.   [10]
BL-3
CO-2;   b.   (3 Marks – Concept of Bias–Variance Tradeoff)   [10]
BL-3   In machine learning, prediction error can be decomposed as:
Bias: Error due to overly simple model assumptions
Variance: Error due to model sensitivity to data
High bias leads to underfitting, where the model fails to capture
underlying patterns.
(3 Marks – Analysis of Underfitting)
In predictive maintenance systems, high bias occurs when:
• Model is too simple (few layers/neurons)
•   Insufficient features or weak representations
• Excessive regularization
Effects:
• High training error
• Poor performance on both training and validation data
********** 6 **********

[Text in pictures on this page, read by OCR]
(3 Marks — Architecture)
Input > Hidden layers — Output

AQ=x
(3 Marks - Forward Propagation)

ZY weal tl 4 pl

All = 9(Z")
(4 Marks - Backpropagation)
Loss:
J==Sy-a
m ‘ .
Gradient:
Od
dW = —
ow
Update:

W=W—- adW
--- page 7 ---
Thus, the model is unable to learn meaningful relationships from sensor
data.
(4 Marks – Methods to Improve Performance)
To reduce bias and improve performance:
🔹 1. Increase Model Complexity
• Add more layers or neurons
• Use deeper architectures
🔹 2. Reduce Regularization
• Lower L2 penalty:
3. Improve Feature Representation
• Add more relevant features
• Use feature engineering or deep learning
4. Train Longer / Tune Hyperparameters
•   Increase epochs
• Adjust learning rate for better convergence
Conclusion
High bias leads to underfitting, which can be addressed by increasing
model capacity, reducing regularization, and improving feature
representation to achieve better learning and performance.
Q3
CO-2;   a.   Mini-batch Gradient Descent updates model parameters using small   [10]
BL-3   batches of data instead of the entire dataset. Momentum improves
gradient descent by adding a velocity term to accelerate convergence.
RMSProp adapts learning rates for each parameter using squared
gradients. Adam combines both Momentum and RMSProp for efficient
optimization.
********** 7 **********
--- page 8 ---
(3 Marks – Comparison)
Mini-batch GD balances efficiency and stability but may still oscillate.
Momentum accelerates convergence in relevant directions and reduces
oscillations. RMSProp adjusts learning rates dynamically, making it
effective for non-stationary problems. Adam combines both advantages,
providing faster convergence and better handling of sparse gradients.
(4 Marks – Justification)
Adam optimizer is generally the most suitable choice for large-scale
stock prediction models because it adapts learning rates for each
parameter and incorporates momentum, resulting in faster and more
stable convergence. Its update rule is:
This makes Adam highly efficient for complex and noisy datasets.
CO-3;   b.   3 Marks – Architectures Overview)   [10]
BL-3
********** 8 **********
--- page 9 ---
• VGGNet (by Visual Geometry Group):
Uses deep architecture (16–19 layers) with small
3×33\times33×3 filters for detailed feature extraction.
• ResNet (Residual Network):
Introduces skip connections to enable very deep networks (50+
layers) without degradation.
(3 Marks – Comparison Table)
Feature   VGGNet   ResNet
Depth   Deep (16–19 layers)   Very Deep (50+ layers)
Filters   Small (3×3) filters   Small filters + skip connections
Complexity High   Moderate (efficient design)
********** 9 **********

[Text in pictures on this page, read by OCR]
VGG - 16
Conv £axa filte), «=

\ae- 14
1, same MAX-POOL = 2x2, s=2_ J —

ZW TUM KG
° a ERO
—&
fae 112x112 x64 112x112 x128 ———> 56x56 x128
icons POOL [CONV.128) POOL
x2

2BAKB2A x3

Ny

cv
56x56 X256 ———> 38x28 x256 28x28 x512 ——® 14x14x512
(conca38) POOL {convi2) POOL

x3 x3
14x14 x512 7X7x512 FC FC Softmax
tcow(sia} POOL 4096 4096 1000
x3
Nartes & ad ASTM
ee

Simonyan & Zisserman 2015. Very deep convolutional networks for large-scale image recognition] Andrew Ng
--- page 10 ---
Gradient   Vanishing gradient   Solved using residual links
Issue
Use Case   Complex images   Large-scale applications
(4 Marks – Justification for Best Architecture)
ResNet is most suitable for large-scale deployment due to its ability
to train very deep networks efficiently.
Key equation:
• Enables direct gradient flow, preventing vanishing gradients
• Allows deeper feature extraction → better performance
• More scalable for large datasets like product catalogs
•   Efficient despite depth due to residual learning
Q4
CO-3;   a.   (3 Marks – Working with Equations)   [10]
BL-3
(4 Marks – Advantage)
LSTMs solve the vanishing gradient problem by maintaining a constant
error flow through the cell state. The gating mechanism allows the
network to retain relevant information over long sequences, making it
highly effective for tasks like machine translation and speech
recognition.
CO-3;   b.   (3 Marks – GAN Architecture & Concept)   [10]
********** 10 **********

[Text in pictures on this page, read by OCR]
Forget gate:
fe = o(Wy|he-1, x1] + bf)
Input gate:
i¢ = o(Wi[ht-1, 2t] + bi)
Candidate memory:
C; = tanh(W-[hi-1, x1] + be)
Cell state update:

Ce= fir + uC
--- page 11 ---
BL-3
A Generative Adversarial Network (GAN) consists of two neural
networks:
• Generator G(z)G(z)G(z): generates fake images from random
noise zzz
• Discriminator D(x)D(x)D(x): distinguishes between real and
generated images
The goal is to train GGG to produce realistic images that can fool DDD.
(3 Marks – Working & Interaction)
GAN training is based on a minimax game:
The generator tries to minimize this loss by generating realistic
samples
********** 11 **********
--- page 12 ---
• The discriminator tries to maximize it by correctly classifying
real vs fake
Interaction Process:
1. Generator produces fake image G(z)G(z)G(z)
2. Discriminator evaluates both real xxx and fake G(z)G(z)G(z)
3. Errors are backpropagated to update both networks
(4 Marks – Training Challenges & Analysis)
GAN training faces several challenges:
• Mode Collapse: Generator produces similar outputs repeatedly
• Training Instability: Generator and discriminator may not
converge
• Vanishing Gradients: If discriminator becomes too strong:
Balance Issue: One network overpowering the other leads to
poor learning
Solutions (brief):
• Use improved loss functions (Wasserstein GAN)
• Apply normalization techniques
•   Carefully tune learning rates
Q5
CO-2;   a.   (3 Marks – Concept)   [10]
BL-3   Mini-batch gradient descent divides the dataset into smaller batches and
updates weights after processing each batch instead of the entire dataset.
(3 Marks – Comparison)
Batch GD processes the entire dataset and is computationally expensive.
Stochastic GD updates weights for each sample and is noisy. Mini-batch
GD balances both by providing stable and efficient updates.
********** 12 **********
--- page 13 ---
(4 Marks – Advantages with Equation)
Mini-batch update:
It improves convergence speed, reduces memory usage, and enables
parallel computation on GPUs, making it ideal for large datasets.
CO-3;   b.   (2 Marks – Basic Architecture Description)   [5]
BL-2,3   LeNet (by Yann LeCun) is an early CNN with a simple architecture
consisting of a few convolution, pooling, and fully connected layers,
mainly used for digit recognition.
AlexNet (by Alex Krizhevsky and team at University of Toronto) is a
deeper CNN with 8 layers, designed for large-scale image
classification (ImageNet).
********** 13 **********
--- page 14 ---
(3 Marks – Comparison, Improvements & Impact)
• Design: LeNet is shallow and sequential, while AlexNet is
deeper and more complex
•   Activation: LeNet uses sigmoid/tanh; AlexNet uses ReLU
(faster training)
•   Regularization: AlexNet introduces dropout to reduce
overfitting
• Computation: AlexNet uses GPU training and handles large
datasets
Impact:
LeNet laid the foundation of CNNs, while AlexNet revolutionized
********** 14 **********

[Text in pictures on this page, read by OCR]
AlexNet

MAX-POOL MAX-POOL,
_ _ _ —
ux 11 3x3 5x5 3x3
s=4 s=2 same s=2
55x55 x96 x96 27x27 x96 x96 27x27 eet) 13x13 x256__
227x227 x3
227x227 x3
MAX-POOL had Xs
_—
axa 3x3 3x3 8 es 3 cae
1000
13x13 x384 13x13 x384 13x13 x256 6x6 256 9216 4096 4096
. - AU
- Svatlaeye a aba, hob tou, ‘age . ALOM Poretec
— &LY
— Moltide GPUS. 3


[Krizhevsky et al.. 2012. ImageNet classification with deep convolutional neural networks] <——— Andrew Ng

Year CNN Developed Place Top-5 error —_| No. of
by rate parameters

et al

2012 AlexNet(7) Alex ist 15.3% 60 million
Krizhevsky,
Geoffrey
Hinton, Ilya
Sutskever

2013 ZFNet() Matthew ist 14.8%
Zeiler and
Rob Fergus

2014 GoogLeNet(1 | Google ist 6.67% 4 million
9)

2014 VGG Net(16) | Simonyan, 2nd 7.3% 138 million
Zisserman

2015 ResNet(152) |Kaiming He | ist 3.6%
--- page 15 ---
deep learning by achieving breakthrough performance on ImageNet
and enabling modern deep architectures.
CO-2;   c.   (2 Marks – Idea)   [5]
BL-2   Backpropagation computes gradients of the loss function and
propagates error backward through the network.
(3 Marks – Process with Equation)
Gradient:
Weights updated as:
This iterative process minimizes the loss function.
Q6
CO-3;   a.   i.   [10]
import tensorflow as tf
BL-3
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
# Load dataset
(x_train, y_train), (x_test, y_test) =
tf.keras.datasets.fashion_mnist.load_data()
# Normalize
x_train = x_train / 255.0
x_test = x_test / 255.0
# One-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
# Model
model = Sequential([
Flatten(input_shape=(28,28)),
Dense(256, activation='relu'),
********** 15 **********
--- page 16 ---
Dense(128, activation='relu'),
Dense(64, activation='relu'),
Dense(10, activation='softmax')
])
# Compile
model.compile(optimizer='rmsprop',
loss='categorical_crossentropy',
metrics=['accuracy'])
# Train
history = model.fit(x_train, y_train,
validation_split=0.2,
epochs=15,
batch_size=128)
# Evaluate
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test Accuracy:", test_acc)
ii.
# Plot accuracy
plt.plot(history.history['accuracy'], label='train_acc')
plt.plot(history.history['val_accuracy'], label='val_acc')
plt.legend()
plt.title("Accuracy vs Epochs")
plt.show()
# Plot loss
plt.plot(history.history['loss'], label='train_loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.legend()
plt.title("Loss vs Epochs")
plt.show()
CO-3;   b.   from tensorflow.keras.layers import Dropout   [10]
BL-3,4
********** 16 **********
--- page 17 ---
from tensorflow.keras.regularizers import l2
model_reg = Sequential([
Flatten(input_shape=(28,28)),
Dense(256, activation='relu', kernel_regularizer=l2(0.001)),
Dropout(0.4),
Dense(128, activation='relu', kernel_regularizer=l2(0.001)),
Dropout(0.4),
Dense(64, activation='relu', kernel_regularizer=l2(0.001)),
Dropout(0.4),
Dense(10, activation='softmax')
])
model_reg.compile(optimizer='rmsprop',
loss='categorical_crossentropy',
metrics=['accuracy'])
history_reg = model_reg.fit(x_train, y_train,
validation_split=0.2,
epochs=15,
batch_size=128)
# Evaluate
test_loss_reg, test_acc_reg = model_reg.evaluate(x_test, y_test)
print("Regularized Model Accuracy:", test_acc_reg)
********** 17 **********
--- page 18 ---
FR ICR 7] QA HH
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper fb6152a14549

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/MBATech_DS_7052/Neural Networks and Deep Learning/ANS_Neural Networks and Deep Learning(702DB0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100
- Text: mixed (19 pages), mean OCR confidence 76.3

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026
Program/s: B Tech/MBA Tech   Year: IV Semester: VII
Stream/s: Data Science
Subject: Neural Networks and Deep Learning   Time: hrs (______to_______)
Date:   /   / 2025   No. of Pages: 06
Marks: 100
Final Examination
Instructions:
1. This question paper contains 1 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   Marks
a.   Explain concept in detail with diagram.
CO-2;
SO-2;   5
BL-2
1

[Text in pictures on this page, read by OCR]
Explanation / Steps:
1. Input Layer:
Input features 21, Z2, ... are applied to the network.
2. Weighted Sum:

Each neuron calculates a linear combination of inputs and weights and adds bias:
eS Ss wr; +b

The weighted sum is passed through an activation function such as sigmoid / ReLU / tanh:

a= f(z)

3. Activation Function:

4. Propagation:
Output of one layer becomes input to the next layer.
5. Output Layer:

Final layer produces the predicted output.
--- page 2 ---
b   Feedforward Neural Network Diagram (Information flows only in one direction)
Recurrent Neural Network (RNN) diagram (Feedback connection showing
dependence on previous time step)
5
Feedforward Neural   Recurrent Neural Network
Aspect
Network   (RNN)
Has feedback / recurrent
Data flow   One-way (input → output)
connections
Memory   No memory of past inputs Maintains state (memory)
Sequential / time-dependent
Input type   Fixed-size input
input
Time
CO-2,5;   Not considered   Explicitly considered
dependency
SO-2;
BL-2   Applications   Classification, regression NLP, speech, time-series
c   Diagram: Bias–Variance Tradeoff
CO-3;   (Any equivalent conceptual diagram acceptable)   5
SO-2;
Meaning of Bias and Variance
BL-1
2

[Text in pictures on this page, read by OCR]
Small Numerical Example (any suitable example acceptable)
e Inputs: 2] = 1,22 = 2
¢ Weights: w; = 0.5, wo = 1.0
¢ Bias: b = 0.5

z=(1x0.5)+ (2x 1.0)+05=3

Using sigmoid:

1

a= 3 + 0.95

Mathematical Representation (any equivalent form acceptable)

Feedforward Neural Network:
z=Wr+b, y = f(z)
Recurrent Neural Network:

hi = f(Wa,+Uh1+6), y% = 9(hi)
--- page 3 ---
•   Bias:
Bias refers to the error due to oversimplified assumptions made by the
model.
High bias models fail to capture the underlying pattern of data.
•   Variance:
Variance refers to the error due to model sensitivity to training data.
High variance models fit training data very closely but perform poorly on
new data.
Explain with diagram in detail.
s
Relationship with Underfitting and Overfitting
•   Underfitting:
Occurs when the model is too simple
→ High bias, low variance
•   Overfitting:
Occurs when the model is too complex
→ Low bias, high variance
d   Concept
•   Vanishing-Gradient:
A problem where gradients become very small during backpropagation,
causing very slow or no learning in early layers.
•   Exploding-Gradient:
A problem where gradients grow very large, leading to unstable updates and
divergence during training.
5
Why They Occur (Explain with gradient formula)
•   During backpropagation, gradients are computed using the chain rule.
•   In deep networks, this involves multiplication of many derivatives.
•   If derivatives are:
Less than 1 → gradients shrink → vanishing gradient
Greater than 1 → gradients grow → exploding gradient
CO-3;   • Common causes:
SO-2;
Deep network depth
BL-2
3
--- page 4 ---
Poor weight initialization
Use of activation functions like sigmoid/tanh
Repeated matrix multiplications
a.   Introduction
GoogleNet (Inception-v1) is a deep convolutional neural network introduced by
Google that won ILSVRC-2014.
Its key idea is the Inception module, which enables the network to learn multi-scale
features efficiently while keeping the number of parameters low.
Below or any equivalent valid architecture is acceptable
10
Architectural Features of GoogleNet (Explain in detail)
(5+5)
1. Depth:
~22 layers deep (excluding pooling layers)
2. Inception Modules:
Multiple stacked inception blocks extract features at different scales.
3. Auxiliary Classifiers:
Two additional classifiers connected to intermediate layers
Help reduce vanishing gradient problem
Used only during training
4. Global Average Pooling:
Replaces fully connected layers
Reduces overfitting
Reduces number of parameters
Q2
CO-5;   Advantages of GoogleNet
SO2;
•   Efficient computation with fewer parameters
BL-2
4
--- page 5 ---
•   Better feature extraction using multi-scale filters
•   Improved training of deep networks
• Reduced overfitting
b. Backpropagation is a supervised learning algorithm used to train neural
networks by minimizing the loss function.
It works by:
• Computing the error at the output,
•   Propagating this error backward through the network,
•   Updating weights using gradient descent (SGD).
Neural Network Diagram
(Any equivalent neat, labeled diagram acceptable)
Steps of Backpropagation Algorithm (Explain in detail)
1. Forward Propagation
2. Loss Calculation
10 (4
3. Backward Propagation (Gradient Computation)
theory
4. Weight Update using SGD
+ 6
examp
le)
Q3
CO-2;
SO-2;
BL-5
5

[Text in pictures on this page, read by OCR]
Step 1: Forward Propagation

Hidden layer computation:
Zn = (a1w1 + wo) + by

zp = (1x 0.1+2 x 0.2) +0.1 = 0.6

1
h = 0(0.6) = Tpe08 = 0.645

Output layer computation:
Zo = (h x ws) + be
2 = (0.645 x 0.3) + 0.1 = 0.2935
y = (0.2935) ~ 0.572
--- page 6 ---
Q3   a.
GRU Cell Architecture – Diagram   10 (6
CO-5;
SO-2;   (Any equivalent neat, labeled diagram acceptable)   theory
BL-6
6

[Text in pictures on this page, read by OCR]
Step 4: Weight Update using SGD
Update output weight w3:
wy” = w3 — (50 - h)
w3°” = 0.3 — 0.1(—0.105 x 0.645)

w3°" & 0.307

Update hidden weights:

new

wr” = wi — (dn: £1)

wi” = 0.1 —0.1(—0.0072 x 1) = 0.1007

new

wy” = w. — (dn + £2)

wy” = 0.2 — 0.1(—0.0072 x 2) = 0.2014
--- page 7 ---
+ 4
code)
Key Characteristics of GRU
• No separate cell state (unlike LSTM)
• Fewer gates → faster training
•   Efficient for time series and sequence modeling
•   Handles long-term dependencies better than vanilla RNN
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
# Define GRU model
model = Sequential([
GRU(32, input_shape=(10, 1), return_sequences=False),
Dense(1)
])
# Compile model
model.compile(optimizer='adam', loss='mse')
# Dummy time-series data
X_train = tf.random.normal((100, 10, 1))
7

[Text in pictures on this page, read by OCR]
Components of GRU
1. Update Gate (z,):

Controls how much past information should be carried forward.

2 = 0(W.a, + ULy_-1)
2. Reset Gate (r,):

Controls how much past information should be forgotten.

r, = o(W,a, + U,ht-1)
3. Candidate Hidden State (h,):

hy = tanh(Wa;, + U(r © hy-1))
4. Final Hidden State:

ky = (1— 21) Ohi t2@h

(Any equivalent mathematical representation acceptable)
--- page 8 ---
y_train = tf.random.normal((100, 1))
# Train model
model.fit(X_train, y_train, epochs=10, batch_size=16)
b.   Definition of Overfitting
Overfitting occurs when a deep learning model learns the training data too well,
including noise and minor fluctuations, and therefore performs poorly on unseen
(test) data.
•   Training error → very low
•   Validation/Test error → high
Diagram: Overfitting Concept
(Any equivalent neat, labeled diagram acceptable)
Diagram: Underfitting vs Good Fit vs Overfitting
(Any equivalent diagram acceptable)
Explain below points in more detail:-
10
(5+5)
Dropout
Dropout randomly deactivates neurons during training.
•   Prevents dependency on specific neurons
•   Acts as model averaging
Dropout Diagram
(Any equivalent diagram acceptable)
Data Augmentation
Q3   Data augmentation artificially increases training data by applying transformations.
CO-3;
•   Rotation
SO-2;
BL-1,6   •   Flipping
8

[Text in pictures on this page, read by OCR]
1. Regularization

Regularization adds a penalty term to the loss function to discourage complex models.

¢ L1 Regularization: Encourages sparsity

¢ L2 Regularization: Penalizes large weights
Inew =L+% Ss w

Effect:

¢ Reduces model complexity

¢ Prevents very large weights
--- page 9 ---
•   Scaling
•   Noise addition
a. A Convolutional Neural Network (CNN) is a deep learning architecture mainly used
for image and spatial data processing.
It automatically learns hierarchical features from raw input data.
. Pooling Layer
Explanation
•   Reduces spatial dimensions of feature maps.
• Common types: Max pooling, Average pooling
• Makes features translation invariant.
Diagram
(Any equivalent diagram acceptable)
Role in Feature Extraction
•   Reduces computation
•   Retains most important features
•   Controls overfitting
3. Activation Function
Explanation
•   Introduces non-linearity into the network.
• Common activations: ReLU, Sigmoid, Tanh
ReLU Function   10
𝑓(𝑥) = max⁡(0, 𝑥)
(3+3+
Diagram   4)
(Any equivalent plot acceptable)
1. Convolution Layer
Explanation
•   Applies learnable filters (kernels) to the input image.
•   Each filter slides over the input to generate a feature map.
•   Captures local patterns such as edges, textures, and shapes.
Equation (conceptual)
𝐹𝑒𝑎𝑡𝑢𝑟𝑒 𝑀   𝑎𝑝
= 𝐼𝑛𝑝𝑢𝑡∗𝐾𝑒𝑟𝑛𝑒𝑙+ 𝐵𝑖𝑎𝑠
Diagram
(Any equivalent neat, labeled diagram acceptable)
Fully Connected (FC) Layer
Explanation
Q4   • Neurons are fully connected to previous layer.
CO-5;   • Combines extracted features for final decision.
SO-2;
Diagram
BL-2
(Any equivalent diagram acceptable)
9
--- page 10 ---
Component   Role
Convolution Layer   Extract spatial features using filters.
Pooling Layer   Reduce size, retain important info (max/avg pooling).
Activation (ReLU)   Nonlinearity, removes negatives.
Fully Connected Layer Combine extracted features for output.
Softmax   Converts logits to probabilities.
b.   Introduction
In RNN-based sequence-to-sequence (Seq2Seq) models, the attention mechanism
allows the decoder to focus on relevant parts of the input sequence while
generating each output token, instead of relying on a single fixed context vector.
Limitation of Basic Seq2Seq Model (Without Attention)
•   Encoder compresses entire input sequence into one context vector
• Long sentences → information loss
•   Poor performance for long-range dependencies
Diagram: Seq2Seq without Attention
(Any equivalent diagram acceptable)
10 (6
How Attention Improves Machine Translation Performance
theory
1. Dynamic Context Selection
+ 4
•   Focuses on relevant source words for each target word
explai
•   Handles long sentences effectively
n)
2. Better Word Alignment
•   Learns soft alignment between source and target words
•   Improves translation accuracy
3. Reduced Information Bottleneck
• No single fixed context vector
•   Encoder states are directly accessible
4. Improved Handling of Long-Range Dependencies
•   Maintains performance even for long sequences
5. Improved Translation Quality
Q4   •   Higher BLEU scores
CO-5;
• More fluent and accurate translations
SO-2;
BL-5
10
--- page 11 ---
a.   •   1. Input Layer
•   Definition:
The input layer receives the raw features of the data and passes them to the
network.
• No computation is performed
• Number of neurons = number of input features
•   2. Hidden Layer
•   Definition:
Hidden layers perform feature transformation using weights, bias, and
activation functions.
•   Learns intermediate representations
• One or more hidden layers may be used
•   3. Output Layer
•   Definition:
10 (6
The output layer produces the final prediction of the network.
theory
•   For binary classification → single neuron
+ 4
•   Typically uses sigmoid activation
code)
•
•   4. Activation Function
•   Definition:
An activation function introduces non-linearity so the network can learn
complex patterns.
• Common functions:
• ReLU
•   Sigmoid
• Tanh
• Example (Sigmoid):
1
Q5   𝑓(𝑥) = 1 + 𝑒−𝑥
CO-3;
Neural Network Architecture Diagram
SO-2;
BL-1,6   (Any equivalent neat, labeled diagram acceptable)
11
--- page 12 ---
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# Define the model
model = Sequential([
Dense(8, activation='relu', input_shape=(4,)), # Hidden layer
Dense(1, activation='sigmoid')   # Output layer
])
# Compile the model
model.compile(optimizer='adam',
loss='binary_crossentropy',
metrics=['accuracy'])
# Dummy training data
X_train = tf.random.normal((100, 4))
y_train = tf.random.uniform((100, 1), minval=0, maxval=2, dtype=tf.int32)
# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=16)
b.   Introduction
10 (5
A Generative Adversarial Network (GAN) consists of two neural networks:
• Generator (G): Generates fake data   theory
•   Discriminator (D): Distinguishes real data from fake data
+ 5
They are trained in a min–max game.
Basic GAN Architecture – Diagram   equati
Q5
(Any equivalent neat, labeled diagram acceptable)
CO-5;   ons /
Key Training Challenges in GANs
SO-2;
code)
BL-2
1. Mode Collapse
12
--- page 13 ---
Definition:
Mode collapse occurs when the generator produces very limited or identical
outputs, ignoring diversity in the data.
•   Generator learns to fool discriminator with few samples
•   Diversity in generated data is lost
2. Unstable Convergence
Definition:
GAN training may:
•   Oscillate without convergence
•   Diverge due to imbalance between G and D
Reasons:
•   Vanishing gradients
•   Discriminator becoming too strong
• Min–max optimization difficulty
Methods to Overcome GAN Training Issues
1. Wasserstein GAN (WGAN)
Key-Idea:
Replaces Jensen–Shannon divergence with Wasserstein (Earth Mover’s)
distance, providing smoother gradients.
Advantages of WGAN
•   Stable training
• Reduced mode collapse
•   Meaningful loss curves
•   Improved convergence
2. Feature Matching
Key-Idea:
Instead of directly fooling the discriminator, the generator tries to match feature
statistics of real data.
code
import tensorflow as tf
from tensorflow.keras import layers
# Generator
generator = tf.keras.Sequential([
layers.Dense(16, activation='relu', input_shape=(10,)),
layers.Dense(1)
])
# Discriminator
discriminator = tf.keras.Sequential([
layers.Dense(16, activation='relu', input_shape=(1,)),
layers.Dense(1, activation='sigmoid')
13
--- page 14 ---
])
# Compile discriminator
discriminator.compile(optimizer='adam',
loss='binary_crossentropy')
# GAN model
discriminator.trainable = False
gan = tf.keras.Sequential([generator, discriminator])
gan.compile(optimizer='adam', loss='binary_crossentropy')
a.
10 (6
code +
4
explan
ation)
Role of Each Layer in detail explanation
Layer   Function   Contribution
Convolution Feature extraction Detects edges, shapes
Pooling   Downsampling   Reduces computation
FC   Decision making Combines features
Softmax   Classification   Produces probabilities
import tensorflow as tf
Q6   from tensorflow.keras import layers, models
CO-5;
SO-2;
BL-6   # Load MNIST dataset
14

[Text in pictures on this page, read by OCR]
Input Image (28x28)
+
Convolution + ReLU
+
Max Pooling
+
Convolution + ReLU
+
Max Pooling
+
Flatten
+
Fully Connected
+
Softmax Output (0-9)
--- page 15 ---
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# Normalize and reshape data
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0
# Define CNN model
model = models.Sequential([
layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
layers.MaxPooling2D((2,2)),
layers.Conv2D(64, (3,3), activation='relu'),
layers.MaxPooling2D((2,2)),
layers.Flatten(),
layers.Dense(128, activation='relu'),
layers.Dense(10, activation='softmax')
])
# Compile model
model.compile(optimizer='adam',
loss='sparse_categorical_crossentropy',
metrics=['accuracy'])
# Train model
model.fit(x_train, y_train, epochs=5, batch_size=64)
b.   ntroduction
Batch Normalization and Dropout are widely used techniques to improve
10 (6
generalization and training stability in deep neural networks by reducing overfitting
code +
and internal covariate shift.
4
1. Batch Normalization
theory
Q6   Concept
CO-3;   )
Batch Normalization normalizes the output of a layer using mini-batch statistics,
SO-2;
BL-6   ensuring stable and faster training.
15
--- page 16 ---
Equation
Diagram: Batch Normalization
(Any equivalent neat diagram acceptable)
Linear Output ──► Normalize ──► Scale & Shift ──► Activation
How Batch Normalization Improves Generalization
•   Reduces internal covariate shift
•   Allows higher learning rates
•   Acts as a regularizer
•   Speeds up convergence
2. Dropout
Concept
Dropout randomly deactivates neurons during training with a fixed probability 𝑝,
preventing reliance on specific neurons.
How Dropout Improves Generalization
•   Prevents co-adaptation of neurons
•   Acts like ensemble learning
•   Reduces overfitting
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout
model = Sequential([
Dense(128, input_shape=(20,)),
BatchNormalization(),
16
--- page 17 ---
tf.keras.layers.Activation('relu'),
Dropout(0.5),
Dense(64),
BatchNormalization(),
tf.keras.layers.Activation('relu'),
Dropout(0.3),
Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam',
loss='binary_crossentropy',
metrics=['accuracy'])
# Dummy training data
X_train = tf.random.normal((100, 20))
y_train = tf.random.uniform((100, 1), minval=0, maxval=2, dtype=tf.int32)
model.fit(X_train, y_train, epochs=10, batch_size=16)
a.   Aspect   Transfer Learning Multi-Task Learning
Training style   Sequential   Simultaneous
Number of tasks   One target task   Multiple tasks
Data usage   Source → target   Shared across tasks
Knowledge sharing Pretrained weights Shared representations
Typical use   Small datasets   Related tasks
10
How They Reduce Training Time and Improve Accuracy
(5+5)
Reduce Training Time
•   Transfer-Learning:
Starts from pretrained weights → fewer epochs
Q7
CO-4;   • MTL:
SO-2;   Shared training reduces redundancy
BL-2   Improve Accuracy
17
--- page 18 ---
•   Transfer-Learning:
Uses rich pretrained features
• MTL:
Learns robust features via task diversity
Diagram: Knowledge Sharing Comparison
(Any conceptual diagram acceptable)
b. What is Gradient Descent?
Gradient Descent is an optimization algorithm used to minimize a loss function by
iteratively updating model parameters in the opposite direction of the gradient.
Basic Update Rule
Diagram: Gradient Descent Intuition
(Any equivalent conceptual diagram acceptable)
10 (6
theory
+ 4
equati
ons)
Q7
CO-3;
SO-2;
BL-2
18

[Text in pictures on this page, read by OCR]
1. Batch Gradient Descent
Definition:
Uses the entire training dataset to compute gradients.

0 = 0 — nVL (full dataset)

Characteristics:
* Stable convergence
* Computationally expensive

© Slow for large datasets

2. Stochastic Gradient Descent (SGD)
Definition:
Updates parameters using one training sample at a time.

0=0-—nVL(z;)

Characteristics:
e Faster updates
e Noisy convergence

© Can escape local minima
--- page 19 ---
3. Mini-batch Gradient Descent

Definition:

Uses a small batch of samples (e.g., 32, 64).
0 = 6 — nVL(mini-batch)

Characteristics:

e Balance between batch and SGD
¢ Efficient and stable

*¢ Most commonly used

Adam Update Equations
1. Gradient
n = VL(H)
2. First moment (mean)
m, = Bym-1 + (1 — Bi) ge
3. Second moment (variance)
ve = Bovr-1 + (1 — Bo) g?

4. Bias correction

m™m * Ut
= %=
1-p’? * 1-65

™m

5. Parameter update

19
````
