import tkinter as tk

#window
wind = tk.Tk()
#CRETE TITLE
wind.title('Calculator')
#background
wind.config(bg='lavender')
#size
wind.geometry('400x500')
wind.resizable(False,False)
#titre
titre = tk.Label(wind,text='Your Calculator',font=('Arial'),fg='white',bg='purple')
titre.place(x=0,y=0,width=400,height=50)
#input box
input_box = tk.Entry(wind, bd = 1,bg ='white',font=('Aril'))
input_box.place(x=50,y=60,width=300,height=30)
#functions
def button_click(btn_num):
    current_num = input_box.get()
    input_box.delete(0,tk.END)
    input_box.insert(0,str(current_num) + str(btn_num)  )


#clear_button
def button_clear():
    input_box.delete(0,tk.END)
    

    
# ADD FUNCTION
def sum_numbers():
    first_str_num = input_box.get()
    
    global first_num
    global op
    
    first_num = float(first_str_num)
    op = "+"
    input_box.delete(0,tk.END)

    
#SUBTRACT FUN
def subtract_numbers():
    
    global first_num
    global op
    first_str_num = input_box.get()
   
    first_num = float(first_str_num)
    
    op = "-"
    
    input_box.delete(0,tk.END)

    
#Mult button
def multiply_numbers():
    
    global first_num
    global op
    first_str_num = input_box.get()
    
    
    first_num = float(first_str_num)
    
    op = "x"
    
    input_box.delete(0,tk.END)
#devide_butt
def divide_numbers():
    global first_num
    global op
    first_str_num = input_box.get()
    first_num = float(first_str_num)
    op = "/"
    input_box.delete(0,tk.END)


    
#EQ FUNCTION
def equ_butt():
    second_num = input_box.get()
    input_box.delete(0,tk.END)

    if op == "+":
        input_box.insert(0,first_num + float(second_num))
    if op == "-":
        input_box.insert(0,first_num - float(second_num))
    if op == "x":
        input_box.insert(0,first_num * float(second_num))
    if op == "/":
        try:
            input_box.delete(0, tk.END)  # Efface le contenu de la boîte
            input_box.insert(0, first_num / float(second_num))
        except ZeroDivisionError:
            wind.title("Erreur : Division par zéro")


     
        
    
 
    

#define buttons
#Button 1
button1 =tk.Button(wind, text='1',bg ='white',font=('Aril'),bd=1, command = lambda: button_click(1))
button1.place(x=0,y=100,width=100,height=100)
#button 2
button2 =tk.Button(wind, text='2',bg ='white',font=('Aril'),bd=1, command = lambda: button_click(2))
button2.place(x=100,y=100,width=100,height=100)
#button 3
button3 =tk.Button(wind, text='3',bg ='white',font=('Aril'),bd=1, command = lambda: button_click(3))
button3.place(x=200,y=100,width=100,height=100)
#button 4
button4 =tk.Button(wind, text='4',bg ='white',font=('Aril'),bd=1, command = lambda: button_click(4))
button4.place(x=0,y=200,width=100,height=100)
#button 5
button5 =tk.Button(wind, text='5',bg ='white',font=('Aril'),bd=1, command = lambda: button_click(5))
button5.place(x=100,y=200,width=100,height=100)
#button 6
button6 =tk.Button(wind, text='6',bg ='white',font=('Aril'),bd=1, command = lambda: button_click(6))
button6.place(x=200,y=200,width=100,height=100)
#button 7
button7 =tk.Button(wind, text='7',bg ='white',font=('Aril'),bd=1, command = lambda: button_click(7))
button7.place(x=0,y=300,width=100,height=100)
#button 8
button8 =tk.Button(wind, text='8',bg ='white',font=('Aril'),bd=1, command = lambda: button_click(8))
button8.place(x=100,y=300,width=100,height=100)
#button 9
button9 =tk.Button(wind, text='9',bg ='white',font=('Aril'),bd=1, command = lambda: button_click(9))
button9.place(x=200,y=300,width=100,height=100)
#Button_add
button_add = tk.Button(wind,text = '+',bd = 1, bg = 'white', font = 'Arial',command =sum_numbers)
button_add.place(x=300,y=100,width=100,height=100)
#Button_subtract
button_subtract = tk.Button(wind,text = '-',bd = 1, bg = 'white', font = 'Arial',command =subtract_numbers)
button_subtract.place(x=300,y=200,width=100,height=100)
#Button_multiply
button_multiply = tk.Button(wind,text = 'x',bd = 1, bg = 'white', font = 'Arial',command =multiply_numbers)
button_multiply.place(x=300,y=300,width=100,height=100)
#Button_division
button_division = tk.Button(wind,text = '/',bd = 1, bg = 'white', font = 'Arial',command =divide_numbers)
button_division.place(x=300,y=400,width=100,height=100)
#Button_equ
button_equ = tk.Button(wind,text = '=',bd = 1, bg = 'white', font = 'Arial', command =equ_butt)
button_equ.place(x=200,y=400,width=100,height=100)
#Button 0
button_0 = tk.Button(wind,text = '0',bd = 1, bg = 'white', font = 'Arial', command = lambda: button_click(0))
button_0.place(x=100,y=400,width=100,height=100)

#Button_clear
button_clear = tk.Button(wind,text = 'C',bd = 1, bg = 'white', font = 'Arial', command =button_clear)
button_clear.place(x=0,y=400,width=100,height=100)


#affichege
wind.mainloop()
