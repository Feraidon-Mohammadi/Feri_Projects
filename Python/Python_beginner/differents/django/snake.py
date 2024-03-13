import tkinter as tk
root = tk.Tk()

#set size of the window tkinter
window_width = 1080
window_height = 720
root.geometry(f"{window_width}x{window_height}")

#change background color
background_color = "black"
root.configure(bg=background_color)

#add label to  window
#label = tk.Label(root, text="window, hello", bg=background_color)
#label.pack()

# Create a canvas widget to draw on
canvas = tk.Canvas(root, width=window_width, height=window_height, bg=background_color)
canvas.pack()

#################################################################################
#############################snake Head##########################################
snake_size = 15

snakheadx = window_width // 2
snakheady = window_height // 2

x1 = snakheadx - snake_size // 2
y1 = snakheady - snake_size // 2
x2 = snakheadx + snake_size // 2
y2 = snakheady + snake_size // 2

head = canvas.create_rectangle( x1, y1, x2, y2, fill="red", width=0)

#################################################################################
################################# snake body ####################################
'''  
'''
snake_body = []
segment_size = 12
x , y = 50 ,50
for _ in range(3):
    segment = canvas.create_rectangle(x, y, x + segment_size, y + segment_size, fill="green")
    snake_body.append(segment)
    x += segment_size + 1  # Add some spacing between segments

def move_snak(dx, dy):
    canvas.move(head, dx, dy)










move_snak(segment_size + 1, 0)





































#run loop tkinter
root.mainloop()