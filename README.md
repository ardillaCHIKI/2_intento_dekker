# 2_intento_dekker
# 2_intento_dekker

Este proyecto implementa una simulación del algoritmo de exclusión mutua de Dekker utilizando Python y la biblioteca `curses` para la interfaz de texto. El objetivo es ilustrar cómo dos procesos pueden compartir una sección crítica sin interferencias, evitando condiciones de carrera.

## ¿Qué hace el código?

El programa simula dos procesos (hilos) que intentan acceder a una sección crítica. Cada proceso imprime un carácter diferente en su propia ventana de la terminal:

- El **proceso 1** imprime el carácter `+`.
- El **proceso 2** imprime el carácter `*`.

Ambos procesos utilizan variables compartidas para coordinar el acceso a la sección crítica, siguiendo una variante del algoritmo de Dekker.

## ¿Cómo funciona?

- Se crean dos ventanas laterales usando `curses`, una para cada proceso.
- Cada proceso ejecuta un bucle donde:
  - Indica que quiere entrar a la sección crítica.
  - Espera si el otro proceso también quiere entrar.
  - Si puede, entra a la sección crítica y escribe su carácter.
  - Sale de la sección crítica y repite el ciclo.
- El usuario puede finalizar la simulación presionando `[Enter]`.

## Variables principales

- `proceso1_puede_entrar` y `proceso2_puede_entrar`: Indican si cada proceso desea entrar a la sección crítica.
- `cancelar`: Permite terminar ambos procesos cuando el usuario lo solicita.

## Ejecución

Para ejecutar el programa:

```sh
python3 [main.py](http://_vscodecontentref_/0)