import os, glob,re
import shutil
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as me
import tkinter.scrolledtext as sc


class sort_app(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize ()

    def initialize(self):

        self.minsize (width=450, height=500)
        self.maxsize (width=450, height=500)

        self.grid_columnconfigure (2, weight=1)

        textFrame = tk.LabelFrame(self, text = "Here is short introduction of it", height= 200, width = 450)
        textFrame.grid(row = 0, column = 0, columnspan = 3, sticky='NSEW',  padx=5)

        attentionLabel = tk.Label (textFrame,text = "Attention: ", fg = 'red').grid (column=0, row=0, columnspan=2)
        attention1 = tk.Label (textFrame,text = " This Tool works default on electro. component sort, "
                                                "the filename like:", anchor = "center")
        attention1.grid (column=0, row=1, columnspan=2)

        attention2 = tk.Label (textFrame, text="*** AUD/?÷C123÷ *** or ***AUD/?÷Comp.C123.Pin***, "
                                               "search light type.", anchor="center")
        attention2.grid (column=0, row=2, columnspan=2)

        setupLabel = tk.Label (textFrame, text="Setup: ", fg='red',
                                  anchor="center").grid (column=0, row=3, columnspan=2)

        setup1 = tk.Label (textFrame, text="'sort directly' sorts all possible images directly under given folder.",
                           anchor="center")
        setup1.grid (column=0, row=4, columnspan=2)

        setup2 = tk.Label (textFrame, text="'sort into subDIR' sorts images into last folder.",
                           anchor="center")
        setup2.grid (column=0, row=5, columnspan=2)

        setup3 = tk.Label (textFrame, text="'New Rules' could defined your own rules for sorting.",
                           anchor="center")
        setup3.grid (column=0, row=6, columnspan=2)


        choiceFrame = tk.LabelFrame (self,  text ="Sort Choice")
        choiceFrame.grid (row=6, columnspan=3, sticky='NSEW',  padx=5)

        self.choice_value = tk.StringVar ()
        choiceComb = ttk.Combobox (choiceFrame, textvariable=self.choice_value)
        choiceComb['values'] = ('sort directly', 'sort into subDIR')
        choiceComb.current (0)
        choiceComb.grid(row = 0, column = 0, rowspan = 2, columnspan =2,  sticky='NW',padx=5, pady = 5)

        self.newDefination_var = tk.IntVar ()
        newCheck = tk.Checkbutton (choiceFrame, text="New Rules",
                                    variable=self.newDefination_var, command=self.OnCheckClick). \
            grid (column=0, row=2, sticky='NW', rowspan=2, pady=3)


        self.textfield = sc.ScrolledText (choiceFrame, height =2, wrap=tk.WORD, state=tk.DISABLED)
        self.textfield.grid(column=0, row=4, sticky='WENS', columnspan=3, padx=5, pady=5)
        choiceFrame.grid_columnconfigure (1, weight=1)



        configFrame = tk.LabelFrame (self, text=" Input Configure ")
        configFrame.grid (row=14, columnspan=3, sticky='NSEW',  padx=5, pady = 5)

        self.baseCheck_var = tk.IntVar()
        baseCheck = tk.Checkbutton(configFrame, text = "Base",
                                   variable =  self.baseCheck_var, command =self.OnCheckClick).\
            grid(column=0, row = 0, sticky='NW', rowspan = 2, pady = 3)

        baseLabel = tk.Label (configFrame, text=" Base Folder").\
            grid(column = 0, row =2, sticky='NW', rowspan = 2, pady = 3)

        self.BEntry_var = tk.StringVar()
        self.entry_base = tk.Entry (configFrame, textvariable= self.BEntry_var, state = "disabled")
        self.entry_base.grid (column=1, row=2, sticky='WENS', rowspan = 2,columnspan = 2, padx = 5, pady = 3 )
        self.entry_base.bind ("<Return>", self.OnPressEnter)

        sourceLabel = tk.Label (configFrame, text=" Source Folder")
        sourceLabel.grid (column=0, row=6, rowspan = 2, sticky = 'NW', pady = 3)

        self.SEntry_var = tk.StringVar ()
        self.entry_S = tk.Entry (configFrame, textvariable = self.SEntry_var)
        self.entry_S.grid (column=1, row=6, sticky='NSEW',rowspan = 2, columnspan = 2, padx = 5, pady = 3 )
        self.entry_S.bind ("<Return>", self.OnPressEnter)


        destinationLabel = tk.Label (configFrame, text=" Destination Folder")
        destinationLabel.grid (column=0, row=8, rowspan = 2, sticky = 'NW', pady = 3)

        self.DEntry_var = tk.StringVar ()
        self.entry_D = tk.Entry (configFrame, textvariable = self.DEntry_var)
        self.entry_D.grid (column=1, row=8, sticky='NSEW', padx = 5, columnspan = 2, pady = 5)
        self.entry_D.bind ("<Return>", self.OnPressEnter)
        configFrame.grid_columnconfigure (1, weight=1)

        button = tk.Button (self, text=u"Start !", bg = 'light blue', height = 2, width = 10,
                            command=self.OnButtonClick)
        button.grid (column=1, row=22, rowspan =2, columnspan = 2)

    def OnCheckClick(self):
        if self.baseCheck_var.get() == 1:
            self.entry_base.config(state = 'normal')
        else:
            self.entry_base.delete('0', tk.END)
            self.entry_base.config(state = 'disabled')

        if self.newDefination_var.get() ==1:
            self.textfield.config(state = tk.NORMAL)
            
        else:
            self.textfield.delete ('1.0', tk.END)
            self.textfield.config (state=tk.DISABLED)



    def OnPressEnter(self, event):
        if self.entry_base:
            self.entry_S.focus ()
        if self.entry_S:
            self.entry_D.focus()


    def OnButtonClick(self):

        base =  self.BEntry_var.get()
        src = self.SEntry_var.get()
        des = self.DEntry_var.get()

        source_path = os.path.join(base , src)
        des_path = os.path.join(base, des)


        if not os.path.isdir(source_path):
            me.showinfo ("Warning", "Please give the right source path!")
            return

        if os.path.isdir(source_path) and not os.path.isdir(des_path):
            if callback(src):
                self.DEntry_var.set(source_path + '_Sort')
                des_path = source_path + '_Sort'

            else:
                return

        if os.path.isdir(base) and des =='':
            if callback(source_path):
                self.DEntry_var.set (source_path + '_Sort')
                des_path = source_path + '_Sort'
            else:
                return

        if not os.path.exists (des_path):
            os.makedirs (des_path)

        image_list =[]
        recursive_index (source_path, image_list)

        if self.newDefination_var.get() ==1 and self.textfield.get ('1.0', tk.END)!='':
            Pattern = self.textfield.get('1.0', tk.END)
        else:
            Pattern = '(?<=AUD÷).*?(?=÷|\\.Pin)|(?<=AUD_20÷).*?(?=÷|\\.Pin)' \
                      '|(?<=LEVEL_3÷).*?(?=÷|\\.Pin)|(?<=AUFL÷).*?(?=÷|\\.Pin)' \
                      '|(?<=AUDAngl÷).*?(?=÷|\\.Pin)|(?<=UWDIFF_Angl÷).*?(?=÷|\\.Pin)' \
                      '|(?<=WDIFF÷).*?(?=÷|\\.Pin)|(?<=ANGL_BDIFF÷).*?(?=÷|\\.Pin)' \
                      '|(?<=ADIFF÷).*?(?=÷|\\.Pin)|(?<=DIFF÷).*?(?=÷|\\.Pin)' \
                      '|(?<=ADIFF_SingleColor÷).*?(?=÷|\\.Pin)'

        result_path = os.path.join(des_path,'result.txt')
        result = open(result_path, 'w')

        for im in image_list:
            base_name = os.path.basename(im)
            print(base_name)

            last_folder = os.path.basename(os.path.dirname(im))
            print(last_folder)

            try:
                b_type = re.search (Pattern, base_name)
                print (b_type.group ())
            except:
                me.showinfo ("Warning", "Sorry, your Search Rules might not right!")
                return

            if self.choice_value.get () == 'sort directly':
                save_path = (os.path.join(des_path, b_type.group()))
            else:
                save_path = os.path.join(os.path.join(des_path,last_folder ),b_type.group())

            if self.newDefination_var.get () == 1 and self.textfield.get ('1.0', tk.END) != '':
                try:
                    if not os.path.exists (save_path):
                        os.makedirs (save_path)
                    shutil.copyfile (im, os.path.join (save_path, base_name))
                except:
                    result.write (im + '\n')
                    continue
            else:
                if re.match ('Comp.', b_type.group ()):
                    continue
                else:
                    try:
                        if not os.path.exists (save_path):
                            os.makedirs (save_path)
                        shutil.copyfile (im, os.path.join (save_path, base_name))
                    except:
                        result.write (im + '\n')
                        continue


        result.close()
        if os.stat (result_path).st_size == 0:
            os.remove(result_path)
            me.showinfo ("Succeed", "Sorted Successfully!")
        else:
            me.showinfo ("Warning", "Finished Sort, but there are some images might not"
                                    " sorted successfully, please check the result file!")


def recursive_index(dir, image_list):

    image_extensions = ['bmp', 'png', 'giff', 'tiff', 'tif', 'jpg', 'jpeg']

    for ext in image_extensions:
        search_str = os.path.join (dir, '*.%s' % ext)
        image_list.extend (glob.glob (search_str))

    if len (image_list) == 0:
        folder_list = [os.path.join (dir, f)
                       for f in os.listdir (dir)
                       if os.path.isdir (os.path.join (dir, f))]

        for f in folder_list:
            recursive_index (f, image_list)


def callback(path):
    if me.askyesno ('Verify', 'There have no available destination path, you want to save as '
                                  + path + '_Sort?'):
        return True
    else:
        me.showinfo ('No', 'Please give the right destination path')
        return False





if __name__ == "__main__":
    app = sort_app(None)
    app.title ('File Sort')
    app.mainloop()
