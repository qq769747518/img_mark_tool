import cv2
import shutil
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory
import re
import os
import json
from collections import OrderedDict
from tkinter.messagebox import *

class Tk_window():


    def __init__(self):
        self.window = tk.Tk()

        # 第2步，给窗口的可视化起名字
        self.window.title('My Window')

        # 第3步，设定窗口的大小(长 * 宽)
        self.window.geometry('1200x650')  # 这里的乘是小x

        _img = Image.open('./default.jpg')

        _img = _img.resize((640, 360))
        self.img = ImageTk.PhotoImage(_img)
        # 第4步，place 放置方法（精准的放置到指定坐标点的位置上）
        self.img_lab =tk.Label(self.window, image =self.img)
        self.img_lab.place(x=50, y=80, anchor='nw')

        self.img_mark_info = ' '
        # 第4步，place 放置方法（精准的放置到指定坐标点的位置上）
        self.mark_info_lab =tk.Label(self.window, text=self.img_mark_info, font=('Arial', 20), )
        self.mark_info_lab.place(x=150, y=35, anchor='nw')
        tk.Button(self.window, text='下一张', font=('Arial', 13), width=10, height=1, command=self.next_img).place(x=720, y=80, anchor='nw')
        tk.Button(self.window, text='上一张', font=('Arial', 13), width=10, height=1, command=self.before_img).place(x=860, y=80,anchor='nw')
        tk.Button(self.window, text='生成标注图片', font=('Arial', 13), width=10, height=1, command=self.create_mark_img).place(x=1010,y=80,anchor='nw')

        self.var = tk.StringVar()
        self.var.set(0)
        tk.Radiobutton(self.window, text="行走/站立",variable=self.var, value=1, font=('Arial', 13),width=10, height=1, ).place(x=730, y=140,anchor='nw')
        tk.Radiobutton(self.window, text="站起",variable=self.var, value=2, font=('Arial', 13), width=10, height=1, ).place(x=710,y=170,anchor='nw')
        tk.Radiobutton(self.window, text="坐下",variable=self.var, value=3, font=('Arial', 13), width=10, height=1, ).place(x=710, y=200,anchor='nw')
        tk.Radiobutton(self.window, text="坐着/坐定",variable=self.var, value=4, font=('Arial', 13), width=10, height=1, ).place(x=730, y=230,anchor='nw')
        tk.Radiobutton(self.window, text="跌倒",variable=self.var, value=5, font=('Arial', 13), width=10, height=1, ).place(x=710, y=260,anchor='nw')
        tk.Radiobutton(self.window, text="躺/倒定",variable=self.var, value=6, font=('Arial', 13), width=10, height=1, ).place(x=720, y=290,anchor='nw')
        tk.Radiobutton(self.window, text="抬手/挥手",variable=self.var, value=7, font=('Arial', 13), width=10, height=1, ).place(x=730, y=320,anchor='nw')
        tk.Radiobutton(self.window, text="弯腰",variable=self.var, value=8, font=('Arial', 13), width=10, height=1, ).place(x=710, y=350,anchor='nw')
        tk.Radiobutton(self.window, text="跳跃",variable=self.var, value=9, font=('Arial', 13), width=10, height=1, ).place(x=710, y=380,anchor='nw')



        self.gui_path = tk.StringVar()
        self.path=''
        tk.Label(self.window, text="要标注的图片路径:",font=('Arial', 13), width=15, height=1).place(x=50, y=470,anchor='nw')
        tk.Entry(self.window, textvariable=self.gui_path, width=45).place(x=200, y=470,anchor='nw')
        tk.Button(self.window, text="路径选择",font=('Arial', 13), width=10, height=1, command=self.selectPath).place(x=580, y=464,anchor='nw')

        self.video_path = tk.StringVar()
        tk.Label(self.window, text="要拆分成图片的视频路径:", font=('Arial', 13), width=22, height=1).place(x=45, y=530, anchor='nw')
        tk.Entry(self.window, textvariable=self.video_path, width=38).place(x=250, y=530, anchor='nw')
        tk.Button(self.window, text="路径选择", font=('Arial', 13), width=10, height=1, command=self.video_selectPath).place(
            x=580, y=524, anchor='nw')

        self.scale_lenth =1000
        self.scale_lab = tk.Scale(self.window, label='滑动图片', from_=1, to=self.scale_lenth, orient=tk.HORIZONTAL, length=1100, showvalue=1,resolution=1, command=self.skip_selection)
        self.scale_lab.place(x=45, y=565,anchor='nw')

        self.mark_from_num = 1
        # self.mark_from_vnum = tk.StringVar()
        # self.mark_from_vnum.set(self.mark_from_num)
        #
        # self.mark_to_num = 1
        self.mark_to_vnum = tk.StringVar()
        self.mark_to_vnum.set(self.mark_to_num)

        self.del_from_num = 1
        self.del_from_vnum = tk.StringVar()
        self.del_from_vnum.set(self.del_from_num)

        self.del_to_num = 1
        self.del_to_vnum = tk.StringVar()
        self.del_to_vnum.set(self.del_to_num)

        tk.Label(self.window, text="从第", font=('Arial', 13), width=8, height=1).place(x=730, y=420, anchor='nw')
        tk.Entry(self.window, textvariable=self.mark_from_vnum,width=8).place(x=790, y=420, anchor='nw')
        tk.Label(self.window, text="张图到第", font=('Arial', 13), width=7, height=1).place(x=865, y=420, anchor='nw')
        tk.Entry(self.window, textvariable=self.mark_to_vnum, width=8).place(x=940, y=420, anchor='nw')
        tk.Label(self.window, text="张图", font=('Arial', 13), width=5, height=1).place(x=1000, y=420, anchor='nw')
        tk.Button(self.window, text="批量标注", font=('Arial', 13), width=6, height=1, command=self.mark_many_img).place(x=1065, y=413, anchor='nw')
        #
        tk.Label(self.window, text="从第", font=('Arial', 13), width=8, height=1).place(x=730, y=465, anchor='nw')
        tk.Entry(self.window, textvariable=self.del_from_vnum, width=8).place(x=790, y=465, anchor='nw')
        tk.Label(self.window, text="张图到第", font=('Arial', 13), width=7, height=1).place(x=865, y=465, anchor='nw')
        tk.Entry(self.window, textvariable=self.del_to_vnum, width=8).place(x=940, y=465, anchor='nw')
        tk.Label(self.window, text="张图", font=('Arial', 13), width=5, height=1).place(x=1000, y=465, anchor='nw')
        tk.Button(self.window, text="批量删除", font=('Arial', 13), width=6, height=1, command=self.del_many_img).place(x=1065, y=458, anchor='nw')

        self.img_list=[]
        self.current_img=1
        self.img_total_num=0

    def skip_selection(self,V):
        if self.img_list == []:
            pass
        else:
            self.skip_img(int(V))

    def update_img_info(self):
        self.img_mark_info='img mark info:  {}/{}'.format(self.img_list[self.current_img-1],self.img_total_num)
        self.mark_info_lab.configure(text=self.img_mark_info)

    def reset_to_from(self,value):
        self.del_from_num=value
        self.del_from_vnum.set(value)
        self.del_to_vnum.set(value)
        self.mark_from_num=value
        self.mark_to_num = value
        self.mark_from_vnum.set(value)
        self.mark_to_vnum.set(value)

    def selectPath(self):
        path_ = askdirectory() #返回文件夹路径
        self.path = path_
        self.gui_path.set(path_) #在图形化界面显示文件夹路径
        img_list =os.listdir(self.path)
        self.current_img = 1
        self.reset_to_from(self.current_img)
        #---------------获取截取图片顺序号的字符串和下标-------------------
        img_name_1 = img_list[0]
        img_name_len = len(img_name_1)
        for i in img_list[1:]:
            if len(i) == img_name_len:
                img_name_2 = i
                break
        try:
            img_name_1 = img_name_1.split('.')[0]
            img_name_2 = img_name_2.split('.')[0]
        except:
            tk.messagebox.showwarning('警告', '    选择的图片文件夹有误或包含非图片文件!       ')
            return

        same_part = ''
        same_part_list = []
        for index, i in enumerate(img_name_1):
            if i == img_name_2[index]:
                same_part += i
            if i != img_name_2[index]:
                same_part_list.append(same_part)
                same_part = ''
        same_part_list.append(same_part)
        for i in same_part_list:
            if i != '' and not i.isdigit():
                flag = i.strip('[0123456789]')
                break

        a = img_name_1.split(flag)
        if a[0] != '':
            j = 0
        else:
            j = 1
        # ---------------获取截取图片顺序号的字符串和下标-------------------

        try:
            for index, i in enumerate(img_list):
                img_name = i.split('.')[0]
                img_list[index] = (i, eval(img_name.split(flag)[j].lstrip('[0]')))
        except:
            tk.messagebox.showwarning('警告', '    选择的图片文件夹有误或包含非图片文件!       ')
            return
        img_list.sort(key=lambda x: x[1])
        self.img_list=[]
        for i in img_list:
            self.img_list.append(i[0])
        self.mark_img_dict = {}
        for i in self.img_list:
            self.mark_img_dict[i]=0


        self.skip_img(1)
        self.img_total_num = len(img_list)
        self.update_img_info()
        self.scale_lenth=self.img_total_num
        self.scale_lab.configure(to=self.scale_lenth)

        re_str=re.match('(.*/)(.*)', self.path)
        self.mark_img_folder=re_str.group(1)+'mark_{}'.format(re_str.group(2))
        if 'mark_{}'.format(re_str.group(2)) not in os.listdir(re_str.group(1)):
            os.mkdir(self.mark_img_folder)

    def video_selectPath(self):
        filename = tk.filedialog.askopenfilename()
        print(filename)
        self.video_path.set(filename)
        reader = cv2.VideoCapture(filename)
        # 视频的帧率
        fps = int(reader.get(cv2.CAP_PROP_FPS))
        re_str = re.match('(.*/)(.*)', filename)
        img_name_pre = re_str.group(2).split('.')[0]
        floder_name_pre = img_name_pre + '_{}'.format(fps)
        try:
            os.mkdir(re_str.group(1) + floder_name_pre)
        except Exception as e:
            return e
        img_name_tem = re_str.group(1) + floder_name_pre + '/' + '{}' + '_' + img_name_pre + '.jpg'
        print(img_name_tem)
        i = 1
        while True:
            ret, img_np = reader.read()
            # print(img_np)
            if not ret:
                break
            ret, jpeg = cv2.imencode('.jpg', img_np)
            frame = jpeg.tobytes()
            #
            with open(img_name_tem.format(i), 'wb') as f:
                #
                f.write(frame)
            i += 1
        tk.messagebox.showinfo('通知', '    拆分视频成功!     ')







    def save_var_value(self):
        value=self.var.get()
        key=self.img_list[self.current_img-1]
        self.mark_img_dict[key]=value


    def set_var_value(self):
        key=self.img_list[self.current_img-1]
        value=self.mark_img_dict[key]
        self.var.set(value)

    def next_img(self):
        self.save_var_value()
        self.current_img+=1
        self.skip_img(self.current_img)
        self.del_to_vnum.set(self.current_img)
        self.mark_to_vnum.set(self.current_img)


    def before_img(self):
        self.save_var_value()
        self.current_img -= 1
        self.skip_img(self.current_img)
        self.del_to_vnum.set(self.current_img)
        self.mark_to_vnum.set(self.current_img)


    def mark_many_img(self):
        try:
            self.mark_from_num=int(self.mark_from_vnum.get())
            self.mark_to_num = int(self.mark_to_vnum.get())
        except:
            tk.messagebox.showwarning('警告', '    输入的内容包含字符串,请输入纯数字!       ')
            return
        if self.mark_from_num<1 or self.mark_from_num>self.img_total_num:
            tk.messagebox.showwarning('警告', '    请输入1到{}之间的数字!     '.format(self.img_total_num))
            return
        if self.mark_to_num<1 or self.mark_to_num>self.img_total_num:
            tk.messagebox.showwarning('警告', '    请输入1到{}之间的数字!     '.format(self.img_total_num))
            return
        if self.mark_from_num>=self.mark_to_num:
            tk.messagebox.showwarning('警告', '    截取范围有误!无法标注{}到{}之间的图片     '.format(self.mark_from_num,self.mark_to_num))
            return

        value = self.var.get()
        for i in self.img_list[self.mark_from_num-1:self.mark_to_num]:
            self.mark_img_dict[i]=value
        if self.mark_to_num +1<self.img_total_num:
            self.mark_to_num=self.mark_to_num +1
        self.current_img=self.mark_to_num
        self.skip_img(self.current_img)
        self.mark_from_vnum.set(self.mark_to_num)
        self.del_from_vnum.set(self.mark_to_num)


    def del_many_img(self):
        try:
            self.del_from_num = int(self.del_from_vnum.get())
            self.del_to_num = int(self.del_to_vnum.get())
        except:
            tk.messagebox.showwarning('警告', '    输入的内容包含字符串,请输入纯数字!       ')
            return
        if self.del_from_num < 1 or self.del_from_num > self.img_total_num:
            tk.messagebox.showwarning('警告', '    请输入1到{}之间的数字!     '.format(self.img_total_num))
            return
        if self.del_to_num < 1 or self.del_to_num > self.img_total_num:
            tk.messagebox.showwarning('警告', '    请输入1到{}之间的数字!     '.format(self.img_total_num))
            return
        if self.del_from_num >= self.del_to_num:
            tk.messagebox.showwarning('警告','    截取范围有误!无法删除{}到{}之间的图片     '.format(self.del_from_num, self.del_to_num))
            return
        del self.img_list[self.del_from_num-1:self.del_to_num]

        self.current_img = self.del_from_num
        self.img_total_num = len(self.img_list)
        self.update_img_info()
        self.scale_lenth = self.img_total_num
        self.scale_lab.configure(to=self.scale_lenth)



        self.del_to_num = self.current_img
        self.skip_img(self.current_img)
        self.mark_to_vnum.set(self.current_img)
        self.del_to_vnum.set(self.current_img)


    def skip_img(self,img_num):
        _img = Image.open(self.path+'/'+self.img_list[img_num-1])
        _img = _img.resize((640, 360))
        self.img = ImageTk.PhotoImage(_img)
        self.img_lab.configure(image=self.img)
        self.current_img=img_num
        self.set_var_value()
        self.update_img_info()


        self.del_to_vnum.set(self.current_img)
        self.mark_to_vnum.set(self.current_img)

    def create_mark_img(self):
        mark_img_list=os.listdir(self.mark_img_folder)
        if mark_img_list !=[]:
            shutil.rmtree(self.mark_img_folder)
            os.mkdir(self.mark_img_folder)
        for i in self.img_list:
            value=self.mark_img_dict[i]
            shutil.copyfile(self.path+'/'+i,self.mark_img_folder+'/'+i.split('.')[0]+'_{}'.format(value)+'.jpg')
        tk.messagebox.showinfo('通知', '    生成标标注图片成功!     ')




window=Tk_window()
window.window.mainloop()
