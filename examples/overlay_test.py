import pymeow as pm

from math import fmod
from time import time


def main():
    overlay = pm.overlay_init()
    font = pm.font_init(20, "Impact")
    radius = 50
    r, g, b = 0.0, 0.3, 0.6
    x, y = overlay["midX"], overlay["midY"]
    speed = 3
    ball_left, ball_down = False, False
    
    frames, fps = 0, 0
    prev_time = time()
    curr_time = None

    while pm.overlay_loop(overlay):
        pm.overlay_update(overlay)
        if pm.key_pressed(35):
            pm.overlay_close(overlay)
        
        curr_time = time()
        frames += 1

        if curr_time - prev_time > 1.0:
            fps = frames
            frames = 0
            prev_time = curr_time
        
        pm.font_print(
            font,
            overlay["midX"] - 100, overlay["midY"],
            f"FPS: {fps}", 
            [b, r, g]
        )

        if ball_left:
            if x > overlay["width"] - radius:
                ball_left = False
            else:
                x += speed
        else:
            if x < -1 + radius:
                ball_left = True
            else:
                x -= speed

        if ball_down:
            if y > overlay["height"] - radius:
                ball_down = False
            else:
                y += speed
        else:
            if y < -1 + radius:
                ball_down = True
            else:
                y -= speed

        r = fmod(r + 0.001, 1)
        g = fmod(g + 0.002, 1)
        b = fmod(b + 0.003, 1)

        pm.circle(
            x=x,
            y=y,
            radius=radius,
            color=[r, g, b],
            filled=True,
        )

if __name__ == "__main__":
    main()
