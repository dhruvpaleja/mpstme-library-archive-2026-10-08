# Advanced Artificial Intelligence and Deep Learning: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 058b458b4bd5

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Advanced Artificial Intelligence & Deep Learning/ANS_Advanced Artificial Intelligence & Deep Learning(703DB0C060)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Advanced Artificial Intelligence & Deep Learning
Date: 11 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   Marks
a.   • Forward propagation computes output layer by layer using:
𝑍= 𝑊𝑋+ 𝑏, 𝐴= 𝑓(𝑍)
CO-1;
SO-2;   where 𝑓is activation function. (2 marks)   [5]
BL-2   •   Activation functions (ReLU, sigmoid, tanh) introduce non-linearity,
allowing complex pattern learning and influencing output distribution
at each layer. (3 marks)
b LSTM is a type of RNN with memory cells and gates to control information [5]
CO-2;   flow. (2 marks)
SO-2;
It addresses vanishing gradient problem, enabling learning of long-term
BL-1
dependencies in sequential data. (3 marks)
c   Data augmentation applies transformations like rotation, flipping, scaling to [5]
CO-4;   increase dataset size. (2 marks)
SO-2;
Improves model performance by reducing overfitting and enhancing
BL-2
generalization. (3 marks)
d   Training error is error on training data; testing error is error on unseen data. (2 [5]
CO-3;   marks)
SO-2;
Large gap indicates overfitting; both high indicates underfitting, helping
BL-2
evaluate model performance. (3 marks)
a.   • ResNet uses residual blocks with identity mapping:
Q2   [10]
𝑦= 𝐹(𝑥) + 𝑥
********** 1 **********
--- page 2 ---
CO-2;
SO-2;
where 𝐹(𝑥)is residual mapping. (5 marks)
BL-2
• Skip connections allow gradient flow, reduce vanishing gradient, and
enable training of very deep networks. (5 marks)
b.   • Forward computes output; backprop computes gradients using loss   [10]
function. (5 marks)
Code (TensorFlow):
import tensorflow as tf
model = tf.keras.Sequential([
tf.keras.layers.Dense(8, activation='relu', input_shape=(4,)),
tf.keras.layers.Dense(1)
])
Q2
loss_fn = tf.keras.losses.MeanSquaredError()
CO-1;   optimizer = tf.keras.optimizers.SGD()
SO-2;
BL-5   x = tf.random.normal((1,4))
y = tf.random.normal((1,1))
with tf.GradientTape() as tape:
pred = model(x)
loss = loss_fn(y, pred)
grads = tape.gradient(loss, model.trainable_variables)
optimizer.apply_gradients(zip(grads, model.trainable_variables))
Loss computes error; gradients update weights to minimize loss. (5 marks)
a.   Processes sequence in forward and backward directions using two LSTMs. (5 [10]
Q3
marks)
CO-2;
SO-2;   Combines past and future context, improving accuracy in sequence tasks like
BL-2   NLP. (5 marks)
b. Enhances dataset using transformations. (5 marks)   [10]
Code (Keras):
from tensorflow.keras.preprocessing.image import ImageDataGenerator
Q3
datagen = ImageDataGenerator(
CO-4;
rotation_range=20,
SO-2;
horizontal_flip=True,
BL-5
zoom_range=0.2
)
train = datagen.flow_from_directory('data/', target_size=(224,224))
• Improves robustness and reduces overfitting. (5 marks)
********** 2 **********
--- page 3 ---
a.   Feature maps are outputs of convolution:   [10]
𝐹𝑒𝑎𝑡𝑢𝑟𝑒= 𝐼𝑛𝑝𝑢𝑡∗𝐹𝑖𝑙𝑡𝑒𝑟
Q4
CO-2;
SO-2;   represent learned patterns. (5 marks)
BL-4
• They capture edges, textures, and higher-level features; deeper layers
learn more abstract representations. (5 marks)
b.   •   In a standard RNN, the hidden state is updated using input and previous [10]
state:
ℎ𝑡= 𝑓(𝑊𝑥𝑥𝑡+ 𝑊ℎℎ𝑡−1 + 𝑏ℎ)
𝑦𝑡= 𝑔(𝑊𝑦ℎ𝑡+ 𝑏𝑦)
Q4
CO-2;
SO-2;   where 𝑊𝑥, 𝑊ℎ, 𝑊𝑦are weight matrices and 𝑓is activation (tanh/ReLU). (5
BL-1
marks)
• Weight matrices control contribution of current input and past
memory, while activation functions introduce non-linearity, enabling
the network to learn temporal patterns. (5 marks)
a.   • L1 regularization adds absolute weight penalty:   [10]
𝐿= 𝐿0 + 𝜆∑∣𝑤∣
which encourages sparse weights (feature selection). (5 marks)
• Code (TensorFlow):
Q5   import tensorflow as tf
CO-3;   from tensorflow.keras import layers, regularizers
SO-2;
BL-6
model = tf.keras.Sequential([
layers.Dense(64, activation='relu',
kernel_regularizer=regularizers.l1(0.01)),
layers.Dense(1)
])
Q5   b.   [10]
• Batch Normalization normalizes the input of each layer using mini-
CO-4;
SO-2;   batch statistics:
BL-2   𝑚   𝑚
1   1
∑   ∑
********** 3 **********
--- page 4 ---
𝑦𝑖= 𝛾𝑥̂𝑖+ 𝛽
where 𝛾, 𝛽are learnable parameters. (5 marks)
•   It reduces internal covariate shift by stabilizing input distributions
across layers, allowing higher learning rates, faster convergence, and
improved training stability in deep networks. (5 marks)
a.   • A Convolutional Neural Network (CNN) for multi-class classification [10]
consists of convolution, pooling, and dense layers for feature
extraction and classification. (5 marks)
• Code (TensorFlow/Keras):
import tensorflow as tf
model = tf.keras.Sequential([
tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)),
Q6   tf.keras.layers.MaxPooling2D(2,2),
CO-3;   tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
SO-2;
BL-6   tf.keras.layers.MaxPooling2D(2,2),
tf.keras.layers.Flatten(),
tf.keras.layers.Dense(64, activation='relu'),
tf.keras.layers.Dense(10, activation='softmax')
])
• Convolution layers extract features, pooling reduces spatial
dimensions, flatten converts to vector, and dense layers perform
multi-class classification. (5 marks)
b.   • NAG computes gradients at a look-ahead position to improve [10]
optimization:
𝑣𝑡= 𝛽𝑣𝑡−1 + 𝜂∇𝐿(𝜃𝑡−1 −𝛽𝑣𝑡−1)
Q6   𝜃𝑡= 𝜃𝑡−1 −𝑣𝑡
CO-4;
SO-2;
BL-6   where 𝑣𝑡is velocity, 𝛽momentum term, and 𝜂learning rate. (5 marks)
• The look-ahead mechanism anticipates future parameter position,
reducing oscillations and enabling faster and more stable convergence
compared to standard momentum-based SGD. (5 marks)
Q7   a. Bias is the error due to overly simple assumptions in the model, while variance [10]
CO-3;   is the error due to high sensitivity to training data. High bias leads to
SO-2;
BL-2   underfitting, and high variance leads to overfitting. (5 marks)
********** 4 **********
--- page 5 ---
The trade-off involves selecting a model with optimal complexity: increasing
complexity reduces bias but increases variance. A balanced model minimizes
total error and improves generalization on unseen data. (5 marks)
b.   • RMSProp adapts the learning rate by maintaining an exponentially [10]
weighted average of squared gradients:
𝑣𝑡= 𝛽𝑣𝑡−1 + (1 −𝛽)𝑔𝑡 2
𝜂
Q7   𝜃𝑡= 𝜃𝑡−1 −    𝑔𝑡
√𝑣𝑡+ 𝜖
CO1-;
SO-2;
BL-2   where 𝑔𝑡is gradient, 𝛽decay factor. (5 marks)
•   It normalizes gradient updates, prevents large oscillations, and
provides faster and more stable convergence compared to standard
SGD, especially for non-stationary objectives. (5 marks)
********** 5 **********
````

