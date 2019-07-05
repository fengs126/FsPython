'''
Created on 2019/06/13

@author: Fengs
@version: 1.14
'''
import tkinter as tk
from tkinter import filedialog
import random
import re


def main():
    title = '単語 v1.14'
    window = tk.Tk()
    window.title(title)
    window.geometry('270x141')
    window.resizable(0, 0)

    tfile = tk.Text(window, width=30, height=2, state='disabled')
    tfile.place(x=0, y=0, anchor='nw')
    lvalue = ''
    flines = []
    fdicts = dict()
    idx = 0

    def createidx():
        while True:
            rdmidx = random.randint(0, len(flines) - 1)
            level = fdicts.get(re.split(',|\t', flines[rdmidx])[0], 3)
            rdm = random.randint(1, 100)

            if level == 1 and (rdm >= 1 and rdm <= 20):
                window.title(title + ' | ' + str(level))
                return rdmidx
            if level == 2 and (rdm >= 1 and rdm <= 40):
                window.title(title + ' | ' + str(level))
                return rdmidx
            if level == 3 and (rdm >= 1 and rdm <= 60):
                window.title(title + ' | ' + str(level))
                return rdmidx
            if level == 4 and (rdm >= 1 and rdm <= 80):
                window.title(title + ' | ' + str(level))
                return rdmidx
            if level == 5 and (rdm >= 1 and rdm <= 100):
                window.title(title + ' | ' + str(level))
                return rdmidx

    def openfile():
        global idx
        global lvalue

        if sfile.get() == 'GO':
            if len(flines) == 0:
                tfile.config(state='normal')
                tfile.delete('0.0', 'end')
                tfile.insert('end', '文件读取失败.')
                tfile.config(state='disabled')
                sfile.set('Open')
                return

            ltext.set('')
            lvalue = ''
            lexamination.config(bg='yellow')
            bentry.delete(0, 'end')
            tinfo.config(state='normal')
            tinfo.delete('0.0', 'end')
            tinfo.config(state='disabled')
            idx = createidx()
            ltext.set(re.split(',|\t', flines[idx])[0].strip())
            if len(re.split(',|\t', flines[idx])) > 1:
                lvalue = re.split(',|\t', flines[idx])[1].strip()
            else:
                lvalue = re.split(',|\t', flines[idx])[0].strip()

            bentry.config(state='normal')

        else:
            filename = filedialog.askopenfilename(title='Open file', filetypes=[('Text', '*.txt'), ('All Files', '*')])

            if filename.strip():
                tfile.config(state='normal')
                tfile.delete('0.0', 'end')
                tfile.insert('end', filename)
                tfile.config(state='disabled')
                sfile.set('GO')

                ffile = open(filename.strip(), 'r', encoding='UTF-8')
                for l in ffile.readlines():
                    lformat = l.strip('\n').strip()

                    if lformat and not lformat in flines:
                        flines.append(lformat)

                ffile.close()

    def clearfile():
        global lvalue

        if tfile.get('0.0', 'end').strip():
            tfile.config(state='normal')
            tfile.delete('0.0', 'end')
            tfile.config(state='disabled')
            sfile.set('Open')
            ltext.set('')
            lvalue = ''
            lexamination.config(bg='yellow')
            flines.clear()
            bentry.delete(0, 'end')
            bentry.config(state='disabled')
            tinfo.config(state='normal')
            tinfo.delete('0.0', 'end')
            tinfo.config(state='disabled')

    def keyReturn(event):
        global idx
        global lvalue

        if event.keysym == 'Return':
            if lexamination.config('bg')[4] == 'green':
                idx = createidx()
                ltext.set(re.split(',|\t', flines[idx])[0].strip())
                if len(re.split(',|\t', flines[idx])) > 1:
                    lvalue = re.split(',|\t', flines[idx])[1].strip()
                else:
                    lvalue = re.split(',|\t', flines[idx])[0].strip()

                lexamination.config(bg='yellow')
                bentry.delete(0, 'end')
                tinfo.config(state='normal')
                tinfo.delete('0.0', 'end')
                tinfo.config(state='disabled')

            elif bentry.get() == '':
                pass

            elif bentry.get() == ' ' or bentry.get() == '　':
                level = fdicts.get(re.split(',|\t', flines[idx])[0], 3)
                if level < 5:
                    fdicts.update({re.split(',|\t', flines[idx])[0]:level + 1})
                else:
                    fdicts.update({re.split(',|\t', flines[idx])[0]:5})

                bentry.delete(0, 'end')
                tinfo.config(state='normal')
                tinfo.delete('0.0', 'end')
                tinfo.insert('end', flines[idx])
                tinfo.config(state='disabled')

            elif bentry.get() == ltext.get() or bentry.get() == lvalue:
                if not tinfo.get('0.0', 'end').strip():
                    level = fdicts.get(re.split(',|\t', flines[idx])[0], 3)
                    if level > 1:
                        fdicts.update({re.split(',|\t', flines[idx])[0]:level - 1})
                    else:
                        fdicts.update({re.split(',|\t', flines[idx])[0]:1})

                lexamination.config(bg='green')
                tinfo.config(state='normal')
                tinfo.delete('0.0', 'end')
                tinfo.insert('end', flines[idx])
                tinfo.config(state='disabled')

            else:
                fdicts.update({re.split(',|\t', flines[idx])[0]:5})
                lexamination.config(bg='red')

    def keyTab(event):
        global idx
        global lvalue

        if event.keysym == 'Tab':
            ltext.set('')
            lvalue = ''
            lexamination.config(bg='yellow')
            bentry.delete(0, 'end')
            tinfo.config(state='normal')
            tinfo.delete('0.0', 'end')
            tinfo.config(state='disabled')
            idx = createidx()
            ltext.set(re.split(',|\t', flines[idx])[0].strip())
            if len(re.split(',|\t', flines[idx])) > 1:
                lvalue = re.split(',|\t', flines[idx])[1].strip()
            else:
                lvalue = re.split(',|\t', flines[idx])[0].strip()

    bclear = tk.Button(window, text='×', width=1, height=1, relief='groove', command=clearfile)
    bclear.place(x=211, y=0, anchor='nw')

    sfile = tk.StringVar()
    sfile.set('Open')
    bfile = tk.Button(window, textvariable=sfile, width=5, height=1, relief='groove', command=openfile)
    bfile.place(x=226, y=0, anchor='nw')

    ltext = tk.StringVar()
    lexamination = tk.Label(window, textvariable=ltext, bg='yellow', font=('Arial', 16), anchor='w', width=22, height=1)
    lexamination.place(x=0, y=31, anchor='nw')

    bentry = tk.Entry(window, width=38, state='disabled')
    bentry.place(x=0, y=62, anchor='nw')
    bentry.focus()
    bentry.bind_all('<Key-Return>', keyReturn)
    bentry.bind_all('<Key-Tab>', keyTab)

    tinfo = tk.Text(window, width=38, height=4, state='disabled')
    tinfo.place(x=0, y=85, anchor='nw')

    window.mainloop()


main();
