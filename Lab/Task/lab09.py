from tkinter import *

root =Tk()
root.state("zoomed")

#Creating main frame
fram_top = Frame(root, bg= "#243239", height= 30 )
fram_center = Frame(root, bg = "white",)
fram_bottom = Frame(root, bg ="#243239",height=20)

#creating body frame
fram_center_right = Frame(fram_center,  bg="black")
fram_center_left = Frame(fram_center,  bg="red", width= 100)


#Packing main the frame
fram_top.pack(side=TOP, fill=X)
fram_center.pack(side=TOP, fill=BOTH, expand=TRUE)
fram_bottom.pack(side=TOP, fill=X)

#Packing body the frame
fram_center_left.pack(side=LEFT, fill=BOTH)
fram_center_right.pack(side=LEFT, fill=BOTH, expand=TRUE)
root.mainloop()