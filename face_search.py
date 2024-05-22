import cv2

def detect_faces(image_path):
    # Загрузка каскада Хаара для обнаружения лиц
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Загрузка изображения
    img = cv2.imread(image_path)
    # Преобразование изображения в черно-белое
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Обнаружение лиц
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Рисование прямоугольников вокруг лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Отображение результата
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

# Путь к вашему изображению
image_path = 'path/to/your/image.jpg'
detect_faces(image_path)