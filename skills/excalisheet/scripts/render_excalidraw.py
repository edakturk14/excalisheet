#!/usr/bin/env python3
import json, sys, random, time
from pathlib import Path

W = 1600
MARGIN = 40
LEFT_W = 350
PANEL_GAP = 22
PANEL_H = 215
HEADER_H = 180
SUMMARY_H = 145

def seed():
    return random.randint(1, 2_000_000_000)

def base(t, x, y, w, h, stroke="#1e1e1e", bg="transparent", rough=0, roundness=None):
    s = seed()
    return {
        "id": f"el_{s}",
        "type": t, "x": x, "y": y, "width": w, "height": h, "angle": 0,
        "strokeColor": stroke, "backgroundColor": bg, "fillStyle": "hachure",
        "strokeWidth": 2, "strokeStyle": "solid", "roughness": rough, "opacity": 100,
        "groupIds": [], "frameId": None, "index": None, "roundness": roundness,
        "seed": s, "version": 1, "versionNonce": seed(), "isDeleted": False,
        "boundElements": [], "updated": int(time.time()*1000), "link": None, "locked": False
    }

def text(x, y, w, h, value, size=18, align="left", color="#1e1e1e"):
    e = base("text", x, y, w, h, stroke=color, rough=0)
    e.update({
        "fontSize": size, "fontFamily": 1, "text": value, "rawText": value,
        "textAlign": align, "verticalAlign": "middle", "containerId": None,
        "originalText": value, "autoResize": True, "lineHeight": 1.25
    })
    return e

def rect(x, y, w, h, bg="#ffffff", stroke="#9c9c9c", rough=0):
    return base("rectangle", x, y, w, h, stroke=stroke, bg=bg, rough=rough, roundness={"type": 3})

def arrow(x1, y1, x2, y2, stroke="#1e1e1e"):
    x, y = min(x1,x2), min(y1,y2)
    e = base("arrow", x, y, abs(x2-x1), abs(y2-y1), stroke=stroke, rough=1)
    e.update({
        "points": [[x1-x,y1-y],[x2-x,y2-y]], "lastCommittedPoint": None,
        "startBinding": None, "endBinding": None, "startArrowhead": None,
        "endArrowhead": "arrow", "elbowed": False
    })
    return e

def line(x1,y1,x2,y2,stroke="#d0d0d0",width=1):
    x, y = min(x1,x2), min(y1,y2)
    e = base("line", x, y, abs(x2-x1), abs(y2-y1), stroke=stroke, rough=0)
    e["strokeWidth"] = width
    e.update({"points":[[x1-x,y1-y],[x2-x,y2-y]],"lastCommittedPoint":None,
              "startBinding":None,"endBinding":None,"startArrowhead":None,"endArrowhead":None})
    return e

def add_box(els, x, y, w, h, title, body=None, stroke="#9c9c9c", bg="#ffffff"):
    els.append(rect(x,y,w,h,bg=bg,stroke=stroke))
    els.append(text(x+22,y+16,w-44,30,title,22))
    body = body or []
    if isinstance(body, str):
        body = [body]
    if body:
        els.append(text(x+22,y+52,w-44,h-62,"\n".join(body),16))

