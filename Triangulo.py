import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Triangulo", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glClearColor(0.0, 0.0, 0.0, 1.0)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        #CORPO
        glColor3f(0.7, 0.7, 0.7)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.5, -0.8)
        glVertex2f(0.5, -0.8)
        glVertex2f(0.0, -0.1)
        glEnd()

        #CABEÇA
        glColor3f(0.85, 0.85, 0.85)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.2, -0.1)
        glVertex2f(0.2, -0.1)
        glVertex2f(0.0, 0.3)
        glEnd()

        #ORELHA ESQUERDA
        glColor3f(1.0, 0.8, 0.8)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.2, 0.3)
        glVertex2f(-0.05, 0.3)
        glVertex2f(-0.15, 0.7)
        glEnd()

        #ORELHA DIREITA
        glBegin(GL_TRIANGLES)
        glVertex2f(0.2, 0.3)
        glVertex2f(0.05, 0.3)
        glVertex2f(0.15, 0.7)
        glEnd()

        #OLHO ESQUERDO
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(0.05, 0.1)
        glVertex2f(0.05, 0.05)

        glVertex2f(0.1, 0.05)
        glVertex2f(0.1, 0.1)     

        glEnd()

        #OLHO DIREITO
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(-0.05, 0.1)
        glVertex2f(-0.05, 0.05)

        glVertex2f(-0.1, 0.05)
        glVertex2f(-0.1, 0.1)     

        glEnd()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

main()