def fingers_open(handlms, img_shape):
    h, w, _ = img_shape
    tip_ids = [4, 8, 12, 16, 20]
    pip_ids = [3, 6, 10, 14, 18]

    open_fingers = 0

    # Thumb (x-axis)
    if handlms.landmark[tip_ids[0]].x > handlms.landmark[pip_ids[0]].x:
        open_fingers += 1

    # Other fingers (y-axis)
    for i in range(1, 5):
        if handlms.landmark[tip_ids[i]].y < handlms.landmark[pip_ids[i]].y:
            open_fingers += 1

    return open_fingers
