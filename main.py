import tkinter
from tkinter import messagebox as mb
from utils import searcher
from utils import data

def search():
    if query.get() == '':
        mb.showwarning(title='warning', message="you can't search with empty input")
        return

    engines = []
    for engine in searcher.engines:
        check = engine_checks[engine['name']].get()
        if bool(check):
            engines.append(engine)

    result = searcher.super_search(query.get(), engines)

    data.result_to_csv(result)

    mb.showinfo(title='good!', message='successfully made a data in datas folder')

window = tkinter.Tk()

window.title('SUPER SEARCHER - hooss-only')
window.geometry("640x400+100+100")
window.resizable(False, False)

engine_frame = tkinter.LabelFrame(window, text='select engines to search')
engine_frame.pack()

engine_checks = {}
for engine in searcher.engines:
    name = engine['name']
    engine_checks[name] = tkinter.IntVar()
    cb = tkinter.Checkbutton(engine_frame, text=name, variable=engine_checks[name])
    cb.select()
    cb.pack(anchor='w')

search_frame = tkinter.LabelFrame(window, text='type query')
search_frame.pack()

query = tkinter.StringVar()
query_box=tkinter.Entry(search_frame, textvariable=query)
query_box.pack()

search_button = tkinter.Button(search_frame, text='search', command=search)
search_button.pack()

credit = tkinter.Label(window, text='made by hooss-only')
credit.pack(side='bottom')

window.mainloop()
