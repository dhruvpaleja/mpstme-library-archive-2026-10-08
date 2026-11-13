# Artificial Intelligence - Deep Learning and Generative AI: question papers in full

5 unique papers · 2024-25 to 2025-26 · Artificial Intelligence

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 2 · paper e7b3303d3083

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Artificial Intelligence - Deep Learning_7071ba3b/QP_Artificial Intelligence - Deep Learning & Generative AI(703DB0C066)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Artificial Intelligence - Deep Learning & Generative AI
Date: 11 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 1; SO-   a. A neural network trained on a small dataset achieves near-zero training error [5]
2 ; BL-1
but performs poorly on unseen data. Explain what is happening internally and
how training dynamics contribute to this behaviour.
CO-3 ; SO-   b. Explain the training process of Generative Adversarial Networks. What [5]
3; BL-2
challenges are faced during training?
CO-3 ; SO-   c. Analyze the impact of incorporating an attention mechanism in a sequence- [5]
2; BL-4
to-sequence model. How does it affect the model’s handling of long
sequences compared to a standard encoder-decoder architecture without
attention.
CO-4 ; SO-   d.   Identify and list the different types of bias that can arise in AI systems.   [5]
2 ; BL-2
Q2   A neural network consists of two input neurons, one hidden layer with two
CO-1; SO-   neurons, and one output neuron.
2; BL-5
[10]
Given:
x1=0.5,  x2=0.3
W1=0.3,W2=0.5,W3=0.4,W4=0.7 ,W5=0.6,W6=0.8
b1=0.2,b2=0.3,b3=0.5
Activation: Linear, α=0.01, Target: y=1
[10]
Perform a complete forward pass and compute the final output.
Perform one iteration of backpropagation to:
********** 1 **********
--- page 2 ---
• Compute error and gradients
• Update weights and biases
Evaluate the effect of using a linear activation function in this network.
Q3   a   While designing a CNN for detecting objects in images, explain how different [10]
CO-2;   layers (convolution, activation, pooling) contribute to feature learning. Apply
SO-2;
this understanding to justify how CNNs capture both low-level and high-level
BL-3
features.
Q3   b   Explain the concepts of AI transparency and explainability, and discuss the   [10]
CO-4;   challenges in achieving explainability in deep learning models.
SO-2;
BL-2
Q4   a   Explain the working of the self-attention mechanism in Transformer models, [10]
CO-2;   highlighting the roles of Query, Key, and Value vectors. Further, summarize
SO-2;
the concept of multi-head attention and explain why multiple attention heads
BL-2
improve performance compared to a single attention head.
Q4   b   Given a translation task with very long sentences, evaluate whether a [10]
CO-2;   Transformer’s self-attention mechanism or a traditional seq2seq attention
SO-2;
mechanism would yield better results. Justify your reasoning in terms of
BL-5
information flow, computational efficiency, and accuracy.
Q 5   a.   In the context of image synthesis, apply the concept of Generative Adversarial [10]
CO-3;
Networks (GAN) to explain how realistic images can be generated. Describe
SO-2;
BL-5   the roles of the generator and discriminator and how they interact during
training.
Q5   b. Compare Variational Autoencoders (VAE) and Generative Adversarial [10]
CO-3;
Networks (GAN) in terms of the outputs they generate. Explain why VAEs
SO-2;
BL-4   tend to produce smoother images while GANs produce sharper but less stable
results.
Q6   Suppose you are building a text generation system using sequential data.
CO-2;   Answer the following:
SO-2;
(a) Explain the working of an LSTM-based model for sequence prediction.   [8]
BL-5
In your answer:
********** 2 **********
--- page 3 ---
• Explain how LSTM handles long-term dependencies compared to a
basic RNN.
• Describe the roles of input, forget, and output gates in controlling the
flow of information.
• Compare LSTM and GRU in terms of structure and computational
efficiency
(b) A student implements an LSTM-based sequence model, but the code   [6]
contains errors. Identify and correct the errors in the given code snippet.
Also, explain the purpose of each corrected component.
(c) After training the model, the validation loss is significantly higher than
the training loss.   [6]
• What does this indicate about the model?
• Suggest two techniques to improve validation performance and
explain how they help.
Q 7   Design a Transformer-based model for text generation.
CO-3;
Write Python-like code (or pseudocode) to:   [20]
SO-2;
BL-1,4,6   •   prepare input-target sequences from text data
• implement masked self-attention
•   construct a Transformer block (multi-head attention, feedforward,
layer normalization, residual connections)
• perform forward pass and compute loss
•   generate text sequentially
********** 3 **********

