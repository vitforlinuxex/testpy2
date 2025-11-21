import cv2
import numpy as np
import mss
import time

def record_screen(duration=5, output_filename='output.avi', fps=20.0):
    with mss.mss() as sct:
        # Prendi le dimensioni dello schermo
        monitor = sct.monitors[1]  # monitor[0] è un placeholder, monitor[1] è lo schermo principale
        width = monitor['width']
        height = monitor['height']

        # Definisci il codec e crea il VideoWriter
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

        start_time = time.time()
        while True:
            # Cattura lo schermo
            img = sct.grab(monitor)
            # Converti l'immagine in un array numpy, e da BGRA a BGR
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

            # Scrivi il frame nel file video
            out.write(frame)

            # Controlla la durata
            if time.time() - start_time > duration:
                break

        out.release()
        print(f"Video salvato come {output_filename}")

if __name__ == "__main__":
    record_screen()