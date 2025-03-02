import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import threading

f = open('./hyperparameter-tuning.ipynb')
nb = nbformat.read(f, as_version=4)
ep = ExecutePreprocessor(kernel_name='python3')
def save_notebook():
    threading.Timer(1.0, save_notebook).start()
    with open('executed_nlp_cw.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
save_notebook()

ep.preprocess(nb)

print('ended')