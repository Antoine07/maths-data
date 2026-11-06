"""Extension facultative : comparer NumPy et autograd, sans nouvel entraînement."""
import numpy as np
import torch
from correction import initialiser_reseau, reseau_cout_gradients

X = np.array([[.1, .3], [-.4, .2], [.2, -.1]])
y = np.array([0., 1., 1.])
parametres = initialiser_reseau(2)
cout, gradients = reseau_cout_gradients(X, y, parametres)
xt = torch.tensor(X, dtype=torch.float64)
yt = torch.tensor(y, dtype=torch.float64)
w1, b1, w2, b2 = [torch.tensor(p, dtype=torch.float64, requires_grad=True) for p in parametres]
logits = (torch.tanh(xt @ w1 + b1) @ w2 + b2).flatten()
perte = torch.nn.functional.binary_cross_entropy_with_logits(logits, yt)
perte.backward()
np.testing.assert_allclose(perte.detach().numpy(), cout, atol=1e-12)
for parametre, attendu in zip((w1, b1, w2, b2), gradients):
    np.testing.assert_allclose(parametre.grad.numpy(), attendu, atol=1e-10)
print("NumPy et PyTorch : mêmes pertes et gradients.")
