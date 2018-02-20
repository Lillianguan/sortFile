import glob
import os
import re
import shutil
import tkinter as tk
import tkinter.messagebox as me
import tkinter.ttk as ttk


class sort_app(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize ()

    def initialize(self):

        # set the fest size of the window
        self.minsize (width=450, height=450)
        self.maxsize (width=450, height=450)

        self.grid_columnconfigure (2, weight=1)

        # first frame for introduction
        textFrame = tk.LabelFrame(self, text = "Here is short introduction of it", height= 200, width = 450)
        textFrame.grid(row = 0, column = 0, columnspan = 3, sticky='NSEW',  padx=5)

        attentionLabel = tk.Label (textFrame,text = "Attention: ", fg = 'red').grid (column=0, row=0, columnspan=2)
        attention1 = tk.Label (textFrame,text = " This Tool works default on electro. component sort, "
                                                "the filename like:", anchor = "center")
        attention1.grid (column=0, row=1, columnspan=2)

        attention2 = tk.Label (textFrame, text="*** ÷***÷...÷***", anchor="center")
        attention2.grid (column=0, row=2, columnspan=2)

        setupLabel = tk.Label (textFrame, text="Setup: ", fg='red',
                                  anchor="center").grid (column=0, row=3, columnspan=2)

        setup1 = tk.Label (textFrame, text="'sort directly' sorts all possible images directly under given folder.",
                           anchor="center")
        setup1.grid (column=0, row=4, columnspan=2)

        setup2 = tk.Label (textFrame, text="'sort into subDIR' sorts images into last folder.",
                           anchor="center")
        setup2.grid (column=0, row=5, columnspan=2)

        setup2 = tk.Label (textFrame, text="'Choose sort type', the different sort choice could be used.",
                           anchor="center")
        setup2.grid (column=0, row=6, columnspan=2)

        # second frame for the sort choice
        choiceFrame = tk.LabelFrame (self, text="Sort Choice", height=100, width=450)
        choiceFrame.grid (row=6, columnspan=3, sticky='NSEW',  padx=5)

        sortDirLabel = tk.Label (choiceFrame, text="Choose architecture:")
        sortDirLabel.grid (column=0, row=0, sticky='NW')

        sortTypeLabel = tk.Label (choiceFrame, text="Choose sort methode:")
        sortTypeLabel.grid (column=2, row=0, columnspan=2, sticky='NE')

        self.choice_value = tk.StringVar ()
        choiceComb = ttk.Combobox (choiceFrame, textvariable=self.choice_value)
        choiceComb['values'] = ('sort directly', 'sort into subDIR')
        choiceComb.current (0)
        choiceComb.grid (row=2, column=0, rowspan=2, sticky='NW', padx=5, pady=5)

        self.choice_sort = tk.StringVar ()
        choiceComb_S = ttk.Combobox (choiceFrame, textvariable=self.choice_sort, width=30)
        choiceComb_S['values'] = ('Custom', 'Board', 'Barcode', 'Element group',
                                  'Lighting', 'Eletrc. Component without Pin', 'Eletrc. Component with Pin', 'Pin')
        choiceComb_S.current (5)
        choiceComb_S.grid (row=2, column=3, rowspan=2, columnspan=2, sticky='NE', padx=5, pady=5)

        # third frame for the input configuration
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

        button = tk.Button (self, text=u"Start", bg='light blue', height=2, width=10,
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
        # get source path and destination path
        base =  self.BEntry_var.get()
        src = self.SEntry_var.get()
        des = self.DEntry_var.get()

        source_path = os.path.join(base , src)
        des_path = os.path.join(base, des)

        # check the path
        if not os.path.isdir(source_path):
            me.showinfo ("Warning", "Please give the right source path!")
            return
        # choose the sort way you want
        if os.path.isdir(source_path) and not os.path.isdir(des_path):
            if callback(src):
                self.DEntry_var.set(source_path + '_Sort')
                des_path = source_path + '_Sort'

            else:
                return

        # choose the sort way you want
        if os.path.isdir(base) and des =='':
            if callback(source_path):
                self.DEntry_var.set (source_path + '_Sort')
                des_path = source_path + '_Sort'
            else:
                return
        # check the destination path
        if not os.path.exists (des_path):
            os.makedirs (des_path)

        me.showinfo ("Sorting", "Start Sorting...")

        # get all the image file
        image_list =[]
        recursive_index (source_path, image_list)

        # open the result file and ready to write
        result_path = os.path.join(des_path,'result.txt')
        result = open(result_path, 'w')

        # start sorting the images
        for im in image_list:
            # get the basename and last folder name for the later saving
            base_name = os.path.basename(im)
            last_folder = os.path.basename(os.path.dirname(im))
            matches = self.get_pattern (base_name)

            # continue the loop
            if matches == '÷':
                continue

            if self.choice_value.get () == 'sort directly':
                save_path = (os.path.join (des_path, matches))
            else:
                save_path = os.path.join (os.path.join (des_path, last_folder), matches)

            # if the use the new rules to sort the image files
            try:
                if not os.path.exists (save_path):
                    os.makedirs (save_path)
                shutil.copyfile (im, os.path.join (save_path, base_name))
            except:
                result.write (im + '\n')
                continue


        # close the result file and check if it is empty
        result.close()
        if os.stat (result_path).st_size == 0:
            os.remove(result_path)
            me.showinfo ("Succeed", "Sorted Successfully!")
        else:
            me.showinfo ("Warning", "Finished Sort, but there are some images might not"
                                    " sorted successfully, please check the result file!")

    # get the the sort pattern
    def get_pattern(self, base_name):

        if self.choice_sort.get () == 'Custom':
            pattern = '^(?:[^÷]*\÷){0}([^÷]*)'
        elif self.choice_sort.get () == 'Board':
            pattern = '^(?:[^÷]*\÷){1}([^÷]*)'
        elif self.choice_sort.get () == 'Barcode':
            pattern = '^(?:[^÷]*\÷){2}([^÷]*)'
        elif self.choice_sort.get () == 'Element group':
            pattern = '^(?:[^÷]*\÷){5}([^÷]*)'
        elif self.choice_sort.get () == 'Lighting':
            if base_name.count ('÷') == 12:
                pattern = '^(?:[^÷]*\÷){8}([^÷]*)'
            elif base_name.count ('÷') == 13:
                pattern = '^(?:[^÷]*\÷){9}([^÷]*)'
        elif self.choice_sort.get () == 'Eletrc. Component without Pin':
            if base_name.count ('÷') == 12:
                pattern = '^(?:[^÷]*\÷){9}([^÷]*)'
            elif base_name.count ('÷') == 13:
                pattern = '÷'
        elif self.choice_sort.get () == 'Eletrc. Component with Pin':
            if base_name.count ('÷') == 12:
                pattern = '^(?:[^÷]*\÷){9}([^÷]*)'
            elif base_name.count ('÷') == 13:
                pattern = '^(?:[^÷]*\÷){10}([^÷]*)'
        elif self.choice_sort.get () == 'Pin':
            if base_name.count ('÷') == 12:
                pattern = '÷'
            elif base_name.count ('÷') == 13:
                pattern = '^(?:[^÷]*\÷){10}([^÷]*)'
        else:
            raise Exception ('There is no such sort way!')

        try:
            result = re.search (pattern, base_name)
        except:
            print ('This file might something wrong!')
            return

        if result.groups ():
            if self.choice_sort.get () == 'Eletrc. Component with Pin':
                result_ = re.search ('(?<=Comp.).*?(?=.Pin)', result.group (1))
                if result_:
                    print (result_.group (0))
                    return result_.group (0)

                else:
                    return result.group (1)
            else:
                print ('Result:' + str (result.group (1)))
                return result.group (1)
        else:
            return result.group (0)



# recursively parse the image files under a directionary
def recursive_index(dir, image_list):
    # all possible image extensions
    image_extensions = ['bmp', 'png', 'giff', 'tiff', 'tif', 'jpg', 'jpeg']
    image = []

    for ext in image_extensions:
        search_str = os.path.join (dir, '*.%s' % ext)
        image_list.extend (glob.glob (search_str))
        image.extend (glob.glob (search_str))

    if len (image) == 0:
        folder_list = [os.path.join (dir, f)
                       for f in os.listdir (dir)
                       if os.path.isdir (os.path.join (dir, f))]

        for f in folder_list:
            print (f)
            recursive_index (f, image_list)

# callback function for the questioning
def callback(path):
    if me.askyesno ('Verify', 'There have no available destination path, you want to save as '
                                  + path + '_Sort?'):
        return True
    else:
        me.showinfo ('No', 'Please give the right destination path')
        return False


# define the cmd start function
if __name__ == "__main__":
    app = sort_app(None)
    app.title ('Image File Sort')
    app.mainloop()