## 2024-25 · Final-Exam · Sem 2 · Answer key · paper 9143845e02d9

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Advanced Artificial Intelligence & Deep Learning/ANS_Advanced Artificial Intelligence & Deep Learning(703DB0C060)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2025
- Text: mixed (9 pages), mean OCR confidence 83.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Advanced Artificial Intelligence & Deep Learning
Date: 07 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   Marks
a.   Role of Activation Functions:
•   Introduce non-linearity to neural networks.
•   Help in learning complex patterns and decision boundaries.
•   Ensure effective backpropagation by controlling gradient flow.
Types of Activation Functions:
[5]
b   [5]
********** 1 **********

[Text in pictures on this page, read by OCR]
1. Mathematical Formulation of Bidirectional RNN (Bi-RNN):

© Forward hidden state:

hi = fWilar + UfhL, +0)
¢ Backward hidden state:

hi = f (Whar + Upht., +b)

© Final output:
4 = 9 V [hf he] + by)

2. Difference from Standard RNN:
¢ Standard RNN processes input only in one direction (past > future).

© Bi-RNN processes input in both directions (past — future and future — past), capturing richer

contextual information.
--- page 2 ---
Cc

1. Batch Normalization (BN):
¢ A technique that normalizes activations within a mini-batch to stabilize training.

