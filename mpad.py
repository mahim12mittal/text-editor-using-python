import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser , font , messagebox, filedialog
import os 
main_app =tk.Tk()
main_app.geometry('1200x800')
main_app.title("mahim's text editor")   
main_app.wm_iconbitmap('icon.ico')
main_menu=tk.Menu()
# icon of file
new_icon = tk.PhotoImage(file='icons/new.png')
open_icon = tk.PhotoImage(file='icons/open.png')
save_icon = tk.PhotoImage(file='icons/save.png')
save_as_icon = tk.PhotoImage(file='icons/save_as.png')
exit_icon = tk.PhotoImage(file='icons/exit.png')

files =tk.Menu(main_menu,tearoff=False)

# icon of file
cut_icon = tk.PhotoImage(file='icons/cut.png')
copy_icon = tk.PhotoImage(file='icons/copy.png')
paste_icon = tk.PhotoImage(file='icons/paste.png')
clear_all_icon = tk.PhotoImage(file='icons/clear_all.png')
find_icon = tk.PhotoImage(file='icons/find.png')

edit =tk.Menu(main_menu,tearoff=False)

# icon of file
tool_bar_icon = tk.PhotoImage(file='icons/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons/status_bar.png')

view =tk.Menu(main_menu,tearoff=False)

# icon of color theme
light_default_icon = tk.PhotoImage(file='icons/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons/light_plus.png')
dark_icon = tk.PhotoImage(file='icons/dark.png')
red_icon = tk.PhotoImage(file='icons/red.png')
monokai_icon = tk.PhotoImage(file='icons/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons/night_blue.png')

theme_choice=tk.StringVar()
color_theme =tk.Menu(main_menu,tearoff=False)

color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_dict={
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b744','#474747'),
    'Night Blue':('#ededed','#6b9dc2')
}
# main menu-----------------
main_menu.add_cascade(label="File",menu=files)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Color Theme",menu=color_theme)


# tool bar------------------start

tool_bar=ttk.Label(main_app)
tool_bar.pack(side=tk.TOP,fill=tk.X)
#font box
font_tuples=tk.font.families()
font_var = tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_var,state='readonly')
font_box['values']=font_tuples
font_box.current(font_tuples.index('Arial'))
font_box.grid(row=0,column=0,padx=5)
#size box
size_var= tk.StringVar()
size_box=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
size_box['values']=tuple(range(8,80,2))
size_box.current(2)
size_box.grid(row=0,column=1,padx=5)
#bold button
bold_icon=tk.PhotoImage(file='icons/bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)
#italic button
italic_icon=tk.PhotoImage(file='icons/italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)
#underline button
underline_icon=tk.PhotoImage(file='icons/underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)
#font color
font_color_icon=tk.PhotoImage(file='icons/font_color.png')
font_color_btn=ttk.Button(tool_bar,image=font_color_icon) 
font_color_btn.grid(row=0,column=5,padx=5)
# align left
align_left_icon=tk.PhotoImage(file='icons/align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)
# align center
align_center_icon=tk.PhotoImage(file='icons/align_center.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)
# align right
align_right_icon=tk.PhotoImage(file='icons/align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)



#tool bar------------------------------end

#text editor--------------------------start

text_editor=tk.Text(main_app)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_app)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font functionality----start

current_font_family='Arial'
current_font_size=12
text_editor.configure(font=('Arial',12))


def change_font(event=None):
    global current_font_family
    current_font_family=font_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size(event=None):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font)
size_box.bind("<<ComboboxSelected>>", change_font_size)

# font functionality-----end


# button property ------ start
#  this is the actual default property of text editor 
# {'family': 'Courier New', 'size': 10, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
#  we can obtain this by tk.font.Font(font=text_editor['font']).actual()

# bold button functionality

def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))    
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_btn.configure(command=change_bold)

# italic button functionality
def change_slant():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))    
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))
italic_btn.configure(command=change_slant)

# under line button
def change_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))    
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
underline_btn.configure(command=change_underline)

# font color property
def font_color_change():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=font_color_change)


# align property
# align left
def align_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_btn.configure(command=align_left)
# align center
def align_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_btn.configure(command=align_center)
# align right
def align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_btn.configure(command=align_right)

# button property ------ end



#text editor----------------------------end

#status bar-------------------------start

