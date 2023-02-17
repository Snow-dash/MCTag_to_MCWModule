import sys, json, os


def upper_dirs(path):
    return str.join("\\",str.split(path, "\\")[0:-1])

def lastone(path):
    return  str.split(path,"\\")[-1]

def lasttwo(path):
    return str.join("\\",str.split(path,"\\")[-2:-1])

def backtwo(path):
    return str.split(path,"\\")[-2]


def load(path,out=None):  # \data\minecraft\tags
    if out is None:
        out = {}
    tag_path = path + "\\data\\minecraft\\tags"
    tagpath_li = []
    for root, dirs, files in os.walk(tag_path, topdown=True):
        #print(root, dirs, files)
        # print("\n")

        if len(files) != 0:
            #print(root, dirs, files)
            #print(upper_dirs(root))
            if upper_dirs(root) in tagpath_li:
                for fi in files:
                    with open(root + "\\" + fi) as onejsonfi:
                        context = json.loads(onejsonfi.read())
                        if backtwo(root) not in out:
                            out[backtwo(root)] = {}
                        if lastone(root) + "/" + fi[0:-5] not in out[backtwo(root)]:
                            out[backtwo(root)][lastone(root) + "/" + fi[0:-5]] = []
                        for item in context["values"]:
                            out[backtwo(root)][lastone(root) + "/" + fi[0:-5]].append(item)
            else:
                for fi in files:
                    with open(root + "\\" + fi) as onejsonfi:
                        context = json.loads(onejsonfi.read())
                        if lastone(root) not in out:
                            out[lastone(root)] = {}
                        if fi[0:-5] not in out[lastone(root)]:
                            out[lastone(root)][fi[0:-5]] = []
                        for item in context["values"]:
                            out[lastone(root)][fi[0:-5]].append(item)


            if root not in tagpath_li:
                tagpath_li.append(root)
    return out

def sort(dic):
    for tp in dic:
        for tag in dic[tp]:
            dic[tp][tag] = sorted(list(set(dic[tp][tag])))
    return dic

