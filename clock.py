#-*-coding:utf-8-*-
'''
Created on 2015年11月25日

@author: Zroad
'''

from Tkinter import *
import time

class StopWatch(Frame):
    """实现一个秒表部件"""
    msec = 50

    def __init__(self,parent = None,**kw):
        Frame.__init__(self,parent,kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = False
        self.timestr = StringVar()
        self.makeWidgets() 

    def makeWidgets(self):
        """制作时间标签"""
        l = Label(self,textvariable = self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill = X, expand = NO, pady = 2, padx = 2)

    def _update(self):
        """用逝去的时间更新标签"""
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(self.msec,self._update)

    def _setTime(self,elap):
        """将时间格式改为分:秒:百分秒"""
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0-seconds)*100)
        self.timestr.set('%02d:%2d:%02d' % (minutes,seconds,hseconds))

    def start(self):
        """启动秒表，如果已启动则忽略"""
        if not self._running:
           self._start = time.time() - self._elapsedtime
           self._update() 
           self._running = True

    def stop(self):
        """停止秒表，若已停止则忽略"""
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = False

    def reset(self):
        """重设秒表"""
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)

if __name__ == "__main__":
    def main():
        root = Tk()
        sw = StopWatch(root)
        sw.pack(side = TOP)
        Button(root, text = 'start', command = sw.start).pack(side = LEFT)
        Button(root, text = 'stop', command = sw.stop).pack(side = LEFT)
        Button(root, text = 'reset', command = sw.reset).pack(side = LEFT)
        Button(root, text = 'quit', command = root.quit).pack(side = LEFT)
        root.mainloop()

    main()