¢ Formula:
T— HB

- Jon +e

y= ye+8

where zp and o% are batch mean and variance, and ¥, 8 are learnable parameters.
2. How It Improves Training:
¢ Reduces internal covariate shift, leading to faster convergence.
¢ Allows higher learning rates without instability.
© Acts as a regularizer, reducing the need for dropout.

¢ Improves gradient flow, preventing vanishing/exploding gradients.

[5]

d

1. Training Error:
© The error measured on the training dataset.
¢ Low training error indicates that the model has learned patterns from the training data.
© If too low, the model may be overfitting (memorizing data instead of generalizing).
2. Generalization Error:
¢ The error measured on unseen test/validation data.
© Indicates how well the model performs on new data.

¢ High generalization error suggests overfitting, while very high training and generalization

errors indicate underfitting.

[5]

Q2

a.

1. GoogleNet Architecture:

© Introduced Inception modules, which apply multiple convolutional filters (1x1, 3x3, 5x5) in

parallel.
¢ Used 1x1 convolutions for dimensionality reduction.

© Total layers: 22 deep, but optimized for efficiency.

2. ResNet Architecture:
© Introduced Residual Blocks with skip (shortcut) connections to allow gradient flow.
© Total layers: 50, 101, or even 152 deep.

e Formula for residual block:
A(x) = f(z) +

where f(z) is a transformation applied to input x.

3. Key Differences:

Feature GoogleNet ResNet
Depth 22 layers 50+ layers

Innovation Inception module Residual connections

Computation Optimized using 1%1 convolutions Easier to train deep models

Gradient Flow _Risk of vanishing gradients Skip connections prevent gradient vanishing

4. Impact of Residual Connections:
¢ Prevents vanishing gradients in deep networks.
© Allows deeper architectures without performance degradation.

© Improves convergence speed during training.

[10]

FIC 2 I HH ar
--- page 3 ---
b.   [10]
import tensorflow as tf
from tensorflow.keras.layers import Dense, Input
# Define input layer
inputs = Input(shape=(10,))
# Define hidden layers
x = Dense(32, activation='relu')(inputs)
Q2   x = Dense(16, activation='relu')(x)
# Define output layer
outputs = Dense(1, activation='sigmoid')(x)
# Create model
model = tf.keras.Model(inputs=inputs, outputs=outputs)
# Compile the model
model.compile(optimizer='adam',   loss='binary_crossentropy',
metrics=['accuracy'])
# Example input data
import numpy as np
X = np.random.rand(5, 10) # 5 samples, 10 features
# Perform forward propagation (prediction)
predictions = model.predict(X)
print(predictions)
a.   [10]
Q3
********** 3 **********

[Text in pictures on this page, read by OCR]
1. Forward Propagation in a Neural Network:

© Forward propagation is the process where input data passes through the network, layer by layer, to

generate an output.

* Each layer performs a linear transformation followed by an activation function:
Z4 = wall + ol
All = ¢(Z")

LSTM (Long Short-Term Memory) Solution:
¢ Introduces cell state C; that maintains long-term memory.

¢ Uses gates to control information flow:

e Forget Gate: Decides what information to discard.

fe = o(Wy[hta, a] + by)
e Input Gate: Decides what new information to store.

i, = o(W;|hi_1, 24] + 0;)

C, = tanh(Wo[hi-1, vi] + bc)
© Cell State Update:
Cr= fi Crit G

¢ Output Gate: Computes the new hidden state.

