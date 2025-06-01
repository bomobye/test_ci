# app/main.py

def add(a, b):
    """İki sayıyı toplar."""
    return a + b


def subtract(a, b):
    """İki sayıdan birini çıkarır."""
    return a - b


if __name__ == "__main__":
    print("Toplam:", add(3, 4))
    print("Fark:", subtract(10, 5))
