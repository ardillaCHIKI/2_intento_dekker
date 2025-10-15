import curses
import threading
import time

proceso1_puede_entrar = False
proceso2_puede_entrar = False
cancelar = False

def retardar_unos_milisegundos(velocidad):
    for _ in range(velocidad):
        if cancelar:
            break
        for _ in range(velocidad):
            if cancelar:
                break

def ejecutar_seccion_critica_1(winA):
    winA.addstr("+")
    winA.refresh()
    retardar_unos_milisegundos(150)

def ejecutar_seccion_critica_2(winB):
    winB.addstr("*")
    winB.refresh()
    retardar_unos_milisegundos(50)

def proceso1(winA):
    global proceso1_puede_entrar, proceso2_puede_entrar, cancelar
    while not cancelar:
        proceso1_puede_entrar = True
        while proceso2_puede_entrar and not cancelar:
            pass
        if cancelar:
            break
        ejecutar_seccion_critica_1(winA)
        proceso1_puede_entrar = False
    winA.addstr("Ha terminado el proceso 1\n")
    winA.refresh()

def proceso2(winB):
    global proceso1_puede_entrar, proceso2_puede_entrar, cancelar
    while not cancelar:
        proceso2_puede_entrar = True
        while proceso1_puede_entrar and not cancelar:
            pass
        if cancelar:
            break
        ejecutar_seccion_critica_2(winB)
        proceso2_puede_entrar = False
    winB.addstr("Ha terminado el proceso 2\n")
    winB.refresh()

def main(stdscr):
    global cancelar, proceso1_puede_entrar, proceso2_puede_entrar

    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    h, w = stdscr.getmaxyx()

    winA = curses.newwin(h - 2, (w // 2) - 1, 1, 0)
    winB = curses.newwin(h - 2, (w // 2) - 1, 1, (w // 2))
    winTop = curses.newwin(1, w, 0, 0)
    winBottom = curses.newwin(1, w, h - 1, 0)

    titulo = "=== Dekker II ==="
    winTop.addstr(0, (w // 2) - len(titulo) // 2, titulo)
    winTop.refresh()

    cancelar = False
    proceso1_puede_entrar = False
    proceso2_puede_entrar = False

    t1 = threading.Thread(target=proceso1, args=(winA,))
    t2 = threading.Thread(target=proceso2, args=(winB,))
    t1.start()
    t2.start()

    winBottom.addstr(0, 0, "Presione la tecla [Enter] para salir.")
    winBottom.refresh()
    stdscr.getch()
    cancelar = True

    t1.join()
    t2.join()

    time.sleep(0.5)  # Espera para mostrar los mensajes finales

if __name__ == "__main__":
    curses.wrapper(main)