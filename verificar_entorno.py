"""Comprueba que el entorno del curso está listo: uv run python verificar_entorno.py"""
import shutil
import sys
from pathlib import Path

import matplotlib
import numpy as np
import tiktoken
import torch

print(f"Python      {sys.version.split()[0]}")
print(f"PyTorch     {torch.__version__} (CUDA disponible: {torch.cuda.is_available()})")
print(f"NumPy       {np.__version__}")
print(f"Matplotlib  {matplotlib.__version__}")
print(f"tiktoken    {tiktoken.__version__}")

# Graphviz necesita el programa `dot` del sistema para dibujar el grafo de micrograd
if shutil.which("dot"):
    print("Graphviz    OK")
else:
    print("Graphviz    FALTA el binario `dot` -> sudo apt install graphviz")

# Prueba rápida de autograd: d/dx (x^2 + 3x) en x=2 debe ser 7
x = torch.tensor(2.0, requires_grad=True)
(x**2 + 3 * x).backward()
assert x.grad.item() == 7.0
print("Autograd    OK")

for f in ["names.txt", "tinyshakespeare.txt"]:
    p = Path(__file__).parent / "data" / f
    print(f"data/{f:<20} {'OK' if p.exists() else 'FALTA'}")
