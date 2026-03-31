import glfw
from OpenGL.GL import *
from OpenGL.GLU import *


def desenha():
    glClear(GL_COLOR_BUFFER_BIT)

    # Cor dos blocos (marrom)
    glColor3f(0.6, 0.3, 0.0)

    x_inicio = 100
    y_inicio = 100
    largura_total = 120
    altura_total = 80

    colunas = 3
    linhas = 2

    largura_bloco = largura_total / colunas
    altura_bloco = altura_total / linhas

    for i in range(colunas):
        for j in range(linhas):
            x = x_inicio + i * largura_bloco
            y = y_inicio + j * altura_bloco

            glBegin(GL_QUADS)
            glVertex2f(x, y)
            glVertex2f(x, y + altura_bloco)
            glVertex2f(x + largura_bloco, y + altura_bloco)
            glVertex2f(x + largura_bloco, y)
            glEnd()

    glColor3f(0.0, 0.0, 0.0)

    for i in range(colunas + 1):
        x = x_inicio + i * largura_bloco
        glBegin(GL_LINES)
        glVertex2f(x, y_inicio)
        glVertex2f(x, y_inicio + altura_total)
        glEnd()

    for j in range(linhas + 1):
        y = y_inicio + j * altura_bloco
        glBegin(GL_LINES)
        glVertex2f(x_inicio, y)
        glVertex2f(x_inicio + largura_total, y)
        glEnd()

def main():
    if not glfw.init():
        print("Erro ao iniciar GLFW")
        return

    window = glfw.create_window(400, 350, "Mistério", None, None)

    if not window:
        glfw.terminate()
        print("Erro ao criar janela")
        return

    glfw.make_context_current(window)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 250, 0, 250)

    while not glfw.window_should_close(window):
        desenha()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

main()
