import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

# Настройки игры
ON = 255  # Живая клетка
OFF = 0  # Мертвая клетка
vals = [ON, OFF]

def randomGrid(N):
    """Возвращает сетку NxN случайных значений."""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def update(frameNum, img, grid, N):
    # копируем сетку
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Считаем количество живых соседей
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
            # Применяем правила "Жизни"
            if grid[i, j]  == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    # обновляем данные
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# Настройка визуализации
def main():
    # Размер сетки
    N = 100
    # Создаем сетку
    grid = randomGrid(N)
    # Интервал обновления в миллисекундах
    updateInterval = 50
    # Настройка анимации
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
                                  frames=10,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()

# Запускаем игру
if __name__ == '__main__':
    main()
