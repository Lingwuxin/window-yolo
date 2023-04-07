from datetime import date
from typing import List
import xml.etree.cElementTree as ET
import os, sys
import glob

from numpy import save
class Data():
    def __init__(self) -> None:
        self.high=None
        self.weigh=None
        self.type=None
        self.xmin=None
        self.ymin=None
        self.xmax=None
        self.ymax=None
    def getBndBox(self,bndbox:list):
        self.xmin=float(bndbox[0])
        self.ymin=float(bndbox[1])
        self.xmax=float(bndbox[2])
        self.ymax=float(bndbox[3])
    def getSize(self,size:list):
        self.weigh=float(size[0])
        self.high=float(size[1])
    def toLine(self)-> List[float]:
        x=(self.xmax+self.xmin)/2/self.weigh
        y=(self.ymax+self.ymin)/2/self.high
        w=(self.xmax-self.xmin)/self.weigh
        h=(self.ymax-self.ymin)/self.high
        return [self.type,x,y,w,h]
class SaveData():
    def __init__(self):
        self.filename=None
        self.data_list:List[Data]=[]
    
    def save(self,path:str=None):
        if path==None:
            path='labels'
        if not os.path.exists(path):
            os.mkdir(path)
        with open(f'{path}/{self.filename}','w') as f:
            datas=''
            for d in self.data_list:
                dataline=[]
                for data in d.toLine():
                    dataline.append(str(data))
                datas+=' '.join(dataline)+'\n'
            f.write(datas)
        
class HandleVocData():
    def __init__(self):
        self.class_txt_dict={}
        self.class_txt_list=[]
        self.file_paths=[]
        self.handle={
            'filename':self.getFileName,
            'size':self.getSize,
            'object':self.getObject,
        }
        self.data=Data()
        self.saves=SaveData()
    def getFileName(self,filename:ET.Element):
        name=filename.text
        name=name[:name.rfind('.')]
        self.saves.filename=name+'.txt'
    def getSize(self,size:ET.Element):
        s=[]
        for i in size:
            s.append(i.text)
        self.weigh=int(s[0])
        self.heigh=int(s[1])
    def getObject(self,object_:ET.Element):
        for child in object_:
            if child.tag=='name':
                if child.text not in self.class_txt_dict:
                    self.class_txt_dict[child.text]=len(self.class_txt_dict)
                self.data.type=self.class_txt_dict[child.text]
                continue
            if child.tag=='bndbox':
                bndbox=[]
                for i in child:
                    bndbox.append(i.text)
                self.data.getBndBox(bndbox)

    def __call__(self, path:str,savepath:str=None)->None:
        xml_list= glob.glob(path + '\*.xml')
        for xml_path in xml_list:
            tree = ET.parse(xml_path)
            root = tree.getroot()
            for child in root.iter():
                if child.tag in self.handle:
                    self.handle[child.tag](child)
                if child.tag == 'object':
                    self.data.weigh=self.weigh
                    self.data.high=self.heigh
                    self.saves.data_list.append(self.data)
                    self.data=Data()
            self.saves.save(savepath)
            self.saves=SaveData()
        print(self.class_txt_dict)
xml_dir=r'D:\Datasets\garbage\garbage\新建文件夹\validation\annotations'
a=HandleVocData()
a(xml_dir,r'D:\Datasets\garbage\garbage\labels\val')