04 = o(Wa|he-1, xt] + bo)

hi = 0, - tanh(C;)
--- page 4 ---
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
# Define LSTM model
model = Sequential([
LSTM(64, return_sequences=True, input_shape=(10, 1)), # LSTM layer
LSTM(32), # Second LSTM layer
Dense(1) # Output layer for regression task
])
# Compile the model
model.compile(optimizer='adam', loss='mse')
# Generate sample time-series data
import numpy as np
X = np.random.rand(100, 10, 1) # 100 samples, 10 time steps, 1 feature
y = np.random.rand(100, 1) # Regression target values
# Train the model
model.fit(X, y, epochs=10, batch_size=16)
# Predict on new data
predictions = model.predict(X[:5])
print(predictions)
b.   [10]
Q3
from tensorflow.keras.preprocessing.image import ImageDataGenerator
datagen = ImageDataGenerator(rotation_range=30, width_shift_range=0.2,
height_shift_range=0.2, horizontal_flip=True)
********** 4 **********

[Text in pictures on this page, read by OCR]
1. Data Augmentation:

¢ A technique to artificially expand the training dataset by applying transformations like rotation,

flipping, scaling, cropping, and color jittering to existing images.
2. How It Improves CNN Performance:
¢ Reduces overfitting by introducing variability.
© Improves generalization to unseen data.
¢ Enhances robustness to distortions and transformations in real-world scenarios.

3. Example (TensorFlow):
--- page 5 ---
a. 1. Role of Convolutional Layers: [10]
¢ Extract spatial features from input images using learnable filters.
© Detects edges, textures, and complex patterns through hierarchical feature extraction.
e Uses the operation:
Z=W*X+b
where W is the filter, X is the input, and b is bias.
2. Role of Pooling Layers:
Q4 * Reduces spatial dimensions while retaining key features.
© Types:
¢ Max Pooling: Takes the maximum value in a region (enhances dominant features).
© Average Pooling: Takes the average value (preserves overall structure).
3. Contribution to Feature Extraction & Computational Efficiency:
Layer Type Feature Extraction Computational Complexity
Convolutional Detects patterns (edges, textures) High (depends on filter size)
Layer
Pooling Layer Retains essential features while Lowers computation by reducing feature map
reducing size dimensions
b. | Architecture....2M [10]

Q4

2. Forward Propagation Equations:
Forward propagation in an RNN at time step t is computed as:

1. Hidden State Calculation:
hi = f(Wrae + Unhi-1 + bp)
where:
e h; = Hidden state at time step t
© 2+ = Input at time step t
e hy_1 = Hidden state at previous time step
© Wh = Weight matrix for input to hidden state connection
e Uy), = Weight matrix for hidden state to hidden state connection
e bp = Bias term

e f = Activation function (commonly tanh or ReLU)

FIC DI EH ar
--- page 6 ---
a.   [10]
import tensorflow as tf
from tensorflow.keras.models import Sequential
Q5
from tensorflow.keras.layers import Dense
# Define model with L2 regularization
model = Sequential([
Dense(64,   activation='relu',
kernel_regularizer=tf.keras.regularizers.l2(0.01), input_shape=(10,)),
Dense(32,   activation='relu',
kernel_regularizer=tf.keras.regularizers.l2(0.01)),
Dense(1, activation='sigmoid')
])
# Compile model
********** 6 **********

[Text in pictures on this page, read by OCR]
2. Output Calculation:

ye = 9(Vh, + by)

where:
© Yt = Output at time step t
e V = Weight matrix for hidden state to output connection
e by = Bias term

e g = Activation function for output (e.g., softmax or sigmoid)

Example:

© Ifinput x, = 2, hy1 = 0.5, weights W;, = 0.8, Un = 0.6, bias b, = 0.1:
h, = tanh(0.8(2) + 0.6(0.5) + 0.1) = tanh(1.6 + 0.3 + 0.1) = tanh(2) ~ 0.964
¢ Ifoutput weight V = 1.2, bias b, = 0.2:

uy = sigmoid(1.2(0.964) + 0.2) = sigmoid(1.3568) ~ 0.795

1. Concept of Regularization:
¢ Regularization prevents overfitting by adding a penalty to large weights.
¢ Common types:
¢ L1 Regularization (Lasso): Encourages sparsity.