def render_section(els, sec, y, accent, tint):
    panel_x = MARGIN
    panel_w = W - 2*MARGIN
    els.append(rect(panel_x,y,panel_w,PANEL_H,bg="#ffffff",stroke="#c9c9c9"))
    divider_x = panel_x + LEFT_W
    els.append(line(divider_x,y+24,divider_x,y+PANEL_H-24))
    els.append(rect(65,y+24,54,42,bg=tint,stroke=tint))
    els.append(text(65,y+24,54,42,str(sec.get("number","")),20,"center",accent))
    els.append(text(65,y+78,265,70,sec.get("title",""),26))
    els.append(text(65,y+148,265,55,sec.get("why",""),17,color="#444444"))

    cx = divider_x + 35
    cw = panel_x + panel_w - cx - 30
    layout = sec.get("layout","flow")
    data = sec.get("data",{})

    if layout == "compare":
        gap = 80
        bw = (cw-gap)//2
        add_box(els,cx+20,y+38,bw-20,135,data["left"]["title"],data["left"].get("body",[]))
        add_box(els,cx+bw+gap,y+38,bw-20,135,data["right"]["title"],data["right"].get("body",[]))
        els.append(arrow(cx+bw+10,y+105,cx+bw+gap-10,y+105,stroke=accent))
    elif layout == "flow":
        steps = data.get("steps",[])
        n=max(1,len(steps))
        gap=34
        bw=(cw-gap*(n-1))//n
        for i,st in enumerate(steps):
            bx=cx+i*(bw+gap)
            add_box(els,bx,y+58,bw,95,st.get("title",""),st.get("body",[]))
            if i<n-1:
                els.append(arrow(bx+bw+6,y+105,bx+bw+gap-6,y+105))
        if data.get("note"):
            els.append(text(cx,y+170,cw,28,data["note"],14,color="#555555"))
    elif layout == "route":
        add_box(els,cx,y+72,150,75,data.get("source","Request"),[])
        router_x=cx+215
        add_box(els,router_x,y+40,370,140,data.get("router",{}).get("title","Routing"),
                ["• "+x for x in data.get("router",{}).get("body",[])])
        els.append(arrow(cx+160,y+110,router_x-10,y+110))
        dx=router_x+475
        dests=data.get("destinations",[])
        for i,d in enumerate(dests[:4]):
            by=y+42+i*42
            els.append(rect(dx,by,220,34,bg="#ffffff",stroke="#9c9c9c"))
            els.append(text(dx,by,220,34,d,16,"center"))
            els.append(arrow(router_x+380,y+110,dx-10,by+17))
        if data.get("note"):
            els.append(text(cx,y+185,cw,25,data["note"],14,color="#555555"))
    elif layout == "stack":
        sx=cx+30
        count=min(4,int(data.get("stack_count",3)))
        for i in range(count):
            els.append(rect(sx,y+48+i*38,190,30,bg="#ffffff",stroke="#666666"))
        els.append(text(sx+35,y+48+count*38,130,24,data.get("stack_title","SERVER"),15,"center"))
        bx=cx+360
        details=data.get("details",[])[:2]
        boxh=150
        els.append(rect(bx,y+34,cw-(bx-cx)-15,boxh,bg="#ffffff",stroke="#8f8f8f"))
        for i,item in enumerate(details):
            yy=y+48+i*68
            els.append(text(bx+25,yy,145,28,item.get("title",""),21))
            els.append(text(bx+180,yy,390,48,"\n".join(item.get("body",[])),15))
            if i==0 and len(details)>1:
                els.append(line(bx+20,y+105,bx+cw-(bx-cx)-35,y+105))
        els.append(arrow(sx+205,y+105,bx-10,y+105))
    elif layout == "tokens":
        add_box(els,cx+10,y+65,220,85,data.get("prompt","Prompt"),[])
        els.append(arrow(cx+240,y+108,cx+310,y+108))
        add_box(els,cx+325,y+45,420,125,data.get("context_title","Input can include:"),
                ["• "+x for x in data.get("context",[])])
        els.append(arrow(cx+755,y+108,cx+835,y+108))
        outputs=data.get("outputs",[])[:2]
        for i,o in enumerate(outputs):
            els.append(rect(cx+850,y+52+i*60,240,44,bg=tint,stroke=tint))
            els.append(text(cx+850,y+52+i*60,240,44,o,17,"center",accent))
    elif layout == "list":
        items=data.get("items",[])[:4]
        gap=28
        bw=(cw-gap*(len(items)-1))//max(1,len(items))
        for i,item in enumerate(items):
            bx=cx+i*(bw+gap)
            add_box(els,bx,y+55,bw,105,item.get("title",""),[item.get("body","")])

