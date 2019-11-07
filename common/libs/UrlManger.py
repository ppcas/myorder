# coding=utf-8 
# /usr/bin/env python

class UrlManger(object):
    @staticmethod
    def buildurl(path):
        return path

    @staticmethod
    def buildstaticurl(path):
        ver = "%s"%(22222)
        path = "/static" + path + "?ver=" + ver
        return UrlManger.buildurl(path)

