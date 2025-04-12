
from enum import Enum


class ModelEvaluationMetric(str, Enum):
    auc = 'AUC'
    accuracy = 'Accuracy'
    f1 = 'F1'
    recall = 'Recall'
    precision = 'Precision'