def render_layout(els, layout, data, x, y, w, h, accent, tint):
    if layout == "compare":
        gap = 80
        bw = (w-gap)//2
        add_box(els,x,y,bw,h,data["left"]["title"],data["left"].get("body",[]))
        add_box(els,x+bw+gap,y,bw,h,data["right"]["title"],data["right"].get("body",[]))
        els.append(arrow(x+bw+10,y+h/2,x+bw+gap-10,y+h/2,stroke=accent))
    elif layout == "flow":
        steps=data.get("steps",[])
        n=max(1,len(steps))
        gap=34
        bw=(w-gap*(n-1))//n
        for i,st in enumerate(steps):
            bx=x+i*(bw+gap)
            add_box(els,bx,y,bw,h,st.get("title",""),st.get("body",[]))
            if i<n-1:
                els.append(arrow(bx+bw+6,y+h/2,bx+bw+gap-6,y+h/2))
    elif layout == "route":
        add_box(els,x,y+h/2-40,150,80,data.get("source","Request"),[])
        router_x=x+220
        add_box(els,router_x,y+h/2-75,360,150,data.get("router",{}).get("title","Routing"),
                ["• "+v for v in data.get("router",{}).get("body",[])])
        els.append(arrow(x+160,y+h/2,router_x-10,y+h/2))
        dx=router_x+470
        dests=data.get("destinations",[])[:4]
        for i,d in enumerate(dests):
            by=y+25+i*55
            els.append(rect(dx,by,220,40,bg="#ffffff",stroke="#9c9c9c"))
            els.append(text(dx,by,220,40,d,16,"center"))
            els.append(arrow(router_x+370,y+h/2,dx-10,by+20))
    elif layout == "stack":
        sx=x+30
        count=min(4,int(data.get("stack_count",3)))
        for i in range(count):
            els.append(rect(sx,y+30+i*45,190,34,bg="#ffffff",stroke="#666666"))
        els.append(text(sx+30,y+30+count*45,130,25,data.get("stack_title","SERVER"),15,"center"))
        bx=x+340
        details=data.get("details",[])[:2]
        els.append(rect(bx,y,w-(bx-x),h,bg="#ffffff",stroke="#8f8f8f"))
        for i,item in enumerate(details):
            yy=y+30+i*(h//2)
            els.append(text(bx+25,yy,155,30,item.get("title",""),21))
            els.append(text(bx+190,yy,w-(bx-x)-220,50,"\n".join(item.get("body",[])),15))
            if i==0 and len(details)>1:
                els.append(line(bx+20,y+h/2,bx+w-(bx-x)-20,y+h/2))
        els.append(arrow(sx+205,y+h/2,bx-10,y+h/2))
    elif layout == "tokens":
        add_box(els,x,y+h/2-45,220,90,data.get("prompt","Prompt"),[])
        els.append(arrow(x+230,y+h/2,x+300,y+h/2))
        add_box(els,x+315,y+20,420,h-40,data.get("context_title","Input can include:"),
                ["• "+v for v in data.get("context",[])])
        els.append(arrow(x+745,y+h/2,x+825,y+h/2))
        for i,o in enumerate(data.get("outputs",[])[:2]):
            els.append(rect(x+840,y+30+i*65,240,46,bg=tint,stroke=tint))
            els.append(text(x+840,y+30+i*65,240,46,o,17,"center",accent))
    elif layout == "list":
        items=data.get("items",[])[:4]
        gap=28
        bw=(w-gap*(len(items)-1))//max(1,len(items))
        for i,item in enumerate(items):
            bx=x+i*(bw+gap)
            add_box(els,bx,y,bw,h,item.get("title",""),[item.get("body","")])

def render_diagram(spec):
    accent=spec.get("accent","#7C5CFC")
    tint=spec.get("accent_tint","#F4F0FF")
    els=[]
    els.append(text(70,45,1200,70,spec["title"],38))
    subtitle=spec.get("subtitle","")
    if subtitle:
        els.append(text(70,110,1200,50,subtitle,19,color="#555555"))
    render_layout(els,spec.get("layout","compare"),spec.get("data",{}),70,210,1460,300,accent,tint)
    return {
        "type":"excalidraw","version":2,"source":"https://excalidraw.com",
        "elements":els,
        "appState":{"gridSize":None,"viewBackgroundColor":"#ffffff","currentItemFontFamily":1},
        "files":{}
    }, 580

def render(spec):
    if spec.get("mode") == "diagram":
        return render_diagram(spec)
    accent=spec.get("accent","#7C5CFC")
    tint=spec.get("accent_tint","#F4F0FF")
    els=[]
    els.append(text(70,40,900,100,spec["title"],40))
    els.append(line(985,45,985,145,width=2))
    els.append(text(1030,55,450,90,spec.get("subtitle",""),21,color="#333333"))

    y=HEADER_H
    for sec in spec.get("sections",[])[:6]:
        render_section(els,sec,y,accent,tint)
        y += PANEL_H + PANEL_GAP

    els.append(rect(MARGIN,y,W-2*MARGIN,SUMMARY_H,bg="#ffffff",stroke="#c9c9c9"))
    els.append(text(70,y+45,200,42,"In short:",30))
    els.append(line(270,y+25,270,y+SUMMARY_H-25))
    summary=spec.get("summary",[])[:6]
    sx=320
    available=W-360
    gap=28
    bw=(available-gap*(len(summary)-1))//max(1,len(summary))
    for i,item in enumerate(summary):
        bx=sx+i*(bw+gap)
        els.append(rect(bx,y+38,bw,72,bg="#ffffff",stroke="#9c9c9c"))
        els.append(text(bx+8,y+38,bw-16,72,item,16,"center"))
        if i<len(summary)-1:
            els.append(arrow(bx+bw+5,y+74,bx+bw+gap-5,y+74,stroke=accent))

    return {
        "type":"excalidraw","version":2,"source":"https://excalidraw.com",
        "elements":els,
        "appState":{"gridSize":None,"viewBackgroundColor":"#ffffff","currentItemFontFamily":1},
        "files":{}
    }, y+SUMMARY_H+40

def main():
    if len(sys.argv)<2:
        print("usage: render_excalidraw.py spec.json [output.excalidraw]")
        raise SystemExit(2)
    spec_path=Path(sys.argv[1])
    spec=json.loads(spec_path.read_text(encoding="utf-8"))
    out=Path(sys.argv[2]) if len(sys.argv)>2 else spec_path.with_suffix(".excalidraw")
    doc,_=render(spec)
    out.write_text(json.dumps(doc,ensure_ascii=False,indent=2),encoding="utf-8")
    print(out)

if __name__=="__main__":
    main()
