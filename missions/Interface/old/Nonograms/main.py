# Game of Life
# @File:   main.py
# @Time:   30/07/2021
# @Author: Gabriel O.

import os
import sys
import tkinter as tk


def parse_click_event(event: tk.Event, canvas: tk.Canvas, width: float, height: float, m_cells: int, n_cells: int):
    """
    Função executada quando qualquer clique é detectado
    :param event: evento do clique
    :param width: largura do canvas
    :param height: altura do canvas
    :param m_cells: numero de elementos na vertical
    :param n_cells: numero de elementos na horizontal
    :return:
    """
    x, y = event.x, event.y
    i = (y * m_cells) // height + 1
    j = (x * n_cells) // width + 1
    if (i, j) not in celulas_pressionadas:
        print(f"Célula pressionada: ({i}, {j})")
        celulas_pressionadas.append((i, j))
        x1 = (j-1) * width / n_cells
        y1 = (i-1) * height / m_cells
        x2 = j * width / n_cells
        y2 = i * height / m_cells
        rectangle = canvas.create_rectangle(x1, y1, x2, y2, width=2)
        rectangles.append(rectangle)
    else:
        print(f"Célula despressionada: ({i}, {j})")
        rectangle_id = celulas_pressionadas.index((i, j))
        celulas_pressionadas.remove((i, j))
        canvas.delete(rectangles[rectangle_id])
        rectangles.pop(rectangle_id)


def main(path, m, n):
    window = tk.Tk()
    window.title('Nonograms')
    m = 9 if m is None else m
    n = 9 if n is None else n
    img_path = f"images/{m}x{n}.png" if path is None else "images/" + path
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Não foi possível encontrar a imagem no caminho fornecido")
    background = tk.PhotoImage(file=img_path)
    bg_width, bg_height = background.width(), background.height()

    # criação dos elementos gráficos
    # canvas para colocar a imagem e detectar cliques
    topo = tk.Canvas(width=bg_width, height=bg_height)
    topo.bind('<Button-1>',
              lambda event, canvas=topo, w_=bg_width, h_=bg_height, m_=m, n_=n:
              parse_click_event(event, canvas, w_, h_, m_, n_))
    topo.create_image(0,0, image=background, anchor='nw')
    topo.pack()
    window.mainloop()


if __name__ == '__main__':
    celulas_pressionadas = []
    rectangles = []
    try:
        caminho = input("Digite o nome do arquivo (com extensao): ")
        linhas = input("Digite a quantidade de linhas: ")
        colunas = input("Digite a quantidade de colunas: ")
        linhas = int(linhas) if linhas else None
        colunas = int(colunas) if colunas else None
        caminho = caminho if caminho else None
        main(caminho, linhas, colunas)
    except IndexError:
        raise Exception("Faltou um argumento")
    except ValueError:
        raise ValueError("Formatacao incorreta dos argumentos")
