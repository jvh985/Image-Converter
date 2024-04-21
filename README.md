# Image Converter Application
This app will allow you to browse your local files and select various image types.
You are able to convert those images into either: JPEG, PNG, or GIF filetypes.

## PyQt5 has an issue with the .connect reference
Pycharm will give you a warning (not error) when using the .connect reference
to assign button functions in this program. To fix it, you can change the settings
in PyCharm to ignore the specific reference in the Unresolved references section,
however I find that to be inadequate because you may want to see 'connect' as a valid
function of .clicked

However, you can alter the stub file "QtCore.pyi" within PyQt5 in site-packages.

Append these lines of code to the pyqtSignal class in the QtCore.pyi file

```python
def connect(self, slot: 'PYQT_SLOT') -> 'QMetaObject.Connection': ...
def emit(self, *args: typing.Any) -> None: ...
```

The warnings will then disappear and you can see connect is a method of clicked.

This solution is from user: Scott Weiss on: <a href="https://stackoverflow.com/questions/65944846/pyqt5-returnpressed-connect-cannot-find-reference-connect-in-function" target="_blank">Stackoverflow</a>
