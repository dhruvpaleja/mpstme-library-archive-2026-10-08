# Artificial Intelligence - Deep Learning and Generative AI: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 7e38554c9cf7

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Artificial Intelligence - Deep Learning_7071ba3b/ANS_Artificial Intelligence - Deep Learning & Generative AI(703DB0C066)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: mixed (15 pages), mean OCR confidence 78.0
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Artificial Intelligence - Deep Learning & Generative AI
Date: 11 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
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
This is a classic case of overfitting.
Explanation:
•   Near-zero training error: The network has memorized the training
examples instead of learning general patterns.
• Poor performance on unseen data: Because the network hasn’t
generalized, it fails to predict new inputs correctly.
•   Training dynamics contributing:
o Small dataset → not enough diverse examples.
o High-capacity network → can fit all training data perfectly.
o Lack of regularization → nothing prevents memorization.
How to address:
•   Increase dataset size or use data augmentation.
• Apply regularization techniques (dropout, weight decay).
• Reduce network complexity.
CO-3 ; SO-   b. Explain the training process of Generative Adversarial Networks. What   [5]
3; BL-2
challenges are faced during training?
********** 1 **********
--- page 2 ---
Training Process of GANs
A Generative Adversarial Network (GAN) consists of two models:
• Generator (G): Generates fake data from random noise
• Discriminator (D): Distinguishes between real and fake data
Steps involved:
1. Random noise is given as input to the generator.
2. The generator produces fake samples (e.g., images).
3. The discriminator receives both real data and generated (fake) data.
4. The discriminator learns to classify inputs as real or fake.
5. Feedback from the discriminator is used to update the generator.
6. This process continues in an adversarial manner until the generator
produces realistic outputs.
Challenges in Training GANs
1. Mode Collapse: Generator produces limited variety of outputs.
2. Training Instability: Difficult to balance generator and
discriminator.
3. Vanishing Gradients: If discriminator becomes too strong,
generator learns slowly.
4. Non-convergence: Model may not reach a stable equilibrium.
CO-3 ; SO-   c. Analyze the impact of incorporating an attention mechanism in a sequence- [5]
2; BL-4
to-sequence model. How does it affect the model’s handling of long
sequences compared to a standard encoder-decoder architecture without
attention.
Impact of attention: The attention mechanism allows the decoder to focus on
relevant parts of the input sequence at each step, rather than relying solely on
a fixed-length context vector from the encoder.
Handling long sequences:
•   In standard encoder-decoder models, long sequences can cause
information bottlenecks, leading to poor performance.
• With attention, the model can dynamically weigh input tokens,
preserving important information and improving translation or
prediction quality for long sequences.
Outcome:
•   Better alignment between input and output.
• Improved accuracy and fluency in sequence generation.
********** 2 **********
--- page 3 ---
• Reduces the degradation of performance seen in long sequences with
standard seq2seq model
CO-4 ; SO-   d.   Identify and list the different types of bias that can arise in AI systems.   [5]
2 ; BL-2
Common types of bias in AI systems include:
1. Data Bias: Arises from unrepresentative, incomplete, or skewed
training data.
2. Algorithmic Bias: When the model or learning algorithm introduces
bias in predictions.
3. Sampling Bias: Occurs when certain groups are under- or over-
represented in the dataset.
4. Measurement Bias: Caused by errors or inconsistencies in how data
is collected or labeled.
5. Confirmation Bias: When the system reinforces existing assumptions
or patterns.
6. Societal or Cultural Bias: Reflects stereotypes or prejudices present
in the data.
Q2   A neural network consists of two input neurons, one hidden layer with two
neurons, and one output neuron.
CO-1; SO-
2; BL-5
Given:
x1=0.5,  x2=0.3
W1=0.3,W2=0.5,W3=0.4,W4=0.7 ,W5=0.6,W6=0.8
b1=0.2,b2=0.3,b3=0.5
Activation: Linear, α=0.01, Target: y=1
Perform a complete forward pass and compute the final output.
[10]
Perform one iteration of backpropagation to:
[10]
• Compute error and gradients
• Update weights and biases
Evaluate the effect of using a linear activation function in this network.
********** 3 **********
--- page 4 ---
4
We have a feedforward neural network:

