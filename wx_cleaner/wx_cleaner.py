def cfile(fdir, fname):
    f = open(fdir+fname, 'r')
    filedata = f.readlines()
    f.close()
    newcontent = ''
    for line in filedata:
        if line.startswith('# -*-'):
            pass
        elif line.startswith('##'):
            pass
        elif line.startswith('import wx.xrc'):
            pass
        elif line.startswith('def __init__'):
            newcontent += line.replace(', parent','')
        elif line.startswith('wx.Frame.__init__'):
            newcontent += line.replace('parent','None')
        else:
            newcontent += line

    return newcontent

fdir = '/home/mvysochinenko/workspace_wxformbuilder/'
fname = 'noname.py'
newcontent = cfile(fdir,fname)
print(newcontent)