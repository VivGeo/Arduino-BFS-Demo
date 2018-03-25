from firebase import firebase


import tkinter as tk
#import Tkinter as Tk





end = 1
start = -1
last = -1
counter = -1

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

graph = {0: set([1, 4]),
         1: set([0, 2, 5]),
         2: set([1, 3, 6]),
         3: set([2, 7]),
         4: set([0, 5, 8]),
         5: set([1, 4, 6, 9]),
         6: set([2, 5, 7, 10]),
         7: set([3, 6, 11]),
         8: set([4, 9]),
         9: set([5, 8, 10]),
         10: set([6, 9, 11]),
         11: set([7, 10])}




def onClick(x):
    global win, start, last, end
    if (end == 0):
        last = x
        win.destroy()
    else:
        start = x
        end-=1
    return

def start():
    buttons = []
    global win
    win = tk.Tk()
    for i in range(3):
        for j in range (4):

            b = tk.Button(win, text=i*4+1+j,height=1, width=25, command=lambda i=i, j=j: onClick(i*4+j)).grid(row=i, column=j)
        buttons.append(b)

start()
win.mainloop()

print(start)
print(last)
path = shortest_path(graph, start, last)
length = len(path)

firebase = firebase.FirebaseApplication(firebaseURL, None)
firebase.put('/', 'step', 0)
firebase.put('/', 'step0', -1)
firebase.put('/', 'step1', -1)
firebase.put('/', 'step2', -1)
firebase.put('/', 'step3', -1)
firebase.put('/', 'step4', -1)
firebase.put('/', 'step5', -2)


if (length >= 1):
    firebase.put('/', 'step0', path[0])
if (length >= 2):
    firebase.put('/', 'step1', path[1])
if (length >= 3):
    firebase.put('/', 'step2', path[2])
if (length >= 4):
    firebase.put('/', 'step3', path[3])
if (length >= 5):
    firebase.put('/', 'step4', path[4])
if (length >= 6):
    firebase.put('/', 'step5', path[5])

output = firebase.get('/', None)
print(output)