© Input layer: 2 neurons (2, 22)

® Hidden layer: 2 neurons (hy, h2)

* Output layer: 1 neuron (a)

* Linear activation throughout (f(2) = x)
© Learning rate: a = 0.01

* Target: y = 1

Weights and biases:

® Hidden layer:
© Ayiw, = 0.3,ws = 0.5,6, = 0.2
. ho wy = 0.4, wy = 0.7, Be = (0.3
* Output layer:
* oO: Ws, = 0.6, wr, => 0.8, by =().5

Input: ry = 0.5, 25 = 0.3
Activation: Linear + output = input of the neuron

Step 1: Forward Pass

Hidden layer outputs:
hy = wx) + wer2 + by = (0.3)(0.5) + (0.5)(0.3) + 0.2
hy = 0.15 + 0.15 + 0.2 = 0.5
hy = wr) + w4r2 + by = (0.4)(0.5) + (0.7)(0.3) + 0.3
hy = 0.2 + 0.21 + 0.3 = 0.71
Output neuron:
o = w;h, + weh2 + by = (0.6)(0.5) + (0.8)(0.71) + 0.5
o= 0.3 + 0.568 + 0.5 = 1.368

(© Forward pass output: o = 1.368

Step 2: Compute Error

Mean Squared Error (MSE) for single sample:
1 > 1 3
E=>5 ? = =(1 — 1.368)?
3(¥— 0) = 5( )

E=0.5 x (—0.368)? = 0.5 x 0.1354 ~ 0.0677

FIC 7) IC HOH
--- page 5 ---
Step 3: Backpropagation (gradients)

Output layer gradient:

Linear activation — derivative f’(2) = 1
OE
6 = — =0-y =1.368 — 1 = 0.368
do

Gradients for output weights and bias:

OE = 6,+ hy = 0.368 - 0.5 = 0.184
Ow;
OE
ZS = 50+ h2 = 0.368 - 0.71 ~ 0.2613
a 7 2
OE
= = 4 = 0.368
Obs

Hidden layer gradients:
oh, = 50° ws - f'(hi) = 0.368 - 0.6 - 1 = 0.2208

bn, = 50 - we + f'(h2) = 0.368 - 0.8 - 1 = 0.2944

Gradients for hidden layer weights and biases:

OF _ 5, 2, = 0.2208 -0.5 = 0.1104
Ow,
OE
= §,, -r2 = 0.2208 - 0.3 ~ 0.0662
Ow.
dE
~ = by, = 0.2208
dh
OF _ 5. = 0.2944-0.5 = 0.1472
Ow; °
dE
S&S = §,. - 22 = 0.2944 - 0.3 = 0.0883
Ow, °
dE
= 5, = 0.2944
db,

FIC DI EH ar
--- page 6 ---
Q3   a   While designing a CNN for detecting objects in images, explain how different [10]
CO-2;   layers (convolution, activation, pooling) contribute to feature learning. Apply
SO-2;
this understanding to justify how CNNs capture both low-level and high-level
BL-3
features.
Convolution Layer:
Applies learnable filters to the input image to extract local patterns such as
edges, textures, and simple shapes.
Each filter produces a feature map highlighting the presence of a specific
feature.
Activation Layer (e.g., ReLU):
Introduces non-linearity, enabling the network to model complex
relationships between features.
Helps the network respond strongly to important features while suppressing
irrelevant ones.
********** 6 **********

[Text in pictures on this page, read by OCR]
Step 4: Update weights (Gradient Descent)
OE

Wnew = Wold — &* D—

Ow

Hidden layer:
w; = 0.3 — 0.01 - 0.1104 = 0.2989
wy = 0.5 — 0.01 - 0.0662 ~ 0.4993
b, = 0.2 — 0.01 - 0.2208 ~ 0.1978
ws = 0.4 — 0.01 - 0.1472 = 0.3985
w, = 0.7 — 0.01 - 0.0883 = 0.6991
by = 0.3 — 0.01 - 0.2944 = 0.2971
Output layer:
w; = 0.6 — 0.01 - 0.184 ~ 0.5982
we = 0.8 — 0.01 - 0.2613 = 0.7974

