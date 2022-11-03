import os
import sys

import tool

originPath = sys.path[0]

sys.path.append(originPath + "\\slpp-23-master")

os.chdir(originPath)

from slpp import slpp as lua


def gen_tag(dic):
    out = {}
    re = False
    for tp in dic:
        for tag in dic[tp]:
            if tp not in out:
                out[tp] = {}
            if tag not in out[tp]:
                out[tp][tag] = []
            for item in dic[tp][tag]:
                if "#" in item:
                    for i in dic[tp][item[11:]]:
                        if i.startswith("minecraft:"):
                            out[tp][tag].append(i[10:])
                        else:
                            out[tp][tag].append(i)
                    re = True
                else:
                    if item.startswith("minecraft:"):
                        out[tp][tag].append(item[10:])
                    else:
                        out[tp][tag].append(item)
    if re:
        return gen_tag(out)
    return out


def gen_id(dic):
    out = {}
    for tp in dic:
        if tp not in out:
            out[tp] = {}
        for tag in dic[tp]:
            for i in dic[tp][tag]:
                if i not in out[tp]:
                    out[tp][i] = []
                out[tp][i].append(tag)
    out = tool.sort(out)
    return out


if __name__ == "__main__":
    result = {}
    if len(sys.argv) == 1:
        print("usage: main.py [path]")
    else:
        tagdic = {}
        temp = sorted(sys.argv[1:])
        for pa in temp:
            tagdic = tool.load(pa, tagdic)

        tagdic = tool.sort(tagdic)
        result["tag_ori"] = tagdic

        result["tag"] = gen_tag(tagdic)

        result["ID"] = gen_id(result["tag"])
        with open("out.txt", "w") as fiout:
            fiout.write(lua.encode(result))