¢ L2 Regularization (Ridge): Penalizes large weights, preventing over-complexity.

2. L2 Regularization Formula:
Lrotat = Lioss + 4) w?

where A controls the regularization strength.
--- page 7 ---
model.compile(optimizer='adam',   loss='binary_crossentropy',
metrics=['accuracy'])
b.   [10]
Q5
a.   [10]
Q6
b.   import tensorflow as tf   [10]
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
Q6
# Define LSTM model with gradient clipping
model = Sequential([
LSTM(64, return_sequences=True, input_shape=(10, 1)),
LSTM(32),
********** 7 **********

[Text in pictures on this page, read by OCR]
1. Structure of GRU (Gated Recurrent Unit):
* GRU is a variant of RNN that reduces vanishing gradients and improves long-term dependencies.
¢ Uses two gates instead of three (as in LSTM):
¢ Reset Gate (7;) — Controls how much past information to forget.
Update Gate (z,) —- Controls how much past memory to retain.

© No separate cell state like LSTM; hidden state h; directly stores information.

. Reset Gate:

r= o(W,[he-1, x4| + b,)

. Update Gate:

Zt = o(W.[hi-1, Zt] + b.)

. Candidate Hidden State:

hi => tanh(W), [rt . hi-1, 4] + bp)
. Final Hidden State Update:

hy = (1-2) + Ina + he

. Convolutional Layers ( Conv2D )

e Extracts features such as edges and textures using filters.

¢ Uses ReLU activation to introduce non-linearity.
. Pooling Layers ( MaxPooling2D )

¢ Reduces the size of feature maps while retaining important information.

¢ Max pooling selects the highest value in a region to keep dominant features.
. Flatten Layer ( Flatten )

© Converts 2D feature maps into a 1D vector for input to fully connected layers.
. Fully Connected Layers ( Dense )

¢ First dense layer learns patterns, while the final softmax layer predicts class probabilities.
. Compilation & Training

¢ Uses Adam optimizer for adaptive learning rate.

© Sparse categorical cross-entropy loss for multi-class classification.
--- page 8 ---
Dense(1)
])
# Compile with gradient clipping
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001, clipnorm=1.0)
# Clipping norm to 1.0
model.compile(optimizer=optimizer, loss='mse')
# Example data
import numpy as np
X = np.random.rand(100, 10, 1)
y = np.random.rand(100, 1)
# Train model
model.fit(X, y, epochs=5, batch_size=16)
a.   [10]
Q7
********** 8 **********

[Text in pictures on this page, read by OCR]
1. Human-Level Performance (HLP) in Machine Learning:
© HLP is the accuracy level a well-trained human expert achieves on a given task.
© It serves as a benchmark to evaluate machine learning models.

¢ If a model performs close to or better than HLP, further improvements may be difficult due to

inherent noise in data (e.g., mislabeled samples).

2. Error Analysis for Improving Model Performance:
¢ Breaks down model errors into different categories:
© Bias Error (Underfitting): Model is too simple, needs more features or complexity.
¢ Variance Error (Overfitting): Model memorizes training data, needs regularization.

¢ Data Mismatch Error: Training and test data distributions differ, requiring better data

collection.

¢ Human-Labeling Error: Data might contain incorrect labels, requiring manual review.

3. How Error Analysis Helps:
e Identifies dominant sources of error to prioritize fixes.
¢ Suggests targeted improvements, e.g.:
e High bias — Use a more complex model or add features.
e High variance — Use regularization, more data, or dropout.

¢ Mismatched data — Use transfer learning or domain adaptation.
--- page 9 ---
Q7

1. Compute gradients at time step t:
= VL(w:)
2. Update biased first moment estimate (Momentum):

m, = Bym1 + (1 — Bi) ge

3. Update biased second moment estimate (RMSprop-like scaling):

Ue = Bovy1 + (1 — Be) 9?

4. Bias correction to counter initial zero moments:

~ ™e ~ Ut
mm = Ut =
it? t
1— By 1)
5. Update parameters:
Ui] a
Wty = Wt -— Fe _™
VU + €
Feature SGD Adam
Learning Rate Fixed Adaptive per weight
Convergence Speed Slower Faster
Gradient Noise High Lower (smooth updates)
Suitable for Large, simple datasets Complex deep networks

[10]

FIC QF OH ar
````
