"""LakaPDF Alpha 0.3.1 — © 2026 Larx Vo — vovinhlac.com"""
import sys, os, tempfile, tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import fitz
from PIL import Image, ImageTk
def self_test():
 with tempfile.TemporaryDirectory() as d:
  p=os.path.join(d,'test.pdf');a=fitz.open();a.new_page().insert_text((70,80),'LakaPDF test');a.save(p);a.close()
  with fitz.open(p) as r:assert r.is_pdf and 'LakaPDF' in r[0].get_text()
 print('LakaPDF SELF_TEST_OK')
class App(tk.Tk):
 def __init__(self):
  super().__init__();self.title('LakaPDF · Larx Vo');self.geometry('1200x790');self.configure(bg='#eaf0f6')
  self.doc=None;self.path=None;self.index=0;self.zoom=1.;self.changed=False;self.selected=None;self.history=[]
  self.ui();self.protocol('WM_DELETE_WINDOW',self.close)
 def ui(self):
  top=tk.Frame(self,bg='white');top.pack(fill='x')
  tk.Label(top,text='▣ LakaPDF',bg='white',font=('Segoe UI',17,'bold')).pack(side='left',padx=16)
  actions=[('Open',self.open),('Save',self.save),('Save As',self.save_as),('Undo',self.undo),('About',self.about),('Prev',lambda:self.page(-1)),('Next',lambda:self.page(1)),('Zoom +',lambda:self.scale(.2)),('Zoom -',lambda:self.scale(-.2)),('Find',self.find),('Highlight',self.highlight),('Edit selected',self.edit),('Add text',self.add_text),('Rotate',self.rotate),('Delete',self.delete),('Merge',self.merge),('Split',self.split),('Export PNG',self.png),('Sign image',self.sign)]
  for n,f in actions:
   tk.Button(top,text=n,command=f,relief='flat',bg='white',padx=6,pady=12).pack(side='left')
  body=tk.PanedWindow(self,orient='horizontal',sashwidth=5,bg='#d2d9e5');body.pack(fill='both',expand=True)
  l=tk.Frame(body,bg='white',width=125);body.add(l,minsize=90)
  tk.Label(l,text='PAGES',bg='white').pack(pady=10)
  self.pages=tk.Listbox(l,relief='flat');self.pages.pack(fill='both',expand=True)
  self.pages.bind('<<ListboxSelect>>',self.choose_page)
  center=tk.Frame(body);body.add(center,minsize=380)
  self.cv=tk.Canvas(center,bg='#d6deeb',highlightthickness=0);self.cv.pack(side='left',fill='both',expand=True)
  sy=tk.Scrollbar(center,command=self.cv.yview);sy.pack(side='right',fill='y');self.cv.config(yscrollcommand=sy.set)
  self.cv.bind('<Button-1>',self.pick)
  r=tk.Frame(body,bg='white',width=220);body.add(r,minsize=140)
  tk.Label(r,text='INSPECTOR',bg='white').pack(pady=9)
  self.info=tk.Text(r,wrap='word',relief='flat');self.info.pack(fill='both',expand=True)
  tk.Button(r,text='Inspect fonts',command=self.fonts).pack(fill='x')
  self.status=tk.Label(self,text='Open PDF to begin · © 2026 Larx Vo · vovinhlac.com',bg='white',anchor='w');self.status.pack(fill='x')
 def need(self):
  if self.doc:return True
  messagebox.showinfo('LakaPDF','Open a PDF first');return False
 def confirm(self):
  if not self.changed:return True
  a=messagebox.askyesnocancel('Unsaved changes','Save changes?')
  if a is None:return False
  return self.save() if a else True
 def open(self):
  p=filedialog.askopenfilename(filetypes=[('PDF','*.pdf')])
  if not p or not self.confirm():return
  try:
   d=fitz.open(p)
   if not d.is_pdf:raise ValueError('Not PDF')
   if d.needs_pass:
    pwd=simpledialog.askstring('Password','PDF password:',show='*')
    if not pwd or not d.authenticate(pwd):d.close();return
   if self.doc:self.doc.close()
   self.doc=d;self.path=p;self.index=0;self.changed=False;self.history=[];self.selected=None;self.refresh()
  except Exception as e:messagebox.showerror('Open failed',str(e))
 def snapshot(self):
  try:self.history.append(self.doc.tobytes(garbage=3,deflate=True));self.history=self.history[-10:];return True
  except Exception as e:messagebox.showerror('Snapshot failed',str(e));return False
 def undo(self):
  if self.doc and self.history:
   b=self.history.pop();self.doc.close();self.doc=fitz.open(stream=b,filetype='pdf');self.index=min(self.index,len(self.doc)-1);self.changed=True;self.refresh()
 def refresh(self):
  self.pages.delete(0,'end')
  for i in range(len(self.doc)):self.pages.insert('end','Page '+str(i+1))
  self.pages.selection_set(self.index);self.pages.see(self.index);self.render()
  self.status.config(text=f'{os.path.basename(self.path or "Untitled")} · {self.index+1}/{len(self.doc)} · {int(self.zoom*100)}%'+(' · Modified' if self.changed else ''))
 def render(self):
  p=self.doc[self.index].get_pixmap(matrix=fitz.Matrix(self.zoom,self.zoom),alpha=False)
  self.photo=ImageTk.PhotoImage(Image.frombytes('RGB',(p.width,p.height),p.samples));self.cv.delete('all')
  self.x=max(16,(self.cv.winfo_width()-p.width)//2);self.cv.create_image(self.x,16,image=self.photo,anchor='nw')
  self.cv.config(scrollregion=(0,0,self.x+p.width+16,p.height+32))
  if self.selected:
   r=fitz.Rect(self.selected['bbox']);self.cv.create_rectangle(self.x+r.x0*self.zoom,16+r.y0*self.zoom,self.x+r.x1*self.zoom,16+r.y1*self.zoom,outline='#246ae5',width=2)
 def choose_page(self,event):
  if self.doc and self.pages.curselection():
   v=self.pages.curselection()[0]
   if v!=self.index:self.index=v;self.selected=None;self.refresh()
 def page(self,n):
  if self.need():self.index=max(0,min(len(self.doc)-1,self.index+n));self.selected=None;self.refresh()
 def scale(self,n):
  if self.need():self.zoom=max(.3,min(3,self.zoom+n));self.refresh()
 def spans(self):
  return [s for b in self.doc[self.index].get_text('dict')['blocks'] for l in b.get('lines',[]) for s in l.get('spans',[]) if s['text'].strip()]
 def inspect(self,t):
  self.info.delete('1.0','end');self.info.insert('1.0',t)
 def pick(self,event):
  if not self.doc:return
  pt=fitz.Point((self.cv.canvasx(event.x)-self.x)/self.zoom,(self.cv.canvasy(event.y)-16)/self.zoom)
  self.selected=next((s for s in self.spans() if fitz.Rect(s['bbox']).contains(pt)),None);self.render()
  if self.selected:
   s=self.selected;self.inspect(f"TEXT: {s['text']}\nFONT: {s['font']}\nSIZE: {s['size']}\n\nEditing replaces a text REGION, not original PDF text operators.")
 def fonts(self):
  if self.need():self.inspect('\n'.join(sorted({str(f[3]) for p in self.doc for f in p.get_fonts(full=True)})))
 def find(self):
  if not self.need():return
  q=simpledialog.askstring('Find','Text to find:')
  if q:
   rects=self.doc[self.index].search_for(q);self.render();self.inspect(str(len(rects))+' matches')
   for r in rects:self.cv.create_rectangle(self.x+r.x0*self.zoom,16+r.y0*self.zoom,self.x+r.x1*self.zoom,16+r.y1*self.zoom,outline='orange',width=2)
 def highlight(self):
  if not self.need():return
  q=simpledialog.askstring('Highlight','Text to highlight:')
  if q and self.snapshot():
   for r in self.doc[self.index].search_for(q):self.doc[self.index].add_highlight_annot(r)
   self.changed=True;self.refresh()
 def edit(self):
  if not self.need():return
  if not self.selected:messagebox.showinfo('Edit','Click text to select a span');return
  value=simpledialog.askstring('Edit','New text:',initialvalue=self.selected['text'])
  if value is None or value==self.selected['text']:return
  font=filedialog.askopenfilename(title='Unicode TTF/OTF font',filetypes=[('Font','*.ttf *.otf')])
  if not font or not messagebox.askyesno('Text reconstruction','Remove text in the selected region and redraw? Layout may change.'):return
  try:
   import native_engine
   if self.snapshot():native_engine.reconstruct(self.doc[self.index],self.selected,value,font);self.selected=None;self.changed=True;self.refresh()
  except Exception as e:messagebox.showerror('Edit failed',str(e))
 def add_text(self):
  if not self.need():return
  s=simpledialog.askstring('Add text','Simple Latin text:')
  if s and self.snapshot():self.doc[self.index].insert_text((72,125),s,fontsize=12);self.changed=True;self.refresh()
 def rotate(self):
  if self.need() and self.snapshot():p=self.doc[self.index];p.set_rotation((p.rotation+90)%360);self.changed=True;self.refresh()
 def delete(self):
  if self.need() and len(self.doc)>1 and messagebox.askyesno('Delete','Delete page?') and self.snapshot():
   self.doc.delete_page(self.index);self.index=min(self.index,len(self.doc)-1);self.changed=True;self.refresh()
 def merge(self):
  if not self.need():return
  path=filedialog.askopenfilename(filetypes=[('PDF','*.pdf')])
  if path:
   try:
    with fitz.open(path) as d:
     if d.needs_pass:raise ValueError('Unlock PDF first')
     if self.snapshot():self.doc.insert_pdf(d);self.changed=True;self.refresh()
   except Exception as e:messagebox.showerror('Merge error',str(e))
 def split(self):
  if not self.need():return
  path=filedialog.askdirectory()
  if path:
   for i in range(len(self.doc)):
    with fitz.open() as d:d.insert_pdf(self.doc,from_page=i,to_page=i);d.save(os.path.join(path,f'page-{i+1:04}.pdf'))
   messagebox.showinfo('Split','Pages exported')
 def png(self):
  if not self.need():return
  path=filedialog.asksaveasfilename(defaultextension='.png')
  if path:self.doc[self.index].get_pixmap(matrix=fitz.Matrix(2,2)).save(path)
 def sign(self):
  if not self.need():return
  path=filedialog.askopenfilename(filetypes=[('Images','*.png *.jpg *.jpeg')])
  if path and self.snapshot():self.doc[self.index].insert_image(fitz.Rect(72,540,235,610),filename=path);self.changed=True;self.refresh()
 def save(self):
  if not self.need():return False
  return self.write(self.path) if self.path else self.save_as()
 def save_as(self):
  if not self.need():return False
  path=filedialog.asksaveasfilename(defaultextension='.pdf',filetypes=[('PDF','*.pdf')])
  return self.write(path) if path else False
 def write(self,path):
  fd,tmp=tempfile.mkstemp(suffix='.pdf',dir=os.path.dirname(os.path.abspath(path)));os.close(fd)
  try:
   self.doc.save(tmp,garbage=3,deflate=True)
   with fitz.open(tmp) as d:assert d.is_pdf and len(d)==len(self.doc)
   os.replace(tmp,path);self.path=path;self.changed=False;self.refresh();return True
  except Exception as e:messagebox.showerror('Save failed',str(e));return False
  finally:
   if os.path.exists(tmp):os.remove(tmp)
 def about(self):messagebox.showinfo('About LakaPDF','LakaPDF Alpha 0.3.1\n© 2026 Larx Vo\nvovinhlac.com\n\nFree local-first. No subscription or watermark.\nText editing reconstructs regions; this is not full Acrobat editing.')
 def close(self):
  if self.confirm():
   if self.doc:self.doc.close()
   self.destroy()
if __name__=='__main__':
 if '--self-test' in sys.argv:self_test()
 else:App().mainloop()
