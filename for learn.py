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
input_box.place(x=80,y=60,width=300,height=30)
#delete_function
def delete_function():
    current_text = input_box.get()
    input_box.delete(len(current_text)-1, tk.END)
    

#functions
def button_click(btn_num):
    current_text = input_box.get()
    input_box.delete(0,tk.END)
    input_box.insert(0,str(current_text) + str(btn_num)  )
#clear_button
def button_clear():
    input_box.delete(0,tk.END)
    

# ADD FUNCTION
def sum_numbers():
    global op
    current_text = input_box.get()
    input_box.delete(0, tk.END)
    input_box.insert(0, current_text + '+')
    

    
#SUBTRACT FUN
def subtract_numbers():
    global op
    current_text = input_box.get()
    input_box.delete(0, tk.END)
    input_box.insert(0, current_text + '-')
    
#Mult button
def multiply_numbers():
    global op
    current_text = input_box.get()
    input_box.delete(0, tk.END)
    input_box.insert(0, current_text + 'x')
    
    
#devide_butt
def divide_numbers():
    global op
    current_text = input_box.get()
    input_box.delete(0, tk.END)
    input_box.insert(0, current_text + '/')
 
#EQ FUNCTION
def equ_butt():
    current_text = input_box.get()  # Récupère le texte actuel dans le champ de saisie
    
    try:
        result = eval(current_text.replace('x', '*'))  # Remplace 'x' par '*' et évalue l'expression
        input_box.delete(0, tk.END)  # Efface le contenu de la boîte
        input_box.insert(0, str(result))  # Affiche le résultat
    except ZeroDivisionError:
        input_box.delete(0, tk.END)
        input_box.insert(0, "Erreur : Division par zéro")
    except Exception as e:
        input_box.delete(0, tk.END)
        input_box.insert(0, "Erreur")


#define buttons
#delete button
butt_del = tk.Button(wind,text="Delete", bg ='white',bd = 0, command =  delete_function)
butt_del.place(x=4,y=60,width=70,height=30)  
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