bs = 0.5 — 0.01 - 0.368 = 0.4963

Step 5: Effect of Linear Activation
© Linear activation does not introduce non-linearity, so the network is equivalent to a single linear
transformation from input to output.
* Multiple layers with linear activation cannot model complex relationships.
* Suitable only for simple regression tasks; poor choice for tasks requiring non-linear mapping (like
classification or complex function approximation).
--- page 7 ---
Pooling Layer (e.g., Max Pooling):
Reduces spatial dimensions of feature maps, retaining the most important
information.
Adds translation invariance, so features can be recognized even if slightly
shifted.
Feature Learning Hierarchy:
Low-level features: Early convolution layers capture edges, corners, and
textures.
High-level features: Deeper layers combine low-level features to detect
complex patterns like object parts or full objects.
Justification:
By stacking convolution, activation, and pooling layers, CNNs progressively
build a hierarchy of features, enabling robust detection of objects in images.
Q3   b   Explain the concepts of AI transparency and explainability, and discuss the   [10]
challenges in achieving explainability in deep learning models.
CO-4;
SO-2;
AI Transparency: Refers to the openness of an AI system—how easily users
BL-2
can see and understand how the system works, including data, algorithms,
and decision-making processes.
AI Explainability: Refers to the ability to interpret and understand why a
model made a particular prediction or decision, often by providing human-
understandable explanations.
Challenges in Deep Learning:
Complexity: Deep neural networks have millions of parameters, making
internal workings hard to interpret.
Non-linearity: Layers of non-linear transformations make it difficult to trace
how inputs influence outputs.
Feature abstraction: High-level features learned automatically may not
correspond to intuitive human concepts.
Trade-off with performance: Simplifying models for interpretability may
reduce accuracy.
Black-box nature: Many deep learning architectures inherently lack
interpretability mechanisms.
Q4   a   Explain the working of the self-attention mechanism in Transformer models, [10]
CO-2;   highlighting the roles of Query, Key, and Value vectors. Further, summarize
SO-2;
********** 7 **********
--- page 8 ---
BL-2   the concept of multi-head attention and explain why multiple attention heads
improve performance compared to a single attention head.
Q4   b   Given a translation task with very long sentences, evaluate whether a [10]
Transformer’s self-attention mechanism or a traditional seq2seq attention
CO-2;
mechanism would yield better results. Justify your reasoning in terms of
SO-2;
information flow, computational efficiency, and accuracy.
********** 8 **********

[Text in pictures on this page, read by OCR]
Self-Attention Mechanism:

© Purpose: Allows a Transformer to weigh the importance of different words (or tokens) in a sequence
when encoding a particular token.

* Key components:

1. Query (Q): Represents the token for which we are calculating attention.

2. Key (K): Represents each token’s identity in the sequence.

3. Value (V): Holds the actual information of each token to be combined based on attention scores.
* Working Steps:

1. Compute attention scores by taking the dot product of the query with all keys, then scale and

apply softmax:

Attention(Q, K,V) = softmax (=) v

2. Multiply the attention weights with the values to get a weighted sum, emphasizing relevant tokens
for the current query.

Multi-Head Attention:

* Instead of a single attention calculation, the model uses multiple attention heads (each with its own Q,
K, V projections).

* Each head learns different types of relationships or patterns in the sequence.

© The outputs of all heads are concatenated and linearly transformed to form the final representation.

Advantages of Multiple Heads:

1. Captures diverse contextual information simultaneously.

2. Helps the model attend to different positions and features in the sequence.

3. Improves representation quality, leading to better performance on tasks like translation,
summarization, and text generation.

Summary: Self-attention computes contextualized representations using Q, K, and V, while multi-head
attention allows the model to capture multiple aspects of relationships in the data, improving learning
capacity and expressiveness.

Self-Attention in Transformer Models

+ Attention Scores
Softmax & Weighed Sum