status_bar=ttk.Label(main_app,text='status bar') 
status_bar.pack(side=tk.BOTTOM,fill=tk.Y)
text_changed=False
def status(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c').replace(' ','')) # we here used replace to not count spaces as character
        status_bar.configure(text=f'characters: {characters} words: {words}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',status)


#status bar --------------------------end


# main menu ---------------------------start

# files-------------------------------------start
url=''

#new functionality

def new_file(event=None):
    global url
    url=0
    text_editor.delete(1.0,'end')

#open functionality

def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select file',filetypes=(('Text file','*.TXT'),('All file','*.*')))
    try:
        with open(url,'r') as rf:
            text_editor.delete(1.0,'end')
            text_editor.insert(1.0,rf.read())
    except FileNotFoundError:
        return
    except:
        return
    main_app.title(os.path.basename(url))
# save functionality

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as wf:
                wf.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w',defaultextension ='.TXT' ,filetypes=(('Text file','*.TXT'),('All file','*.*')))
            content2 = text_editor.get(1.0,'end')
            url.write(content2)
            url.close()
    except:
        return
# save as functionality
def save_as_file(event=None):
    global url
    try: 
        content= text_editor.get(1.0,tk.END)    
        url=filedialog.asksaveasfile(mode='w',defaultextension ='.TXT' ,filetypes=(('Text file','*.TXT'),('All file','*.*')))
        url.write(content)  
    except:
        return
         
# exit functionality
def exit_func(event=None):
    global url , text_changed
    try:
        if text_changed:
            mbox= messagebox.askyesnocancel('Warning','Do you want to exit without saving?')    
            if mbox is True:
                if url :
                    content = text_editor.get(1.0,'end')
                    with open(url,'w',encoding='utf-8') as wf:
                        wf.write(content)
                        main_app.destroy()
                else:
                    content2= str(text_editor.get(1.0,'end'))  # str is used just to ensure that there is no error in the saving of file
                    url=filedialog.asksaveasfile(mode='w',defaultextension ='.TXT' ,filetypes=(('Text file','*.TXT'),('All file','*.*')))
                    url.write(content2)
                    url.close()
                    main_app.destroy()
            if mbox is False:
                main_app.destroy()
        else:
            main_app.destroy()
    except:
        return    

# file commands
files.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='CTRL+N',command=new_file)
files.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='CTRL+O',command=open_file)
files.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='CTRL+S',command=save_file)
files.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='CTRL+Alt',command=save_as_file)
files.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='CTRL+Q',command=exit_func)


# files-------------------------------------end

# edit ------------------------------------start

# find functionality

def find_func(event=None):
    def find():
        # ye to muje bhi pura smj nhi aya abhi
        word=find_entry.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0 
        if word:
            start_pos='1.0'
            while True:
                start_pos = text_editor.search(word,start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')                
    def replace():
        word =find_entry.get()
        replace_txt=replace_entry.get()
        content = text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_txt)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_dialogue=tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0) # by thhis the size will remain same
    # frame
    find_frame=ttk.LabelFrame(find_dialogue,text='Find/Replace')
    find_frame.pack(pady=20)
    #labels
    text_find_label=ttk.Label(find_frame,text='Find : ')
    text_replace_label=ttk.Label(find_frame,text='Replace : ')
    # entry box
    find_entry=ttk.Entry(find_frame,width=16)    
    replace_entry=ttk.Entry(find_frame,width=16)    
    # buttons
    find_btn = ttk.Button(find_frame,text ='Find',command=find)
    replace_btn = ttk.Button(find_frame,text ='Replace',command=replace)
    # grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)
    find_entry.grid(row=0,column=1,padx=4,pady=4)
    replace_entry.grid(row=1,column=1,padx=4,pady=4)
    find_btn.grid(row=2,column=0,padx=8,pady=4)
    replace_btn.grid(row=2,column=1,padx=8,pady=4)

    find_dialogue.mainloop()
    
    
# edit commands
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='CTRL+X',command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='CTRL+C',command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='CTRL+V',command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='CTRL+Alt+X',command=lambda:text_editor.delete(1.0,'end'))
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='CTRL+F',command=find_func) 


# edit ------------------------end


# view ------------------------start


#view checkbutton

show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar =True
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True


view.add_checkbutton(label='Tool Bar' ,onvalue=True,offvalue=False,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=True,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)

# view ------------------------start

#color theme radiobutton
def change_theme():
    chosen_theme= theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)
count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1
# view --------------------end

#  ---------------

# --------------
main_app.config(menu=main_menu)

#bind shortcut keys---------

main_app.bind("<Control-n>",new_file)
main_app.bind("<Control-o>",open_file)
main_app.bind("<Control-s>",save_file)
main_app.bind("<Control-Alt-s>",save_as_file)
main_app.bind("<Control-q>",exit_func)
main_app.bind("<Control-f>",find_func)

main_app.mainloop()