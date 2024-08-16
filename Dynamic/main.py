from pyscript import document

colors = ["red", "green", "blue"]
current_color_index = 0

def cycle_color(event):
    global current_color_index
    current_color_index = current_color_index + 1
    if current_color_index >= len(colors):
        current_color_index = 0

    document.getElementById("changeable-paragraph").style.color = colors[current_color_index]

def change_text(event):
    document.getElementById("changeable-paragraph").textContent = "Text has been changed!"

def change_font(event):
    document.getElementById("changeable-paragraph").style.fontFamily = "Arial, sans-serif"

def change_text_size(event):
    document.getElementById("changeable-paragraph").style.fontSize = "20px"