—$— fae

gen

Multi-Head Attention

Parallel Processing

e-(]-o

Concatenated Output

Multiple Attention Heads

Captures both
detailed and
broad patterns
--- page 9 ---
BL-5   For very long sentences, a Transformer’s self-attention generally performs
better than traditional seq2seq attention:
Information flow: Self-attention allows every token to directly attend to all
other tokens, capturing long-range dependencies efficiently. Seq2seq
attention still relies on sequential decoding, which can dilute long-distance
relationships.
Computational efficiency: Transformers can parallelize computations across
tokens, while RNN-based seq2seq processes tokens sequentially, making it
slower for long sentences.
Accuracy: By modeling all token interactions simultaneously, Transformers
reduce information loss and improve translation quality, especially for
complex, long sentences.
Overall, Transformers handle long sequences more effectively in both speed
and accuracy.
Q 5   a.   In the context of image synthesis, apply the concept of Generative [10]
CO-3;
Adversarial Networks (GAN) to explain how realistic images can be
SO-2;
BL-5   generated. Describe the roles of the generator and discriminator and how they
interact during training.
In image synthesis using GANs, two neural networks compete to improve
image realism:
1. Generator
o Creates fake images from random noise.
o Tries to produce images that look real enough to fool the
discriminator.
2. Discriminator
o Evaluates images and predicts whether they are real (from
dataset) or fake (from generator).
o Provides feedback to the generator about how realistic its
images are.
Training interaction:
• The generator and discriminator are trained together in a loop.
• The generator improves to produce more realistic images, while the
discriminator improves to better detect fakes.
• This adversarial process continues until the generator produces
images that the discriminator cannot reliably distinguish from real
ones, resulting in highly realistic synthetic images.
********** 9 **********
--- page 10 ---
Q5   b. Compare Variational Autoencoders (VAE) and Generative Adversarial [10]
CO-3;
Networks (GAN) in terms of the outputs they generate. Explain why VAEs
SO-2;
BL-4   tend to produce smoother images while GANs produce sharper but less stable
results.
Variational Autoencoder (VAE):
• Learns a probabilistic latent space and reconstructs images by
sampling from it.
• Outputs tend to be smooth and blurry because the model averages over
the possible variations in the latent space, prioritizing overall structure
rather than fine details.
Generative Adversarial Network (GAN):
•   Trains a generator to fool a discriminator, focusing on making images
look realistic.
• Outputs are usually sharper and more detailed, but training can be
unstable (mode collapse, artifacts) because the generator may overfit
to fool the discriminator.
Summary:
• VAE → smooth, stable, less detailed
• GAN → sharp, realistic, but potentially unstable
********** 10 **********
--- page 11 ---
Q6   Suppose you are building a text generation system using sequential data.
CO-2;   Answer the following:
SO-2;
(a) Explain the working of an LSTM-based model for sequence prediction.   [8]
BL-5
In your answer:
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
the training loss.
• What does this indicate about the model?
• Suggest two techniques to improve validation performance and
explain how they help.   [6]
(a) LSTM-based sequence prediction:
• Handling long-term dependencies: Unlike a basic RNN, which suffers
from vanishing gradients and struggles to remember information over
long sequences, an LSTM uses a memory cell that maintains
information over time. This allows   it to capture long-term
dependencies effectively.
• Gates in LSTM:
o Input gate: Controls how much new information from the
current input is added to the cell state.
o Forget gate: Decides which information from the previous cell
state should be retained or discarded.
********** 11 **********

[Text in pictures on this page, read by OCR]
import torch
import torch.nn as nn

class LSTMModel{nn.Module):
def _ init__(self, vocab_size, embed_size, hidden_size):
super().__init__()
self.embedding = nn.Embedding(voceb_size, embed_size)
self.istm = nn.LSTM(embed_size, hidden_size)
self.fc = nn.Linear(hidden_size, vwocab_size)

def forward(self, x):
x = self.embedding(x)
out, _ = self.1stm(x)
out = self.fcf{out[:, -1])
return out

model = LSTMModel(vocab_size=100, embed_size=32, hidden_size=64)

