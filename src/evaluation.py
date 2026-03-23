from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def plot_confusion(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)

    sns.heatmap(cm, annot=True, fmt="d")
    plt.title("Confusion Matrix")
    plt.savefig("results/confusion_matrix.png")
    plt.close()


# Example test
if __name__ == "__main__":
    y_true = [0, 0, 1, 1]
    y_pred = [0, 1, 1, 1]

    plot_confusion(y_true, y_pred)
