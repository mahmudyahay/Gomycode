import numpy as np
from opengrad import Tensor
from opengrad.nn import MLP
from opengrad.optim import Adam

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
Y = np.array([[0], [1], [1], [0]], dtype=float)

model = MLP([2, 8, 1])
opt = Adam(model.parameters(), lr=0.05)

x, y = Tensor(X, requires_grad=False), Tensor(Y, requires_grad=False)

for step in range(300):
    pred = model(x).sigmoid()
    loss = ((pred - y) ** 2).mean()
    opt.zero_grad()
    loss.backward()
    opt.step()

print(model(x).sigmoid().data)  # ~[0, 1, 1, 0]
