#coding:utf-8
import os
import platform

import jpype

class TestJpype:
    def __init__(self):
        jvm_path = jpype.getDefaultJVMPath()
        dependence_dirs = list()
        dependence_dirs.append(os.path.join(os.path.abspath("Hel2pool")))  # 当前目录，所要使用的jar则放在该目录
        dependence_dirs.append(r'D:\A3pool\Eclipse4.5.1x86\sdk\tools\lib')  # 被依赖的jar所在的目录，被依赖的目录可能由多个，自行append即可
        dependence_dirs.append(r'D:\A3pool\Eclipse4.5.1x86\sdk\tools\lib\x86')
        if platform.system() == "Windows":  # 处理分隔符号
            java_dirs = ";".join(dependence_dirs)
        else:
            java_dirs = ":".join(dependence_dirs)
        jpype.startJVM(jvm_path, '-ea', '-Djava.ext.dirs=%s' % java_dirs, convertStrings=True)
        self.By = jpype.JClass('com.android.hvhelper.By')
        self.CompType = jpype.JClass('com.android.hvhelper.CompType')
        self.NodeLocInfo = jpype.JClass('com.android.hvhelper.NodeLocInfo')
        self.NodeLocMap = jpype.JClass('com.android.hvhelper.NodeLocMap')
        self.P = jpype.JClass('com.android.hvhelper.P')
        self.Id = jpype.JClass('com.android.hvhelper.Id')
        # self.ViewNode = jpype.JClass('com.android.hierarchyviewerlib.models.ViewNode')
        self.class_hvh = jpype.JClass('com.android.hvhelper.HvHelper')
        self.instn_hvh = self.class_hvh("127.0.0.1:21503")  # 实例化java类

    def find_node(self, by):
        # class_hvh.getInstance().findNode(by)
        return self.instn_hvh.findNode(by)

    def find_nodes(self, by):
        # class_hvh.getInstance().findNode(by)
        return self.instn_hvh.findNodes(by)

    def find_nodes_by_maps(self, parNode, locMaps):
        return self.instn_hvh.findNodesByMaps(parNode, locMaps)

    def getWindow(self, window_name,  ct):
        return self.instn_hvh.getWindow(window_name, ct)

    def getViewIdList(self):
        return self.instn_hvh.getViewIdList()


tj = TestJpype()
# print(f"枚举值：{tj.CompType.Contains}")
# node = tj.find_node(tj.By.id("id/showToastButton"))
# window = tj.getWindow("testapp", tj.CompType.Contains)
# ids = tj.getViewIdList()
# nodes = tj.find_nodes(tj.By.id("id/text1"))
# node = nodes.get(1)
node = tj.find_node(tj.By.id("id/list"))
locInfo_00_Id = tj.NodeLocInfo(tj.Id.list, tj.P.mID, tj.CompType.Equals);
locInfo_01_Id = tj.NodeLocInfo(tj.Id.text1, tj.P.mID, tj.CompType.Equals);
locMap_00 = tj.NodeLocMap();
locMap_00.add(locInfo_00_Id);
locMap_01 = tj.NodeLocMap();
locMap_01.add(locInfo_01_Id);
# locMaps = ArrayList <> ();
locMaps = jpype.java.util.ArrayList();
locMaps.add(locMap_00);
locMaps.add(locMap_01);
outNodes = tj.find_nodes_by_maps(node, locMaps);
jpype.shutdownJVM()
pass

