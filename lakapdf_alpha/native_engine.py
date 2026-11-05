import fitz
def reconstruct(page,span,text,fontpath):
 rect=fitz.Rect(span['bbox']);size=float(span['size']);rect.y0-=1;rect.y1+=max(2,size*.4)
 f=fitz.Font(fontfile=fontpath)
 if not text.strip() or any(not f.has_glyph(ord(c)) for c in text):raise ValueError('Missing glyph or empty text')
 if f.text_length(text,fontsize=size)>rect.width:raise ValueError('Text too wide')
 page.add_redact_annot(rect,fill=False,cross_out=False);page.apply_redactions(images=0,graphics=0,text=0)
 sh=page.new_shape();sh.insert_text((rect.x0,rect.y0+size),text,fontfile=fontpath,fontname='laka_unicode',fontsize=size);sh.commit(overlay=True)
