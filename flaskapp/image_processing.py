import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg (non-GUI)

from PIL import Image, ImageEnhance
import numpy as np
import matplotlib.pyplot as plt

def process_image(image_path, contrast_level):
    image = Image.open(image_path)

    enhancer = ImageEnhance.Contrast(image)
    processed_image = enhancer.enhance(contrast_level)

    processed_image_path = 'static/processed_image.jpg'
    processed_image.save(processed_image_path)

    # График распределения цветов исходной картинки
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.hist(np.array(image).ravel(), bins=256, color='r', alpha=0.5)
    plt.title('Original Image')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')

    # График распределения цветов обработанной картинки
    plt.subplot(1, 2, 2)
    plt.hist(np.array(processed_image).ravel(), bins=256, color='b', alpha=0.5)
    plt.title('Processed Image')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')

    plt.savefig('static/histograms.jpg')  # Сохраняем графики в файл
    plt.close()  # Закрываем текущее изображение, чтобы не засорять память

    return 'static/histograms.jpg'