output = model(x)

loss_fn = on.CrossEntropyLoss()
target = torch.randint(@, 106, (16, 18))

loss = loss_fn(output, target)
--- page 12 ---
o Output gate: Determines how much of the cell state is exposed
to the hidden state (i.e., the output at the current time step).
• LSTM vs GRU:
o   Structure: LSTM has three gates (input, forget, output) and a
separate cell state, while GRU combines the input and forget
gates into an update gate and merges the cell and hidden states.
o Efficiency: GRU is simpler and faster to compute, making it
more efficient for smaller datasets or less complex tasks, while
LSTM may perform better for tasks requiring modeling of
very long sequences.
(b) Error 1: Missing batch_first=True
Students should know input is (batch, seq_len)
Error 2: Wrong indexing
out[:, -1] is incomplete
Error 3: Incorrect target shape
Target should be 1D
(c ) Training loss low → Model fits the training data closely.
Validation loss high → Model performs poorly on unseen data,
meaning it hasn’t generalized well.
Two techniques to improve validation performance:
1. Regularization (e.g., L1/L2 or Dropout)
o How it helps: Adds a penalty for large weights (L1/L2) or
randomly disables neurons during training (Dropout). This
prevents the model from relying too heavily on specific
features, encouraging it to learn more general patterns that
perform better on validation data.
2. Data Augmentation or More Training Data
o How   it helps: By expanding the training dataset with
variations (like rotations, scaling, or noise in images, or
synonym replacement in text), the model learns to generalize
better instead of memorizing the training examples. More
diverse data reduces overfitting and improves validation
performance.
Other options can include early stopping or simplifying the model (reducing
layers or neurons) if it’s too complex for the data.
********** 12 **********
--- page 13 ---
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
********** 13 **********

[Text in pictures on this page, read by OCR]
import torch
import torch.nn as nn
import torch.nn.functional as F

#1. Prepare Input-Target Sequences

def create_sequences(text, seq_len, tokenizer):

tokens = tokenizer.encode(text) # convert text to token IDs

input_seq = []

target_seq = []

for i in range(len(tokens) - seq_len):
input_seq.append(tokens[i:i+seq_len])
target_seq.append(tokens[i+1:i+seq_len+1]) # next-token prediction

return torch.tensor(input_seq), torch.tensor(target_seq)
--- page 14 ---
# 2. Masked Self-Attention

