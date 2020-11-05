from tkinter import *

root =Tk()
root.state("zoomed")

#Creating main frame
fram_tope = Frame(root, bg= "#243239", height= 40 )
frame_center = Frame(root, bg = "white")
frame_bottom = Frame(root, bg ="#243239",height=20)

#creating body frame with color
frame_center_right = Frame(frame_center,  bg="white")
frame_center_left = Frame(frame_center,  bg="red", width= 100)
#creating body frame without color
# frame_center_right = Frame(frame_center)
# frame_center_left = Frame(frame_center, width= 100)

#creating top frame for the buttons with color
#frame_tope_btn1 = Frame(fram_tope, bg="blue", height= 20)
#frame_tope_btn2 = Frame(fram_tope, bg="green", height= 20)
#frame_tope_btn3 = Frame(fram_tope, bg="brown", height= 20)
#creating top frame for buttons without color
frame_tope_btn1 = Frame(fram_tope, height= 20, bg= "#243239")
frame_tope_btn2 = Frame(fram_tope, height= 20, bg= "#243239")
frame_tope_btn3 = Frame(fram_tope, height= 20, bg= "#243239")

#creating center left frame for buttons with color
# frame_center_left_btn4 = Frame(frame_center_left, width= 100, bg= "blue")
# frame_center_left_btn5 = Frame(frame_center_left, width= 100, bg= "red")
# frame_center_left_btn6 = Frame(frame_center_left, width= 100, bg= "yellow")
#creating top frame for buttons without color
frame_center_left_btn4 = Frame(frame_center_left, width= 100, bg= "black")
frame_center_left_btn5 = Frame(frame_center_left, width= 100, bg= "black")
frame_center_left_btn6 = Frame(frame_center_left, width= 100, bg= "black")

#creating bottom frame for the buttons with color
# frame_bottom_btn7 = Frame(frame_bottom, bg="blue", height= 20)
# frame_bottom_btn8 = Frame(frame_bottom, bg="green", height= 20)
# frame_bottom_btn9 = Frame(frame_bottom, bg="brown", height= 20)
#creating bottomframe for buttons without color
frame_bottom_btn7 = Frame(frame_bottom, height= 20, bg= "#243239")
frame_bottom_btn8 = Frame(frame_bottom, height= 20, bg= "#243239")
frame_bottom_btn9 = Frame(frame_bottom, height= 20, bg= "#243239")

#creating button for top frame
btn1 = Button(frame_tope_btn1, text="button01")
btn2 = Button(frame_tope_btn2, text="button02")
btn3 = Button(frame_tope_btn3, text="button03")

#creating button for left center frame
btn4 = Button(frame_center_left_btn4, text="button04")
btn5 = Button(frame_center_left_btn5, text="button05")
btn6 = Button(frame_center_left_btn6, text="button06")

#creating button for botton frame
btn7 = Button(frame_bottom_btn7, text="button07")
btn8 = Button(frame_bottom_btn8, text="button08")
btn9 = Button(frame_bottom_btn9, text="button09")

#Packing main the frame
fram_tope.pack(side=TOP, fill=X)
frame_center.pack(side=TOP, fill=BOTH, expand=TRUE)
frame_bottom.pack(side=TOP, fill=X)

#Packing body the frame
frame_center_left.pack(side=LEFT, fill=BOTH)
frame_center_right.pack(side=LEFT, fill=BOTH, expand=TRUE)

#Packing top frame for the buttons
frame_tope_btn1.pack(side=LEFT, fill=BOTH, expand=TRUE)
frame_tope_btn2.pack(side=LEFT, fill=BOTH, expand=TRUE)
frame_tope_btn3.pack(side=LEFT, fill=BOTH, expand=TRUE)

#Packing center left the frame for the buttons
frame_center_left_btn4.pack(side=TOP, fill=BOTH, expand=TRUE)
frame_center_left_btn5.pack(side=TOP, fill=BOTH, expand=TRUE)
frame_center_left_btn6.pack(side=TOP, fill=BOTH, expand=TRUE)

#Packing bottom frame for the buttons
frame_bottom_btn7.pack(side=LEFT, fill=BOTH, expand=TRUE)
frame_bottom_btn8.pack(side=LEFT, fill=BOTH, expand=TRUE)
frame_bottom_btn9.pack(side=LEFT, fill=BOTH, expand=TRUE)

#Packing button for top frame
btn1.pack()
btn2.pack()
btn3.pack()

#Packing button for certer left frame
btn4.pack()
btn5.pack()
btn6.pack()

#Packing button for bottom frame
btn7.pack()
btn8.pack()
btn9.pack()

root.mainloop()