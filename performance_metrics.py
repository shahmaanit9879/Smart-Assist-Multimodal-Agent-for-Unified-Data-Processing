# performance_metrics.py

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import time

def measure_classification_metrics(true_labels, predicted_labels):
    return {
        "accuracy": accuracy_score(true_labels, predicted_labels),
        "precision": precision_score(true_labels, predicted_labels, average='weighted'),
        "recall": recall_score(true_labels, predicted_labels, average='weighted'),
        "f1_score": f1_score(true_labels, predicted_labels, average='weighted')
    }

def measure_latency(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start

def cross_modal_consistency(text_output, image_output, audio_output):
    return text_output in image_output or text_output in audio_output