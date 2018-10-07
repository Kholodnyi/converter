from tkinter import *
from tkinter import ttk

def convert_n_to_m():
    
    x = input_number.get()
    str_n = input_n.get()
    str_m = input_m.get()
 
    # converting input in a list of symbols and check for empty
    string_x = str(x)
    list_x = []
    for item in string_x:
        if item == ' ':
            continue
        list_x.append(item.upper()) # transforming all letters to uppercase 
    if list_x == []:
        answer_number.configure(text = "put a number!", foreground='#f00')
        return False

    # check for wrong range of n and m
    try:
        m = int(str_m)
        n = int(str_n)
        if not 2 <= n <= 36 or not 2 <= m <= 36:
            answer_number.configure(text = "num sys should be in range from 2 to 36", foreground='#f00')
            return False
    except:
        answer_number.configure(text = "num sys should be in range from 2 to 36", foreground='#f00')
        return False

    # checklist creating
    checklist = []
    for item in range(n): 
        checklist.append(dictionary[item])
    
    # checking for the presence of input symbols in checklist
    for item in list_x:
        if item not in checklist:
            answer_number.configure(text = "invalid number", foreground='#f00')
            return False
    
    # convert from n to 10
    converted_to_10 = 0	
    i = len(list_x) - 1
    for item in list_x:
        converted_to_10 += dictionary_reverse[item]*n**i
        i -= 1
    
    # convert from 10 to m
    reversed_num_list = []

    while True:
        if converted_to_10 < m:
            reversed_num_list.append(converted_to_10)
            break
        reversed_num_list.append(converted_to_10%m)
        converted_to_10 //= m
    
    num_list = reversed_num_list[::-1]

    lettercase = var.get()

    answer = ''
    for item in num_list:
        if lettercase == 1:
            answer += dictionary[item]
        else:
            answer += dictionary[item].lower()
    answer_number.configure(text=answer, foreground='#000')

    h = len(answer)//60 + 1
    if h >= 11:
        h = 10	
        #answer_label.configure(relief='solid')
        answer_number.configure(background='#fcc')
    else:
        answer_number.configure(background='#f0f0f0')
    answer_number.configure(text=answer, foreground='#000', height=h)
    #answer_label.configure(relief='groove')

def copy_to_clipboard():
    answer = answer_number.cget("text") 
    window.clipboard_clear()
    window.clipboard_append(answer)

def clear_entry():
    input_number.delete(0, 'end')


window=Tk()
window.title("Number converter")

dictionary = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 
              10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I',
              19:'J', 20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 25:'P', 26:'Q', 27:'R',
              28:'S', 29:'T', 30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}

# dictionary reversing           
dictionary_reverse = dict(zip(dict.values(dictionary), dict.keys(dictionary)))

var = IntVar()
var.set(1)

x=4
y=4
text = 'dsfg'
# s = 'you can use a lowercase and uppercase letters'

# row 0 - description
lable_frame1 = Frame(window)
lable_frame1.grid(row=0, column=0, columnspan=6, sticky='WE')
lable_frame1.columnconfigure(1, weight=1)

label_number = Label(lable_frame1, text='Put you number for convertation:')
label_number.grid(row=0, column=0, sticky='W', columnspan=6, padx=8, pady=(8, y))

b1 = Button(lable_frame1, text='clear entry', command=clear_entry)
b1.grid(row=0, column=1, sticky='E', padx=8, pady=(8, y), ipadx=10)
# ---

# row 1 - input number
input_number = Entry(window) # , bg='#f00'
input_number.grid(row=1, column=0, columnspan=6, sticky='WE', padx=8, pady=y)
# input_number.insert(0, s)
# ---

# row 2 - input number sys and convert button
inputs_frame = Frame(window)
inputs_frame.grid(row=2, column=0, columnspan=6, sticky='WE')
inputs_frame.columnconfigure(7, weight=1)

label_ns1 = Label(inputs_frame, text='from', width=4)
label_ns1.grid(row=0, column=0, sticky='W', padx=(8, 2), pady=y)
	
input_n = Entry(inputs_frame, width=3)
input_n.grid(row=0, column=1, sticky='W', padx=2, pady=y)

label_ns2 = Label(inputs_frame, text='to', width=2)
label_ns2.grid(row=0, column=2, sticky='W', padx=2, pady=y)

input_m = Entry(inputs_frame, width=3)
input_m.grid(row=0, column=3, sticky='W', padx=2, pady=y)

label_ns3 = Label(inputs_frame, text='numeral system', width=13)
label_ns3.grid(row=0, column=4, sticky='W', padx=2, pady=y)

b2 = Button(inputs_frame, text='convert', command=convert_n_to_m) 
b2.grid(row=0, column=7, sticky='E', padx=(4, 8), pady=y, ipadx=10)

Radiobutton(inputs_frame, text = "A", variable=var, value = 1).grid(row=0, column=5, sticky='W')
Radiobutton(inputs_frame, text = "a", variable=var, value = 2).grid(row=0, column=6, sticky='W')

# ---

# row 3 - answer and copy to clipboard button 
answer_label = LabelFrame(window, text="converted number is:")
answer_label.grid(row=3, column=0, sticky='WE', columnspan=6, padx=1.8*x, pady=y, ipadx=4, ipady=4) 
answer_label.columnconfigure(0, weight=1)

answer_number = Label(answer_label, text=' ', wraplength=360, height=1)
answer_number.grid(row=0, column=0, sticky='WE')


# ---

# row 4 - footer
footer = Frame(window)
footer.grid(row=4, column=0, columnspan=6, sticky='WE')

footer.columnconfigure(1, minsize=250)

about = Label(footer, text='2018 \xa9 YKh')
about.grid(row=0, column=0, sticky='W', padx=(8, x), pady=(y, 8))

b3 = Button(footer, text='copy to clipboard', command=copy_to_clipboard) #, image=button_quit_image
b3.grid(row=0, column=1, sticky='E', padx=x, pady=(y, 8), ipadx=10)

b0 = Button(footer, text='exit', command=window.quit) #, image=button_quit_image
b0.grid(row=0, column=2, sticky='E', padx=(x, 8), pady=(y, 8), ipadx=10)
# ---


window.resizable(width = False, height = False)
window.mainloop()