class MaskedSelfAttention(nn.Module):
def __init_(self, embed_size, heads):
super().__init_(
self.embed_size = embed_size
self.heads = heads
self.head_dim = embed_size // heads

self.query = nn.Linear(embed_size, embed_size)
self.key = nn.Linear(embed_size, embed_size)
self.value = nn.Linear(embed_size, embed_size)
self.fc_out = nn.Linear(embed_size, embed_size)

def forward(self, x):
N, seqlen, embed_size = x.shape

# Linear projections
Q

self.query(x)
self-key(x)
V = self.value(x)

# Split into heads

Q = Q.view(N, seq_len, self.heads, self.head_dim).transpose(1,2) # (N, heads, seq len, head_dim)
K = K.view(N, seq_len, self.heads, self.head_dim).transpose(1,2)

V = V.view(N, seq_len, self.heads, self.head_dim).transpose(1,2)

# Scaled dot-product attention
scores = Q @ K.transpose(-2, -1) / (self.head_dim ** 9.5)

# Mask future tokens (causal mask)
mask = torch.tril(torch.ones(seq_len, seq_len)).to(x.device)
scores = scores.masked_fill(mask == @, float('-inf'))

attention = F.softmax(scores, dim=-1)
out = attention @V # (N, heads, seq_len, head_dim)

# Concatenate heads
out = out.transpose(1,2).contiguous().view(N, seq_len, embed_size)
return self.f¢_out(out)

#
#3. Transformer Block
#
class TransformerBlock(nn.Module):
def _ init_(self, embed_size, heads, ff_hidden):
super()._ init_()
self.attention = MaskedSelfAttention(embed_size, heads)
self.norml = nn.LayerNorm(embed_size)
self.norm2 = nn.LayerNorm(embed_size)
self.ff = nn.Sequential(
nn.Linear(embed_size, ff_hidden),
nn.ReLUt),
nn.Linear(ff_hidden, embed_size)

def forward(self, x):
# Multi-head attention with residual and Layer norm
attn_out = self.attention(x)
x = self.norml(x + attn_out)

# Feedforward with residual and Layer norm
ff_out = self.ff(x)

x = self.norm2(x + #f_out)

return x

FRR IC 7 I OH
--- page 15 ---
#
# 4. Transformer Model
#
class TransformerTextGen(nn.Module) :
def _init_(self, vocab_size, embed_size, seq_len, heads, ff_hidden, num_layers):
super().__init_()
self.embed = nn.Embedding(vocab_size, embed_size)
self.pos_embed = nn.Embedding(seq_len, embed_size)
self.layers = nn.ModuleList([TransformerBlock(embed_size, heads, ff_hidden) for
self.fc_out = nn.Linear(embed_size, vocab_size)

in range(num_layers)])

def forward(self, x):
N, seq_len = x.shape

positions = torch.arange(@, seq_len).unsqueeze(@).expand(N, seq_len).to(x.device)
x = self.embed(x) + self.pos_embed(positions)
for layer in self.layers:
x = layer(x)
logits = self.fc_out(x)
return logits

#
#5. Loss Computation
#

def compute_loss(model, input_seg, target_seq):
logits = model(input_sea)
# Flatten for cross-entropy
N, seq_len, vocab_size = logits.shape
loss = F.cross_entropy(logits.view(N*seq_len, vocab_size), target_seq.view(-1))
return loss

#6. Text Generation (Autoregressive)

def generate_text(model, start_seq, tokenizer, max_len):

model..eval()

generated = start_seq

for _ in range(max_len):
input_tensor = torch.tensor(generated[-seq_len:]).unsqueeze(@) # (1, seq_len)
logits = model(input_tensor)
next_token = torch.argmax(logits[@, -1, :]).item()
generated .append(next_token)
if next_token == tokenizer.eos_token_id: # stop if E0S

break
return tokenizer.decode(generated)

FRR IC 7 DA HOH
````

## 2024-25 · Final-Exam · Sem 2 · Answer key · paper 5d400dd0788d

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Artificial Intelligence - Deep Learning_7071ba3b/ANS_Artificial Intelligence - Deep Learning & Generative AI(703DB0C066)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2025
- Text: mixed (7 pages), mean OCR confidence 77.5
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Artificial Intelligence - Deep Learning & Generative AI
Date: 05 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 7 pages.
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
The learning rate controls how much model weights update during
training.
A high learning rate speeds up convergence but risks overshooting, while
a low rate ensures stability but slows down training.
CO-3 ; SO- 3;   b. How do VAEs differ from GANs in generative modeling?   [5]
BL-2
Variational Autoencoders (VAEs): Encode data into a probabilistic
latent space and generate smooth variations of data.
Generative Adversarial Networks (GANs): Use a generator-
discriminator approach to produce realistic samples without explicit
probability modeling.
CO-3 ; SO- 2;   c. Describe the transformer architecture and its impact on NLP   [5]
BL-4
Key components: Self-Attention, Multi-Head Attention, Feedforward
layers, and Positional Encoding.
Impact: Enables parallel processing and long-range dependencies,
leading to breakthroughs in NLP (e.g., BERT, GPT).
CO-4 ; SO-2 ;   d. What are the key ethical concerns related to bias in AI?   [5]
BL-2
Bias can lead to unfair decisions in hiring, lending, and law enforcement.
Causes: Skewed training data, human biases, and flawed models.
********** 1 **********
--- page 2 ---
Solutions: Diverse datasets, fairness-aware algorithms, and transparency.

Q2 Step 1: Forward Pass [20]
CO-1 3 SO- Compute Hidden Layer Outputs
2; BL-5 For Hidden Neuron 1:

Hy = (Wi - 21) + (We - 22) + bi
Hy = (0.3 x 0.5) + (0.5 x 0.3) + 0.2
A, = 0.15 4+ 0.15 + 0.2 = 0.5

For Hidden Neuron 2:

(Ws - 21) + (W4 - @2) + be
H = (0.4 x 0.5) + (0.7 x 0.3) + 0.3
Ay = 0.2 + 0.21 + 0.3 = 0.71
Compute Output Layer Output
O = (0.6 x 0.5) + (0.8 x 0.71) + 0.5

O = 0.3 + 0.568 + 0.5 = 1.368

Step 2: Compute Error
E= Sly —o)
>i 2
B= 5(1— 1.368)
E= 1 0.368)?
z(-0.3

E= ; = 0.1354 = 0.0677

Step 3: Compute Gradients (Backpropagation)
Output Layer Gradients

Gradient w.rt Ws
bE
aws
= (1.368 — 1) x 0.5

=(O-—y)-Mm

= 0.368 x 0.5 = 0.184

Gradient w.rt Wo

@E
owe

=(O—y)-He
= 0.368 x 0.71 = 0.2613

Gradient w.rt B

OE

op, = O-»

FIC 2 I HH ar
--- page 3 ---
Hidden Layer Gradients

Gradient w.r.t W,

Sas = (O-v) Worn
= 0.368 x 0.6 x 0.5
= 0.1104
Gradient w.rt W>

Fae = (0-u)- Weems
= 0.368 x 0.6 x 0.3
= 0.06624
Gradient w.r.t Ws

dE
2” = (0-y)-We-
ows (O-y)-We- a

= 0.368 x 0.8 x 0.5
= 0.1472
Gradient w.r.t Wy

OE 7.
aw, (0-9) Woe

= 0.368 x 0.8 x 0.3

= 0.08832
Gradient w.rt by
OE
= (0-y)-W;
am, (OW) Ws
= 0.368 x 0.6 = 0.2208
Gradient wart b2

OE
— =(0O-y)-W
Ob (O-y)-We

= 0.368 x 0.8 = 0.2944

Step 4: Update Weights and Biases

Using the update rule:
iw ab
Waew = Wola — @- ow
Bue = B, OE
new = Bold — a+ ae
Updated Weights

Wi = 0.3 — (0.01 x 0.1104) = 0.2989
W2 = 0.5 — (0.01 x 0.06624) = 0.4993
Ws = 0.4 — (0.01 x 0.1472) = 0.3985
W, = 0.7 — (0.01 x 0.08832) = 0.6991
Ws; = 0.6 — (0.01 x 0.184) = 0.5982

We = 0.8 — (0.01 x 0.2613) = 0.7974

FC QI a iar
--- page 4 ---
Q3   a Draw and explain the architecture of a CNN, covering convolutional   [10]
CO-2;   layers, pooling layers, and fully connected layers
SO-2;
BL-3
CNN Architecture Explanation
• Convolutional Layer: Extracts spatial features using filters.
• Pooling Layer: Reduces dimensions while retaining key features
(Max Pooling, Average Pooling).
• Fully Connected Layer: Maps extracted features to output
classes.
Q3   b   Explain the importance of AI transparency and explainability.   [10]
CO-2;
SO-2;
BL-2   AI Transparency & Explainability
• Transparency ensures AI decisions can be understood and audited.
•   Explainability helps in trust-building and debugging AI models.
• Methods: Feature importance, SHAP, LIME.
Q4   a   Write a pseudo-code to train an LSTM model for text generation. Explain [20]
CO-2;   each step.
SO-2;
BL-2
Pseudo-Code for LSTM-based Text Generation
• Tokenize and pad text.
• Build an LSTM model with embedding, LSTM, and dense layers.
• Train using cross-entropy loss and Adam optimizer.
• Generate text using the trained model.
Q4   b   Recurrent Neural Networks (RNNs) are commonly used for sequential
CO-2;   data processing, but they suffer from issues such as vanishing and
SO-2;
BL-5
********** 4 **********

[Text in pictures on this page, read by OCR]
Updated Biases
b, = 0.2 — (0.01 x 0.2208) = 0.1978
by = 0.3 — (0.01 x 0.2944) = 0.2971

Bs = 0.5 — (0.01 x 0.368) = 0.4963

Final Answer

After one iteration of backpropagation:
+ Updated Weights:
+ Updated Biases:
by = 0.1978, bz = 0.2971, By = 0.4963
--- page 5 ---
exploding gradients. Explain the architecture of a basic RNN, derive its
forward and backward propagation equations, and discuss how
architectures of GRU help in overcoming these challenges..
Bidirectional RNN vs. Unidirectional RNN
• Unidirectional: Processes input sequentially from past to future.
•   Bidirectional: Uses two RNNs (forward and backward) to capture
context from both directions.
• Example: Improves accuracy in NLP tasks like sentiment
analysis.
Q 5   a. Explain the role of loss functions in generative models and compare the   [10]
CO-3;
SO-2;   losses used in VAEs and GANs.
BL-3
Loss Functions in VAEs & GANs
• VAE Loss: Combines reconstruction loss (MSE/BCE) with KL
divergence.
• GAN Loss: Uses adversarial loss (Binary Cross-Entropy) for
Generator & Discriminator.
b) Training Process of GANs
• Step 1: Train Discriminator on real & fake data.
• Step 2: Train Generator to fool Discriminator.
• Step 3: Alternate training in a loop.
• Diagram: Includes Generator, Discriminator, and Adversarial
training loop.
Q5   b. Describe the step-by-step training process of a GAN and provide a high-   [10]
CO-3;
SO-2;   level architecture diagram.
BL-4
• Step 1: Train Discriminator on real & fake data.
• Step 2: Train Generator to fool Discriminator.
• Step 3: Alternate training in a loop.
• Diagram: Includes Generator, Discriminator, and Adversarial
training loop.
********** 5 **********
--- page 6 ---
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
(i) Feature Extraction in Convolutional Layer
• Uses filters to detect edges, textures, and patterns.
(ii) Why Pooling Layers?
• Reduce spatial size, speed up computation, and enhance feature
robustness.
• Max Pooling retains strongest features, Average Pooling
smooths information.
(iii) Flattening in CNN
• Converts 2D feature maps into a 1D vector before feeding into
fully connected layers.
(iv) CNN Validation Accuracy Issues
•   Indicates overfitting.
•   Solutions: Regularization (Dropout, L2), Data Augmentation, or
reducing model complexity.
(b) Below is an implementation of a CNN for image classification,
but there are errors in the code. Identify and correct the mistakes.
Also, explain the purpose of each corrected component.
********** 6 **********
--- page 7 ---
(c) You trained a CNN model, and its validation accuracy is much
lower than the training accuracy.
(i) What does this indicate?
(ii) Suggest two ways to improve validation accuracy and explain
how they help.
Q 7   Explain how Cross-Attention differs from Self-Attention and where it is used
CO-3; SO-   in Transformers like BERT or T5. Describe its significance in machine   [20]
2;
BL-4   translation and image-captioning models. Finally, discuss the impact of
removing Cross-Attention from a Transformer-based architecture.
• Self-Attention: Helps models focus on different parts of the input
sequence.
• Cross-Attention: Allows a model to focus on another input (e.g.,
image captioning using text & image features).
• Impact in Transformers (BERT, T5): Essential for tasks like
translation, multimodal learning.
• Effect of Removing Cross-Attention: Reduces effectiveness in tasks
requiring external context understanding.
********** 7 **********

[Text in pictures on this page, read by OCR]
import tensorflow as tf
from tensorflow.keras import layers, models

model = models Sequential ([
layers Conv20(64, (5,5), activation='relu', input_shape=(28, 28)), # Error 1
layers.MaxPooling2D(3,3), # Error 2
layers.Conv2D(32, (3,3), activation='relu'),
layers. MaxPooling2D(2,2) ,
layers.Dense(128, activation='relu'), # Error 3
layers Dropout (0.5),
layers.Dense(10, activation='sigmoid') # Error 4

})

model. compile(optimizer='adam', loss='mean_squared_error’, metrics=['accuracy']) # Error 5
````
