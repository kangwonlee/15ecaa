# -*- coding: utf8 -*-
import Tkinter as tk
import math

# ref : http://effbot.org/tkinterbook/canvas.htm

deg2rad = math.pi / 180


class Tkplot(object):
    def __init__(self, x, y):
        """
        Initialize tk plot
        """
        # Tk root
        self.root = tk.Tk()
        self.master = self.root

        # width, height        
        self.w = 400
        self.h = 400
        
        # canvas object : where plots are made
        self.canvas = tk.Canvas(self.master, width = self.w, height = self.h)
        self.canvas.pack()
        
        # data
        self.x = tuple(x)
        self.y = tuple(y)
        
        # plot data
        self.draw_graph()
        
    def line(self, x0, y0, x1, y1):
        self.canvas.create_line(x0, self.h*.5 - y0, x1, self.h*.5 - y1)
        
    def draw_graph(self):
        """
        make plot of x, y data given @ creation
        """
        
        xy = zip(self.x, self.y)
        xy_p = xy[0]
        for xy_i in xy[1:]:
            self.line(xy_p[0], xy_p[1], xy_i[0], xy_i[1])
            xy_p = xy_i
    
    def show(self):
        self.root.mainloop()

        
if "__main__" == __name__:
    # prepare for data to be plotted
    x_deg = range(360 + 1)
    x_rad = [xi_deg * deg2rad for xi_deg in x_deg]
    y = [math.sin(xi_rad) * 100. for xi_rad in x_rad]
        
    # create plot object
    p = Tkplot(x_deg, y)
    
    # run main loop
    p.show()
