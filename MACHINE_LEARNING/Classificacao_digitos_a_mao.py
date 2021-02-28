# Importa datasets, classificador e métricas de performance 
from sklearn import datasets, svm, metrics

# Dataset dígitos 
digits = datasets.load_digits()

# Para aplicar um classificador nestes dados, precisamos nivelar a imagem, para
 # transformar os dados em uma matriz (amostras, recursos):
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Criando o classificador,  máquina de vetor de suporte 
classifier = svm.SVC(gamma=0.001)

# Aprenda is digitos na primeira metade dos dígitos 
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

# Agora preveja o valor do dígito na segunda metade:
expected = digits.target[n_samples // 2:]
predicted = classifier.predict(data[n_samples // 2:])

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
