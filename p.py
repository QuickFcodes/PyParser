PLUS = "+"
MUL = "*"
SUB = "-"
LET = "let"
NUM = "num"
DIV = "/"
FUNC = "func"
POS = "."
ID = "id"
RIGH = "}"
LEFT = "{"
EDL = "endl"
LP = "("
RP = ")"
CL = ":"
EQU = "="
PLEQ = "+="
SUWQ = "-="
MUEQ = "*="
DIEQ = "/="
CMA = ","
STR = "string"
SM = "<"
BM = ">"
NO = "!"
FOR = "for"
IF = "if"
WHILE = "while"
SWITCH = "switch"
CASE = "case"
alls = "+-=/*{}().:\n ,<>!\";"
dl = {"for":FOR,"if":IF,"while":WHILE,"switch":SWITCH,"let":LET,"case":CASE}
class token:
    def __init__(self,t: str,v: any = None) -> None:
        self.t = t
        self.v = v
def putt(g: token):
    return f"<{g.t}:{g.v}>"
buff: str = ''
tks: list[token] = []
def loader(name: str) -> None:
    global buff
    try:
        j = open(name,"r")
    except:
        print("未找到文件")
        return
    buff = j.read()
    j.close()
    return
def inte() -> None:
    global buff,tks
    i=0
    j:list = []
    for l in buff:
        j.append(l)
    while i < len(j):
        match j[i]:
            case '+':
                tks.append(token(PLUS))
                i+=1
                continue
            case ' ':
                i+=1
                continue
            case '-':
                tks.append(token(SUB))
                i+=1
                continue
            case '*':
                tks.append(token(MUL))
                i+=1
                continue
            case '/':
                tks.append(token(DIV))
                i+=1
                continue
            case ':':
                tks.append(token(CL))
                i+=1
                continue
            case ";":
                tks.append(token(EDL))
                i+=1
                continue
            case '\n':
                tks.append(token(EDL))
                i+=1
                continue
            case '{':
                tks.append(token(LEFT))
                i+=1
                continue
            case '}':
                tks.append(token(RIGH))
                i+=1
                continue
            case '(':
                tks.append(token(LP))
                i+=1
                continue
            case ')':
                tks.append(token(RP))
                i+=1
                continue
            case '.':
                tks.append(token(POS))
                i+=1
                continue
            case "=":
                tks.append(token(EQU))
                i+=1
                continue
            case ',':
                tks.append(token(CMA))
                i+=1
                continue
            case '>':
                tks.append(token(BM))
                i+=1
                continue
            case "<":
                tks.append(token(SM))
                i+=1
                continue
            case '!':
                tks.append(token(NO))
                i+=1
                continue
        cache = ""
        castr = ""
        stfg = 0
        if j[i] == "\"":
            stfg = 1
        while i<len(j):
            if (j[i] not in alls) and (stfg==0):
                cache = cache + j[i]
            elif stfg == 1:
                cache = cache + j[i]
                if (j[i] == "\"") and (cache != "\""):
                    stfg=0
                    i+=1
                    break
            else:
                break
            i+=1
        if cache != "":
            try:
                tks.append(token(NUM,int(cache)))
            except:
                if cache[0]!="\"":
                    tks.append(token(ID,cache))
                else:
                    tks.append(token(STR,cache))
            continue
        i+=1
    for i in range(len(tks)):
        if tks[i].t == ID:
            if tks[i].v in dl:
                tks[i].t = dl[tks[i].v]
                tks[i].v = None
while 1:
    u = input(":")
    if u == "exit":
        exit(0)
    loader(u)
    inte()
    u = input(":")
    u = open(u,"w")
    for i in range(len(tks)):
        if not (i==len(tks)-1):
            u.write(putt(tks[i])+"\n")
        else:
            u.write(putt(tks[i]))
    u.close()
