from Tkinter import Frame, Label, CENTER
import FinalLogic
import constants as c

class Game2048(Frame):
    def __init__(self):
        #frame is created on the self object
        Frame.__init__(self)
    #tkinter has grid manager which allows
    #us to create all the objects in the form of grid
        self.grid()
    #everything in the frame has masterclass
    #when we write master.title our master gets a title
        self.master.title("2048")
    #when our focus in on master and when the key
    #event is happening then the corresponding function is called
        self.master.bind("<Key>",self.key_down)
    #setting map of key functions corresponding to keys
        self.commands={
            c.KEY_UP:FinalLogic.move_up,
            c.KEY_DOWN:FinalLogic.move_down,
            c.KEY_LEFT:FinalLogic.move_left,
            c.KEY_RIGHT:FinalLogic.move_right
        }
    #creating the grid cells
        self.grid_cells=[]
    #it will add the grid cells
        self.init_grid()
    #init matrix startsthegame by creating matrix and 
    #adds 2 2's to the matrix
        self.init_matrix()
    #it changes the UI (sets the color according to the numbers)
        self.update_grid_cells()
    #it actually runs the program 
        self.mainloop()
    def init_matrix(self):
        self.matrix=FinalLogic.start_game()
        FinalLogic.add_new_2(self.matrix)
        FinalLogic.add_new_2(self.matrix)

    
    def init_grid(self):
        #inside the grid creating another frame of size 400 X 400
        #now this acts as backgroud
        background=Frame(self,bg=c.BACKGROUND_COLOR_GAME,width=c.SIZE,height=c.SIZE)
        background.grid()
        #adding the cells in this grid
        for i in range(c.GRID_LEN):
            grid_row=[]
            for j in range(c.GRID_LEN):
                cell=Frame(background,bg=c.BACKGROUND_COLOR_CELL_EMPTY,width=c.SIZE/c.GRID_LEN,height=c.SIZE/c.GRID_LEN)
                cell.grid(row=i,column=j,padx=c.GRID_PADDING,pady=c.GRID_PADDING)
                #label covers the cell cells won't be changed but the label will be changed(lable color and text is cahnged)
                t=Label(master=cell,text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY,justify=CENTER,font=c.FONT,width=5,height=2)
                t.grid()

                grid_row.append(t)
            self.grid_cells.append(grid_row)
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks()
    def key_down(self,event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix,changed=self.commands[repr(event.char)](self.matrix)
            if changed:
                FinalLogic.add_new_2(self.matrix)
                self.update_grid_cells()
                changed=False
                if FinalLogic.get_current_state(self.matrix)=="WON":
                    self.grid_cells[1][1].configure(text="You",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if FinalLogic.get_current_state(self.matrix)=="LOST":
                    self.grid_cells[1][1].configure(text="You",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
garegrid=Game2048()