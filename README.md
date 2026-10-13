# Neural Networks: Zero to Hero

Ejercicios del curso de Andrej Karpathy:
[playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) ·
[notebooks oficiales](https://github.com/karpathy/nn-zero-to-hero)

## Uso

```bash
uv run jupyter lab                 # abrir notebooks
uv run python verificar_entorno.py # comprobar que todo funciona
uv add <paquete>                   # instalar algo nuevo
```

En VS Code: abre la carpeta y elige el intérprete `.venv`.

## Lecciones

| Carpeta | Video |
|---|---|
| `01_micrograd` | Intro a redes neuronales y backpropagation: construyendo micrograd |
| `02_makemore_bigramas` | Intro a modelado de lenguaje: makemore |
| `03_makemore_mlp` | makemore parte 2: MLP |
| `04_makemore_activaciones_batchnorm` | makemore parte 3: activaciones, gradientes y BatchNorm |
| `05_makemore_backprop_ninja` | makemore parte 4: backprop a mano |
| `06_makemore_wavenet` | makemore parte 5: WaveNet |
| `07_gpt` | Construyamos GPT desde cero |
| `08_tokenizer` | Construyamos el tokenizer de GPT |

`data/` tiene `names.txt` (makemore) y `tinyshakespeare.txt` (GPT).

## Método por lección

1. **Primera pasada:** ver el video escribiendo el código a la par (sin copiar y pegar).
2. **Segunda pasada:** uno o dos días después, reescribirlo desde cero sin mirar el video.
3. Revisar con Claude y comparar los gradientes con PyTorch.