[Text in pictures on this page, read by OCR]
import torch
import torch.nn as nn

class LSTMModel(nn.Module):
def _ init__(self, vocab_size, embed_size, hidden_size):
super().__init__()
self.embedding = nn.Embedding({voceb_size, embed_size})
self.istm = nn.LS7M(embed_size, hidden_size)
self.fc = nn.Linear(hidden_size, vocab_size)

def forward(self, x):
x = self.embedding(x)
out, _ = self.istm({x)
out = self.fc(out[:, -1])
return out

model = LSTMModel(vocab_size=100, embed_size=32, hidden_size=64)

x = torch.randint(@, 100, (16, 18)) # (batch_size, seq_len)
output = model({x)

loss_fn = nn.CrossEntropyLoss()
target = torch.randint(@, 108, (16, 18))

loss = loss_fn{output, target)
````

## 2024-25 · Final-Exam · Sem 2 · paper 161974283a57

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Artificial Intelligence - Deep Learning_7071ba3b/QP_Artificial Intelligence - Deep Learning & Generative AI(703DB0C066)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2025
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Artificial Intelligence - Deep Learning & Generative AI
Date: 05 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 1; SO-2 ;   a. Define and explain the importance of learning rate in deep learning.   [5]
BL-1
CO-3 ; SO- 3;   b. How do VAEs differ from GANs in generative modeling?   [5]
BL-2
CO-3 ; SO- 2;   c. Describe the transformer architecture and its impact on NLP   [5]
BL-4
CO-4 ; SO-2 ;   d. What are the key ethical concerns related to bias in AI?   [5]
BL-2
Q2   A neural network consists of two input neurons, one hidden layer with two [20]
CO-1; SO-   neurons, and one output neuron.Given Data:
2; BL-5
Input values: (x₁=0.5, x₂=0.3)
Initial Weights:
Input to Hidden Layer:
W1=0.3 (from x1 to Hidden Neuron 1)
W2=0.5(from x2 to Hidden Neuron 1)
W3=0.4 (from x1 to Hidden Neuron 2)
W4=0.7 (from x2 to Hidden Neuron 2)
Hidden to Output Layer:
W5=0.6 (from Hidden Neuron 1 to Output)
W6=0.8 (from Hidden Neuron 2 to Output)
Bias values:
Hidden Layer:
b1=0.2 (for Hidden Neuron 1)
********** 1 **********
--- page 2 ---
b2=0.3 (for Hidden Neuron 2)
Output Layer:
B3=0.5 (for Output Neuron)
Additional Information:
Activation Function: Linear for all layers
Learning Rate: α=0.01
Target Output: y=1
Task:
Perform a forward pass to compute the network’s output. Compute the
error gradient using backpropagation. Update the weights and biases
after one iteration of backpropagation.
Q3   a Draw and explain the architecture of a CNN, covering convolutional   [10]
CO-2;   layers, pooling layers, and fully connected layers.
SO-2;
BL-3
Q3   b   Explain the importance of AI transparency and explainability.   [10]
CO-2;
SO-2;
BL-2
Q4   a   Write a pseudo-code to train an LSTM model for text generation. Explain [10]
CO-2;   each step.
SO-2;
BL-2
Q4   b   Recurrent Neural Networks (RNNs) are commonly used for sequential [10]
CO-2;   data processing, but they suffer from issues such as vanishing and
SO-2;
BL-5   exploding gradients. Explain the architecture of a basic RNN, derive its
forward and backward propagation equations, and discuss how
architectures of GRU help in overcoming these challenges.
Q 5   a.   Justify the role of loss functions in generative models and compare the   [10]
CO-3;
SO-2;   losses used in VAEs and GANs.
BL-5
Q5   b.   Illustrate the step-by-step training process of a GAN and provide a high-   [10]
CO-3;
SO-2;   level architecture diagram.
BL-4
********** 2 **********
--- page 3 ---
Q6   Suppose you are working on image classification. and need to build a [20]
CO-2;   Convolutional Neural Network (CNN) model for classification. Answer
SO-2;
the following:
BL-5
(a) Explain the working of CNN used for image classification and
answer following:
(i) How does the Convolutional Layer extract features?
(ii) Why do we use Pooling Layers? Compare Max Pooling and
Average Pooling.
(iii) What is the role of Flattening in a CNN?
(b) Below is an implementation of a CNN for image classification,
but there are errors in the code. Identify and correct the
mistakes. Also, explain the purpose of each corrected
component.
(c) You trained a CNN model, and its validation accuracy is much
lower than the training accuracy.
(i) What does this indicate?
(ii) Suggest two ways to improve validation accuracy and explain
how they help.
Q 7   Explain how Cross-Attention differs from Self-Attention and where it is used
CO-3; SO-   in Transformers like BERT or T5. Conclude its significance in machine   [20]
2;
BL-1,4   translation and image-captioning models. Finally, discuss the impact of
removing Cross-Attention from a Transformer-based architecture.
********** 3 **********

[Text in pictures on this page, read by OCR]
import tensorflow as tf
from tensorflow.keras import layers, models

model = models. Sequential ([
layers.Conv2D(64, (5,5), activation='relu', input_shape=(28, 28)), # Error 1
layers.MaxPooling2D(3,3), # Error 2
layers.Conv20(32, (3,3), activation='relu'),
layers .MaxPooling2D(2,2) ,
layers.Dense(128, activation='relu'), # Error 3
layers Dropout(@.5)
layers.Dense(10, activation="sigmoid') # Error 4

})

model. compile(optimizer='adam', loss='mean_squared_error’, metrics=['accuracy']) # Error 5
````

## 2024-25 · Final-Exam · Sem 2 · paper 603bbc0039d8

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENT
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ARTIFICIAL INTELLIGENT/SEM II/Artificial Intelligence - Deep Learning_7071ba3b/Artificial Intelligence - Deep Learning & Generative AI Batch 2024-25 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2025
- Text: ocr (3 pages), mean OCR confidence 87.5
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGEN

SVKMs NMIMS

Year: I/Semester II(Exam Year: 2024-2025)

¥

Subject: Artificial Intelligence - Deep Learning & Generative AI ae

Date: 05 May 2025
Max. Marks: 100

Instructions:

Time: 02:00 pm to 05:00 pm (03:00 Hrs.)

FINAL EXAMINATION (Acad. Year:2024-2025)

1. This question paper contains 3 pages.

2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks

4. Question No._1____ is compulsory.

5. Out of remaining questions, attempt any 4 __ questions.
6. Inall__5_ questions to be attempted.

7. All questions carry equal marks.

8. Assume Suitable data if necessary.

Ql Answer briefly: [20]
a 1; S0-2; | a. | Define and explain the importance of learning rate in deep learning. [5]
-1

aA ; SO- 3; | b. | How do VAEs differ from GANs in generative modeling? [5]

ey ;SO-2; | c. | Describe the transformer architecture and its impact on NLP [5]

Bho ;SO-2; | d. | What are the key ethical concerns related to bias in AI? [5]
L-2

Q2 A neural network consists of two input neurons, one hidden layer-with two | [20]

CO-1; SO- neurons, and one output neuron. Given Data:

2; BL-5

Input values: (x:=0.5, x2=0.3)
Initial Weights:

Input to Hidden Layer:

W1=0.3 (from x1 to Hidden Neuron 1)
W2=0.5(from x2 to Hidden Neuron 1)
W3=0.4 (from x1 to Hidden Neuron 2)
W4=0.7 (from x2 to Hidden Neuron 2)

Hidden to Output Layer:
W5=0.6 (from Hidden Neuron | to Output)
W6=0.8 (from Hidden Neuron 2 to Output)

Bias values:
Hidden Layer:
b1=0.2 (for Hidden Neuron 1)

FRR 7 RE
--- page 2 ---
b2=0.3 (for Hidden Neuron 2)

Output Layer:

B3=0.5 (for Output Neuron) ve
Additional Information: :
Activation Function: Linear for all layers

Learning Rate: a=0.01

Target Output: y=1

Task:

Perform a forward pass to compute the network’s output. Compute the
error gradient using backpropagation. Update the weights and biases

after one iteration of backpropagation.

Q3 Draw and explain the architecture of a CNN, covering convolutional [10]

nai layers, pooling layers, and fully connected layers.

BL-3

Q3 Explain the importance of AI transparency and explainability. [10]

CO-2;

SO-2;

BL-2

Q4 Write a pseudo-code to train an LSTM model for text generation. Explain | [10]

CO-2;

S0-2: each step.

BL-2

Q4 Recurrent Neural Networks (RNNs) are commonly used for sequential | [10]

oo data processing, but they -suffer from issues such as vanishing and-

BL-5 exploding gradients. Explain the architecture of a basic RNN, derive its
forward and backward propagation equations, and discuss how
architectures of GRU help in overcoming these challenges.

an ‘4 Justify the role of loss functions in generative models and compare the [10]

S0-2: losses used in VAEs and GANs.

BL-5

oe 3 Illustrate the step-by-step training process of a GAN and‘provide a high- | [10]

$0-2: level architecture diagram.

BL-4


My
--- page 3 ---
Q6

Suppose you are working on image classification. and need to build a | [20]

CO-2; Convolutional Neural Network (CNN) model for classification. Answer 1
SO-2; a ‘
BL-5 the following: a

(a) Explain the working of CNN used for image classification and
answer following:

(i) How does the Convolutional Layer extract features?

(ii) Why do we use Pooling Layers? Compare Max Pooling and
Average Pooling.

(iii) What is the role of Flattening in a CNN?

(b) Below is an implementation of a CNN for image classification,
but there are errors in the code. Identify and correct the
mistakes. Also, explain the purpose of each corrected
component.
import tensorflow as tf
from tensorflow.keras import layers, models ~ ”
model = models Sequential ([

layers.Conv20(64, (5,5), activation="relu', input_shape=(28, 28)), # Error 1
layers.MaxPooling2D(3,3), # Error 2
layers.Conv2D(32, (3,3), activation="relu'),
layers MaxPooling2D(2,2),
layers.Dense(128, activation='relu'), # Error 3
layers Dropout (@.5),
layers.Dense(10, activation='sigmoid') # Error 4
})
model. compile(optimizer=‘adan', loss='mean_squared_error’, metrics=[‘accuracy’]) # Error 5

(c) You trained a CNN model, and its validation accuracy is much
lower than the training accuracy. ______ themes © osmosis
(i) What does this indicate?

(ii) Suggest two ways to improve validation accuracy and explain

how they help.
Q7 Explain how Cross-Attention differs from Self-Attention and where it is used
ial SO- in Transformers like BERT or T5. Conclude its significance in machine [20]
BL-1 4 translation and image-captioning models. Finally, discuss the impact of

removing Cross-Attention from a Transformer-based architecture.

````
