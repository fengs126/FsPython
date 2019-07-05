'''
Created on 2019/06/13

@author: Fengs
@version: 2.13
'''
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import random
import re


def main():
    title = '単語 v2.13'
    lline = []
    lvalue = ''
    flines = []
    clines = []
    tlines = []
    blines = []

    def createline():
        if len(tlines) == 0:
            if len(clines) == 0:
                for fline in flines:
                    rline = re.split(',|\t', fline)
                    tvalue = ''
                    if len(rline) > 1:
                        tvalue = rline[1].strip()
                    else:
                        tvalue = rline[0].strip()

                    if ifiliter1.get() == 1 and len(tvalue) == 1:
                        clines.append(rline.copy())
                    if ifiliter2.get() == 1 and len(tvalue) == 2:
                        clines.append(rline.copy())
                    if ifiliter3.get() == 1 and len(tvalue) == 3:
                        clines.append(rline.copy())
                    if ifiliter4.get() == 1 and len(tvalue) == 4:
                        clines.append(rline.copy())
                    if ifiliter5.get() == 1 and len(tvalue) == 5:
                        clines.append(rline.copy())
                    if ifiliter9.get() == 1 and len(tvalue) > 5:
                        clines.append(rline.copy())

                if len(clines) == 0:
                    tfile.config(state='normal')
                    tfile.delete('0.0', 'end')
                    tfile.insert('end', '字符集错误.')
                    tfile.config(state='disabled')
                    sfile.set('Open')
                    ltext.set('')
                    lvalue = ''
                    lexamination.config(bg='yellow')
                    bentry.delete(0, 'end')
                    bentry.config(state='disabled')
                    tinfo.config(state='normal')
                    tinfo.delete('0.0', 'end')
                    tinfo.config(state='disabled')
                    return

            tlines.clear()
            for bline in blines:
                tlines.append(bline.copy())

            blines.clear()

            random.shuffle(clines)
            for cline in clines:
                if llimit.get().isnumeric() and len(tlines) == int(llimit.get()):
                    break

                if cline in tlines:
                    continue

                tlines.append(cline.copy())

        tline = random.choice(tlines)
        lline.clear()
        lline.extend(tline.copy())

    def openfile():
        global lvalue

        if sfile.get() == 'GO':
            if bentry.config('state')[4] == 'normal':
                ltext.set('')
                lvalue = ''
                lexamination.config(bg='yellow')
                bentry.delete(0, 'end')
                tinfo.config(state='normal')
                tinfo.delete('0.0', 'end')
                tinfo.config(state='disabled')
                createline()
                if len(lline) == 0:
                    tfile.config(state='normal')
                    tfile.delete('0.0', 'end')
                    tfile.insert('end', '字符集错误.')
                    tfile.config(state='disabled')
                    sfile.set('Open')
                    ltext.set('')
                    lvalue = ''
                    lexamination.config(bg='yellow')
                    bentry.delete(0, 'end')
                    bentry.config(state='disabled')
                    tinfo.config(state='normal')
                    tinfo.delete('0.0', 'end')
                    tinfo.config(state='disabled')
                    return

                ltext.set(lline[0].strip())
                if len(lline) > 1:
                    lvalue = lline[1].strip()
                else:
                    lvalue = lline[0].strip()

            if len(flines) == 0:
                tfile.config(state='normal')
                tfile.delete('0.0', 'end')
                tfile.insert('end', '文件读取失败.')
                tfile.config(state='disabled')
                sfile.set('Open')
                return

            if ifiliter1.get() == 0 and ifiliter2.get() == 0 and ifiliter3.get() == 0 and ifiliter4.get() == 0 and ifiliter5.get() == 0 and ifiliter9.get() == 0:
                tfile.config(state='normal')
                tfile.delete('0.0', 'end')
                tfile.insert('end', '筛选条件必须选择.')
                tfile.config(state='disabled')
                sfile.set('Open')
                ltext.set('')
                lvalue = ''
                lexamination.config(bg='yellow')
                bentry.delete(0, 'end')
                bentry.config(state='disabled')
                tinfo.config(state='normal')
                tinfo.delete('0.0', 'end')
                tinfo.config(state='disabled')
                return

            else:
                clines.clear()
                for fline in flines:
                    rline = re.split(',|\t', fline)
                    tvalue = ''
                    if len(rline) > 1:
                        tvalue = rline[1].strip()
                    else:
                        tvalue = rline[0].strip()

                    if ifiliter1.get() == 1 and len(tvalue) == 1:
                        clines.append(rline.copy())
                    if ifiliter2.get() == 1 and len(tvalue) == 2:
                        clines.append(rline.copy())
                    if ifiliter3.get() == 1 and len(tvalue) == 3:
                        clines.append(rline.copy())
                    if ifiliter4.get() == 1 and len(tvalue) == 4:
                        clines.append(rline.copy())
                    if ifiliter5.get() == 1 and len(tvalue) == 5:
                        clines.append(rline.copy())
                    if ifiliter9.get() == 1 and len(tvalue) > 5:
                        clines.append(rline.copy())

                if len(clines) == 0:
                    tfile.config(state='normal')
                    tfile.delete('0.0', 'end')
                    tfile.insert('end', '字符集错误.')
                    tfile.config(state='disabled')
                    sfile.set('Open')
                    ltext.set('')
                    lvalue = ''
                    lexamination.config(bg='yellow')
                    bentry.delete(0, 'end')
                    bentry.config(state='disabled')
                    tinfo.config(state='normal')
                    tinfo.delete('0.0', 'end')
                    tinfo.config(state='disabled')
                    return

                tlines.clear()
                for bline in blines:
                    tlines.append(bline.copy())

                blines.clear()

                random.shuffle(clines)
                for cline in clines:
                    if llimit.get().isnumeric() and len(tlines) == int(llimit.get()):
                        break

                    if cline in tlines:
                        continue

                    tlines.append(cline.copy())

            ltext.set('')
            lvalue = ''
            lexamination.config(bg='yellow')
            bentry.delete(0, 'end')
            tinfo.config(state='normal')
            tinfo.delete('0.0', 'end')
            tinfo.config(state='disabled')
            createline()
            if len(lline) == 0:
                tfile.config(state='normal')
                tfile.delete('0.0', 'end')
                tfile.insert('end', '字符集错误.')
                tfile.config(state='disabled')
                sfile.set('Open')
                ltext.set('')
                lvalue = ''
                lexamination.config(bg='yellow')
                bentry.delete(0, 'end')
                bentry.config(state='disabled')
                tinfo.config(state='normal')
                tinfo.delete('0.0', 'end')
                tinfo.config(state='disabled')
                return

            ltext.set(lline[0].strip())
            if len(lline) > 1:
                lvalue = lline[1].strip()
            else:
                lvalue = lline[0].strip()

            bentry.config(state='normal')
            bentry.focus()
            window.title(title + ' | ' + str(len(clines)) + ' | ' + str(len(tlines)))

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

        lline.clear()
        lvalue = ''
        flines.clear()
        clines.clear()
        tlines.clear()
        blines.clear()
        tfile.config(state='normal')
        tfile.delete('0.0', 'end')
        tfile.config(state='disabled')
        sfile.set('Open')
        ltext.set('')
        lexamination.config(bg='yellow')
        bentry.delete(0, 'end')
        bentry.config(state='disabled')
        tinfo.config(state='normal')
        tinfo.delete('0.0', 'end')
        tinfo.config(state='disabled')
        ifiliter1.set(1)
        ifiliter2.set(1)
        ifiliter3.set(1)
        ifiliter4.set(1)
        ifiliter5.set(1)
        ifiliter9.set(1)
        llimit.current(0)
        window.title(title + ' | ')

    def keyReturn(event):
        global lvalue

        if event.keysym == 'Return':
            if lexamination.config('bg')[4] == 'green':
                createline()
                if len(lline) == 0:
                    tfile.config(state='normal')
                    tfile.delete('0.0', 'end')
                    tfile.insert('end', '字符集错误.')
                    tfile.config(state='disabled')
                    sfile.set('Open')
                    ltext.set('')
                    lvalue = ''
                    lexamination.config(bg='yellow')
                    bentry.delete(0, 'end')
                    bentry.config(state='disabled')
                    tinfo.config(state='normal')
                    tinfo.delete('0.0', 'end')
                    tinfo.config(state='disabled')
                    return

                ltext.set(lline[0].strip())
                if len(lline) > 1:
                    lvalue = lline[1].strip()
                else:
                    lvalue = lline[0].strip()

                lexamination.config(bg='yellow')
                bentry.delete(0, 'end')
                tinfo.config(state='normal')
                tinfo.delete('0.0', 'end')
                tinfo.config(state='disabled')
                window.title(title + ' | ' + str(len(clines)) + ' | ' + str(len(tlines)))

            elif bentry.get() == '':
                pass

            elif bentry.get() == ' ' or bentry.get() == '　':
                bentry.delete(0, 'end')
                tinfo.config(state='normal')
                tinfo.delete('0.0', 'end')
                tinfo.insert('end', ','.join(lline))
                tinfo.config(state='disabled')
                if not lline in blines:
                    blines.append(lline.copy())

            elif bentry.get() == ltext.get() or bentry.get() == lvalue:
                if not tinfo.get('0.0', 'end').strip() and lexamination.config('bg')[4] == 'yellow':
                    if not lline in blines:
                        clines.remove(lline)

                    tlines.remove(lline)

                lexamination.config(bg='green')
                tinfo.config(state='normal')
                tinfo.delete('0.0', 'end')
                tinfo.insert('end', ','.join(lline))
                tinfo.config(state='disabled')

            else:
                lexamination.config(bg='red')
                if not lline in blines:
                    blines.append(lline.copy())

    def keyTab(event):
        global lvalue

        if event.keysym == 'Tab' and bentry.config('state')[4] == 'normal':
            tlines.remove(lline)
            ltext.set('')
            lvalue = ''
            lexamination.config(bg='yellow')
            bentry.delete(0, 'end')
            tinfo.config(state='normal')
            tinfo.delete('0.0', 'end')
            tinfo.config(state='disabled')
            createline()
            if len(lline) == 0:
                tfile.config(state='normal')
                tfile.delete('0.0', 'end')
                tfile.insert('end', '字符集错误.')
                tfile.config(state='disabled')
                sfile.set('Open')
                ltext.set('')
                lvalue = ''
                lexamination.config(bg='yellow')
                bentry.delete(0, 'end')
                bentry.config(state='disabled')
                tinfo.config(state='normal')
                tinfo.delete('0.0', 'end')
                tinfo.config(state='disabled')
                return

            ltext.set(lline[0].strip())
            if len(lline) > 1:
                lvalue = lline[1].strip()
            else:
                lvalue = lline[0].strip()

            window.title(title + ' | ' + str(len(clines)) + ' | ' + str(len(tlines)))

    def callback():
        clickkey = messagebox.askyesnocancel('操作确认', 'Y:关闭\nN:最小化/恢复')
        if clickkey == True:
            window.destroy()
        elif clickkey == False:
            if window.state() == 'normal':
                window.iconify()
            elif window.state() == 'iconic':
                window.deiconify()
                bentry.focus()

    window = tk.Tk()
    window.title(title)
    window.geometry('270x168')
    window.resizable(0, 0)
    window.attributes("-toolwindow", True)
    window.attributes("-topmost", True)
    window.protocol("WM_DELETE_WINDOW", callback)

    tfile = tk.Text(window, width=30, height=2, state='disabled')
    tfile.place(x=0, y=0, anchor='nw')

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

    ifiliter1 = tk.IntVar()
    ifiliter1.set(1)
    cfilter1 = tk.Checkbutton(window, text='1', variable=ifiliter1, onvalue=1, offvalue=0)
    cfilter1.place(x=0, y=141, anchor='nw')

    ifiliter2 = tk.IntVar()
    ifiliter2.set(1)
    cfilter2 = tk.Checkbutton(window, text='2', variable=ifiliter2, onvalue=1, offvalue=0)
    cfilter2.place(x=35, y=141, anchor='nw')

    ifiliter3 = tk.IntVar()
    ifiliter3.set(1)
    cfilter3 = tk.Checkbutton(window, text='3', variable=ifiliter3, onvalue=1, offvalue=0)
    cfilter3.place(x=70, y=141, anchor='nw')

    ifiliter4 = tk.IntVar()
    ifiliter4.set(1)
    cfilter4 = tk.Checkbutton(window, text='4', variable=ifiliter4, onvalue=1, offvalue=0)
    cfilter4.place(x=105, y=141, anchor='nw')

    ifiliter5 = tk.IntVar()
    ifiliter5.set(1)
    cfilter5 = tk.Checkbutton(window, text='5', variable=ifiliter5, onvalue=1, offvalue=0)
    cfilter5.place(x=140, y=141, anchor='nw')

    ifiliter9 = tk.IntVar()
    ifiliter9.set(1)
    cfilter9 = tk.Checkbutton(window, text='5+', variable=ifiliter9, onvalue=1, offvalue=0)
    cfilter9.place(x=175, y=141, anchor='nw')

    llimit = ttk.Combobox(window, width=3)
    llimit.place(x=220, y=143, anchor='nw')
    llimit['value'] = ('*', '20', '40', '60', '80', '100')
    llimit.current(0)

    window.mainloop()


main();
