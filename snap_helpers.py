import subprocess

def snap_window(position):
    def get_active_window():
        try:
            return subprocess.check_output(["xdotool", "getactivewindow"]).strip().decode()
        except:
            return None

    def get_screen_size():
        output = subprocess.check_output("xdpyinfo | grep dimensions", shell=True).decode()
        dims = output.strip().split()[1].split("x")
        return int(dims[0]), int(dims[1])

    def move_window(win_id, x, y, width, height):
        geo_str = f"0,{x},{y},{width},{height}"
        subprocess.call(["wmctrl", "-ir", win_id, "-e", geo_str])

    win_id = get_active_window()
    if win_id:
        w, h = get_screen_size()
        if position == "top":
            move_window(win_id, 0, 0, w, h // 2)
        elif position == "bottom":
            move_window(win_id, 0, h // 2, w, h // 2)
        elif position == "left":
            move_window(win_id, 0, 0, w // 2, h)
        elif position == "right":
            move_window(win_id, w // 2, 0, w // 2, h)
