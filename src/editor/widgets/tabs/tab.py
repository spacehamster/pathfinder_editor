from tkinter import ttk, Label, StringVar, Entry, OptionMenu
from tkinter import W, EW
from editor.widgets.defaults import DEFAULT_BACKGROUND


class Tab():
    # pylint: disable=too-few-public-methods
    def __init__(self, notebook):
        self._panel = ttk.Frame(notebook, style='Default.TFrame')
        self._notebook = notebook
        self._dirty_lock = False

    def _add_large_label(self, a_row, colspan, label_text):
        label = Label(self._panel, text=label_text, borderwidth=1, fg='red')
        label.configure(background=DEFAULT_BACKGROUND)
        label.grid(row=a_row, columnspan=colspan, sticky=W)

    def _add_field(self, a_row, a_col, label_text, function):
        col = a_col*2
        self._add_label(a_row, col, label_text)
        variable = StringVar()
        variable.trace('w', function)
        entry = Entry(self._panel, textvariable=variable)
        entry.grid(row=a_row, column=col+1, sticky=W)
        return variable

    def _add_dropdown(self, a_row, a_col, label, choices, function):
        # pylint: disable=too-many-arguments
        col = a_col*2
        self._add_label(a_row, col, label)
        variable = StringVar()
        variable.trace('w', function)
        entry = OptionMenu(self._panel, variable, *choices)
        entry.grid(row=a_row, column=col+1, sticky=EW)
        return variable

    def _add_label(self, a_row, a_col, label_text):
        label = Label(self._panel, text=label_text, borderwidth=1)
        label.configure(background=DEFAULT_BACKGROUND)
        label.grid(row=a_row, column=a_col, sticky=W)
        return label

    def _update(self, field, function):
        if field.get() and not self._dirty_lock:
            function(field.get())
